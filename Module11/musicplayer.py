from pygame import mixer
from tkinter import *
import tkinter.font as font 
from tkinter import filedialog

# Add songs to the playlist
def addsongs():
    # List of songs is returned
    temp_song = filedialog.askopenfilenames (initialdir="Music/", title="Choose a Song", filetypes=(("mp3 Files","*.mp3"),))
    # Loop through every song in list
    for s in temp_song:
        s = s.replace("C:/Users/jfoes/Music/Spotify","")
        songs_list.insert(END,s)

# Delete a song from the playlist
def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])

# Play a song
def Play():
    song = songs_list.get(ACTIVE)
    song = f'C:/Users/jfoes/Music/Spotify/{song}'
    mixer.music.load(song)
    mixer.music.play()

# Pausing a song
def Pause():
    mixer.music.pause()

# Stop a song
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

# To Resume playing of a song
def Resume():
    mixer.music.unpause()

# Function to navigate from the current song
def Previous():

    # Accessing the selected song index
    previous_one = songs_list.curselection()

    # Accessing the previous song index
    previous_one = previous_one[0]-1

    # Access the previous song
    temp2 = songs_list.get(previous_one)
    temp2 = f'C:/Users/jfoes/Music/Spotify/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)

    # Begin a new song
    songs_list.activate(previous_one)

    # Set the next song
    songs_list.selection_set(previous_one)

def Next():

    # Access the selected song index
    next_one = songs_list.curselection()

    # Access next song index
    next_one = next_one[0]+1

    # Access the next song
    temp = songs_list.get(next_one)
    temp = f'C:/Users/jfoes/Music/Spotify/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)

    # Activate new song
    songs_list.activate(next_one)

    # Set the next song
    songs_list.selection_set(next_one)

# Create the root window
root = Tk()
root.title('PythonProject Music Player App')

# Initialize mixer
mixer.init()

# Create listbox to contian the songs
songs_list = Listbox(root,selectmode=SINGLE, bg="black", fg="green", font=('arial', 12), height=12, width=47, selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9)

# Font for buttons
defined_font = font.Font(family='Arial')

# Play Button
play_button = Button(root, text="Play", width=7, command=Play)
play_button['font']=defined_font
play_button.grid(row=1, column=0)

# Pause Button
pause_button = Button(root, text="Pause", width=7, command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1, column=1)

# Stop Button
stop_button = Button(root,text="Stop",width=7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1, column=2)

# Resume Button
resume_button = Button(root,text="Resume", width=7, command=Resume)
resume_button['font']=defined_font
resume_button.grid(row=1,column=3)

# Previous Button
previous_button = Button(root,text="Prev", width=7, command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)

# Next Button
next_button = Button(root,text="Next", width=7, command=Next)
next_button['font']=defined_font
previous_button.grid(row=1, column=4)

# Menu
my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)
add_song_menu.add_command(label="Delete Song", command=deletesong)

mainloop()
