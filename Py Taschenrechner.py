import tkinter as tk 

root = tk.Tk()

root.geometry("400x500")
root.resizable(False, False)
root.title("Calculator")

label = tk.Label(root, text = " Calculator" , font =('Arial', 18))
label.grid(row=0, column=0,columnspan=3, pady=5)


#eingabe array
eingabe_array = []

#eingabe ins array von op

def add_wert(wert):
 eingabe_array.append(wert)
 eingabe.delete("1.0",tk.END)
 eingabe.insert(tk.END, "".join(eingabe_array))


#eingabe frame für =

frame_eingabe = tk.Frame(root)
frame_eingabe.grid(row=1, column=2,columnspan=2)

#eingabe

eingabe = tk.Text(frame_eingabe, height=2, width=20, font= ('Arial', 18))
eingabe.grid(row=0, column=0, padx=0, pady=2,)

#frame

button_frame = tk.Frame(root)
button_frame.grid(row=3, column=2, pady=50)


zahlen = [str(i) for i in range(1, 10)]

for index, zahl in enumerate(zahlen):
 
 startzeile = 2
 row = index // 3 
 column = index % 3

 button = tk.Button(button_frame, text= zahl, width=5, height=2, font=('Arial', 15),command=lambda z=zahl: add_wert(z) )
    
 button.grid(row=row , column=column, padx = 5, pady = 5)


# operatoren
#_op  = + 
#_op1 = -
#_op2 = /
#_op3 = *
#_op4 = = 
#_op5 = C (löschen)


def rechnung():
    try:
        ausdruck = "".join(eingabe_array)  
        ergebnis = eval(ausdruck)    
        eingabe_array.clear()              
        eingabe_array.append(str(ergebnis))  
        eingabe.delete("1.0", tk.END)
        eingabe.insert(tk.END, str(ergebnis))
    except:
        eingabe_array.clear()
        eingabe.delete("1.0", tk.END)
        eingabe.insert(tk.END, "Fehler")


button_op = tk.Button(button_frame, text= '+', width=5, height=2, font=('Arial', 15),command=lambda: add_wert('+'))
button_op.grid(row=0, column=3, padx=0)

button_op1 = tk.Button(button_frame, text= '-', width=5, height=2, font=('Arial', 15),command=lambda: add_wert('-'))
button_op1.grid(row=1, column=3, padx=25)

button_op2 = tk.Button(button_frame, text= '/', width=5, height=2, font=('Arial', 15),command=lambda: add_wert('/'))
button_op2.grid(row=2, column=3, padx=25)

button_op3 = tk.Button(button_frame, text= '*', width=4, height=2, font=('Arial', 15),command=lambda: add_wert('*'))
button_op3.grid(row= 0, column=4, padx = 1)

# =
button_op4 = tk.Button(frame_eingabe, text= '=', width=2, height=1, font=('Arial', 15),command= rechnung)
button_op4.grid(row=0, column=2, padx=0, pady=2)

#C = löschen

def clear_eingabe():
 eingabe.delete("1.0", tk.END)
 eingabe_array.clear()

button_op3 = tk.Button(button_frame, text= 'C', width=4, height=2, font=('Arial', 15),command=clear_eingabe)
button_op3.grid(row= 1, column=4, padx = 1)


root.mainloop()
