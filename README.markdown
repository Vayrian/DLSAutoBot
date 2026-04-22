# 🚀 DLSAutoBot

**Dynamic Window Auto Farmer for _Doomsday: Last Survivors_ (Windows)**

A smart automation bot designed to mimic human behavior while farming efficiently.  
No fixed window positioning. No rigid patterns. Just smooth, randomized, human-like automation.

This system is fully modular and customizable to your specific base layout. It will also work with other click-based games.

Recommended for use during work or times you will not be using your computer.

---
## ✨ What changed?
### Complete bot overhaul updates:
**UPDATE 2.0**
- **Bot now only focuses on the selected window**, preventing you from having to use pixel-perfection or alignment to use without it clicking off the game. You can now put the game window anywhere on your screen, and it will always click inside it. (Be aware that you must not be using your pc at the same time as running the bot, as it will control your mouse.

- **New cooldown feature** allows you to time and run actions at different times for full customization.


  ```
  ***Example***
  heal_troops - 10 mins
  zombies - 4 mins
  alliance donations - 5 hours
  ```
## ✨ Features

- 🧠 **Dynamic Window Detection**  
  Works no matter where your game window is placed or resized

- ⏱️ **Per-Action Cooldowns**  
  Customize cooldown timers (in minutes) for each action

- 🔀 **Randomized Action Order**  
  Prevents predictable patterns by shuffling actions every cycle

- 🖱️ **Human-Like Clicking**  
  Smooth mouse movement, focus handling, and realistic delays

- 🛠️ **Action Recorder Tool**  
  Easily create custom actions without coding everything manually

- 🛑 **Emergency Stop (ESC)**  
  Instantly stop the bot at any time

- 🔒 **Administrator terminal Recommended**  
  Improves compatibility with the game window

---

## 📦 Requirements

- Python **3.8+**
- Windows OS
- _Doomsday: Last Survivors_ (Official Windows App)

---

## ⚙️ Installation

Install required dependencies:

```bash
pip install pyautogui pygetwindow keyboard pynput
```

 📁 Project Structure

    Doomsday_AutoActionClicker/
    ├── main.py
    ├── create_action.py
    ├── actions/
    │   ├── action_zombie_farm.py (example)
    │   ├── action_check_mail.py (example)
    │   └── action_help_members.py (example)

---

## 🚀 Getting Started

### 1. Run Terminal as Administrator (Recommended)

- Right-click **Command Prompt** or **PowerShell**
- Click **Run as administrator**

---

### 2. Navigate to Project Folder

```bash
cd "C:\your\path\to\DLSAutoBot"
```

## 3. Create Custom Actions (Recommended)

### Run the action creator:
``` 
python create_action.py
```
During setup, you’ll be prompted for:


- Action name (e.g. zombie_farm)
- Cooldown in minutes
  0 = no cooldown
  15 = runs every 15 minutes
  
### 🎯 Recording Controls:
- Hover mouse over a button → Press C
- Repeat for each step in the sequence
- Press Q to finish recording

## 4. Run the Bot
```
python main.py
```
- Click once on the game window to focus it
You can minimize the terminal
Press ESC anytime to safely stop


## ⏱️ Cooldown System

### Each action file contains its own cooldown:
```
COOLDOWN_MINUTES = 15  # 0 = no cooldown
Behavior:
Actions on cooldown are skipped
If all actions are on cooldown → bot waits and retries automatically
```

## 🧩 Example Action File

```
import time
import random
from main import click_in_window

COOLDOWN_MINUTES = 15

def execute():
    print("Executing action_zombie_farm")

    click_sequence = [
        (271, 613, 1.0),
        (850, 420, 1.0),
    ]

    for x, y, delay in click_sequence:
        if click_in_window(x, y):
            print(f"Clicked at ({x}, {y})")
            time.sleep(random.uniform(delay * 0.8, delay * 1.3))
        else:
            print(f"Skipped ({x}, {y})") 

```
            
## 💡 Tips & Best Practices
- Keep the game window visible (not minimized)
- Run as Administrator for best results
- You can freely move/resize the game window
- Adjust delays in main.py to control speed
- Use longer cooldowns for repetitive actions
- Avoid overly fast or robotic behavior patterns

## ⚠️ Limitations
- Only supports the official Windows version of the game
- UI changes in the game may break recorded actions
- May not work properly if the game is minimized

## ⚖️ Disclaimer
```
This project is for educational purposes only.
Automation tools may violate the game's Terms of Service.
Use at your own risk.
```

## 📜 License

Free to use, modify, and distribute.
Attribution is appreciated but not required.

## ❤️ Contributing

### Pull requests, improvements, and ideas are welcome!
Feel free to fork and build your own features.

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!