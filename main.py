import keyboard
import time

print("Any time you press 'ctrl+x', the bot will delete your last message.")

pause = 0.15


def delete(key):
    if keyboard.is_pressed("ctrl+x"):
        time.sleep(pause)

        print("deleting")

        keyboard.press("up")
        time.sleep(0.05)
        keyboard.release("up")

        time.sleep(pause)

        keyboard.press("ctrl+a")
        time.sleep(0.05)
        keyboard.release("ctrl+a")

        time.sleep(pause)

        keyboard.press("delete")
        time.sleep(0.05)
        keyboard.release("delete")

        time.sleep(pause)

        keyboard.press("enter")
        time.sleep(0.05)
        keyboard.release("enter")

        time.sleep(pause)

        keyboard.press("enter")
        time.sleep(0.05)
        keyboard.release("enter")

        time.sleep(pause)

        keyboard.press("tab")
        time.sleep(0.05)
        keyboard.release("tab")


keyboard.on_press(delete)
keyboard.wait()
