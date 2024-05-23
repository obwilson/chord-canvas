from customtkinter import *
from PIL import Image


class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Chord Canvas")
        self.geometry("960x624")

        self.icon = CTkImage(light_image=Image.open("icon.png"), size=(64, 64))

        self.grid_columnconfigure((1), weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Create Sidebar

        self.sidebar_frame = CTkFrame(self, width=144, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = CTkLabel(self.sidebar_frame, text="", image=self.icon)
        self.logo_label.grid(row=0, padx=40, pady=(32, 24))
        self.new_project_button = CTkButton(
            self.sidebar_frame, text="New", width=112, height=32, corner_radius=8
        )
        self.new_project_button.grid(row=1, padx=16, pady=8)
        self.open_project_button = CTkButton(
            self.sidebar_frame, text="Open", width=112, height=32, corner_radius=8
        )
        self.open_project_button.grid(row=2, padx=16, pady=8)
        self.save_project_button = CTkButton(
            self.sidebar_frame, text="Save", width=112, height=32, corner_radius=8
        )
        self.save_project_button.grid(row=3, padx=16, pady=8)
        self.export_midi_button = CTkButton(
            self.sidebar_frame, text="Export", width=112, height=32, corner_radius=8
        )
        self.export_midi_button.grid(row=4, padx=16, pady=8)
        self.settings_button = CTkButton(
            self.sidebar_frame, text="Settings", width=112, height=32, corner_radius=8
        )
        self.settings_button.grid(row=6, padx=16, pady=16)

        # Create Center Frame

        self.center_frame = CTkFrame(self, width=636, corner_radius=0)
        self.center_frame.grid(row=0, column=1, rowspan=5, padx=2, sticky="nsew")
        self.center_frame.grid_rowconfigure(3, weight=1)
        self.tabs = CTkTabview(
            self.center_frame, width=576, height=280, corner_radius=8
        )
        self.tabs.grid(row=0, column=0, rowspan=4, padx=30, pady=32)
        self.tabs.add("Palette")
        self.tabs.add("Lyrics")
        self.timeline_frame = CTkScrollableFrame(
            self.center_frame,
            orientation=HORIZONTAL,
            width=608,
            height=96,
            corner_radius=8,
        )
        self.timeline_frame.grid(row=2, column=0, rowspan=3, padx=12)

        # Create Info Frame
        self.info_frame = CTkFrame(self, width=174, corner_radius=0)
        self.info_frame.grid(row=0, column=2, rowspan=3, sticky="nsew")


app = App()
app.mainloop()
