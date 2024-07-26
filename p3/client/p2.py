from tkinter import *
from requests import get

root = Tk()
root.title("Motivational Msg Wallah")
root.geometry("1000x300+300+50")
root.configure(bg="linen")

f = ("Ink Free", 70, "bold")
lab = Label(root, font=f, fg="red", bg="linen")
lab.pack(pady=10)

def gm():
    try:
        url = "http://127.0.0.1:8000/"
        res = get(url)
        data = res.json()
        m = data.get("m", "No message found")
        lab.configure(text=m)
    except Exception as e:
        msg = "Issue: " + str(e)
        lab.configure(text=msg)
    root.after(5000, gm)

gm()
root.mainloop()

