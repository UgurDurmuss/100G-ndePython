import tkinter as tk
from tkinter import Entry

def delete():
    text=entry.get()#giriş kutucuğundaki son elemanı alır
    new_text=text[:-1]#son eleman hariç yeni elemanları yeni bir listeye atar
    entry.delete(0,tk.END)
    entry.insert(0,new_text)
def write(number):
    entry.insert(tk.END,number)#entry kutucuğuna sondan başlayarak ekler
num1=None #bu değşkenler sonradan şekileneceği için ilk değerleri olmalı
islem=None


def choose_operator(operator):
    global num1,islem#bu değişkenler her yerde geçerli olur
    try:
        num1=int(entry.get())#girilen ilk sayıyı al
        islem=operator#girilen işlemi kaydettik
        entry.delete(0,tk.END)
    except ValueError:
        entry.delete(0,tk.END)
        entry.insert(0,"undefined number")
def calculate():
    global num1,islem
    try:
        num2=int(entry.get())
        result=0
        if islem=="+":
             result=num1+num2
        elif islem=="-":
             result=num1-num2
        elif islem=="*":
            result=num1*num2
        elif result=="/":
            if num2==0:
                entry.delete(0,tk.END)
                entry.insert(0,"no divide to zero")
                return
            else:
                result=float(num1/num2)
        num1=None#şimdi kullanıcı burdan sonra birkaç işlem daha yaparsa ,son atanmış işlem ve değerleri silmemiz gerekir
        islem=None
        entry.delete(0,tk.END)
        entry.insert(0,str(result))#stringi yazdırı

    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Hata")




window=tk.Tk()
window.title("Calculator")
window.geometry("300x400")

entry=tk.Entry(window,width=20,justify="center")#pencereyi içine alır
#width=kutunun uzunluğunu belirler,justify ise metin sağa mı solamı merkeze mi
entry.grid(row=0,column=0,columnspan=2,padx=5,pady=5)#columnspan=2 ile bir widget birden fazla sütunu kaplayabiliyor,padx/pady ile butonlar arası boşluk bırakıyoruz

tk.Button(window,text="1",width=5,command=lambda:write("1")).grid(row=1,column=0,padx=2,pady=2)#lambda ile yukarıdaki fonksiyonumuzu bu tuşa command olarak atadık,böylece sayıyı yazdırmış olacak
tk.Button(window,text="2",width=5,command=lambda:write("2")).grid(row=1,column=1,padx=2,pady=2)
tk.Button(window,text="3",width=5,command=lambda:write("3")).grid(row=1,column=2,padx=2,pady=2)
tk.Button(window,text="+",width=5,command=lambda:choose_operator("+")).grid(row=1,column=3,padx=2,pady=2)
tk.Button(window,text="4",width=5,command=lambda:write("4")).grid(row=2,column=0,padx=2,pady=2)
tk.Button(window,text="5",width=5,command=lambda:write("5")).grid(row=2,column=1,padx=2,pady=2)
tk.Button(window,text="6",width=5,command=lambda:write("6")).grid(row=2,column=2,padx=2,pady=2)
tk.Button(window,text="-",width=5,command=lambda:choose_operator("-")).grid(row=2,column=3,padx=2,pady=2)
tk.Button(window,text="7",width=5,command=lambda:write("7")).grid(row=3,column=0,padx=2,pady=2)
tk.Button(window,text="7",width=5,command=lambda:write("8")).grid(row=4,column=2,padx=2,pady=2)
tk.Button(window,text="9",width=5,command=lambda:write("9")).grid(row=3,column=1,padx=2,pady=2)
tk.Button(window,text="0",width=5,command=lambda:write("0")).grid(row=3,column=2,padx=2,pady=2)
tk.Button(window,text="*",width=5,command=lambda:choose_operator("*")).grid(row=3,column=3,padx=2,pady=2)
tk.Button(window,text="/",width=5,command=lambda:choose_operator("/")).grid(row=4,column=3,padx=2,pady=2)
tk.Button(window,text="=",width=5,command=lambda:calculate()).grid(row=5,column=3,padx=2,pady=2)
myButton=tk.Button(window,text="delete",command=lambda:delete())
myButton.grid(row=6,column=7,padx=30,pady=40)

window.mainloop()#pencerenin kapanmasını önlemek için


