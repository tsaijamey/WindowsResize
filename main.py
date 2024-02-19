import win32gui  
from pystray import MenuItem as item, Icon
from PIL import Image
import time
import threading
from pynput.keyboard import Key, Listener
import sys
import os

run_detection = True

def on_press(key):
	if key == Key.alt_l:
		resize_window()
	
def keyboard_listener_thread():
    with Listener(on_press=on_press) as listener:
        listener.join()

def resize_window():
	window_handle = win32gui.GetForegroundWindow()
	x, y, _ , _ = win32gui.GetWindowRect(window_handle)
	win32gui.MoveWindow(window_handle, x, y, 800, 600, True)

def quit_app():
	global run_detection
	run_detection = False
	icon.stop()
	
# def detection_thread():
# 	global run_detection

# 	while run_detection:
# 		window_handle = win32gui.GetForegroundWindow()
# 		window_title = win32gui.GetWindowText(window_handle)
# 		time.sleep(0.5)

if getattr(sys, 'frozen', False):
    image_path = os.path.join(sys._MEIPASS, 'res', 'resize-bottom-right-custom.png')
else:
    image_path = 'res\resize-bottom-right-custom.png'

image = Image.open(image_path)

def setup(icon):
	icon.visible = True
	# detection_t = threading.Thread(target=detection_thread)
	# detection_t.daemon = True
	# detection_t.start()

	keyboard_listener_t = threading.Thread(target=keyboard_listener_thread)
	keyboard_listener_t.daemon = True
	keyboard_listener_t.start()

icon = Icon("name", image, "WindowsResize", menu=[item('Resize', resize_window), item('Exit', quit_app)])

icon.run(setup=setup)