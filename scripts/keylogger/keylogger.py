import keyboard

try:
    keys = keyboard.record(until='ENTER')
    keyboard.play(keys)
except Exception as e:
    print(f"An error occurred: {str(e)}")
