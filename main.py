from customtkinter import *

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Chord Canvas")
        self.geometry(f"{960}x{624}")

        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.FONT = CTkFont(family="./Assets/Inter.ttf", size=16)


        # Create Frames

        self.sidebar_frame = CTkFrame(self, width=144, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.center_frame = CTkFrame(self, width=636, corner_radius=0)
        self.center_frame.grid(row=0, column=1, rowspan=4, padx=2, sticky="nsew")
        self.info_frame = CTkFrame(self, width=176, corner_radius=0)
        self.info_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")

        # Sidebar

        self.icon_label = CTkFrame(self.sidebar_frame, width=64, height=64, fg_color="#CC6C60", corner_radius=0)
        self.icon_label.grid(row=0, column=0, padx=40, pady=(32, 24))
        self.new_button = CTkButton(self.sidebar_frame, width=112, height=32, text="New", font=self.FONT, corner_radius=8)
        self.new_button.grid(row=1, column=0, padx=16, pady=8)
        self.open_button = CTkButton(self.sidebar_frame, width=112, height=32, text="Open", font=self.FONT, corner_radius=8)
        self.open_button.grid(row=2, column=0, padx=16, pady=8)
        self.save_button = CTkButton(self.sidebar_frame, width=112, height=32, text="Save", font=self.FONT, corner_radius=8)
        self.save_button.grid(row=3, column=0, padx=16, pady=8)
        self.export_button = CTkButton(self.sidebar_frame, width=112, height=32, text="Export", font=self.FONT, corner_radius=8)
        self.export_button.grid(row=4, column=0, padx=16, pady=8)
        self.settings_button = CTkButton(self.sidebar_frame, width=112, height=32, text="Settings", font=self.FONT, corner_radius=8)
        self.settings_button.grid(row=6, column=0, padx=16, pady=16)

app = App()
app.mainloop()