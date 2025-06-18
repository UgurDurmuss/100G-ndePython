


import tkinter as tk
import json
from tkinter import PhotoImage#görsel çekmek için kullandığmız kütüphane


def save_and_encrypt(key,clear_text):#key şifreleme için kullanılacak anahtar kelime,clear_text=şifrelenmek istenen açık metin
    encrypted=[]#şifreli karakterleri depolamak  için kullanılacak liste
    for i in range(len(clear_text)):#metindeki harf uzunluğu kadar bir for döngüsü oluşturduk
        key_char=key[i%len(key)]#hani bir anahtar veriyozya,o anahtarın uzunluğu,ve döngüden gelen sıralama bunlar birbirinden farklı olabilir bu blok sayesinde anahtar üzerinde döngü yaparak
        #döngü kadar stringleri almış oluruz
        encrypted_char=chr((ord(clear_text[i])+ord(key_char))%256)#bu kısımda ord dediğimiz kavram karakterlerin ascıı değerlerini alır
        #clear text'en bir karakteri aldık,ve key'imizden'de bir karakter alarak  bunların asll değerlerini toplayıp 256 ile mod aldığımızda herhangi bir ascıı değeri elde ediyoruz
        encrypted.append(encrypted_char)#elde edilen tüm karakterleri  listemize aldık

    return ''.join(encrypted)#listemizdeki karakterleri yan yana yazdırır




def decrypt_notes(key,encrypted_text):
     decrypted=[]#şifreyi çözdüğümüzde ortaya çıkacak  metin
     for i in range(len(encrypted_text)):
         key_char=key[i%len(key)]
         decrypted_char=chr((ord(encrypted_text[i])-ord(key_char))%256)#daha önce şifrelediğmiz metinde asıı değerlerini toplayarak elde etmiştik
         #şimdi ise şifreli metinde bulunan ascıı değerlerini çıkararak eski karakterlerimiz elde ettik
         #ve ayrıca negatif bir değer çıkması bir şey değiştirmez modunu aldığında her türlü pozitif bir sayı çıkar
         decrypted.append(decrypted_char)
     return ''.join(decrypted)



window=tk.Tk()
window.title("Secret Notes")
window.configure(bg="light grey")
window.config(padx=30,pady=30)#bunun sayesinde yaptığımız her değişikler sağ ve sol kenarlara 30
#piksellik boşlukla yerleşir
try:
   image=PhotoImage(file="görsel.png")
   label=tk.Label(window,image=image)
   label.pack()
except Exception as e:#hatayı alır e değişkenine atar
    label = tk.Label(window, text="[Görsel yüklenemedi]", bg="light grey")
    label.pack()

title_label=tk.Label(text="Enter your title",font=("Arial", 10), fg="black", bg="light grey")#renk,boyut,yazı tipi
title_label.pack()

title_entry=tk.Entry(width=20)
title_entry.pack()

input_label=tk.Label(text="enter your secret",font=("Arial", 10), fg="black", bg="light grey")
input_label.pack()

input_text=tk.Text(width=20,height=10)#doğrudan input text yazma fonksiyon bu bir widgettir
input_text.pack()

master_key=tk.Label(text="Enter your masterkey", font=("Arial", 10), fg="black", bg="light grey")
master_key.pack()

master_key_input=tk.Entry(width=20)
master_key_input.pack()

def save():
    metin=input_text.get("1.0",tk.END)#sen az önce get leri pencere açıkken almaya çalıştın bu değeri girildiği gibi almaya ve boş değer döndürmene sebep olur
    my_key=master_key_input.get()
    sifreli=save_and_encrypt(my_key,metin)
    title_text=title_entry.get()
    with open(title_text,"w") as dosya:#title başlıklı bir dosya oluşturduk
        json.dump(sifreli,dosya)
    input_text.delete("1.0",tk.END)
def encrypt():
    metin = input_text.get("1.0",tk.END)
    my_key = master_key_input.get()
    sifresiz=decrypt_notes(my_key,metin)
    input_text.delete("1.0", tk.END)
    input_text.insert("1.0", sifresiz)



save_button=tk.Button(text="Save&Encrypt",command=save)
save_button.pack()

decrypt_button=tk.Button(text="Decrypt",command=encrypt)
decrypt_button.pack()
window.mainloop()



