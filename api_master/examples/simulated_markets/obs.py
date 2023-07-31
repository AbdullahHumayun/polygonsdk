import time
import pyautogui

def switch_windows():
    # You can customize the number of times you want to switch between windows
    num_switches = 5

    for _ in range(num_switches):
        # Simulate pressing the Alt + Tab keys to switch between windows
        pyautogui.hotkey('alt', 'tab')
        # Wait for a short duration to see the switch effect
        time.sleep(1)

if __name__ == "__main__":
    switch_windows()