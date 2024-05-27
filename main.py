from customtkinter import *
from PIL import Image

set_appearance_mode("System")
set_default_color_theme("./assets/theme.json")


class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Chord Canvas")
        self.geometry(f"{960}x{624}")

        # self.resizable(False, False)
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

        self.tempo = 120
        self.time_signature = "4/4"

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
            self.sidebar_frame, width=112, height=32, text="New", fg_color="#ECECED", hover_color="#AFB5C7"
        )
        self.new_button.grid(row=1, column=0, padx=16, pady=8)
        self.open_button = CTkButton(
            self.sidebar_frame, width=112, height=32, text="Open", fg_color="#ECECED", hover_color="#AFB5C7"
        )
        self.open_button.grid(row=2, column=0, padx=16, pady=8)
        self.save_button = CTkButton(
            self.sidebar_frame, width=112, height=32, text="Save", fg_color="#ECECED", hover_color="#AFB5C7"
        )
        self.save_button.grid(row=3, column=0, padx=16, pady=8)
        self.export_button = CTkButton(
            self.sidebar_frame, width=112, height=32, text="Export", fg_color="#ECECED", hover_color="#AFB5C7"
        )
        self.export_button.grid(row=4, column=0, padx=16, pady=8)
        self.settings_button = CTkButton(
            self.sidebar_frame, width=112, height=32, text="Settings", fg_color="#ECECED", hover_color="#AFB5C7"
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
        self.palette_menu_bar.grid(row=0, column=0, padx=16, pady=8, sticky="ew")
        self.palette_frame = CTkFrame(
            self.tabs.tab("Palette"), width=552, height=40, fg_color="#ECECED"
        )
        self.palette_frame.grid(row=1, column=0, padx=8)
        self.tonic_menu = CTkOptionMenu(
            self.palette_menu_bar,
            width=64,
            height=32,
            font=self.FONT,
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
        self.tonic_menu.grid(row=0, column=0, padx=(0, 8))
        self.mode_menu = CTkOptionMenu(
            self.palette_menu_bar,
            width=144,
            height=32,
            font=self.FONT,
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
        self.mode_menu.grid(row=0, column=1, padx=8)
        self.modulate_button = CTkButton(
            self.palette_menu_bar, width=144, height=32, text="Change Key"
        )
        self.modulate_button.grid(row=0, column=3)

        for i in range(4):
            for f in range(7):
                chord_block = CTkButton(
                    self.palette_frame,
                    text="Csus2",
                    width=64,
                    height=32,
                    font=self.FONT,
                )
                chord_block.grid(row=i + 1, column=f, padx=8, pady=8)

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
            row=3, column=0, rowspan=3, padx=14, pady=16, sticky="ew"
        )
        self.playback_frame.grid_columnconfigure(3, weight=1)
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
        self.instrument_menu = CTkOptionMenu(self.playback_frame, width=120, height=32, values=["Piano", "Guitar", "8bit"])

        self.tempo_menu = CTkButton(
            self.playback_frame, text=f"{self.tempo}bpm", width=80, height=32
        )
        self.tempo_menu.grid(row=0, column=4, padx=8, pady=8)
        self.ts_menu = CTkOptionMenu(
            self.playback_frame,
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
        self.ts_menu.grid(row=0, column=5, padx=8, pady=8)


app = App()
app.mainloop()
