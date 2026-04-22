import os
from pynput import keyboard
import pyautogui
import pygetwindow as gw

ACTION_DIR = "actions"

action_name = None
coords = []
recording = True
cooldown_minutes = 0


def get_game_window():
    try:
        all_windows = gw.getAllWindows()
        matching = [w for w in all_windows 
                   if "Doomsday: Last Survivors".lower() in w.title.lower() and w.visible]
        if matching:
            win = matching[0]
            if win.isMinimized:
                win.restore()
            return win
    except:
        pass
    return None


def get_action_name():
    name = input("Enter action name (no spaces, snake_case recommended): ").strip()
    if not name:
        print("Invalid name. Try again.")
        return get_action_name()
    return name


def get_cooldown():
    global cooldown_minutes
    while True:
        try:
            ans = input("\nCooldown before this action can run again? (minutes, 0 = no cooldown): ").strip()
            if ans == "":
                cooldown_minutes = 0
                return 0
            minutes = float(ans)
            if minutes >= 0:
                cooldown_minutes = minutes
                return minutes
            else:
                print("Please enter 0 or a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def on_press(key):
    global recording
    try:
        if hasattr(key, 'char') and key.char.lower() == 'c':
            x, y = pyautogui.position()
            win = get_game_window()

            if not win:
                print("❌ Could not find Doomsday window!")
                return

            rel_x = x - win.left
            rel_y = y - win.top

            coords.append((rel_x, rel_y))
            print(f"✅ Recorded: ({rel_x}, {rel_y})")

    except Exception as e:
        print(f"Error: {e}")

    if key == keyboard.Key.esc:
        print("❌ Cancelled without saving.")
        recording = False
        return False

    if key == keyboard.KeyCode.from_char('q') or key == keyboard.KeyCode.from_char('Q'):
        print("💾 Saving action...")
        recording = False
        return False


def create_action_file(action_name, coord_list, cooldown):
    os.makedirs(ACTION_DIR, exist_ok=True)
    filename = os.path.join(ACTION_DIR, f"action_{action_name}.py")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("import time\nimport random\nfrom main import click_in_window\n\n")
        
        # Add cooldown line
        f.write(f"COOLDOWN_MINUTES = {cooldown}   # minutes (0 = no cooldown)\n\n")
        
        f.write("def execute():\n")
        f.write(f'    print("Executing action_{action_name}")\n\n')
        
        f.write("    click_sequence = [\n")
        for x, y in coord_list:
            f.write(f"        ({x}, {y}, 1.0),\n")
        f.write("    ]\n\n")
        
        f.write("    for x, y, delay in click_sequence:\n")
        f.write("        if click_in_window(x, y):\n")
        f.write('            print(f"Clicked at ({x}, {y})")\n')
        f.write("            time.sleep(random.uniform(delay*0.8, delay*1.3))\n")
        f.write("        else:\n")
        f.write('            print(f"Skipped ({x}, {y})")\n')

    print(f"\n🎉 Action successfully created: {filename}")
    print(f"   Cooldown set to: {cooldown} minutes")


def main():
    global action_name, coords, recording, cooldown_minutes

    print("="*75)
    print("   Doomsday Auto Clicker - Action Creator with Cooldown")
    print("="*75)
    print("Instructions:")
    print("   1. Open Doomsday: Last Survivors")
    print("   2. Hover mouse over button → Press C")
    print("   3. Press Q when finished\n")

    action_name = get_action_name()
    cooldown_minutes = get_cooldown()

    coords = []
    recording = True

    print(f"\n🎤 Recording started... Cooldown will be set to {cooldown_minutes} minutes.")
    print("Press C to record clicks\n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    if coords:
        create_action_file(action_name, coords, cooldown_minutes)
    else:
        print("No positions recorded.")


if __name__ == "__main__":
    main()