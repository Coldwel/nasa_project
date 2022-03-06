from tkinter import *
import requests
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

NASA_ENDPOINT = "https://api.nasa.gov/planetary/apod"
API_KEY = "Pe6gqyxa8Os3ydb4WKPnlhTUlaZ6Kb77z3dHhaip"

picture_today = {
    "api_key": API_KEY,
}

# Picture of day data
response = requests.get(NASA_ENDPOINT, params=picture_today)
data = response.json()

# Picture
title_image = data['title']
info_data = data['explanation']
current_date = data['date']

# URL picture
image_url = data['url']
image = urlopen(image_url)
image_raw = image.read()
image.close()
im = Image.open(BytesIO(image_raw)).resize((600, 600))

# Main window
window = Tk()
window.title("Nasa picture of day")
window.geometry("280x280")
window.config(bg="black", padx=15, pady=10)


# Function canvas with today's image
def today_image():
    window.destroy()
    new_window = Tk()
    new_window.title(title_image)
    new_window.config(bg='black', padx=10, pady=10)
    canvas = Canvas(new_window, width=700, height=650, bg='black', highlightthickness=0)
    photo = ImageTk.PhotoImage(im)
    label = Label(image=photo)
    date_label = Label(new_window, text=current_date, bg='black', fg='white')
    info_button = Button(new_window, text="Description", command=today_des)
    label.image = photo
    canvas.grid()
    label.grid(row=0, column=0)
    info_button.grid(row=1, column=0, columnspan=2, sticky='s')
    date_label.grid(row=0, column=0, columnspan=2, sticky='n')
    new_window.mainloop()


def today_des():
    info_window = Tk()
    info_window.title(title_image)
    info_window.config(bg='black', padx=20, pady=10)
    info_label = Label(info_window, text=info_data, wraplength=300, justify='left', bg='black', fg='white')
    info_label.grid()


# Label for main window
nasa_logo = PhotoImage(file="nasa_logo.png")
nasa_label = Label(window, image=nasa_logo)
nasa_label.grid(row=0, column=1, columnspan=2)

# Buttons for main window
today_button = Button(window, text="Today's picture", width=15, command=today_image)
today_button.grid(row=2, column=1, pady=15, columnspan=2)

window.mainloop()
