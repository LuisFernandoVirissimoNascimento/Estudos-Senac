from tkinter import Tk, font

root = Tk()
available_fonts = list(font.families())
root.destroy()

print("Segoe UI" in available_fonts)  # This will print True if the font is available, otherwise False.
