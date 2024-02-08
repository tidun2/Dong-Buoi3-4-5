import customtkinter
import os
from utils import *
from constants import *
from Trie import *


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
                itemHeight = 80

                frame = customtkinter.CTkFrame(self)
                frame.pack(anchor="e")

                label = customtkinter.CTkLabel(
                    frame, text=item)
                label.pack(side="left")
                self.text_widgets.append(label)

                imageLabel = FrameImage(master=frame, height=itemHeight)
                imageLabel.pack(side="right")


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        resizable = False
        self.inputArr = []
        self.title("Đông Sun")
        self.geometry("500x800")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.resizable(width=resizable, height=resizable)

        # set frameScroll
        self.frame_scrollbar = FrameScrollBar(self, self.inputArr)
        self.frame_scrollbar.pack(expand=True, fill="both")
        # input
        entry = customtkinter.CTkEntry(self, width=200)
        entry.pack(pady=10)

        button = customtkinter.CTkButton(
            self, text="Send", command=lambda entry=entry: self.getInputText(entry))
        button.pack(pady=10)
        # bind Enter key
        self.bind('<Return>', lambda event,
                  entry=entry: self.getInputText(entry))

    def getInputText(self, entry):
        userWords = entry.get().split()
        newUserWords = []
        for word in userWords:
            isBanned = tree.search(word)
            # nếu có chữ trùng thì replace chữ đó thành ...
            if isBanned:
                newUserWords.append('***')
            else:
                newUserWords.append(word)
        sentence = " ".join(newUserWords)

        self.inputArr.append(sentence)
        entry.delete(0, "end")
        # validation words

        self.frame_scrollbar.display_input_texts()
        print('inputTxts: ', self.inputArr)


class FrameImage(customtkinter.CTkFrame):
    def __init__(self, master, height):
        super().__init__(master)
        image_folder = 'img'
        # SensityWords\img\avatar.jpg
        image_path = os.path.join(image_folder, "avatar.jpeg")
        rounded_image = add_border_radius(image_path, 50)

        avatar = customtkinter.CTkImage(light_image=rounded_image,
                                        dark_image=rounded_image,
                                        size=(height, height))
        label = customtkinter.CTkLabel(self, image=avatar, text='')
        label.pack()


app = App()
tree = Trie()
for word in bannedWords:
    tree.insert(word)
app.mainloop()
