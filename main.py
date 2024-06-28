from tkinter import *
from PIL import ImageTk, Image

my_window = Tk()
my_window.title("Gizli Notlar")
my_window.minsize(width=400, height=647)
my_window.config(padx=30, pady=30)

#image
my_image = Image.open("secret.png")
max_width, max_height = 100, 100
my_image.thumbnail((max_width, max_height))
my_photo = ImageTk.PhotoImage(my_image)
my_image_label = Label(my_window, image = my_photo)
my_image_label.pack()

#title label and entry
my_title_label = Label(text="Başlığı giriniz")
my_title_label.config(padx=10, pady=10)
my_title_label.pack()
my_title_entry = Entry()
my_title_entry.config(width=30)
my_title_entry.pack()

#secret label and text
my_secret_label = Label(text="Şifrelemek istediğiniz metni giriniz")
my_secret_label.config(padx=10, pady=10)
my_secret_label.pack()
my_secret_text = Text()
my_secret_text.config(width=30, height=15)
my_secret_text.pack()

#key label and entry
my_key_label = Label(text="Anahtar giriniz")
my_key_label.config(padx=10, pady=10)
my_key_label.pack()
my_key_entry = Entry()
my_key_entry.config(width=30)
my_key_entry.pack()

#buttons
my_encrypt_button = Button(text="Kaydet ve şifrele")
my_encrypt_button.pack(pady=10)
my_decrypt_button = Button(text="Çöz")
my_decrypt_button.pack()

my_window.mainloop()