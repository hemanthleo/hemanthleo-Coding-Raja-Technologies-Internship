from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do-List-App',
                           font='ariel, 25 bold', width=10, bd=5, bg='green', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
                            font='ariel, 20 bold', width=10, bd=5, bg='green', fg='black')
        self.label2.place(x=40, y=60)

        self.label3 = Label(self.root, text='Task',
                            font='ariel, 20 bold', width=10, bd=5, bg='green', fg='black')
        self.label3.place(x=320, y=60)

        self.main_text = Listbox(self.root, height=10, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=20, y=120)

        # ============add task============#

        def add():
            content = self.text.get(1.0, END).strip()
            if content:  
                self.main_text.insert(END, content)
                with open('data.txt', 'a') as file:
                    file.write(content + '\n')
                self.text.delete(1.0, END)

        def delete():
            try:
                delete_ = self.main_text.curselection()
                look = self.main_text.get(delete_)
                self.main_text.delete(delete_)
                with open('data.txt', 'r') as f:
                    lines = f.readlines()
                with open('data.txt', 'w') as f:
                    for line in lines:
                        if line.strip("\n") != look:
                            f.write(line)
            except:
                pass 

        self.button = Button(self.root, text="Add", font='sarif, 20 bold italic',
                             width=10, bd=5, bg='green', fg='black', command=add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic',
                              width=10, bd=5, bg='green', fg='black', command=delete)
        self.button2.place(x=30, y=250)


def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
