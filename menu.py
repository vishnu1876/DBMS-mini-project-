import customtkinter as ctk
import subprocess
app = ctk.CTk()
app.geometry("300x205")

def PredictNew():
    app.destroy()
    command = r"python C:\ProgrammingProjects\ML-Project\predict.py"
    subprocess.run(command)
    

PredictNewButton = ctk.CTkButton(app,text = "Predict New Record",command=PredictNew)
PredictNewButton.place(x = 85,y=50)


ViewTableButton = ctk.CTkButton(app,text = "View Predictions",)
ViewTableButton.place(x = 85,y=105)


app.mainloop()


