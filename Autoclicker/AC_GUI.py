import tkinter as tk
from tkinter import ttk
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key
import threading
import time

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

def set_speed():
    speed_input = speed_var.get()
    if speed_input != "":
        delay = 1 / float(speed_input)
    else:
        delay = 1
        speed_entry.insert(0, "1")
    click_thread.delay = delay

def quit_app():
    click_thread.exit()
    root.quit()

# Initialize tkinter window
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("600x400")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", quit_app)

# Create mouse controller instance
mouse = Controller()

# Set initial delay and button
delay = 1
button = Button.left
start_stop_key = Key.space
stop_key = KeyCode(char='q')

# Create ClickMouse instance
click_thread = ClickMouse(delay, button)
click_thread.start()

background_image=tk.PhotoImage(file="Autoclicker/bg.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0)

# Create a label and entry for setting speed
speed_label = ttk.Label(root, text="Clicks per Second:")
speed_label.grid(row=0, column=0, padx=10, pady=10)

speed_var = tk.StringVar()
speed_entry = ttk.Entry(root, textvariable=speed_var)
speed_entry.insert(0, "1")
speed_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a button to set speed
set_speed_button = ttk.Button(root, text="Set Speed", command=set_speed)
set_speed_button.grid(row=1, columnspan=2, padx=10, pady=10)

start_label = ttk.Label(root, text="Start Key:")
start_label.grid(row=2, column=0, padx=10, pady=10)

start_var = tk.StringVar()
start_entry = ttk.Entry(root, textvariable=start_var)
start_entry.insert(0, "1")
start_entry.grid(row=2, column=1, padx=10, pady=10)

# Create a button to set speed
set_start_button = ttk.Button(root, text="Set Start Key")
set_start_button.grid(row=3, columnspan=2, padx=10, pady=10)

quit_button = ttk.Button(root, text="Quit", command=quit_app)
quit_button.grid(row=4, columnspan=2, padx=10, pady=10)

# Create keyboard listener
with Listener(on_press=on_press) as listener:
    root.mainloop()

listener.join()
