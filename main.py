from customtkinter import *
from PIL import Image
from music21 import *
from pychord import Chord
import numpy

set_appearance_mode("System")
set_default_color_theme("./assets/theme.json")

DEFAULT_TONIC = "C"
DEFAULT_MODE = "Major"
DEFAULT_INSTRUMENT = "Piano"
DEFAULT_TEMPO = 120
DEFAULT_TIME_SIGNATURE = "4/4"


class ProjectManager:
    def __init__(self, FONT, palette_menu_bar, chord_button_menu, playback_frame):
        self.tonic_menu = CTkOptionMenu(
            palette_menu_bar,
            width=64,
            height=32,
            font=FONT,
            values=[
                "C",
                "C#",
                "Db",
                "D",
                "D#",
                "Eb",
                "E",
                "F",
                "F#",
                "Gb",
                "G",
                "G#",
                "Ab",
                "A",
                "A#",
                "Bb",
                "B",
            ],
        )
        self.mode_menu = CTkOptionMenu(
            palette_menu_bar,
            width=144,
            height=32,
            font=FONT,
            values=[
                "Major",
                "Minor",
                "Dorian",
                "Phrygian",
                "Lydian",
                "Mixolydian",
                "Locrian",
            ],
        )
        self.time_signature_menu = CTkOptionMenu(
            playback_frame,
            values=[
                "2/2",
                "4/2",
                "2/4",
                "3/4",
                "4/4",
                "5/4",
                "7/4",
                "3/8",
                "5/8",
                "6/8",
                "7/8",
                "9/8",
                "12/8",
            ],
            width=80,
            height=32,
        )
        self.instrument_menu = CTkOptionMenu(
            playback_frame, width=120, height=32, values=["Piano", "Guitar", "8bit"]
        )
        self.tempo_menu = CTkButton(
            playback_frame, text=f"{120}bpm", width=80, height=32
        )

        # Create buttons

        self.chord_buttons = []
        for column in range(7):
            for row in range(4):
                self.chord_buttons.append(
                    CTkButton(
                        chord_button_menu,
                        text="Chord",
                        font=FONT,
                        corner_radius=8,
                        width=64,
                        height=32,
                    )
                )

                self.chord_buttons[-1].grid(row=row, column=column, padx=8, pady=8)

        # Set default values

        self.tonic_menu.set(DEFAULT_TONIC)
        self.mode_menu.set(DEFAULT_MODE)
        self.instrument_menu.set(DEFAULT_INSTRUMENT)
        self.time_signature_menu.set(DEFAULT_TIME_SIGNATURE)

    def get_tonic(self):
        return self.tonic_menu.get()

    def get_mode(self):
        return self.mode_menu.get()

    def get_key(self):
        return key.Key(self.tonic_menu.get(), self.mode_menu.get())

    def get_scale(self):
        self.key = key.Key(self.tonic_menu.get(), self.mode_menu.get())
        return self.key.getScale()

    def get_relative(self):
        self.key = key.Key(self.tonic_menu.get(), self.mode_menu.get())
        return self.key.relative

    def get_time_signature(self):
        return self.time_signature_menu.get()

    def get_tempo(self):
        return self.tempo_menu.get()

    def get_instrument(self):
        return self.instrument_menu.get()

    def get_chords(self):
        numerals = {
            0: "i",
            1: "ii",
            2: "iii",
            3: "iv",
            4: "v",
            5: "vi",
            6: "vii",
            7: "viii",
        }
        chords = {}

        # sus2
        for num in range(7):
            temp_chord = chord.Chord(
                roman.RomanNumeral(
                    f"{numerals[num]}[add2][no3]", self.get_key(), caseMatters=False
                )
            )
            scale_notes = []
            chord_notes = []
            for pitch in self.get_scale().getPitches():
                scale_notes.append(pitch.unicodeName)
            for pitch in temp_chord.pitches:
                chord_notes.append(pitch.unicodeName.replace("♮", ""))

            if not numpy.setdiff1d(chord_notes, scale_notes):
                chords[f"{num}sus2"] = [f"{self.get_scale().getPitches()[num].fullName}sus2", temp_chord]

        # maj/min
        for num in range(7):
            chords[self.get_scale().getPitches()[num].fullName] = chord.Chord(
                    roman.RomanNumeral(numerals[num], self.get_key(), caseMatters=False)
                )
            
            chords[num] = [self.get_scale().getPitches()[num].fullName, temp_chord]

        # sus4
        for num in range(7):
            temp_chord = chord.Chord(
                roman.RomanNumeral(
                    f"{numerals[num]}[add4][no3]", self.get_key(), caseMatters=False
                )
            )
            scale_notes = []
            chord_notes = []
            for pitch in self.get_scale().getPitches():
                scale_notes.append(pitch.unicodeName)
            for pitch in temp_chord.pitches:
                chord_notes.append(pitch.unicodeName.replace("♮", ""))

            if not numpy.setdiff1d(chord_notes, scale_notes):
                chords[f"{num}sus4"] = [f"{self.get_scale().getPitches()[num].fullName}sus4", temp_chord]

        # 7
        for num in range(7):
            temp_chord = chord.Chord(
                roman.RomanNumeral(
                    f"{numerals[num]}7", self.get_key(), caseMatters=False
                )
            )
            scale_notes = []
            chord_notes = []
            for pitch in self.get_scale().getPitches():
                scale_notes.append(pitch.unicodeName)
            for pitch in temp_chord.pitches:
                chord_notes.append(pitch.unicodeName.replace("♮", ""))

            if not numpy.setdiff1d(chord_notes, scale_notes):
                chords[f"{num}7"] = [f"{self.get_scale().getPitches()[num].fullName}7", temp_chord]

        return chords
    
    def set_chords(self):
        chords = self.get_chords()
        # for i in chords:
        #     self.chord_buttons[i].configure(text=)

        print(self.get_chords())


class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Chord Canvas")
        self.geometry(f"{960}x{624}")

        self.resizable(False, False)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.FONT = CTkFont("./assets/Inter.ttf", size=14)
        self.ICON = CTkImage(
            light_image=Image.open("./assets/icons/logo.png"), size=(64, 64)
        )
        self.PLAY_ICON = CTkImage(
            light_image=Image.open("./assets/icons/play.png"), size=(16, 16)
        )
        self.PAUSE_ICON = CTkImage(
            light_image=Image.open("./assets/icons/pause.png"), size=(16, 16)
        )
        self.STOP_ICON = CTkImage(
            light_image=Image.open("./assets/icons/stop.png"), size=(16, 16)
        )

        # Create Frames

        self.sidebar_frame = CTkFrame(self, width=144, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.center_frame = CTkFrame(self, width=636, corner_radius=0)
        self.center_frame.grid(row=0, column=1, rowspan=4, padx=2, sticky="nsew")
        self.center_frame.grid_rowconfigure(1, weight=1)
        self.info_frame = CTkFrame(self, width=176, corner_radius=0)
        self.info_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.info_frame.grid_rowconfigure(5, weight=1)

        # Sidebar

        self.icon_label = CTkLabel(
            self.sidebar_frame, width=64, height=64, text="", image=self.ICON
        )
        self.icon_label.grid(row=0, column=0, padx=40, pady=(32, 24))
        self.new_button = CTkButton(
            self.sidebar_frame,
            width=112,
            height=32,
            text="New",
            fg_color="#ECECED",
            hover_color="#AFB5C7",
        )
        self.new_button.grid(row=1, column=0, padx=16, pady=8)
        self.open_button = CTkButton(
            self.sidebar_frame,
            width=112,
            height=32,
            text="Open",
            fg_color="#ECECED",
            hover_color="#AFB5C7",
        )
        self.open_button.grid(row=2, column=0, padx=16, pady=8)
        self.save_button = CTkButton(
            self.sidebar_frame,
            width=112,
            height=32,
            text="Save",
            fg_color="#ECECED",
            hover_color="#AFB5C7",
        )
        self.save_button.grid(row=3, column=0, padx=16, pady=8)
        self.export_button = CTkButton(
            self.sidebar_frame,
            width=112,
            height=32,
            text="Export",
            fg_color="#ECECED",
            hover_color="#AFB5C7",
        )
        self.export_button.grid(row=4, column=0, padx=16, pady=8)
        self.settings_button = CTkButton(
            self.sidebar_frame,
            width=112,
            height=32,
            text="Settings",
            fg_color="#ECECED",
            hover_color="#AFB5C7",
        )
        self.settings_button.grid(row=6, column=0, padx=16, pady=16)

        # Tabs

        self.tabs = CTkTabview(
            self.center_frame, width=576, height=280, fg_color="#ECECED"
        )
        self.tabs._segmented_button.configure(border_width=4)
        self.tabs.grid(row=0, column=0, padx=30, pady=16, sticky="ew")
        self.tabs.add("Palette")
        self.tabs.add("Lyrics")

        # Palette Menu

        self.palette_menu_bar = CTkFrame(
            self.tabs.tab("Palette"), width=544, height=32, fg_color="#ECECED"
        )
        self.palette_menu_bar.grid_columnconfigure(2, weight=1)
        self.palette_menu_bar.grid(row=0, column=0, padx=(16, 8), pady=8, sticky="ew")
        self.palette_frame = CTkFrame(
            self.tabs.tab("Palette"), width=552, height=40, fg_color="#ECECED"
        )
        self.palette_frame.grid(row=1, column=0, padx=8)
        self.modulate_button = CTkButton(
            self.palette_menu_bar, width=144, height=32, text="Change Key"
        )
        self.modulate_button.grid(row=0, column=3, padx=0)

        self.chord_button_menu = CTkFrame(
            self.tabs.tab("Palette"), width=560, height=192, fg_color="#ECECED"
        )
        self.chord_button_menu.grid(row=1, column=0, rowspan=4, columnspan=7, padx=8)

        # Timeline

        self.timeline_frame = CTkScrollableFrame(
            self.center_frame,
            width=608,
            height=96,
            fg_color="#ECECED",
            orientation=HORIZONTAL,
        )
        self.timeline_frame.grid(row=2, column=0, padx=14, sticky="ew")

        # Playback

        self.playback_frame = CTkFrame(
            self.center_frame, width=608, height=48, fg_color="#ECECED"
        )
        self.playback_frame.grid(
            row=3, column=0, rowspan=4, padx=14, pady=16, sticky="ew"
        )
        self.playback_frame.grid_columnconfigure(4, weight=1)
        self.play_button = CTkButton(
            self.playback_frame,
            width=32,
            height=32,
            text="",
            image=self.PLAY_ICON,
            border_spacing=8,
        )
        self.play_button.grid(row=0, column=0, padx=8, pady=8)
        self.pause_button = CTkButton(
            self.playback_frame,
            width=32,
            height=32,
            text="",
            image=self.PAUSE_ICON,
            border_spacing=8,
        )
        self.pause_button.grid(row=0, column=1, padx=8, pady=8)
        self.stop_button = CTkButton(
            self.playback_frame,
            width=32,
            height=32,
            text="",
            image=self.STOP_ICON,
            border_spacing=8,
        )
        self.stop_button.grid(row=0, column=2, padx=8, pady=8)

        self.manager = ProjectManager(
            self.FONT,
            self.palette_menu_bar,
            self.chord_button_menu,
            self.playback_frame,
        )

        self.manager.tonic_menu.grid(row=0, column=0, padx=(0, 8))
        self.manager.mode_menu.grid(row=0, column=1, padx=8)
        self.manager.instrument_menu.grid(row=0, column=3, padx=8, pady=8)
        self.manager.tempo_menu.grid(row=0, column=5, padx=8, pady=8)
        self.manager.time_signature_menu.grid(row=0, column=6, padx=8, pady=8)

    def loop(self):
        # print(f"{app.manager.get_tonic()} {app.manager.get_mode()}")
        # for chord in app.manager.get_chords():
        #     print(chord.pitchedCommonName)
        app.manager.set_chords()
        print("")

        self.after(10, self.loop)


app = App()
app.loop()
app.mainloop()
