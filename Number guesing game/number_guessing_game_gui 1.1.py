import tkinter as tk
from tkinter import ttk, messagebox
import random

class NumberGuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x600")
        self.root.configure(bg="#2C3E50")
        self.root.resizable(False, False)
        
        # Game variables
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.game_over = False
        
        self.create_widgets()
        
    def create_widgets(self):
        # Style configuration
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#2C3E50", foreground="white")
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("Title.TLabel", font=("Helvetica", 24, "bold"))
        
        # Title
        title_frame = ttk.Frame(self.root, style="Title.TFrame")
        title_frame.pack(pady=30)
        
        ttk.Label(
            title_frame,
            text="Number Guessing Game",
            style="Title.TLabel",
            background="#2C3E50",
            foreground="#ECF0F1"
        ).pack()
        
        # Game info
        self.info_label = ttk.Label(
            self.root,
            text="I'm thinking of a number between 1 and 100.",
            wraplength=350,
            justify="center",
            background="#2C3E50",
            foreground="#ECF0F1"
        )
        self.info_label.pack(pady=20)
        
        # Input frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=20)
        
        # Entry styling
        entry_style = {
            'font': ('Helvetica', 14),
            'width': 10,
            'justify': 'center',
            'relief': 'solid',
            'bd': 1
        }
        
        self.guess_entry = tk.Entry(input_frame, **entry_style)
        self.guess_entry.pack(pady=10)
        self.guess_entry.focus()
        
        # Guess button
        self.guess_button = tk.Button(
            input_frame,
            text="Submit Guess",
            command=self.check_guess,
            font=("Helvetica", 12),
            bg="#3498DB",
            fg="white",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.guess_button.pack(pady=10)
        
        # Feedback frame
        feedback_frame = ttk.Frame(self.root)
        feedback_frame.pack(pady=20, expand=True)
        
        self.feedback_label = ttk.Label(
            feedback_frame,
            text="",
            font=("Helvetica", 14),
            background="#2C3E50",
            foreground="#ECF0F1"
        )
        self.feedback_label.pack()
        
        self.attempts_label = ttk.Label(
            feedback_frame,
            text="Attempts: 0",
            background="#2C3E50",
            foreground="#ECF0F1"
        )
        self.attempts_label.pack(pady=10)
        
        # New Game button (initially hidden)
        self.new_game_button = tk.Button(
            self.root,
            text="New Game",
            command=self.start_new_game,
            font=("Helvetica", 12),
            bg="#2ECC71",
            fg="white",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        
        # Bind Enter key to submit guess
        self.root.bind('<Return>', lambda event: self.check_guess())
        
        # Add hover effects
        self.add_button_hover_effect(self.guess_button, "#2980B9")
        self.add_button_hover_effect(self.new_game_button, "#27AE60")
        
    def add_button_hover_effect(self, button, hover_color):
        button.bind("<Enter>", lambda e: button.configure(bg=hover_color))
        button.bind("<Leave>", lambda e: button.configure(bg=button["bg"]))
        
    def check_guess(self):
        if self.game_over:
            return
            
        # Get and validate input
        try:
            guess = int(self.guess_entry.get())
            if guess < 1 or guess > 100:
                messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100!")
                return
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number!")
            return
            
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        
        # Check guess
        if guess < self.secret_number:
            self.feedback_label.config(text="Too low! Try again.", foreground="#E74C3C")
        elif guess > self.secret_number:
            self.feedback_label.config(text="Too high! Try again.", foreground="#E74C3C")
        else:
            self.game_over = True
            self.feedback_label.config(
                text=f"Congratulations!\nYou've guessed the number in {self.attempts} attempts!",
                foreground="#2ECC71"
            )
            self.new_game_button.pack(pady=20)
            self.guess_button.config(state="disabled")
            
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()
        
    def start_new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.game_over = False
        
        self.feedback_label.config(text="")
        self.attempts_label.config(text="Attempts: 0")
        self.guess_button.config(state="normal")
        self.new_game_button.pack_forget()
        
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGameGUI(root)
    root.mainloop() 