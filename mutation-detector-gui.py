# -*- coding: utf-8 -*-
"""
Created on Tue Feb  11 08:04:47 2024

@author: IAN CARTER KULANI
"""
import tkinter as tk
from tkinter import messagebox

def calculate_mutant_frequency():
    try:
        # Get the user input from the entry fields
        colonies_on_selective = int(selective_entry.get())
        colonies_on_non_selective = int(non_selective_entry.get())
        
        # Check if the number of colonies on non-selective medium is greater than 0
        if colonies_on_non_selective <= 0:
            messagebox.showerror("Input Error", "Number of colonies on non-selective medium must be greater than zero.")
            return
        
        # Calculate the frequency of mutant cells
        mutant_frequency = (colonies_on_selective / colonies_on_non_selective) * 100
        
        # Display the result in the result label
        result_label.config(text=f"Frequency of Mutant Cells: {mutant_frequency:.2f}%")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for the number of colonies.")

# Create the main window
root = tk.Tk()
root.title("Mutant Frequency Calculator")

# Set the background color to yellow
root.configure(bg="yellow")

# Create and place widgets in the window
selective_label = tk.Label(root, text="Enter the number of colonies on the selective medium:", bg="yellow")
selective_label.pack(pady=10)

selective_entry = tk.Entry(root)
selective_entry.pack(pady=5)

non_selective_label = tk.Label(root, text="Enter the number of colonies on the non-selective medium:", bg="yellow")
non_selective_label.pack(pady=10)

non_selective_entry = tk.Entry(root)
non_selective_entry.pack(pady=5)

# Create and place the Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_mutant_frequency)
calculate_button.pack(pady=20)

# Label to display the result
result_label = tk.Label(root, text="", bg="yellow", font=("Arial", 14))
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
