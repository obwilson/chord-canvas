from PIL import Image
from customtkinter import *
from music21 import *
from pychord import Chord


class Key:
    def __init__(self, tonic, mode):
        scale_key = {
            "Major": scale.MajorScale,
            "Minor": scale.MinorScale,
            "Dorian": scale.DorianScale,
            "Phrygian": scale.PhrygianScale,
            "Lydian": scale.LydianScale,
            "Mixolydian": scale.MixolydianScale,
            "Locrian": scale.LocrianScale,
        }

        self.scale = scale_key[mode](pitch.Pitch(tonic))


C_MAJ_KEY = Key("C", "Major")

set_default_color_theme("blue")
set_appearance_mode("light")
# BANNER = CTkImage(Image.open("./assets/banner.png"), size=(100, 50))

root = CTk()
root.title("Chord Canvas")
root.geometry(f"{840}x{420}")

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)

# Sidebar
sidebar_frame = CTkFrame(root, width=150, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsw")
sidebar_frame.grid_rowconfigure(5, weight=1)

# banner_label = CTkLabel(sidebar_frame, text="", image=BANNER)
# banner_label.grid(row=0, column=0, padx=10, pady=(20, 10))

new_project_button = CTkButton(sidebar_frame, text="New Project")
new_project_button.grid(row=1, column=0, padx=10, pady=5)

open_project_button = CTkButton(sidebar_frame, text="Open Project")
open_project_button.grid(row=2, column=0, padx=10, pady=5)

save_project_button = CTkButton(sidebar_frame, text="Save Project")
save_project_button.grid(row=3, column=0, padx=10, pady=5)

export_project_button = CTkButton(sidebar_frame, text="Export Project")
export_project_button.grid(row=4, column=0, padx=10, pady=5)

# Tabs
tabs = CTkTabview(root, height=200)
tabs.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

tabs.add("Palette")
tabs.add("Lyrics")

# Palette
key_frame = CTkFrame(tabs.tab("Palette"), corner_radius=0)
key_frame.grid(row=0, column=0, sticky="w")

key_root_menu = CTkOptionMenu(
    key_frame,
    values=[
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B",
    ],
    width=60,
)
key_root_menu.grid(row=0, column=0, padx=4, pady=4)

key_mode_menu = CTkOptionMenu(
    key_frame,
    values=["Major", "Minor", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Locrian"],
    width=128,
)
key_mode_menu.grid(row=0, column=1, padx=4, pady=4)

modulate_button = CTkButton(key_frame, text="Modulate Key", width=128)
modulate_button.grid(row=0, column=2, padx=4, pady=4, sticky="e")

palette_frame = CTkFrame(tabs.tab("Palette"), corner_radius=0)
palette_frame.grid(row=1, column=0)

for i in range(4):
    for f in range(7):
        open_project_button = CTkButton(
            palette_frame,
            text=f"{Chord.from_note_index(f+1, "", "Cmaj")}sus4",
            width=40,
            height=40,
        )
        open_project_button.grid(row=i, column=f, padx=4, pady=4)
        print(open_project_button.winfo_width())

# Timeline
timeline_frame = CTkFrame(root, height=128)
timeline_frame.grid(row=2, column=1, sticky="sew", padx=5, pady=5)

# Info
info_frame = CTkFrame(root, width=180, corner_radius=0)
info_frame.grid(row=0, column=2, rowspan=4, sticky="nse")

def loop():
    # print(root.winfo_height())
    root.after(100, loop)

root.after(100, loop)
root.mainloop()
