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

# Create and place the timer label
timer_label = Label(root, text="00:00", font=('Helvetica', 48), fg='blue')
timer_label.pack(pady=20)

# Create and place the start timer button
start_timer_button = Button(root, text="Start Timer", command=on_start_timer_click)
start_timer_button.pack(pady=10)

# Create and place the start break button
start_break_button = Button(root, text="Break Time", command=on_start_break_click)
start_break_button.pack(pady=10)

# Create and place the reset button
reset_button = Button(root, text="Reset Timer", command=reset_timer)
reset_button.pack(pady=10)

# Run the application
root.mainloop()
