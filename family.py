import tkinter as tk

def calculate_age_sum_and_average():
    ages = [int(age_entries[i].get()) for i in range(5)]
    total_age = sum(ages)
    average_age = total_age / len(ages)
    
    result_label.config(text=f"Total age: {total_age}\nAverage age: {average_age:.2f}")
    
    if average_age > 60:
        status_label.config(text="The family is mature")
    else:
        status_label.config(text="It's young")

# Create the main window
root = tk.Tk()
root.title("Family Age Calculator")

# Create input labels and entries for family members' names and ages
name_labels = []
age_entries = []
for i in range(5):
    name_label = tk.Label(root, text=f"Family Member {i+1} Name:")
    name_label.grid(row=i, column=0, padx=10, pady=5)
    
    age_entry = tk.Entry(root)
    age_entry.grid(row=i, column=1, padx=10, pady=5)
    
    name_labels.append(name_label)
    age_entries.append(age_entry)

# Create the "Calculate" button
calculate_button = tk.Button(root, text="Calculate", command=calculate_age_sum_and_average)
calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Create the result label
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Create the status label
status_label = tk.Label(root, text="")
status_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Start the main event loop
root.mainloop()