from io import BytesIO
from tkinter import *
from tkinter import ttk
from urllib.request import urlopen

import requests
from PIL import Image, ImageTk

NASA_ENDPOINT = "https://api.nasa.gov/planetary/apod"
API_KEY = "Pe6gqyxa8Os3ydb4WKPnlhTUlaZ6Kb77z3dHhaip"

class NasaPictureApp:
    def __init__(self):
        self.picture_today = {"api_key": API_KEY}
        self.response = requests.get(NASA_ENDPOINT, params=self.picture_today)
        self.data = self.response.json()
        self.title_image = self.data["title"]
        self.info_data = self.data["explanation"]
        self.current_date = self.data["date"]
        self.image_url = self.data["url"]
        self.image_raw = urlopen(self.image_url).read()
        self.im = Image.open(BytesIO(self.image_raw)).resize((600, 600))
        self.setup_main_window()

    def setup_main_window(self):
        self.window = Tk()
        self.window.title("Nasa picture of day")
        self.window.config(bg="black", padx=15, pady=10)

        self.nasa_logo = PhotoImage(file="nasa_logo.png")
        self.nasa_label = Label(self.window, image=self.nasa_logo)
        self.nasa_label.grid(row=0, column=1, columnspan=2)

        self.today_button = Button(self.window, text="Today's picture", width=15, command=self.show_today_image)
        self.today_button.grid(row=2, column=1, pady=15, columnspan=2)

        self.window.mainloop()

    def show_today_image(self):
        self.today_window = Toplevel()
        self.today_window.title(self.title_image)
        self.today_window.config(bg="black", padx=10, pady=10)

        self.tabs = ttk.Notebook(self.today_window)
        self.picture_tab = Frame(self.tabs, bg="black")
        self.info_tab = Frame(self.tabs, bg="black")

        self.tabs.add(self.picture_tab, text="Picture")
        self.tabs.add(self.info_tab, text="Information")

        self.canvas = Canvas(self.picture_tab, width=700, height=650, bg="black", highlightthickness=0)
        self.photo = ImageTk.PhotoImage(self.im)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.date_label = Label(self.picture_tab, text=self.current_date, bg="black", fg="white")
        self.info_button = Button(self.picture_tab, text="More Information", command=self.show_more_info)

        self.canvas.pack()
        self.date_label.pack(side=TOP, pady=10)
        self.info_button.pack(side=BOTTOM, pady=10)

        self.info_label = Label(self.info_tab, text=self.info_data, wraplength=600, justify="left", bg="black",
                                fg="white")
        self.info_label.pack(side=LEFT, padx=10)

        self.tabs.pack(fill=BOTH, expand=1)

    def show_more_info(self):
        self.tabs.select(self.info_tab)


if __name__ == "__main__":
    app = NasaPictureApp()

