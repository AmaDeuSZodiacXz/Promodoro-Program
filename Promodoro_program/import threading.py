import threading
import time
from tkinter import Tk, Label, Button
import pygame  # New library for sound

# Initialize Pygame Mixer
pygame.mixer.init()

# Global variable to control the timer
timer_running = False

def start_timer(label, total_time):
    global timer_running
    timer_running = True

    while total_time > -1 and timer_running:
        mins, secs = divmod(total_time, 60)
        time_formatted = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=time_formatted)
        root.update()
        time.sleep(1)
        total_time -= 1

    if timer_running:
        pygame.mixer.music.load('alert-sound.mp3')  
        pygame.mixer.music.play()
    else:
        label.config(text="00:00")

def on_start_timer_click():
    threading.Thread(target=start_timer, args=(timer_label, 25 * 60,)).start()

def on_start_break_click():
    threading.Thread(target=start_timer, args=(timer_label, 5 * 60,)).start()

def reset_timer():
    global timer_running
    timer_running = False
    pygame.mixer.music.stop()  # Stop playing sound
    timer_label.config(text="00:00")

# Create the main window
root = Tk()
root.title("Timer App")
root.configure(bg='#a74db7')  # Set background color to a purple shade

# Create and place the timer label
timer_label = Label(root, text="00:00", font=('Helvetica', 100), fg='white', bg='#a74db7')
timer_label.pack(pady=20, expand=True)

# Create and place the start timer button
start_timer_button = Button(root, text="Start Timer", command=on_start_timer_click, font=('Helvetica', 30), bg='white', fg='black')
start_timer_button.pack(pady=10, expand=True)

# Create and place the start break button
start_break_button = Button(root, text="Break Time", command=on_start_break_click, font=('Helvetica', 30), bg='white', fg='black')
start_break_button.pack(pady=10, expand=True)

# Create and place the reset button
reset_button = Button(root, text="Reset Timer", command=reset_timer, font=('Helvetica', 30), bg='white', fg='black')
reset_button.pack(pady=10, expand=True)

# Run the application
root.mainloop()
