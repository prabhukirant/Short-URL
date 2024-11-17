import pyshorteners
from tkinter import *
def shorten_url():
    url = url_entry.get()
    

    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    
    
    result.config(state=NORMAL)
    result.delete(1.0,END)
    result.insert(END, shortened_url)
    result.config(state=DISABLED)


window = Tk()
window.title("URL Shortener")
window.minsize(width=100,height=200)
window.maxsize(width=500,height=700)
url_label = Label(window, text="Enter the URL:")
url_label.pack()
url_entry = Entry(window, width=40)
url_entry.pack()

shorten_button =Button(window, text="Shorten", command=shorten_url)
shorten_button.pack()


result =Text(window, height=3, width=40)
result.pack()
result.config(state=DISABLED)




window.mainloop()