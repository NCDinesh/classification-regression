import tkinter as tk
from tkinter import messagebox
import pickle

# Load the trained model
with open('classification.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to predict heart attack
def predict_heart_attack():
    try:
        # Get the input from the entry widgets
        age = float(entries[0].get())
        gender = float(entries[1].get())
        impulse = float(entries[2].get())
        pressure_highest = float(entries[3].get())
        pressure_lowest = float(entries[4].get())
        glucose = float(entries[5].get())
        kcm = float(entries[6].get())
        troponin = float(entries[7].get())
        
        # Predict whether a person is likely to suffer from a heart attack or not
        prediction = model.predict([[age, gender, impulse, pressure_highest, pressure_lowest, glucose, kcm, troponin]])
        
        # Display the prediction in a message box
        if prediction[0] == "positive":
            messagebox.showinfo("Heart Attack Prediction", "Positive! Likely to suffer from a heart attack.")
        else:
            messagebox.showinfo("Heart Attack Prediction", "Negative! Not likely to suffer from a heart attack.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for all input features.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Heart Attack Prediction")

# Create labels and entry widgets for input features
labels = ['Age:', 'Gender:', 'Impulse:', 'Highest Pressure:', 'Lowest Pressure:', 'Glucose:', 'KCM:', 'Troponin:']
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Create a button to predict heart attack
button_predict = tk.Button(root, text="Predict Heart Attack", command=predict_heart_attack)
button_predict.grid(row=len(labels), columnspan=2, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
