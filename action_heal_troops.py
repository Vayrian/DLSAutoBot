import time
import random
from main import click_in_window
COOLDOWN_MINUTES = 29
def execute():
    print("Executing action_heal_troops")
    # Cooldown: 10.0 minutes

    click_sequence = [
        (1148, 581, 1.0),
        (1204, 665, 1.0),
        (1278, 796, 1.0),
        (1154, 476, 1.0),
        (84, 859, 1.0),
        (91, 840, 1.0),
    ]

    for x, y, delay in click_sequence:
        if click_in_window(x, y):
            print(f"Clicked at ({x}, {y})")
            time.sleep(random.uniform(delay*0.8, delay*1.3))
        else:
            print(f"Skipped ({x}, {y})")
