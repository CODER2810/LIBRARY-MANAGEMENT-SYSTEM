from tkinter import *
from tkinter import ttk

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1530x800+0+0")  # Adjusted window size to fit all elements

        # Title Label
        lbltitle = Label(
            self.root,
            text="Library Management System",
            bg="blue",
            fg="green",
            bd=20,
            relief=RIDGE,
            font=("times new roman", 50, "bold"),
            padx=2,
            pady=6,
        )
        lbltitle.pack(side=TOP, fill=X)

        # Main Frame
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # DataFrameLeft
        DataFrameLeft = LabelFrame(
            frame,
            text="Library Membership Information",
            bg="blue",
            fg="green",
            bd=12,
            relief=RIDGE,
            font=("times new roman", 12, "bold"),
        )
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(
            DataFrameLeft,
            text="Member Type",
            bg="blue",
            font=("times new roman", 15, "bold"),
        )
        lblMember.grid(row=0, column=0, sticky=W, padx=10, pady=10)

        comMember = ttk.Combobox(
            DataFrameLeft,
            font=("times new roman", 15, "bold"),
            width=27,
            state="readonly",
        )
        comMember["value"] = ["ADMIN STAFF", "STUDENT", "LECTURER"]
        comMember.grid(row=0, column=1, padx=10, pady=10)

        lblPRN_No = Label(
            DataFrameLeft,
            text="PRN No.",
            bg="blue",
            font=("times new roman", 15, "bold"),
        )
        lblPRN_No.grid(row=1, column=0, sticky=W, padx=10, pady=10)

        txtPRN_NO = Entry(
            DataFrameLeft,
            font=("times new roman", 15, "bold"),
            width=27,
            bg="white",  # Set consistent background color
            relief=SOLID,  # No focus highlight
        )
        txtPRN_NO.grid(row=1, column=1, padx=10, pady=10)

        # Additional rows for DataFrameLeft
        labels = [
            "ID No:",
            "First Name",
            "Last Name",
            "Address1",
            "PLAN/SUBSCRIPTION",
            "Post Code",
            "Mobile",
        ]

        for i, label in enumerate(labels, start=2):
            lbl = Label(
                DataFrameLeft,
                text=label,
                bg="blue",
                font=("times new roman", 15, "bold"),
            )
            lbl.grid(row=i, column=0, sticky=W, padx=10, pady=10)

            entry = Entry(
                DataFrameLeft,
                font=("times new roman", 15, "bold"),
                width=27,
                bg="white",  # Set consistent background color
                relief=SOLID,  # No focus highlight
            )
            entry.grid(row=i, column=1, padx=10, pady=10)

        # DataFrameRight
        DataFrameRight = LabelFrame(
            frame,
            text="Books Details",
            bg="blue",
            fg="green",
            bd=12,
            relief=RIDGE,
            font=("times new roman", 12, "bold"),
        )
        DataFrameRight.place(x=910, y=5, width=450, height=350)
        self.txtBox = Text(DataFrameRight, font=("times new roman", 12, "bold"),width=32,height=20,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        ListBooks = [
                        "To Kill a Mockingbird by Harper Lee",
                        "1984 by George Orwell",
                        "The Great Gatsby by F. Scott Fitzgerald",
                        "Moby-Dick by Herman Melville",
                        "Pride and Prejudice by Jane Austen",
                        "The Catcher in the Rye by J.D. Salinger",
                        "The Alchemist by Paulo Coelho",
                        "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
                        "The Lord of the Rings by J.R.R. Tolkien",
                        "The Da Vinci Code by Dan Brown",
                        "The Hobbit by J.R.R. Tolkien",
                        "War and Peace by Leo Tolstoy",
                        "Brave New World by Aldous Huxley",
                        "Fahrenheit 451 by Ray Bradbury",
                        "Crime and Punishment by Fyodor Dostoevsky",
                        "The Odyssey by Homer",
                        "Frankenstein by Mary Shelley",
                        "Wuthering Heights by Emily Brontë",
                        "The Catcher in the Rye by J.D. Salinger",
                        "The Hunger Games by Suzanne Collins",
                    ]
        ListBox = Listbox(DataFrameRight,font=("times new roman", 12, "bold"), width=20, height=20)
        ListBox.grid(row=0,column=0,padx=4)

        # Button Frame
        framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="blue")
        framebutton.place(x=0, y=530, width=1450, height=70)

        # Info Frame
        frameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="blue")
        frameDetails.place(x=0, y=600, width=1450, height=195)


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
