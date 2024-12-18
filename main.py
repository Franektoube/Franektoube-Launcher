from tkinter import *
import minecraft_launcher_lib
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path
from uuid import uuid4
from random import randint
from subprocess import run

script_dir = Path(__file__).resolve().parent

def play():
    username = str(username_input.get())
    version = str(version_input.get())
    if username and version:
        uuid_gen = str(uuid4())
        access_token = str(randint(1000000, 9999999))
        options = {'username': username, 'uuid': uuid_gen, 'token': access_token}
        minecraft_dir = minecraft_launcher_lib.utils.get_minecraft_directory()
        installed_versions = minecraft_launcher_lib.utils.get_installed_versions(minecraft_dir)
        if version not in installed_versions:
            minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_dir)
        command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_dir, options)
    else:
        messagebox.showinfo("Enter Username", "Enter Username")
        return
    run(command)

root = Tk()
root.title("Franektoube Launcher")
root.geometry(str(350) + "x" + str(250))
root.config(background="#333333")
root.maxsize(350, 250)
root.minsize(350, 250)
root.iconbitmap(Path(str(script_dir) + "\\logo.ico"))

username_label = Label(root)
username_label.config(text="Username", font=("Arial", 14, "bold"), bg="#333333", pady=10, fg="#FFFFFF")

username_input = Entry(root, bg="#FFFFFF", font=("Arial", 12))

version_label = Label(root)
version_label.config(text="Version", font=("Arial", 14, "bold"), bg="#333333", fg="#FFFFFF")

version_list = []
for version in minecraft_launcher_lib.utils.get_version_list():
    if version["type"] == "release":
        version_list.append(version["id"])

version_input = ttk.Combobox(root, values=version_list, state="readonly", width=27)
version_input.set("1.8.8")

play_btn = Button()
play_btn.config(text="Play", bg="#444444", fg="#FFFFFF", font=("Arial", 14, "bold"), width=8, command=play)

username_label.pack()

username_input.pack(pady=7)

version_label.pack(pady=10)

version_input.pack(pady=7)

play_btn.pack(pady=10)

root.mainloop()