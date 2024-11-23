import customtkinter as ctk
import joblib
import pandas as pd
import mysql.connector
from mysql.connector import Error
# Load the saved model
model = joblib.load("heartAttackModel.pkl")
print("Model loaded successfully!")

app = ctk.CTk()
app.geometry("700x720")

#Patient ID
PatientIDlabel = ctk.CTkLabel(app, text="PatientID", font=("Arial", 16))
PatientIDlabel.place(x=100,y=10)

PatientIDlabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
PatientIDlabelsemi.place(x=300,y=10)

PatientIDEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
PatientIDEntry.place(x=400,y=10)

#Age
Agelabel = ctk.CTkLabel(app, text="Age", font=("Arial", 16))
Agelabel.place(x=100,y=50)

Agelabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
Agelabelsemi.place(x=300,y=50)

AgeEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
AgeEntry.place(x=400,y=50)

#Gender
Genderlabel = ctk.CTkLabel(app, text="Gender", font=("Arial", 16))
Genderlabel.place(x=100,y=90)

Genderlabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
Genderlabelsemi.place(x=300,y=90)

GenderEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
GenderEntry.place(x=400,y=90)

#cp
CPlabel = ctk.CTkLabel(app, text="Chest Pain Type", font=("Arial", 16))
CPlabel.place(x=100,y=130)

CPlabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
CPlabelsemi.place(x=300,y=130)

CPEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
CPEntry.place(x=400,y=130)


#trestbps
TrestBPSlabel = ctk.CTkLabel(app, text="Resting BP", font=("Arial", 16))
TrestBPSlabel.place(x=100,y=170)

TrestBPSlabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
TrestBPSlabelsemi.place(x=300,y=170)

TrestBPSEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
TrestBPSEntry.place(x=400,y=170)

#chol
chollabel = ctk.CTkLabel(app, text="Serum Cholesterol", font=("Arial", 16))
chollabel.place(x=100,y=210)

chollabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
chollabelsemi.place(x=300,y=210)

cholEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
cholEntry.place(x=400,y=210)

#fbs
fbslabel = ctk.CTkLabel(app, text="Fasting Blood Sugar", font=("Arial", 16))
fbslabel.place(x=100,y=250)

fbslabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
fbslabelsemi.place(x=300,y=250)

fbsEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
fbsEntry.place(x=400,y=250)

#restecg
RestECGlabel = ctk.CTkLabel(app, text="Resting ECG", font=("Arial", 16))
RestECGlabel.place(x=100,y=290)

RestECGlabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
RestECGlabelsemi.place(x=300,y=290)

RestECGEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
RestECGEntry.place(x=400,y=290)

#thalachh
thalachhlabel = ctk.CTkLabel(app, text="Maximum heart rate", font=("Arial", 16))
thalachhlabel.place(x=100,y=330)

thalachhlabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
thalachhlabelsemi.place(x=300,y=330)

thalachhEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
thalachhEntry.place(x=400,y=330)

#exang
exanglabel = ctk.CTkLabel(app, text="Exercise-induced angina", font=("Arial", 16))
exanglabel.place(x=100,y=370)

exanglabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
exanglabelsemi.place(x=300,y=370)

exangEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
exangEntry.place(x=400,y=370)

#oldpeak
oldpeaklabel = ctk.CTkLabel(app, text="ST depression", font=("Arial", 16))
oldpeaklabel.place(x=100,y=410)

oldpeaklabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
oldpeaklabelsemi.place(x=300,y=410)

oldpeakEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
oldpeakEntry.place(x=400,y=410)

#slope
slopelabel = ctk.CTkLabel(app, text="Slope of the peak exercise\nST segment", font=("Arial", 16))
slopelabel.place(x=100,y=450)

slopelabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 11))
slopelabelsemi.place(x=300,y=450)

slopeEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
slopeEntry.place(x=400,y=450)

#ca
calabel = ctk.CTkLabel(app, text="Number of major vessels\n(0-3) colored by fluoroscopy", font=("Arial", 16))
calabel.place(x=100,y=510)

calabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 11))
calabelsemi.place(x=300,y=510)

caEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
caEntry.place(x=400,y=510)

#thal
thallabel = ctk.CTkLabel(app, text="Thalassemia type", font=("Arial", 16))
thallabel.place(x=100,y=550)

thallabelsemi = ctk.CTkLabel(app, text=":", font=("Arial", 16))
thallabelsemi.place(x=300,y=550)

thalEntry = ctk.CTkEntry(app, placeholder_text="Enter text here")
thalEntry.place(x=400,y=550)

Entries = [AgeEntry,GenderEntry,CPEntry,TrestBPSEntry,cholEntry,fbsEntry,RestECGEntry,thalachhEntry,exangEntry,oldpeakEntry,slopeEntry,caEntry,thalEntry]
# Values = [[]]
Columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
Values = [["Umesh",67,0,2,152,277,0,1,172,0,0.0,2,1,2]]
Values1 = [[67,0,2,152,277,0,1,172,0,0.0,2,1,2]]
#prediction
def predfunc():
    # for i in Entries:
    #     text = i.get()
    #     Values[0].append(text)
    X_Df =  pd.DataFrame(Values1, columns=Columns)
    print(X_Df)
    prediction = model.predict(X_Df)
    if prediction == [1]:
        Text = "High Risk"
    else:
        Text = "Low Risk"
    predLabel = ctk.CTkLabel(app, text=Text, font=("Arial", 16,),text_color="green")
    predLabel.place(x=280,y=650)
    print(prediction)
    # model = joblib.load("heartAttackModel.pkl")
    # model.predict()

def saveInDB():
    # Connect to the MySQL database
    db_connection = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="sivakumar#", 
        database="heartattackpred"
    )
    cursor = db_connection.cursor()
    values=""
    for i in Values[0]:
        if type(i) == str:
            values += '"'
            txt = str(i)
            values+=txt
            values += '",'
        else:
            txt = str(i)+","
            values+=txt
        
    values = values[0:-1]
    
    command = f"""INSERT INTO heartattackpred.patientrecords(PatientName,age, sex, cp, trestbps, chol, fbs, restecg, thalachh, exang, oldpeak, slope, ca, thal) Values({values})"""
    print(command)
    cursor.execute(command)
    db_connection.commit()
    cursor.close()
    db_connection.close()
    savedLabel = ctk.CTkLabel(app, text="Saved in DB", font=("Arial", 16,),text_color="green")
    savedLabel.place(x=280,y=650)

predButton = ctk.CTkButton(app, text="Predict", command=predfunc)
predButton.place(x=140,y=610)

SaveButton = ctk.CTkButton(app,text="Save in DB",command=saveInDB)
SaveButton.place(x=340,y=610)

app.mainloop()
