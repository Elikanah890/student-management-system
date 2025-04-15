import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ---------- Database Connection ----------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Elkanahbaha@2007",  # <- CHANGE this to your real MySQL password
        database="aman2"
    )

# ---------- Main Application ----------
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("700x500")

        # ----- Input Fields -----
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.course_var = tk.StringVar()

        tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.age_var).grid(row=1, column=1)

        tk.Label(root, text="Gender").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.gender_var).grid(row=2, column=1)

        tk.Label(root, text="Course").grid(row=3, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.course_var).grid(row=3, column=1)

        # ----- Buttons -----
        tk.Button(root, text="Add Student", command=self.add_student).grid(row=4, column=0, pady=20)
        tk.Button(root, text="Update Student", command=self.update_student).grid(row=4, column=1)
        tk.Button(root, text="Delete Student", command=self.delete_student).grid(row=4, column=2)
        tk.Button(root, text="View All", command=self.view_students).grid(row=4, column=3)

        # ----- Table for Display -----
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "Gender", "Course"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Course", text="Course")
        self.tree.bind("<ButtonRelease-1>", self.select_row)
        self.tree.place(x=10, y=250, width=680, height=230)

    # ---------- Functions ----------
    def add_student(self):
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO sanga (name, age, gender, course) VALUES (%s, %s, %s, %s)"
        values = (self.name_var.get(), self.age_var.get(), self.gender_var.get(), self.course_var.get())
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student added successfully")
        self.view_students()

    def view_students(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sanga")
        rows = cursor.fetchall()
        conn.close()

        # Clear old rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in rows:
            self.tree.insert("", "end", values=row)

    def select_row(self, event):
        selected = self.tree.focus()
        values = self.tree.item(selected, "values")
        if values:
            self.selected_id = values[0]
            self.name_var.set(values[1])
            self.age_var.set(values[2])
            self.gender_var.set(values[3])
            self.course_var.set(values[4])

    def update_student(self):
        if not hasattr(self, 'selected_id'):
            messagebox.showwarning("Select", "Select a student first")
            return
        conn = connect_db()
        cursor = conn.cursor()
        query = "UPDATE sanga SET name=%s, age=%s, gender=%s, course=%s WHERE id=%s"
        values = (self.name_var.get(), self.age_var.get(), self.gender_var.get(), self.course_var.get(), self.selected_id)
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        messagebox.showinfo("Updated", "Student record updated")
        self.view_students()

    def delete_student(self):
        if not hasattr(self, 'selected_id'):
            messagebox.showwarning("Select", "Select a student to delete")
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sanga WHERE id=%s", (self.selected_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted", "Student deleted")
        self.view_students()
        self.clear_fields()

    def clear_fields(self):
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.course_var.set("")

# ---------- Run App ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
