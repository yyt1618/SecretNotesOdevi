import base64
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Şifreleme ve çözme fonksiyonu
def xor_encrypt_decrypt(text, key):
    text_bytes = text.encode('utf-8')
    key_bytes = key.encode('utf-8')
    encrypted_bytes = bytearray()
    for i in range(len(text_bytes)):
        encrypted_bytes.append(text_bytes[i] ^ key_bytes[i % len(key_bytes)])
    return base64.urlsafe_b64encode(encrypted_bytes).decode('utf-8')

def xor_decrypt(encrypted_text, key):
    encrypted_bytes = base64.urlsafe_b64decode(encrypted_text.encode('utf-8'))
    key_bytes = key.encode('utf-8')
    decrypted_bytes = bytearray()
    for i in range(len(encrypted_bytes)):
        decrypted_bytes.append(encrypted_bytes[i] ^ key_bytes[i % len(key_bytes)])
    return decrypted_bytes.decode('utf-8')

def encrypt_and_save():
    title = my_title_entry.get()
    secret = my_secret_text.get("1.0", END).strip()
    key = my_key_entry.get()

    if not title or not secret or not key:
        messagebox.showerror("Hata", "Tüm alanları doldurun!")
        return

    encrypted_text = xor_encrypt_decrypt(secret, key)

    try:
        with open("encrypted_notes.txt", "a", encoding='utf-8') as file:
            file.write(f"{title}\n{encrypted_text}\n")
        messagebox.showinfo("Başarılı", "Mesaj şifrelendi ve kaydedildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya yazma hatası: {e}")

def decrypt_and_show():
    encrypted_text = my_secret_text.get("1.0", END).strip()
    key = my_key_entry.get()

    if not encrypted_text or not key:
        messagebox.showerror("Hata", "Tüm alanları doldurun!")
        return

    try:
        decrypted_text = xor_decrypt(encrypted_text, key)
        my_secret_text.delete("1.0", END)
        my_secret_text.insert("1.0", decrypted_text)
        messagebox.showinfo("Başarılı", "Mesaj çözüldü.")
    except base64.binascii.Error:
        messagebox.showerror("Hata", "Geçersiz şifreli mesaj: Incorrect padding")
    except Exception as e:
        messagebox.showerror("Hata", f"Çözme hatası: {e}")

# Tkinter arayüzü
my_window = Tk()
my_window.title("Gizli Notlar")
my_window.minsize(width=400, height=647)
my_window.config(padx=30, pady=30)

# image
my_image = Image.open("secret.png")
max_width, max_height = 100, 100
my_image.thumbnail((max_width, max_height))
my_photo = ImageTk.PhotoImage(my_image)
my_image_label = Label(my_window, image=my_photo)
my_image_label.pack()

# title label and entry
my_title_label = Label(text="Başlığı giriniz")
my_title_label.config(padx=10, pady=10)
my_title_label.pack()
my_title_entry = Entry()
my_title_entry.config(width=30)
my_title_entry.pack()

# secret label and text
my_secret_label = Label(text="Şifrelemek istediğiniz metni giriniz")
my_secret_label.config(padx=10, pady=10)
my_secret_label.pack()
my_secret_text = Text()
my_secret_text.config(width=30, height=15)
my_secret_text.pack()

# key label and entry
my_key_label = Label(text="Anahtar giriniz")
my_key_label.config(padx=10, pady=10)
my_key_label.pack()
my_key_entry = Entry()
my_key_entry.config(width=30)
my_key_entry.pack()

# buttons
my_encrypt_button = Button(text="Kaydet ve şifrele", command=encrypt_and_save)
my_encrypt_button.pack(pady=10)
my_decrypt_button = Button(text="Çöz", command=decrypt_and_show)
my_decrypt_button.pack()

my_window.mainloop()