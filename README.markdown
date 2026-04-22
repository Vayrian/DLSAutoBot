# Doomsday_AutoActionClicker

## AutoClickAction Framework

### Overview

The `Doomsday_AutoActionClicker` automates Dommsday: Last survivor tasks in a random way that mimics human behavour, so you can autofarm on a pc you wont be using for a bit.

---

### Current Actions

- **Check_mail**: Automatically checks mail, reads all and accepts all rewards before returing to the main screen.
- **Help_members**: Automatically clicks the help members icon.


---

### Prerequisites

- **Python 3.x**
- Install dependencies:

```bash
pip install pyautogui pygetwindow keyboard
```

---

### Setup Instructions

#### 1. **Place Doomsday Window in Top-Right Corner**

Make sure you move the **Doomsday: Last Survivors** game window to the **top-right corner** of your screen and do not move it again. All coordinates will be based on this position.

#### 2. **Clone or Create Project Directory**

- Place `main.py` in the root folder.
- Create an `/actions` directory for the action files (create using `create_actin.py` or clone the ones from this directory).
- Place `create_action.py` in the root to build new actions if needed.

#### 3. **Run Terminal as Administrator**

To ensure proper functionality:

- Open Command Prompt **as Administrator**
- Navigate to the folder containing the software:

```bash
cd "C:\your\path\to\this\software"
```

- Make sure the terminal is small and docked to the **left side of your screen**, so it doesn't overlap the Doomsday game.

---

### Creating Action Scripts

> Only required when adding new actions

1. Start the game and position the window in the **top-right corner**.
2. Launch `create_action.py`:

```bash
python create_action.py
```

3. When prompted:
   - Enter a name for your action (e.g., `check_mail`)
4. Hover your mouse over a desired click position and press **`C`** to capture it.
5. Repeat for all clicks needed in the action (including navigation back).
6. Press **`Q`** to save and exit. The action script will be saved in the `/actions` folder automatically.

---

### Running Doomsday_AutoActionClicker

1. Open Doomsday and ensure the window is in the **top-right corner**.
2. In your admin terminal (small and on the left side), run:

```bash
python main.py
```

3. After the script launches, **click the game window** to bring it into focus.

---

### Action Script Example

Each action script in `/actions` must define an `execute()` function using a sequence of clicks.

```python
import time
from auto_farm_base import click_in_window

def execute():
    click_sequence = [
        (300, 400, 0.5),  # Click mail icon
        (450, 550, 0.8),  # Click Read All
        (200, 150, 0.6),  # Back button
    ]
    print("Executing mail collection")
    for x, y, delay in click_sequence:
        if click_in_window(x, y):
            print(f"Clicked at ({x}, {y}), waiting {delay}s")
            time.sleep(delay)
        else:
            print(f"Skipped click at ({x}, {y}) due to window error")
```

---

### Directory Structure

```
Doomsday_AutoActionClicker/
├── main.py
├── create_action.py
├── actions/
│   ├── check_mail.py
│   └── other_actions.py
```

---

### Tips & Notes

- Use `pyautogui.displayMousePosition()` if you need to manually inspect coordinates.
- Adjust delays inside each action script to control pacing between clicks.
- You can edit the `MIN_DELAY` and `MAX_DELAY` values in `main.py` to slow down or speed up between actions (it randomizes order and lenth based on these).
- Click the termial & use `CRTL + C` exit the automation at any time.

---

### Limitations

- **Window must stay in the top-right**. Moving it will break coordinate mapping.
- Actions must be updated if Doomsday UI changes.
- Use responsibly; automation can violate game terms of service.

---

### License

You may use this code as you please, all I ask is that you credit the author if reused or modified. This is provided for education purposes. (thestinkyferret)
