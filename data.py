import pandas as pd
import numpy as np
# import matplotlib.pylot as plt
import seaborn as sns

df=pd.read_csv("crime_incidents_messy.csv")
#Making headers understandable 
headers=["Incident_Id","Crime_type","District","City","State","address","Latitude","Longitude","Incident_DateTime","Officer_Id","Office_FirstName","Officer_LastName","Badge_number","Suspect_Id","Suspect_FirstName","Suspect_LastName","Suspect_Age","Suspect_Gender","Suspect_race","Victim_Id","Victim_FirstName","Victim_LastName","Victim_Age","Victim_Gender","Victim_Phone","Weapon_Used","Severity","Case_Status","Resolution","Num_Arrests","Property_loss(in USD)","Reported_Online","notes"]
df.columns=headers
#Basic insights of data :

#give data types of all columns

# print(df.dtypes)

#Statistical summary: for numerical fields

# print(df.describe())

#gives information about row number, data types and memory usage
# print(df.info())


#Converting to correct data types :

df["Property_loss(in USD)"] = pd.to_numeric(
    df["Property_loss(in USD)"],
    errors="coerce"
)

df.loc[df["Property_loss(in USD)"] < 0, "Property_loss(in USD)"] = np.nan

median_loss = df["Property_loss(in USD)"].median()

df["Property_loss(in USD)"] = df["Property_loss(in USD)"].fillna(median_loss)

#dropping null values:

#dropped null badge values because badge value can't have a average values

df.dropna(subset=["Badge_number"],axis=0)

#Replacing null values in numerical columns with their mean values
# print(df["Latitude"])
mean_Latitude=df["Latitude"].mean()
df["Latitude"].replace(np.nan,mean_Latitude)

mean_Longitude=df["Longitude"].mean()
df["Longitude"].replace(np.nan,mean_Longitude)

mean_Suspect_age=df["Suspect_Age"].mean()
df["Suspect_Age"].replace(np.nan,mean_Suspect_age)

mean_Victim_age=df["Victim_Age"].mean()
df.loc[df["Victim_Age"]<0,"Victim_Age"]=np.nan
df["Victim_Age"].replace(np.nan,mean_Victim_age)

mean_Suspect_age=df["Suspect_Age"].mean()
df.loc[df["Suspect_Age"]<0,"Suspect_Age"]=np.nan
df["Suspect_Age"].replace(np.nan,mean_Suspect_age)

# cleaning num_arrests column
df.loc[df["Num_Arrests"]<0,"Num_Arrests"]=np.nan

df["Num_Arrests"]=df["Num_Arrests"].fillna(0)

df["Num_Arrests"]=df["Num_Arrests"].astype("int")

df["Case_Status"]=df["Case_Status"].fillna("Open")
df["Case_Status"].replace(np.nan,"Open")

df["Resolution"]=df["Resolution"].fillna("No Action Taken")
df["Resolution"].replace(np.nan,"No Action Taken")

df["Reported_Online"]=df["Reported_Online"].fillna("Reported through another method")
df["Reported_Online"].replace(np.nan,"Reported through another method")
df.loc[df["Reported_Online"]=="1","Reported_Online"]="True"
df.loc[df["Reported_Online"]=="0","Reported_Online"]="False"

df["notes"]=df["notes"].fillna("No notes were provided for this crime....")

df["Weapon_Used"]=df["Weapon_Used"].fillna("No weapons were found on site")

df["Victim_Id"]=df["Victim_Id"].fillna("No yet Identified")
df["Victim_FirstName"]=df["Victim_FirstName"].fillna("Not yet identified")
df["Victim_LastName"]=df["Victim_LastName"].fillna("Not yet identified")

df["Suspect_Id"]=df["Suspect_Id"].fillna("No yet Identified")
df["Suspect_FirstName"]=df["Suspect_FirstName"].fillna("Not yet identified")
df["Suspect_LastName"]=df["Suspect_LastName"].fillna("Not yet identified")

# df.dropna(inplace=True)
# Nogender=df["Victim_Gender"].isna().sum()
# print(Nogender)
df["Victim_Gender"]=df["Victim_Gender"].fillna("Unknown")

df["Suspect_Gender"]=df["Suspect_Gender"].fillna("Unknown")
print(df.head(10))

# print(df["Latitude"])

# print(df["Suspect_FirstName"].head(30))
df.to_csv("cleaned_crime_data.csv")
print("Successfully written the data in the file")
