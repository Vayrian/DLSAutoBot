import time
import random
from main import click_in_window
 
COOLDOWN_MINUTES = 4

def execute():
    print("Executing action_zombies0")
   
    click_sequence = [
        (97, 855, 1.0),
        (67, 577, 1.0),
        (267, 609, 1.0),
        (811, 472, 1.0),
        (1152, 729, 1.0),
        (1489, 886, 1.0),
        (1217, 850, 1.0),
        (99, 842, 1.0),
    ]

    for x, y, delay in click_sequence:
        if click_in_window(x, y):
            print(f"Clicked at ({x}, {y})")
            time.sleep(random.uniform(delay*0.8, delay*1.3))
        else:
            print(f"Skipped ({x}, {y})")
