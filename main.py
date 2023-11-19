import mysql.connector
from easygui import passwordbox
import csv
from prettytable import PrettyTable
from datetime import date
import pywhatkit
import random
from datetime import datetime
import pyautogui as pg
import feedback


print('\t\t\t\t\t\t\t\t\t\t\t\tWelcome to the online examination system ')
today = date.today()
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", today)


# cs
cs_paper = open("cs.csv", "a", newline='')
cs_paper2 = open("cs.csv", "r", newline='')
content_cs = csv.writer(cs_paper, delimiter=',')
read_cs = csv.reader(cs_paper2, delimiter=',')
score_rec_cs = open("Score_cs.csv", "a+", newline='')
score_write_cs = csv.writer(score_rec_cs, delimiter=',')
score_read_cs = csv.reader(score_rec_cs)


# English
english_paper = open("english.csv", "a", newline='')
english_paper2 = open("english.csv", "r", newline='')
content_english = csv.writer(english_paper, delimiter=',')
read_english = csv.reader(english_paper2, delimiter=',')
score_rec_english = open("Score_english.csv", "a+", newline='')
score_write_english = csv.writer(score_rec_english, delimiter=',')
score_read_english = csv.reader(score_rec_english)


# Chemistry
chemistry_paper = open("Chemistry.csv", "a", newline='')
chemistry_paper2 = open("Chemistry.csv", "r", newline='')
content_chemistry = csv.writer(chemistry_paper, delimiter=',')
read_chemistry = csv.reader(chemistry_paper2, delimiter=',')
score_rec_chemistry = open("Score_Chemistry.csv", "a+", newline='')
score_write_chemistry = csv.writer(score_rec_chemistry, delimiter=',')
score_read_chemistry = csv.reader(score_rec_chemistry)

# Physics
physics_paper = open("Physics.csv", "a", newline='')
physics_paper2 = open("Physics.csv", "r", newline='')
content_physics = csv.writer(physics_paper, delimiter=',')
read_physics = csv.reader(physics_paper2, delimiter=',')
score_rec_physics = open("Score_Physics.csv", "a", newline='')
score_write_physics = csv.writer(score_rec_physics, delimiter=',')
score_read_physics = csv.reader(score_rec_physics)


# Maths
maths_paper = open("Maths.csv", "a", newline='')
maths_paper2 = open("Maths.csv", "r", newline='')
content_maths = csv.writer(maths_paper, delimiter=',')
read_maths = csv.reader(maths_paper2, delimiter=',')
score_rec_maths = open("Score_maths.csv", "a+", newline='')
score_write_maths = csv.writer(score_rec_maths, delimiter=',')
score_maths=open("Score_maths.csv", "r")
score_read_maths = csv.reader(score_rec_maths)


"""# feedback / reviews
feedback = open("feedback.csv", "a", newline='')
feedback2 = open("feedback.csv", "r")
content_feed = csv.writer(feedback, delimiter=',')
read_feed = csv.reader(feedback2, delimiter=',')
"""

# Creating Student Databases
mydb=mysql.connector.connect(
 host="localhost",
 user="Sonali",
 passwd="sohmchacha",
 database="students"
 )
c=mydb.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS students")
c.execute("CREATE TABLE IF NOT EXISTS stu_name(Roll_No INT AUTO_INCREMENT PRIMARY KEY, \
Name VARCHAR(100), \
Password VARCHAR(100), \
Father VARCHAR(250), \
Mother VARCHAR(250), \
Email VARCHAR(100), \
DOB VARCHAR(100), \
Mobile VARCHAR(11), \
Board VARCHAR(100), \
Sate VARCHAR(100), \
City VARCHAR(50)) ")


# Creating Teacher Databases
mydb=mysql.connector.connect(
 host="localhost",
 user="Sonali",
 passwd="sohmchacha",
 database="students"
 )
c=mydb.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS teachers")
c.execute("CREATE TABLE IF NOT EXISTS stu_name(Teacher_ID INT AUTO_INCREMENT PRIMARY KEY, \
Teacher VARCHAR(100), \
Password VARCHAR(100), \
Subject VARCHAR(100), \
Father VARCHAR(250), \
Mother VARCHAR(250), \
Email VARCHAR(100), \
DOB VARCHAR(100), \
Mobile VARCHAR(11), \
Sate VARCHAR(100), \
City VARCHAR(50)) ")



def Verify_User():   #Working fine
    cond = False
    while cond == False:
        uName = input('Enter designation (admin/teacher/student) : ')
        password = passwordbox('Enter your Password')
        if uName.lower() == password == "admin":
            admin()
            cond = True
        elif uName.lower() == password == 'student':
            student()
            cond = True
        elif uName.lower() == password == 'teacher':
            teacher()
            cond = True
        else:
            print("Incorrect username or password!!")
            print("Access Denied, Kindly try again!! \n")

def admin():   #Working fine
    while True:
        print('------------Tasks-------------------')
        print('1: Add student')
        print('2: Delete student')
        print("3: Display Students")
        print('4: Search Student')                                              
        print('5: Add teacher')
        print('6: Delete teacher')
        print("7: Display teacher")
        print('8: Search teacher')
        print('9: Give Feedback')
        print("10: Exit")
        try:
            choice = int(input('Enter your choice : '))
            if choice == 1:
                Student_List()
            elif choice == 2:
                delete_stu()
            elif choice == 3:
                display_stu()
            elif choice == 4:
                search_student()
            elif choice == 5:
                Add_Teacher()
            elif choice == 6:
                Delete_teacher()
            elif choice == 7:
                Display_teacher()
            elif choice == 8:
                Search_teacher()
            elif choice == 9:
                NAME = input("Enter your Name : ")
                feedback.feedback(NAME)
            else:
                break
        except ValueError:
            print("Invalid input !!!")


def Add_Teacher():
    teaName = input("Enter the teacher's name : ")
    Fname = input("Enter the teacher's father name : ")
    Mname = input("Enter the teacher's mother name : ")
    Subject = input("Enter the teacher's Subject : ")
    while True:
        value = input("Enter teacher's Email ID : ")
        if '@' in value and '.com' in value:
            break
        else:
            print("Invalid Email ID\n")
    while True:
        dob = input("Enter date of birth (DD-MM-YYYY) : ")
        if len(dob) == 10 and dob[2] == dob[5] == "-":
            break
        else:
            print("Invalid DOB format !!\n")
    Add = input("Enter the Address : ")
    while True:
        mob = input("Enter the mobile no. : ")
        if len(mob) == 10:
            break
        else:
            print("Invalid Mobile No.")

    while True:
        teaPass = input("Enter the teacher's password : ")
        if len(teaPass) > 8 and '@' or '.' or '#' or '$' or '%' or '&' or '*' or '!' in teaPass:
            break
        else:
            print("Length of password should be more than 8 characters")
    State = input("Enter the states name : ")
    City = input("Enter the city's name : ")
    mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="teachers")
    mycursor = mydb.cursor()
    query = "insert into teachers(Teacher, Password, Subject, Father, Mother, Email, DOB, Mobile, State, City) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(query, (teaName, teaPass, Subject, Fname, Mname, value, dob, mob, State, City))
    mydb.commit()
    print("Teacher added successfully !!!")


"""def feedback(x):
    global feedback
    feed = input("Enter your feedback : ")
    content_feed.writerow([x, feed])
    print("Record successfully updated!!")"""


def Search_teacher():
    roll_no = int(input("Enter ID of teacher to be searched : "))
    mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="teachers")
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("select * from teachers where Teacher_ID = %s", (roll_no, ))
    mydb.commit()
    display = PrettyTable()
    display.field_names = ["Teacher ID", "Teacher", "Password", "Subject", "Father's Name", "Mother's Name", "Email", "DOB", "Mobile No.", "State", "City"]
    for i in mycursor:
        display.add_row(i)
    print(display)


def update_pass(roll):
    passWord = passwordbox("Enter your new password : ")
    mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha",
                                   database="teachers")
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("update teachers set password = %s where Teacher_ID = %s;", (passWord, roll))
    mydb.commit()
    print("Password successfully updated !!!!!!!!!")


def Display_teacher():
    mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="teachers")
    mycursor = mydb.cursor()
    mycursor.execute("select * from teachers")
    display = PrettyTable()
    display.field_names = ["Roll No.", "Name", "Password", "Father's Name", "Mother's Name", "Email", "DOB", "Mobile No.", "Board", "State", "City"]
    for i in mycursor:
        display.add_row(i)
    print(display)


def Delete_teacher():
    roll_no = int(input("Enter ID of Teacher to be deleted : "))
    mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="teachers")
    mycursor = mydb.cursor()
    mycursor.execute("delete from teachers where Teacher_ID = %s", (roll_no, ))
    mydb.commit()
    print("Teacher successfully deleted !!")


def set_ques_paper(a, b):
    ans = 'y'
    while ans == 'y':
        question = input("Enter the question : ")
        opt1 = input("Enter the first option : ")
        opt2 = input("Enter the second option : ")
        opt3 = input("Enter the third option : ")
        opt4 = input("Enter the fourth option : ")
        sol = int(input("Enter the correct option : "))
        a.writerow([question, opt1, opt2, opt3, opt4, sol])
        ans = input("Do you want to add more questions : ")
    b.close()


def teacher_menu():
    print("---------------------------------What you want to do--------------------------------------------")
    print("1 : Set Question Paper")
    print("2 : Check Students Progress")
    print("3 : Delete Student's Response")
    print("4 : Update Password")
    print("5 : Give Feedback")
    print("6 : Exit")


def delete_stu_ans(a):
    lines = list()
    members = input("Please enter a Student's Name to be deleted : ")
    with open(a, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == members.lower():
                    lines.remove(row)
    with open(a, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
        writeFile.close()
    print("Student's response successfully deleted !!")


def check_stu_progress(file):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        display = PrettyTable()
        display.field_names = ["Student", "Marks"]
        for row in spamreader:
            display.add_row([row[0], row[1]])
            print(display)



def teacher():   #Working fine
    roll = int(input("Enter your ID : "))
    ask = input("Do you remember your password ? (y/n) :")
    if ask == 'y':
        passcode = passwordbox("Enter your password : ")
        mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="teachers")
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select * from teachers where Teacher_ID = %s", (roll, ))
        mydb.commit()
        for i in mycursor:
            Name = i[2]
            if i[2] == passcode:
                print("Access Granted !!!!")
                print("You are a :", i[3], "teacher")
                if i[3] in ["Physics", "physics", "PHYSICS"]:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t Subject : Physics")
                    while True:
                        teacher_menu()
                        choice = int(input("Enter your choice : "))
                        if choice == 1:
                            set_ques_paper(content_physics, physics_paper)
                            continue
                        if choice == 2:
                            check_stu_progress("Score_Physics.csv")
                            continue
                        if choice == 3:
                            delete_stu_ans("Score_Physics.csv")
                            continue
                        if choice == 4:
                            update_pass(i[0])
                            continue
                        if choice == 5:
                            feedback.feedback(Name)
                            continue
                        else:
                            break
                if i[3] in ["Maths", "maths", "MATHS"]:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t Subject : Maths")
                    while True:
                        teacher_menu()
                        choice = int(input("Enter your choice : "))
                        if choice == 1:
                            set_ques_paper(content_maths, maths_paper)
                            continue
                        if choice == 2:
                            check_stu_progress("Score_maths.csv")
                            continue
                        if choice == 3:
                            delete_stu_ans("Score_maths.csv")
                            continue
                        if choice == 4:
                            update_pass(i[0])
                            continue
                        if choice == 5:
                            feedback.feedback(Name)
                            continue
                        else:
                            break
                if i[3] in ["Chemistry", "chemistry", "CHEMISTRY"]:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t Subject : Chemistry")
                    while True:
                        teacher_menu()
                        choice = int(input("Enter your choice : "))
                        if choice == 1:
                            set_ques_paper(content_chemistry, chemistry_paper)
                            continue
                        if choice == 2:
                            check_stu_progress("Score_Chemistry.csv")
                            continue
                        if choice == 3:
                            delete_stu_ans("Score_Chemistry.csv")
                            continue
                        if choice == 4:
                            update_pass(i[0])
                            continue
                        if choice == 5:
                            feedback.feedback(Name)
                            continue
                        else:
                            break
                if i[3] in ["English", "english", "ENGLISH"]:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t Subject : English")
                    while True:
                        teacher_menu()
                        choice = int(input("Enter your choice : "))
                        if choice == 1:
                            set_ques_paper(content_english, english_paper)
                            continue
                        if choice == 2:
                            check_stu_progress("Score_english.csv")
                            continue
                        if choice == 3:
                            delete_stu_ans("Score_english.csv")
                            continue
                        if choice == 4:
                            update_pass(i[0])
                            continue
                        if choice == 5:
                            feedback.feedback(Name)
                            continue
                        else:
                            break
                if i[3] in ["Computer", "computer", "COMPUTER"]:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t Subject : Computer Science")
                    while True:
                        teacher_menu()
                        choice = int(input("Enter your choice : "))
                        if choice == 1:
                            set_ques_paper(content_cs, cs_paper)
                            continue
                        if choice == 2:
                            check_stu_progress("Score_cs.csv")
                            continue
                        if choice == 3:
                            delete_stu_ans("Score_cs.csv")
                            continue
                        if choice == 4:
                            update_pass(i[0])
                            continue
                        if choice == 5:
                            feedback.feedback(Name)
                            continue
                        else:
                            break
    elif ask == 'n':
        mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="teachers")
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select * from teachers where Teacher_ID = %s", (roll, ))
        otp = random.randint(100000, 999999)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        msg = "Thankyou for choosing our platform your OTP for app verification is : " + str(otp)
        for i in mycursor:
            mob = int(i[8])
        time = str(current_time)
        hour = int(time[:2])
        min = int(time[3:5])
        mobile = "+91" + str(mob)
        pywhatkit.sendwhatmsg(mobile, msg, hour, min + 2, 32)
        ask_otp = passwordbox("Kindly enter the OTP : ")
        pg.hotkey("Windows", "Down")
        pg.press("Enter")
        if ask_otp == str(otp):
            mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="teachers")
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("select * from teachers where Teacher_ID = %s", (roll,))
            mydb.commit()
            for i in mycursor:
                Name = i[2]
                print("Access Granted !!!!")
                print("You are a :", i[3], "teacher")
                if i[3] in ["Physics", "physics", "PHYSICS"]:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t Subject : Physics")
                    while True:
                        teacher_menu()
                        choice = int(input("Enter your choice : "))
                        if choice == 1:
                            set_ques_paper(content_physics, physics_paper)
                            continue
                        if choice == 2:
                            check_stu_progress("Score_Physics.csv")
                            continue
                        if choice == 3:
                            delete_stu_ans("Score_Physics.csv")
                            continue
                        if choice == 4:
                            update_pass(i[0])
                            continue
                        if choice == 5:
                            feedback.feedback(Name)
                            continue
                        else:
                            break
                if i[3] in ["Maths", "maths", "MATHS"]:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t Subject : Maths")
                    while True:
                        teacher_menu()
                        choice = int(input("Enter your choice : "))
                        if choice == 1:
                            set_ques_paper(content_maths, maths_paper)
                            continue
                        if choice == 2:
                            check_stu_progress("Score_maths.csv")
                            continue
                        if choice == 3:
                            delete_stu_ans("Score_maths.csv")
                            continue
                        if choice == 4:
                            update_pass(i[0])
                            continue
                        if choice == 5:
                            feedback.feedback(Name)
                            continue
                        else:
                            break
                if i[3] in ["Chemistry", "chemistry", "CHEMISTRY"]:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t Subject : Chemistry")
                    while True:
                        teacher_menu()
                        choice = int(input("Enter your choice : "))
                        if choice == 1:
                            set_ques_paper(content_chemistry, chemistry_paper)
                            continue
                        if choice == 2:
                            check_stu_progress("Score_Chemistry.csv")
                            continue
                        if choice == 3:
                            delete_stu_ans("Score_Chemistry.csv")
                            continue
                        if choice == 4:
                            update_pass(i[0])
                            continue
                        if choice == 5:
                            feedback.feedback(Name)
                            continue
                        else:
                            break
                if i[3] in ["English", "english", "ENGLISH"]:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t Subject : English")
                    while True:
                        teacher_menu()
                        choice = int(input("Enter your choice : "))
                        if choice == 1:
                            set_ques_paper(content_english, english_paper)
                            continue
                        if choice == 2:
                            check_stu_progress("Score_english.csv")
                            continue
                        if choice == 3:
                            delete_stu_ans("Score_english.csv")
                            continue
                        if choice == 4:
                            update_pass(i[0])
                            continue
                        if choice == 5:
                            feedback.feedback(Name)
                            continue
                        else:
                            break
                if i[3] in ["Computer", "computer", "COMPUTER"]:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t Subject : Computer Science")
                    while True:
                        teacher_menu()
                        choice = int(input("Enter your choice : "))
                        if choice == 1:
                            set_ques_paper(content_cs, cs_paper)
                            continue
                        if choice == 2:
                            check_stu_progress("Score_cs.csv")
                            continue
                        if choice == 3:
                            delete_stu_ans("Score_cs.csv")
                            continue
                        if choice == 4:
                            update_pass(i[0])
                            continue
                        if choice == 5:
                            feedback.feedback(Name)
                            continue
                        else:
                            break


def attempt_paper(Name, read, score_read, score_write, score_rec):
    score = 0
    L = []
    try:
        found = False
        while found == False:
            for j in read:
                display = PrettyTable()
                display.field_names = ["Question", j[0]]
                display.add_row([1, j[1]])
                display.add_row([2, j[2]])
                display.add_row([3, j[3]])
                display.add_row([4, j[4]])
                print(display)
                ans = int(input("Enter your answer : "))
                if j == []:
                    continue
                if ans == int(j[5]):
                    print("Correct answer !!")
                    score += 4
                else:
                    print("wrong answer !!!!")
                    print("Correct answer was : ", j[5])
                    score -= 1
            print("Your your score is : ", score)
            score_write.writerow([Name, score])
            score_rec.close()
    except ValueError:
        print("You have already attempted the paper!!")


def student():      #Working fine
    roll = int(input("Enter your Roll Number : "))
    ask = input("Do you remember your password ? (y/n) : ")
    if ask == "y":
        passcode = passwordbox("Enter your password : ")
        mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="students")
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select * from stu_name where Roll_No = %s", (roll, ))
        mydb.commit()
        for i in mycursor:
            Name = i[2]
            if i[2] == passcode:
                print("Access Granted !!!!")
                while True:
                    print("----------------------------------Kindly choose from below options----------------------")
                    print("1 : Attempt Physics Paper")
                    print("2 : Attempt Chemistry Paper")
                    print("3 : Attempt Maths Paper")
                    print("4 : Attempt English Paper")
                    print("5 : Attempt CS Paper")
                    print("6 : Update Password")
                    print("7 : Exit")
                    choice = int(input("Enter your choice : "))
                    if choice == 1:
                        attempt_paper(Name, read_physics, score_read_physics, score_write_physics, score_rec_physics)
                    if choice == 2:
                        attempt_paper(Name, read_chemistry, score_read_chemistry, score_write_chemistry,
                                      score_rec_chemistry)
                    if choice == 3:
                        attempt_paper(Name, read_maths, score_read_maths, score_write_maths, score_rec_maths)
                    if choice == 4:
                        attempt_paper(Name, read_english, score_read_english, score_write_english, score_rec_english)
                    if choice == 5:
                        attempt_paper(Name, read_cs, score_read_cs, score_write_cs, score_rec_cs)
                    if choice == 6:
                        passWord = passwordbox("Enter your new password : ")
                        mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha",
                                                       database="students")
                        mycursor = mydb.cursor(buffered=True)
                        mycursor.execute("update stu_name set password = %s where Roll_No = %s;", (passWord, roll))
                        mydb.commit()
                        print("Password successfully updated !!!!!!!!!")
                    if choice == 7:
                        break
    elif ask == "n":
        mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="students")
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select * from stu_name where Roll_No = %s", (roll,))
        otp = random.randint(100000, 999999)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        msg = "Thankyou for choosing our platform your OTP for app verification is : " + str(otp)
        for i in mycursor:
            mob = int(i[7])
            Name = i[2]
        time = str(current_time)
        hour = int(time[:2])
        min = int(time[3:5])
        mobile = "+91" + str(mob)
        pywhatkit.sendwhatmsg(mobile, msg, hour, min + 2, 32)
        ask_otp = passwordbox("Kindly enter the OTP : ")
        pg.hotkey("Windows", "Down")
        pg.press("Enter")
        if ask_otp == str(otp):
            print("Access Granted !!!!")
            while True:
                print("----------------------------------Kindly choose from below options----------------------")
                print("1 : Attempt Physics Paper")
                print("2 : Attempt Chemistry Paper")
                print("3 : Attempt Maths Paper")
                print("4 : Attempt English Paper")
                print("5 : Attempt CS Paper")
                print("6 : Update Password")
                print("7 : Exit")
                choice = int(input("Enter your choice : "))
                if choice == 1:
                    attempt_paper(Name, read_physics, score_read_physics, score_write_physics, score_rec_physics)
                if choice == 2:
                    attempt_paper(Name, read_chemistry, score_read_chemistry, score_write_chemistry,
                                  score_rec_chemistry)
                if choice == 3:
                    attempt_paper(Name, read_maths, score_read_maths, score_write_maths, score_rec_maths)
                if choice == 4:
                    attempt_paper(Name, read_english, score_read_english, score_write_english, score_rec_english)
                if choice == 5:
                    attempt_paper(Name, read_cs, score_read_cs, score_write_cs, score_rec_cs)
                if choice == 6:
                    passWord = passwordbox("Enter your new password : ")
                    mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha",
                                                   database="students")
                    mycursor = mydb.cursor(buffered=True)
                    mycursor.execute("update stu_name set password = %s where Roll_No = %s;", (passWord, roll))
                    mydb.commit()
                    print("Password successfully updated !!!!!!!!!")
                if choice == 7:
                    break



def search_student():   #Working fine
    roll_no = int(input("Enter roll no of student to be searched : "))
    mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="students")
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("select * from stu_name where Roll_No = %s", (roll_no, ))
    mydb.commit()
    display = PrettyTable()
    display.field_names = ["Roll No.", "Name", "Password", "Father's Name", "Mother's Name", "Email", "DOB", "Mobile No.", "Board", "State", "City"]
    for i in mycursor:
        display.add_row(i)
    print(display)



def delete_stu():   #Working fine
    roll_no = int(input("Enter roll no of student to be deleted : "))
    mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="students")
    mycursor = mydb.cursor()
    mycursor.execute("delete from stu_name where Roll_No = %s", (roll_no, ))
    mydb.commit()
    print("Student successfully deleted !!")


def Student_List():   #Working fine
    stuName = input("Enter the students name : ")
    Fname = input("Enter the student's father name : ")
    Mname = input("Enter the student's mother name : ")
    Class = int(input("Enter the student's class : "))
    if Class > 10:
        stream = input("Enter the student's Stream : ")
    while True:
        value = input("Enter your Email ID : ")
        if '@' in value and '.com' in value:
            break
        else:
            print("Invalid Email ID\n")
    while True:
        dob = input("Enter date of birth (DD-MM-YYYY) : ")
        if len(dob) == 10 and dob[2] == dob[5] == "-":
            break
        else:
            print("Invalid DOB format !!\n")
    Add = input("Enter the Address : ")
    while True:
        mob = input("Enter the mobile no. : ")
        if len(mob) == 10:
            break
        else:
            print("Invalid Mobile No.")
    stuPass = input("Enter the student's password : ")
    board = input("Enter the board of student (CBSE, State board) : ")
    State = input("Enter the states name : ")
    City = input("Enter the city's name : ")
    mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="students")
    mycursor = mydb.cursor()
    query = "insert into stu_name(Name, Password, Father, Mother, email, DOB, Mobile, Board, State, City) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(query, (stuName, stuPass, Fname, Mname, value, dob, mob, board, State, City))
    mydb.commit()
    print("Student added successfully !!!")


def display_stu():
    mydb = mysql.connector.connect(host="localhost", user="Sonali", passwd="sohmchacha", database="students")
    mycursor = mydb.cursor()
    mycursor.execute("select * from stu_name")
    display = PrettyTable()
    display.field_names = ["Roll No.", "Name", "Password", "Father's Name", "Mother's Name", "Email", "DOB", "Mobile No.", "Board", "State", "City"]
    for i in mycursor:
        display.add_row(i)
    print(display)


def Helpline():
    help_dict = {"Admin": 9898989898, "Operator" : 7878787878, "Customer Care" : 9564200200, "Email" : "support@onlineexaminationsystem.py"}
    for i in help_dict:
        print(i, help_dict[i])


def thank_you():
    print("-------------------------------Thank-you for using our Software------------------------------------")
    print("-----------------------------Project Created by Class 12th Students--------------------------------")
    print("***************************************************************************************************")
    print("""Team member's are
    1. Shlok Shrikhande
    2. Krishna Patil""")
    print("****************************************************************************************************")


def welcome():
    while True:
        print("--------------------------------------------Kindly Select from following options ----------------------------------------------------------")
        print("1 : Login")
        print("2 : See our reviews")
        print("3 : How to Use ?")
        print("4 : Helpline No./Email")
        print("5 : Exit")
        try:
            ask = int(input("Enter your choice : "))
            if ask == 1:
                Verify_User()

            elif ask == 2:
                display = PrettyTable()
                display.field_names = ["Name", "FeedBack"]
                for i in feedback.read_feed:
                    display.add_row(i)
                print(display)
            elif ask == 3:
                print("""\t\t\t\t1. Enter 1 to login in the system
                2. Enter your designation and password(designation itself, CAPTCHA)
                3. If you are student or teacher enter your name followed by your password
                4. After this you can continue with using our platform
                                THANK-YOU!!!""")
                print("**********************************************************************************")
                print("|                              For Support or Help                               |")
                print("|                  Mail to : support@onlineexaminationsystem.py                  |")
                print("|                     OR give a missed call on 555-8888-5858                     |")
                print("|                                 THANK-YOU                                      |")
                print("**********************************************************************************")
            elif ask == 4:
                Helpline()
            else:
                thank_you()
                break
        except ValueError:
            print("Please enter valid input !!!")


welcome()