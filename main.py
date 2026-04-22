import pyautogui
import random
import time
import importlib
import os
import keyboard
import pygetwindow as gw
from datetime import datetime, timedelta

# ================== CONFIGURATION ==================
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.25

MIN_DELAY = 0.8
MAX_DELAY = 4

WINDOW_TITLE = "Doomsday: Last Survivors"

ACTION_DIR = "actions"
# ===================================================

# Global cooldown tracker: {action_name: next_available_time}
cooldown_tracker = {}

def get_game_window():
    try:
        all_windows = gw.getAllWindows()
        matching = [w for w in all_windows 
                   if WINDOW_TITLE.lower() in w.title.lower() and w.visible]
        if not matching:
            print("⚠️ Game window not found!")
            return None
        win = matching[0]
        if win.isMinimized:
            win.restore()
        return win
    except:
        return None


def click_in_window(rel_x: int, rel_y: int):
    win = get_game_window()
    if not win:
        print("❌ Game window not found")
        return False

    abs_x = win.left + rel_x
    abs_y = win.top + rel_y

    try:
        win.activate()
        time.sleep(0.1)
        
        pyautogui.moveTo(abs_x, abs_y, duration=0.1)
        pyautogui.mouseDown(abs_x, abs_y, button='left')
        time.sleep(0.08)
        pyautogui.mouseUp(abs_x, abs_y, button='left')
        
        print(f"✅ Clicked relative ({rel_x}, {rel_y})")
        return True

    except Exception as e:
        print(f"Click error: {e}")
        return False


def load_action_modules():
    actions = []
    if not os.path.exists(ACTION_DIR):
        print(f"Error: '{ACTION_DIR}' folder not found.")
        return actions

    for filename in os.listdir(ACTION_DIR):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            try:
                module = importlib.import_module(f"{ACTION_DIR}.{module_name}")
                if hasattr(module, "execute"):
                    cooldown = getattr(module, "COOLDOWN_MINUTES", 0)
                    actions.append((module.execute, module_name, cooldown))
                    print(f"Loaded: {module_name} (Cooldown: {cooldown} min)")
            except Exception as e:
                print(f"Failed to load {module_name}: {e}")
    return actions


def can_run_action(action_name: str, cooldown_minutes: float):
    """Check if action is ready to run"""
    if cooldown_minutes <= 0:
        return True
    
    now = datetime.now()
    next_available = cooldown_tracker.get(action_name)
    
    if next_available is None or now >= next_available:
        return True
    return False


def set_action_cooldown(action_name: str, cooldown_minutes: float):
    """Start cooldown timer AFTER action finishes"""
    if cooldown_minutes > 0:
        cooldown_tracker[action_name] = datetime.now() + timedelta(minutes=cooldown_minutes)
        print(f"   → {action_name} now on cooldown for {cooldown_minutes} minutes")


def main():
    stop_requested = False

    def request_stop():
        nonlocal stop_requested
        stop_requested = True
        print("\n🛑 ESC pressed - stopping...")

    keyboard.add_hotkey('esc', request_stop)

    print("🚀 Doomsday AutoActionClicker - Cooldown System v2")
    print("   Press ESC to stop\n")

    action_list = load_action_modules()
    if not action_list:
        print("No actions found.")
        return

    while True:
        if stop_requested:
            break

        # Get only actions that are off cooldown
        available = [(func, name, cd) for func, name, cd in action_list 
                    if can_run_action(name, cd)]

        if not available:
            print("All actions are on cooldown. Waiting 30 seconds...")
            time.sleep(30)
            continue

        random.shuffle(available)

        for func, name, cooldown in available:
            if stop_requested:
                break

            try:
                print(f"\n→ Running action: {name}")
                func()                                   # Run the action
                set_action_cooldown(name, cooldown)      # Start cooldown AFTER it runs
                time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
            except Exception as e:
                print(f"Action error in {name}: {e}")

        # Small delay between cycles
        time.sleep(random.uniform(8, 25))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Script stopped.")