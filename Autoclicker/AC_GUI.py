import tkinter as tk
from tkinter import ttk
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key
import threading
import time

# Set initial delay and button
delay = 1
button = Button.left
start_stop_key = KeyCode(char="w")
start_app = False
click_count = 0

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
        global click_count
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                click_count += 1
                print(click_count)
                time.sleep(self.delay)
            time.sleep(0.1)

def on_press(key):
    if start_app:
        if key == start_stop_key:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()

#SET SPEED OF CLICKS
def set_speed():
    speed_input = speed_var.get()
    if speed_input != "" and speed_input.isnumeric():
        delay = 1 / float(speed_input)
    else:
        delay = 1
        speed_entry.delete(0, tk.END)
        speed_entry.insert(0,"1")
    click_thread.delay = delay

def run_app():
    global start_app 
    start_app = not start_app
    print(start_app)
    if not start_app:
        click_thread.running = False
        run_button.config(text="Run", bg="green")
    else:
        run_button.config(text="Stop", bg="red")

#SET TOGGLE BUTTON
def set_startkey():
    global start_stop_key
    combobox_index=start_entry.current()  
    if combobox_index == 0:
        start_stop_key = KeyCode(char="w")
    elif combobox_index == 1:
        start_stop_key = KeyCode(char="i")
    elif combobox_index ==2:
        start_stop_key = KeyCode(char="o")
    else:
        start_stop_key = KeyCode(char="p")

def quit_app():
    click_thread.exit()
    root.quit()

# Initialize tkinter window
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("450x300")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", quit_app)
root.attributes('-topmost',True)
root.iconphoto(False, tk.PhotoImage(file='Autoclicker/img/cursor.png'))

# Create mouse controller instance
mouse = Controller()

# Create ClickMouse instance
click_thread = ClickMouse(delay, button)
click_thread.start()


canvas = tk.Canvas(root, width=450, height=300, highlightthickness=0)
canvas.pack()

#BACKGROUND
background_image=tk.PhotoImage(file="Autoclicker/img/bg_blur.png")
canvas.create_image(225,150, image=background_image)

#SET SPEED LABEL
speed_label = ttk.Label(root, text="Clicks per Second:", font=("segoe ui",9))
speed_label.place(x=5, y=10, width=125, height=25)

#SET SPEED ENTRY TEXTAREA
speed_var = tk.StringVar()
speed_entry = ttk.Entry(root, textvariable=speed_var)
speed_entry.insert(0, "1")
speed_entry.place(x=135, y=10, width=100, height=25)

#SET SPEED BUTTON
set_speed_button = ttk.Button(root, text="Set Speed", command=set_speed)
set_speed_button.place(x=155, y=50) 

#TOGGLE TEXT
start_label = ttk.Label(root, text="Toggle Key:", font=("segoe ui",9))
start_label.place(x=5, y=90, width=125, height=25)

#TOGGLE BUTTON COMBO BOX
start_var = tk.StringVar()
start_entry = ttk.Combobox(state="readonly", values=["W", "I", "O", "P"])
start_entry.current(0)
start_entry.place(x=135, y=90, width=100, height=25)

#TOGGLE BUTTON
set_start_button = ttk.Button(root, text="Set Start Key", command=set_startkey)
set_start_button.place(x=155, y=130)

clickcount_label = ttk.Label(root, text="Click Count:", font=("segoe ui",9))
clickcount_label.place(x=5, y=170, width=125, height=25)

click_count_var = tk.StringVar()
click_count_var.set(str(click_count))
click_count_entry = ttk.Entry(root, textvariable=click_count_var, state="readonly")
click_count_entry.place(x=135, y=170, width=100, height=25)

def update_click_count():
    global click_count
    click_count_var.set(str(click_count))

    # Schedule next update after 1000ms (1 second)
    root.after(100, update_click_count)

update_click_count()  # Start updating click count

run_button = tk.Button(root, text="Run", command=run_app, bg="green")
run_button.place(x=240, y=10, width=210, height=185)

#QUIT BUTTON
quit_button = tk.Button(root, text="Quit", command=quit_app, bg="grey")
quit_button.place(x=0, y=210, width=450, height=90)

# Create keyboard listener
with Listener(on_press=on_press) as listener:
    root.mainloop()

listener.join()
