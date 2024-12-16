import csv
import os

# Quick Fix
Path = os.path.dirname(os.path.abspath(__file__))
List = os.path.join(Path, 'List.csv')
Data = os.path.join(Path, 'Data.csv')
Theme = os.path.join(Path, 'Theme.csv')
Professor = os.path.join(Path, 'Professor.csv')

#Baca List
Local_List = []
with open(List, mode='r') as file:
    reader = csv.reader(file)
    Local_List = [row for row in reader]
Local_Data = []
with open(Data, mode='r') as file:
    reader = csv.reader(file)
    Local_Data = [row for row in reader]
Local_Theme = []
with open(Theme, mode='r') as file:
    reader = csv.reader(file)
    Local_Theme = [row for row in reader]
Local_Professor = []
with open(Professor, mode='r') as file:
    reader = csv.reader(file)
    Local_Professor = [row for row in reader]

# Login
def Login(List):
    Name = input("Masukan nama: ")
    NRP = input("Masukan NRP: ")

    for user in List:
        if user[0] == Name and user[1] == NRP:
            print(f"Welcome, {Name}!")
            return True, Name

    print("Invalid bro, coba aja lagi.")
    return False, None

# Mengusulkan TA
def Apply(Name, Local_Theme, Local_Professor):
    Title = input("Judul TA : ")
    
    Key = 1
    while Key == 1:
        Theme = input("Tema TA : ")
        if Theme in [item for item in Local_Theme[0]]:
            Key = 0
        else:
            print("Tema salah, ulangi lagi.")
    
    # Plotting Dosen
    Professor = Local_Professor[0][Local_Theme[0].index(Theme)]
            
    Link = input("Link Tugas : ")
    Extra_Data = [[Name, Title, Theme, Professor, Link]]
    
    if Title and Theme and Link:
        return True, Extra_Data
    
    print("Coba lagi bro.")
    return False, None

#Start disini
Starter = 1
while Starter == 1:
    
    Key = False
    while Key == False:
        Key, Name = Login(Local_List)
        
    if Name in [row[0] for row in Local_Data]:
        print("Nama sudah terdaftar.")
        for A in range(len(Local_Data)):
            if Name in Local_Data[A]:
                print(Local_Data[A])
                break
    
    else:
        Key2, Extra_Data = Apply(Name, Local_Theme, Local_Professor)
        if Key2 == True:
            Local_Data += Extra_Data
            with open(Data, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(Local_Data)

    Starter = int(input("Lagi (0/1)? "))
