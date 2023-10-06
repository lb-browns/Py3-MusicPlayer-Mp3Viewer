import tkinter as tk
from tkinter import filedialog
from tkinter import *
import pygame
from pygame import mixer
import time
import os

# initialize Files
mixer.init()

# create Main Window
window = tk.Tk()
window .title("Music Player")

# fuction To Play & Select Music
def playMusic():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# stop Music
def stopMusic():
    pygame.mixer.music.stop()

# load And Display Playlist
def loadPlaylist():
    playlist = filedialog.askdirectory()
    os.chdir(playlist)
    files = os.listdir(playlist)
    for file in files:
        if file.endswith(".mp3"):
            playlistBox.insert(tk.END, file)

# add Play Button
playButton = tk.Button(window, text="Play Music", command=playMusic, fg="red")
playButton.pack()

# add Stop Button
stopButton = tk.Button(window, text="Stop Music", command=stopMusic, fg="green",)
stopButton.pack()

# add Playlist box Window
playlistBox = tk.Listbox(window)
playlistBox.pack(padx=10,pady=25, fill=BOTH, expand=True)

# add Load Playlist Button
loadButton = tk.Button(window, text="Load Playlist", command=loadPlaylist, fg='green')
loadButton.pack()

# start Main Event Loop
window.geometry("500x500")
window.configure(bg="#E44157")
window.mainloop()