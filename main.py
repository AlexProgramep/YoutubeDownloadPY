from tkinter import messagebox, Tk, StringVar, Label, Entry, Button
from tkinter.filedialog import asksaveasfilename
import pafy

width = 400
height = 400

root = Tk()
root.title("YoutubeDownloadPY")
root.geometry(f"{width}x{height}+700+250")
root.minsize(width, height)
root.maxsize(width, height)


def video():
    url = message.get()
    video_url = pafy.new(url)
    title = video_url.title
    best_stream = video_url.getbest()
    file = asksaveasfilename(defaultextension=f".mp4")
    best_stream.download(file)
    messagebox.showinfo("YoutubeDownloadPY",
                        f"Відео {title} було завантажено!")


def audio():
    url = message.get()
    v = pafy.new(url)
    v_title = v.title

    best_audio = v.getbestaudio()
    file = asksaveasfilename(defaultextension=f".mp3")
    best_audio.download(file)
    messagebox.showinfo("YoutubeDownloadPY",
                        f"Аудіо {v_title} було завантажено!")


message = StringVar()

message_label = Label(text="Вставте сюди url із Youtube")
message_label.place(relx=.3, rely=.1)

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.2, anchor="center", width="300", height="25")

message_button = Button(text="Відео",
                        padx="20",
                        pady="15",
                        background="#555",
                        foreground="#fff",
                        command=video)
message_button.place(relx=.5, rely=.5, anchor="center")

message_button_1 = Button(text="Аудіо",
                          padx="20",
                          pady="15",
                          background="#555",
                          foreground="#fff",
                          command=audio)
message_button_1.place(relx=.5, rely=.7, anchor="center")

root.mainloop()
