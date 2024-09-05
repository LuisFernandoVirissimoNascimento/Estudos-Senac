# In this behemoth typhoon we are to read images deposited in the same folder as the script and give them a lil textbox underneath, scroll mouse infinitely expanding downwards aaaaand, I want to save the descriptions :) So that every time we click, it shows up.
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ImageDescriptionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Description Viewer")
        self.geometry("800x600")

        self.image_folder = os.path.dirname(os.path.abspath(__file__)) # Caminho atual de aonde as imagens estão.
        self.descriptions = {}
        self.load_descriptions()

        self.canvas = tk.Canvas(self, bg="#ffe400")
        self.scroll_y = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

        self.frame = tk.Frame(self.canvas, bg="gray")
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scroll_y.pack(side="right", fill="y")

        self.load_images()

    def load_images(self):
        for file_name in os.listdir(self.image_folder):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                self.display_image_with_description(file_name)

    def display_image_with_description(self, file_name):
        image_path = os.path.join(self.image_folder, file_name)
        img = Image.open(image_path)
        img.thumbnail((700, 700))
        photo = ImageTk.PhotoImage(img)

        label_frame = tk.Frame(self.frame, bg="gray", bd=0, highlightthickness=0)
        label_frame.pack(pady=10)

        label = tk.Label(label_frame, image=photo, bg="gray", bd=0)
        label.image = photo
        label.pack()

        entry = ttk.Entry(self.frame, width=100)
        entry.pack(pady=5)
        entry.insert(0, self.descriptions.get(file_name, "Coloque sua descrição aqui"))

        button = ttk.Button(self.frame, text="Save", command=lambda: self.save_description(file_name, entry.get()))
        button.pack(pady=5)

    def save_description(self, file_name, description):
        self.descriptions[file_name] = description
        self.save_descriptions()

    def load_descriptions(self):
        try:
            with open("descriptions.txt", "r") as file:
                for line in file:
                    file_name, description = line.strip().split(':', 1)
                    self.descriptions[file_name] = description
        except FileNotFoundError:
            pass

    def save_descriptions(self):
        with open("descriptions.txt", "w") as file:
            for file_name, description in self.descriptions.items():
                file.write(f"{file_name}:{description}\n")

if __name__ == "__main__":
    app = ImageDescriptionApp()
    app.mainloop()
