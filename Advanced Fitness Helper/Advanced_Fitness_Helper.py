import tkinter
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import math

#ALL METHODS
def process_data():
    terms_check = accept_var.get()
    sex = sex_combobox.get()
    age = str(age_spinbox.get())
    height_ft = str(height_spinbox.get())
    height_in = str(height_inches_spinbox.get())
    goal = goal_combobox.get()
    sleep = str(sleep_spinbox.get())
    energy = energy_combobox.get()
    mood = mood_combobox.get()
    activity = activity_combobox.get()

    if terms_check == "Accepted":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        if (first_name and last_name) and (any(char.isdigit() for char in first_name) == False) and (any(char.isdigit() for char in last_name) == False):
            sex = sex_combobox.get()
            if (sex == "Male") or (sex == "Female"):
                age = str(age_spinbox.get())
                if age.strip().isdigit() and (int(age) >= 12) and (int(age) <= 101):
                    height_ft = height_spinbox.get()
                    height_in = height_inches_spinbox.get()
                    if (height_ft.strip().isdigit()) and (height_in.strip().isdigit()) and (int(height_ft) > 0) and (int(height_in) >= 0) and (int(height_in) <= 11):
                        goal = goal_combobox.get()
                        if (goal == "Maintain weight") or (goal == "Gain weight (bulk)") or (goal == "Lose weight (cut)"):
                            sleep = sleep_spinbox.get()
                            if sleep.strip().isdigit() and (int(sleep) > 0):
                                energy = energy_combobox.get()
                                if (energy == "Very low") or (energy == "Low") or (energy == "Moderate") or (energy == "High") or (energy == "Very High"):
                                    mood = mood_combobox.get()
                                    if (mood == "Depressed (sad or gloomy)") or (mood == "Euthymia (normal feeling)") or (mood == "Content (happy)"):
                                        weight = weight_entry.get()
                                        if weight.strip().isdigit() and (int(weight) > 0):
                                            activity = activity_combobox.get()
                                            def calories(weight, height_ft, height_in, age, sex):
                                                REE = 0
                                                TDEE = 0
                                                weight_kg = math.ceil(float(weight) * 0.453592)
                                                height_cm = math.ceil(float((float(height_ft) * 12) + float(height_in)) * 2.54)
                                                if sex == "Male":
                                                    REE = (10 * weight_kg) + (6.25 * height_cm) - (5 * int(age)) + 5
                                                else:
                                                    REE = (10 * weight_kg) + (6.25 * height_cm) - (5 * int(age)) - 161 
                                                if (activity == "Sedentary: Little to no exercise"):
                                                    TDEE = math.ceil(float(REE) * 1.2)
                                                if (activity == "Light: exercise 1-3 times/week"):
                                                    TDEE = math.ceil(float(REE) * 1.375)
                                                if (activity == "Moderate: exercise 4-5 times/week"):
                                                    TDEE = math.ceil(float(REE) * 1.55)
                                                if (activity == "Very Active: intense exercise 6-7 times/week"):
                                                    TDEE = math.ceil(float(REE) * 1.725)
                                                return (TDEE)
                                            def adjusted_cal(goal):
                                                cals = 0
                                                TDEE = math.ceil(calories(weight, height_ft, height_in, age, sex))
                                                if goal == "Lose weight (cut)":
                                                    cals = TDEE - (TDEE * 0.2)
                                                if goal == "Gain weight (bulk)":
                                                    cals = TDEE + (TDEE * 0.2)
                                                if goal == "Maintain weight":
                                                    cals = TDEE
                                                return (math.ceil(cals))
                                            def carb(calories, protein, fat):
                                                carbs = 0
                                                calories = int(calories)
                                                adj_protein = int(protein) * 4
                                                adj_fat = int(fat) * 9
                                                carbs = math.ceil((calories - (adj_protein + adj_fat)) / 4)
                                                return(carbs)
                                            def sleep_stat(sleep):
                                                sleep_string = ""
                                                if int(sleep) >= 7:
                                                    sleep_string = "You have at least 7 hours of sleep. All good! Keep it up!"
                                                else:
                                                    sleep_string = "Aim for at least 7 hours of sleep to maximize fitness and health"
                                                return (sleep_string)
                                            def energy_levels(energy, sex):
                                                energy_string = ""
                                                if (energy == "Very low" or energy == "Low" or energy == "Moderate") and (sex == "Male"):
                                                    energy_string = "To increase energy levels, consider ways to control stress (yoga, meditation, etc), limit smoking, limit alcohol, and drink at least 3.7 liters of water"
                                                elif (energy == "Very low" or energy == "Low" or energy == "Moderate") and (sex == "Female"):
                                                    energy_string = "To increase energy levels, consider ways to control stress (yoga, meditation, etc), limit smoking, limit alcohol, and drink at least 2.7 liters of water"
                                                else:
                                                    energy_string = "All good! Keep it up!"
                                                return (energy_string)
                                            def mood_levels(mood):
                                                mood_string = ""
                                                if mood == "Depressed (sad or gloomy)":
                                                    mood_string = "Reach out to a health professional to consider psychotherapy or medications. Stay strong, I believe in you!"
                                                else:
                                                    mood_string = "All good! Keep it up!"
                                                return (mood_string)
                                            if (activity == "Sedentary: Little to no exercise") or (activity == "Light: exercise 1-3 times/week") or (activity == "Moderate: exercise 4-5 times/week") or (activity == "Active: daily exercise or intense excercise 3-4 times/week") or (activity == "Very Active: intense exercise 6-7 times/week"):
                                                final_string = ("--------------------------------------------------------------------------" + "\n" + "User Info" + "\n" + "--------------------------------------------------------------------------" + "\n" + "First Name: " + first_name + "\n" + "Last Name: " + last_name + "\n" + "Sex: " + sex + "\n" + "Age: " + age + "\n" + "Height: " + height_ft + "'" + height_in + "\n" + "Weight: " + weight + " lbs" + "\n" + "--------------------------------------------------------------------------" + "\n" + "Calories and Macronutrients" + "\n" + "--------------------------------------------------------------------------" + "\n" + 
                                                "Calorie intake: " + str(adjusted_cal(goal)) + " calories" + "\n" + "Protein intake (1g per lb of body weight): " + weight + " grams" + "\n" + "Fat intake (25% of overall calorie intake): " + str(int((adjusted_cal(goal) * 0.25) / 9)) + " grams" + "\n" + "Carb intake: " + str(carb(adjusted_cal(goal), weight, int((adjusted_cal(goal) * 0.25) / 9))) + " grams" + "\n" + "--------------------------------------------------------------------------" + "\n" + "Sleep" + "\n" + "--------------------------------------------------------------------------" + "\n" + "Sleep advice: " + sleep_stat(sleep) + "\n" +
                                                 "--------------------------------------------------------------------------" + "\n" + "Energy Levels" + "\n" + "--------------------------------------------------------------------------" + "\n" + "Energy levels advice: " + energy_levels(energy, sex) + "\n" + "--------------------------------------------------------------------------" + "\n" + "Mood Levels" + "\n" + "--------------------------------------------------------------------------" + "\n" + "Mood levels advice: " + mood_levels(mood) + "\n" + "--------------------------------------------------------------------------" + "\n" + "Sources: " + "\n" + "--------------------------------------------------------------------------" +
                                                "\n" + "https://healthyeater.com/how-to-calculate-your-macros" + "\n" + "https://www.health.harvard.edu/energy-and-fatigue/9-tips-to-boost-your-energy-naturally" + "\n" + "https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/water/art-20044256#:~:text=The%20U.S.%20National%20Academies%20of,fluids%20a%20day%20for%20women" + "\n" + "https://www.mayoclinic.org/diseases-conditions/depression/diagnosis-treatment/drc-20356013#:~:text=Medications%20and%20psychotherapy%20are%20effective,or%20other%20mental%20health%20professional.")
                                                tkinter.messagebox.showinfo("Results", final_string)
                                            else:
                                                tkinter.messagebox.showwarning("Activity Level Error", "Please enter valid activity level value (Sedentary: Little to no exercise, Light: exercise 1-3 times/week, Moderate: exercise 4-5 times/week, Very Active: intense exercise 6-7 times/week)")
                                        else:
                                            tkinter.messagebox.showwarning("Weight Error", "Please enter valid weight input")
                                            
                                    else:
                                         tkinter.messagebox.showwarning("Mood Level Error", "Please enter valid mood level input from dropdown (Depressed (sad or gloomy), Euthymia (normal feeling), Content (happy))")
                                else:
                                    tkinter.messagebox.showwarning("Energy Level Error", "Please enter valid energy level input from dropdown (Very low, Low, Moderate, High, Very High)")
                            else:
                                tkinter.messagebox.showwarning("Sleep Error", "Please enter valid sleep input")
                        else:
                            tkinter.messagebox.showwarning("Goal Error", "Please enter valid goal input from dropdown (Maintain weight, Gain weight (bulk), Lose weight (cut))")
                    else:
                        tkinter.messagebox.showwarning("Height Error", "Please enter valid height values")
                else:
                    tkinter.messagebox.showwarning("Age Error", "Please enter valid age option from the combobox (ranges 12-101)")
            else:
                tkinter.messagebox.showwarning("Sex Error", "Please enter valid sex option from the dropdown (Male or Female)")
        else:
            tkinter.messagebox.showwarning("Name Error", "Please enter first and last name using letters only.")

    else:
        tkinter.messagebox.showwarning("Error", "Please accept terms and conditions before retrieving data.")

#Window widget that pops up along with its preferred title
window = tkinter.Tk()
window.title("Fitness Helper")

#Main frame within the window widget
frame = tkinter.Frame(window)
frame.pack()

#Sub-frame within the main frame
user_info = tkinter.LabelFrame(frame, text = "Client Information")
user_info.grid(row = 0, column = 0, padx = 20, pady = 10)

#Sub-frame within the sub-frame
sub_frame = tkinter.LabelFrame(frame)
sub_frame.grid(row = 1, column = 0, padx= 20, pady = 10)

#ALL LABELS
#Labels within the first sub-frame
#First name label
first_name = tkinter.Label(user_info, text = "First Name:")
first_name.grid(row = 0, column = 0)
#Last name label
last_name = tkinter.Label(user_info, text = "Last Name:")
last_name.grid(row = 0, column = 1)
#Sex (multiple choice box option)
sex_label = tkinter.Label(user_info, text = "Sex")
sex_combobox = ttk.Combobox(user_info, values = ["Male", "Female"])
sex_label.grid(row = 2, column = 0)
sex_combobox.grid(row = 3, column = 0)
#Age Spinbox
age_label = tkinter.Label(user_info, text = "Age")
age_spinbox = tkinter.Spinbox(user_info, from_ = 12, to = 110)
age_label.grid(row = 2, column = 1)
age_spinbox.grid(row = 3, column = 1)
#Height
height_label_feet = tkinter.Label(user_info, text = "Height (feet)")
height_label_feet.grid(row = 4, column = 0)
height_spinbox = tkinter.Spinbox(user_info, from_ = 1, to = 8)
height_spinbox.grid(row = 5, column = 0)
height_label_inches = tkinter.Label(user_info, text = "(inches)")
height_label_inches.grid(row = 4, column = 1)
height_inches_spinbox = tkinter.Spinbox(user_info, from_ = 0, to = 11)
height_inches_spinbox.grid(row = 5, column = 1)
#Goal
goal_label = tkinter.Label(user_info, text = "Goal")
goal_combobox = ttk.Combobox(user_info, values = ["Maintain weight", "Gain weight (bulk)", "Lose weight (cut)"])
goal_label.grid(row = 6, column = 0)
goal_combobox.grid(row = 7, column = 0)
#Sleep
sleep_label = tkinter.Label(user_info, text = "Hours of sleep")
sleep_spinbox = tkinter.Spinbox(user_info, from_ = 0, to = 24)
sleep_label.grid(row = 6, column = 1)
sleep_spinbox.grid(row = 7, column = 1)
#Energy levels
energy_label = tkinter.Label(user_info, text = "Energy levels")
energy_combobox = ttk.Combobox(user_info, values = ["Very low", "Low", "Moderate", "High", "Very High"])
energy_label.grid(row = 8, column = 0)
energy_combobox.grid(row = 9, column = 0)
#Mood levels
mood_label = tkinter.Label(user_info, text = "Mood levels")
mood_combobox = ttk.Combobox(user_info, values = ["Depressed (sad or gloomy)", "Euthymia (normal feeling)", "Content (happy)" ])
mood_label.grid(row = 8, column = 1)
mood_combobox.grid(row = 9, column = 1)
#Weight
weight_label = tkinter.Label(user_info, text = "Weight (lbs)")
weight_label.grid(row = 10, column = 0)
weight_entry = tkinter.Entry(user_info)
weight_entry.grid(row = 11, column = 0)
#Activity level
activity_label = tkinter.Label(sub_frame, text = "Activity Level")
activity_combobox = ttk.Combobox(sub_frame, values = ["Sedentary: Little to no exercise", "Light: exercise 1-3 times/week", "Moderate: exercise 4-5 times/week", "Very Active: intense exercise 6-7 times/week"], width = 50)
activity_label.grid(row = 0, column = 0)
activity_combobox.grid(row = 1, column = 0)
#Entries for labels
first_name_entry = tkinter.Entry(user_info)
last_name_entry = tkinter.Entry(user_info)
#Actual labels for input entries
first_name_entry.grid(row = 1, column = 0)
last_name_entry.grid(row = 1, column = 1)
#Terms and Conditions
terms_frame = tkinter.LabelFrame(frame, text = "Terms and Conditions")
terms_frame.grid(row = 2, column = 0, padx = 20, pady = 5)
accept_var = tkinter.StringVar(value = "Not accepted")
terms_check = tkinter.Checkbutton(terms_frame, text = "I acknowledge that Fitness Helper is a program that provides an estimate of macronutrients needed for a specific goal along with reccomendations for lifestyle changes. I am liable for any action I take with this given information.",
                                  variable = accept_var, onvalue = "Accepted", offvalue = "Not accepted")
terms_check.grid(row = 1, column = 1)
#Button
button = tkinter.Button(frame, text = "Process Data", command = process_data, height = 1, width = 10)
button.grid(row = 3, column = 0)
#Widget spacing (aesthetics)
for widget in user_info.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

#Command to keep Window widget open until closed
window.mainloop()
