import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from ttkbootstrap import Style

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.title("Todo List App")
        self.geometry("400x400")
        self.maxsize(400, 400)
        self.minsize(400, 400)
        style = Style(theme="flatly")
        self.configure(background="light green")
        
        # Create input field for adding tasks
        self.task_input = ttk.Entry(self,background="#F6FDC3", font=("TkDefaultFont", 16), width=50 ,style="Custom.TEntry")
        self.task_input.pack(padx=10, pady=10)
        # Placeholder for input field
        self.task_input.insert(0, "Enter your todo here...")

        # Clear placeholder when input field is clicked
        self.task_input.bind("<FocusIn>", self.clear_placeholder)
        # Restore placeholder when input field loses focus
        self.task_input.bind("<FocusOut>", self.restore_placeholder)
        
        # Create button for adding tasks
        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)

        # Create listbox to display added tasks
        self.task_list = tk.Listbox(self ,font=("Arial", 16), height=5, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create buttons for marking tasks as done or deleting them
        ttk.Button(self, text="Done", width=8, style="success.TButton", command=self.mark_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete", width=8, style="danger.TButton", command=self.delete_task_dialog).pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Create button for displaying task statistics
        ttk.Button(self, text="View Stats", width=8, style="info.TButton", command=self.view_stats).pack(side=tk.BOTTOM, pady=10)
        
        # Load existing tasks
        self.load_tasks()
    
    # Show task statistics
    def view_stats(self):
        done_count = 0
        total_count = self.task_list.size()
        for i in range(total_count):
            if self.task_list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

    # Add a task
    def add_task(self):
        task = self.task_input.get().strip()
        if task and task != "Enter your todo here...":
            self.task_list.insert(tk.END, task)
            self.task_list.itemconfig(tk.END, fg="#FF2E63")
            self.task_input.delete(0, tk.END)
            self.save_tasks()
            messagebox.showinfo("Task Added", "Task added successfully.")  # Popup message for task added

    # Mark task as done
    def mark_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, fg="green")
            self.save_tasks()

    # Delete task dialog
    def delete_task_dialog(self):
        task_index = simpledialog.askinteger("Delete Task", "Enter the index of the task to delete:", initialvalue=1)
        if task_index is not None:
            self.delete_task(task_index - 1)

    # Delete task
    def delete_task(self, task_index):
        if 0 <= task_index < self.task_list.size():
            self.task_list.delete(task_index)
            self.save_tasks()
            messagebox.showinfo("Task Deleted", "Task deleted successfully.")  # Popup message for task deleted
        else:
            messagebox.showerror("Error", "Invalid task index. Please enter a valid index.")

    # Clear placeholder text
    def clear_placeholder(self, event):
        if self.task_input.get() == "Enter your todo here...":
            self.task_input.delete(0, tk.END)

    # Restore placeholder text
    def restore_placeholder(self, event):
        if self.task_input.get() == "":
            self.task_input.insert(0, "Enter your todo here...")

    # Load tasks from file
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for i, line in enumerate(f, 1):  # Start indexing from 1
                    task, color = line.strip().split("|")
                    self.task_list.insert(tk.END, task)
                    self.task_list.itemconfig(tk.END, fg=color)
        except FileNotFoundError:
            pass
    
    # Save tasks to file
    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for i in range(self.task_list.size()):
                text = self.task_list.get(i)
                color = self.task_list.itemcget(i, "fg")
                f.write(f"{text}|{color}\n")

if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop()
