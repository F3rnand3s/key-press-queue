from pynput.keyboard import Key, Listener
import winsound

def on_press(key):
    winsound.PlaySound('kp1.wav', winsound.SND_FILENAME)
    print('{0} pressed'.format(key))

def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()