import tkinter as tk
from tkinter import filedialog, ttk, simpledialog
import webbrowser

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Campbell's Notepad")
        self.text = tk.Text(self.master, font=("Arial", 12), bg="white", fg="black", insertbackground="black")
        self.text.pack(fill="both", expand=True)
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        supportmenu = tk.Menu(menubar, tearoff=0)
        supportmenu.add_command(label="Follow", command=self.support_github)
        menubar.add_cascade(label="Follow", menu=supportmenu)

        settingsmenu = tk.Menu(menubar, tearoff=0)
        settingsmenu.add_command(label="Font", command=self.change_font)
        settingsmenu.add_command(label="Transparency", command=self.change_transparency)
        settingsmenu.add_separator()
        self.color_var = tk.StringVar(value="light")
        settingsmenu.add_radiobutton(label="Light mode", variable=self.color_var, value="light", command=self.change_color_mode)
        settingsmenu.add_radiobutton(label="Dark mode", variable=self.color_var, value="dark", command=self.change_color_mode)
        menubar.add_cascade(label="Settings", menu=settingsmenu)

        self.master.config(menu=menubar)

    def new_file(self):
        self.text.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as f:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, f.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.text.get(1.0, tk.END))

    def support_github(self):
        webbrowser.open_new("https://github.com/vinscripts")

    def change_font(self):
        font = tk.filedialog.askopenfilename(title="Select font file", filetypes=(("Font files", "*.ttf;*.otf"),))
        if font:
            size = tk.simpledialog.askinteger(title="Font size", prompt="Enter font size", initialvalue=12)
            self.text.configure(font=(font, size))

    def change_transparency(self):
        transparency = tk.simpledialog.askfloat(title="Transparency", prompt="Enter transparency (0-1)", initialvalue=1.0)
        self.master.attributes("-alpha", transparency)

    def change_color_mode(self):
        color_mode = self.color_var.get()
        if color_mode == "light":
            self.text.configure(bg="white", fg="black", insertbackground="black")
        else:
            self.text.configure(bg="black", fg="white", insertbackground="white")

root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
