import serial
import tkinter as tk

root = tk.Tk()
root.title('物件檢測結果視窗')
root.geometry('800x600')
arduino = serial.Serial('COM3', 9600)
a = [0] * 3

text = tk.Label(
    root, 
    text="", 
    bd=2, 
    relief=tk.SUNKEN, 
    anchor=tk.CENTER, 
    font=("Arial", 72)
)
text.pack(expand=True, fill=tk.BOTH) 
i = 0
k = 0
result="None"

def main_func():
    j=0
    global i,result,k
    a[i] = float(arduino.readline().decode('utf-8').strip())
    tmp = sum(a)/3
    print("%.2f" % tmp)
    if i==0:
        j=2
    else:
        j=i-1
    if tmp<1 or (a[j]!=0 and a[i]==0): 
        if (a[j]!=0 and a[i]==0):
            for i in range(3):
                a[i]=0
        result="未檢測到物體"
        k=2
    elif 0 in a:
        result="檢測中"
    else:
        if k>=0:
            result="檢測中"
            k+=-1
            print(k)
        elif 10.5< tmp < 11.5:
            result="長方體"
        elif 8.0<tmp<10:
            result="圓柱"
        elif 7<tmp<8:
            result="正方體"
        else:
            result="三角柱"
        k-=1
    text.config(text=result)
    i = (i + 1) % 3
    print(a)
    root.after(100, main_func)

root.after(200, main_func)
root.mainloop()
