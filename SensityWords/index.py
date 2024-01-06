import customtkinter
import os
from utils import *


class FrameScrollBar(customtkinter.CTkScrollableFrame):
    def __init__(self, master, inputTxts):
        super().__init__(master, fg_color="gray")
        self.inputTxts = inputTxts
        self.text_widgets = []

    def display_input_texts(self):
        # Update existing labels with the updated input_texts
        for i, item in enumerate(self.inputTxts):
            if i < len(self.text_widgets):
                self.text_widgets[i].configure(text=item)
            else:
                print('item:', item)
                label = customtkinter.CTkLabel(self, text=item, height=50)
                label.pack(side="left")
                imageLabel = FrameImage(master=self)
                imageLabel.pack(side="right")
                self.text_widgets.append(label)


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        resizable = False
        self.inputTxts = []
        self.title("Đông Sun")
        self.geometry("500x800")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.resizable(width=resizable, height=resizable)
        # input
        entry = customtkinter.CTkEntry(self, width=200)
        entry.pack(pady=10)

        button = customtkinter.CTkButton(
            self, text="Send", command=lambda entry=entry: self.getInputText(entry))
        button.pack(pady=10)

        # bind Enter key
        self.bind('<Return>', lambda event,
                  entry=entry: self.getInputText(entry))

        # set frameScroll
        self.frame_scrollbar = FrameScrollBar(self, self.inputTxts)
        self.frame_scrollbar.pack(expand=True, fill="both")

    def getInputText(self, entry):
        user_input = entry.get()
        self.inputTxts.append(user_input)
        entry.delete(0, "end")
        self.frame_scrollbar.display_input_texts()
        print('inputTxts: ', self.inputTxts)


class FrameImage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        image_folder = 'img'
        image_path = os.path.join(image_folder, "avatar.jpg")
        rounded_image = add_border_radius(image_path, 500)
        avatar = customtkinter.CTkImage(light_image=rounded_image,
                                        dark_image=rounded_image,
                                        size=(30, 30))
        customtkinter.CTkLabel(self, image=avatar, text='')


app = App()
app.mainloop()
