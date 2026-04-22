import time
import random
from main import click_in_window

COOLDOWN_MINUTES = 25.0   # minutes (0 = no cooldown)

def execute():
    print("Executing action_ir")

    click_sequence = [
        (940, 665, 1.0),
    ]

    for x, y, delay in click_sequence:
        if click_in_window(x, y):
            print(f"Clicked at ({x}, {y})")
            time.sleep(random.uniform(delay*0.8, delay*1.3))
        else:
            print(f"Skipped ({x}, {y})")
