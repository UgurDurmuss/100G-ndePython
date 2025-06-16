import tkinter as tk
num1=0
global metin
def calculate():
    try :
        num1=int(entry1.get())
        entry1.delete(0,tk.END)
        num2=int(entry2.get())
        entry2.delete(0,tk.END)
        BMİ=float(num1/(num2*num2))
        if BMİ<=18.5:
           metin="You are weak"
        elif 18.5<BMİ and BMİ<=24.9:
           metin="you are normal"
        elif 25<=BMİ and BMİ<29.9:
           metin="you are overheight"
        metin_area.delete("1.0", tk.END)  # 1.0 demek baştan başla
        metin_area.insert(tk.END, metin)  # tk end ise sona kadar

    except:
        entry1.delete(0,tk.END)
        entry2.delete(0,tk.END)






window=tk.Tk()
window.title("BMI")
window.geometry("300x300")
window.configure(bg="lightblue")#pencerenin rengini ayarladık

label1=tk.Label(window,width=20,text="what is your weight(kg)")
label1.pack(padx=10,pady=10)
entry1=tk.Entry(window,width=20,justify="center")
entry1.pack(padx=10,pady=10)

label2=tk.Label(window,width=20,text="What is your height(cm)")
label2.pack(padx=20,pady=20)
entry2=tk.Entry(window,width=20,justify="center")
entry2.pack(padx=10,pady=10)

calculateButton=tk.Button(window,text="Calculate",command=lambda :calculate())
calculateButton.pack(padx=21,pady=21)

metin_area=tk.Text(window,height=5,width=40)
metin_area.pack()

window.mainloop()
