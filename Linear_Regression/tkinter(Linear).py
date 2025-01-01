import tkinter as tk
from tkinter import messagebox
import pickle

# Load the trained models
with open('regression_model.pkl', 'rb') as file:
    model_experience = pickle.load(file)

with open('regression_model1.pkl', 'rb') as file:
    model_experience_education = pickle.load(file)

# Function to predict salary using years of experience
def predict_salary_experience():
    try:
        # Get the input from the entry widget
        years_of_experience = float(entry_years_of_experience.get())
        
        # Predict the salary using the model based on experience
        predicted_salary = model_experience.predict([[years_of_experience]])
        
        # Display the predicted salary in a message box
        messagebox.showinfo("Salary Prediction (Experience)", f"Predicted Salary: ${predicted_salary[0]:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for Years of Experience.")

# Function to predict salary using both years of experience and education level
def predict_salary_experience_education():
    try:
        # Get the inputs from the entry widgets
        years_of_experience = float(entry_years_of_experience_education.get())
        education_level = float(entry_education_level.get())
        
        # Predict the salary using the model based on experience and education level
        predicted_salary = model_experience_education.predict([[years_of_experience, education_level]])
        
        # Display the predicted salary in a message box
        messagebox.showinfo("Salary Prediction (Experience & Education)", f"Predicted Salary: ${predicted_salary[0]:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for Years of Experience and Education Level.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Salary Prediction")

# Create frames for organizing widgets
frame_experience = tk.LabelFrame(root, text="Prediction by Years of Experience", padx=10, pady=10)
frame_experience.pack(padx=10, pady=10, fill="both", expand=True)

frame_experience_education = tk.LabelFrame(root, text="Prediction by Years of Experience & Education Level", padx=10, pady=10)
frame_experience_education.pack(padx=10, pady=10, fill="both", expand=True)

# Create widgets for the frame_experience
label_years_of_experience = tk.Label(frame_experience, text="Years of Experience:")
label_years_of_experience.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_years_of_experience = tk.Entry(frame_experience)
entry_years_of_experience.grid(row=0, column=1, padx=10, pady=5)
button_predict_experience = tk.Button(frame_experience, text="Predict Salary", command=predict_salary_experience)
button_predict_experience.grid(row=1, columnspan=2, padx=10, pady=5)

# Create widgets for the frame_experience_education
label_years_of_experience_education = tk.Label(frame_experience_education, text="Years of Experience:")
label_years_of_experience_education.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_years_of_experience_education = tk.Entry(frame_experience_education)
entry_years_of_experience_education.grid(row=0, column=1, padx=10, pady=5)

label_education_level = tk.Label(frame_experience_education, text="Education Level:")
label_education_level.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_education_level = tk.Entry(frame_experience_education)
entry_education_level.grid(row=1, column=1, padx=10, pady=5)

button_predict_experience_education = tk.Button(frame_experience_education, text="Predict Salary", command=predict_salary_experience_education)
button_predict_experience_education.grid(row=2, columnspan=2, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
