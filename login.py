import customtkinter as ctk
import mysql.connector
from mysql.connector import Error
import subprocess


# Connect to the MySQL database
def create_connection():
    return mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="sivakumar#", 
        database="heartattackpred"
    )


app = ctk.CTk()
app.geometry("300x205")


Userlabel = ctk.CTkLabel(app, text="Username", font=("Arial", 15))
Userlabel.place(x=25,y=50)

Userlabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 15))
Userlabelsemi.place(x=100,y=50)

UserEntry = ctk.CTkEntry(app)
UserEntry.place(x=140,y=50)

Passlabel = ctk.CTkLabel(app, text="Password", font=("Arial", 15))
Passlabel.place(x=25,y=90)

Passlabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 15))
Passlabelsemi.place(x=100,y=90)

PassEntry = ctk.CTkEntry(app)
PassEntry.place(x=140,y=90)

def validate_login():
    try:
        username = UserEntry.get()
        password = PassEntry.get()
        # Create a connection to the database
        db_connection = create_connection()
        cursor = db_connection.cursor()

        

        # SQL query to check if the user exists and the password matches
        cursor.execute("SELECT * FROM authentication WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            print("Login successful!")
            app.destroy()
            command = r"python C:\ProgrammingProjects\ML-Project\menu.py"
            subprocess.run(command)
            
        else:
            print("Invalid username or password.")
            Label = ctk.CTkLabel(app,text="Invalid Login")
            Label.place(x =100,y=170)

    except Error as e:
        print(f"Error: {e}")
    


LoginButton = ctk.CTkButton(app,text = "Login",command=validate_login)
LoginButton.place(x = 85,y=140)


app.mainloop()