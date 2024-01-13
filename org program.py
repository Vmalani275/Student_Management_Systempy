import pickle
import os
def get_files_needed_path(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    files_needed_path = os.path.join(current_path, "Files_Needed", filename)
    return files_needed_path
def adminlogin(x):
    adminnames=['vansh','krish','manthan','mihir']
    unames = ['020705', '090605', '060805','170106']
    passwords=['vans2005','kris2005','mant2005','mihi2006']
    if x in adminnames:
        indexingadminnames=adminnames.index(x)
        if str(indexingadminnames).isdigit:
            uname=input("please enter your username:")
            if uname in unames and unames.index(uname)==indexingadminnames:
                indexing=unames.index(uname)                
                if str(indexing).isdigit: 
                    password= input("please enter the password for the username below.")
                    if password in passwords and passwords.index(password)==indexing:
                        print("Welcome",adminnames[indexingadminnames].capitalize())
                    else:
                        print("invalid password. program will terminate.")
                        exit()
            elif uname in unames and unames.index(uname)!=indexingadminnames:
                print("your name and username entered are not matched. program will terminate.")
                exit()            
            elif x not in unames:
                print("username entered is invalid. program will terminate")
                exit()
    elif x not in adminnames:
        print("you are not recognized as an authorised admin member. the program will terminate.")
        exit()
def staffloginwithpass(z):
    teachnames=['Anil Trivedi','Nimesh Ravalji','Reshma Pillai','Hitesh Patel','Salma Paleja','Satya Ramesh','Geetha Velayudhan']
    unames = ['anil', 'nimesh', 'reshma','hitesh','salma','satya','rama','geetha']
    passwords=['anitri','nimrav','respill','hitpat','salpal','satram','geevel']
    file_path=get_files_needed_path("teach.txt")
    staffdat=open(file_path,'r')
    lines=staffdat.readlines()
    tech=[]
    namecap=z.capitalize()
    index=0
    if z in unames:
        indexingteachnames=unames.index(z)
        if str(indexingteachnames).isdigit:
            if z in unames and unames.index(z)==indexingteachnames:
                indexing=unames.index(z)
                tempname=teachnames[indexing]                
                if str(indexing).isdigit: 
                    password= input("Please enter the password for the username: {} \nPassword:".format(tempname))
                    if password in passwords and passwords.index(password)==indexing:
                        for line in lines:
                            if namecap in line:
                                tech.insert(index,line)
                                index+=1
                            staffdat.close()
                            if index==1:
                                print("Welcome",str(tech)[2:-4],"of V and C Patel School")
                                break
                    else:
                        print("invalid password. program will terminate.")
                        exit()
            elif z in unames and unames.index(z)!=indexingteachnames:
                print("Your name and username entered do not match. The program will terminate.")
                exit()                
            elif z not in unames:
                print("Username entered is invalid. Program will terminate")
                exit()
    elif z not in teachnames:
        print("You are not recognized as an authorised faculty. The program will terminate.")
        exit()
def invalid_entry():
    print("Invalid entry. Try again.")
def programrules():
    print(''' **********RULES*****************
IF YOU WANT TO EXIT THE PROGRAM AT ANY TIME, PRESS "*" AND ENTER.
IF YOU WANT TO GO BACK TO PREVIOUS MENU, USE "#"'''          )
def goodbye():
    print('''------------------------------------------------------------------------------------------------------------------------------
|We hope your experience with this program was good. Please contact the administrators and give your reviews about this program.|
|    Name            |Contact No|                                                                                           |
|    Charlie Puth    |1111111111|                                                                                           |
|    Ruskin Bond     |1111111111|                                                                                           |
|    Robert Clive    |1111111111|                                                                                           |
|    Vansh Malani    |1111111111|                                                                                           |
------------------------------------------------------------------------------------------------------------------------------''')
    exit()
def invalidandprogramrules():
    invalid_entry()
    programrules()
adminnames=['Vansh Malani','Krish Lad','Manthan Punjabi','Mihir Thakkar']
while True:
    username=input("Please enter your name:")
    print("Welcome,",username.capitalize())
    programrules()
    stafforstud=input('''Enter your position
    1.Staff.
    2.Student.
    3.Administrator.
    *.Exit the program:''')
    logintype=""
    if stafforstud=="*":
        goodbye()         
    elif int(stafforstud)==1:
        staffloginwithpass(username)
        logintype="staff"
        
        while True:
            print(''' What would you like to do?
        1. View students list.
        2. View all student's percentage.
        3. View student's attendence.
        4. Enter Remarks For Stuendents.
        5. View all student's remarks.
        #. Go to previous menu.
        *. Exit the program.
        ''')
            teachchoice=input("please enter your choice:")
            if teachchoice=='1':
                file_path=get_files_needed_path("stu.dat")
                stufile=open(file_path,"rb")
                try:
                    while True:
                        data=pickle.load(stufile)
                        print(data)
                except EOFError:
                    stufile.close()
            elif teachchoice=='2':
                    stuper_path=get_files_needed_path("names_with_percentage.dat")
                    stuper=open(stuper_path,"rb")
                    try:
                        while True:
                            percent=pickle.load(stuper)
                            print(percent)
                    except EOFError:
                        stuper.close()
            elif teachchoice=="3":
                attend_path=get_files_needed_path("attendence.dat")
                stuattendence=open(attend_path,"rb")
                try:
                    while True:
                        attendence=pickle.load(stuattendence)
                        print(attendence)
                except EOFError:
                    stuattendence.close()
            elif teachchoice=="4":
                file1_path=get_files_needed_path("stu.txt")
                stufile1=open(file1_path)
                file1_path=get_files_needed_path("remarks.txt")
                stureview=open(file1_path,'w')
                file1_path=get_files_needed_path("names_with_percentage.txt")
                stupercent=open(file1_path,'r')
                ans='y'
                while ans=='y':
                    str=stufile1.readline()
                    print(str)
                    y=stupercent.readline()
                    print("10th std percentage of",y)
                    review=input("Enter remark:")
                    stureview.write(y[:-1]+", Remarks:"+review+"\n")
                    ans=input("want to enter more records?(y/n)")
                stureview.close()
            elif teachchoice=="5":
                remarks_path=get_files_needed_path("remarks.dat")
                stufile=open(remarks_path,"rb")
                try:
                    while True:
                        data=pickle.load(stufile)
                        print(data)
                except EOFError:
                    stufile.close()
            elif teachchoice=="*":
                goodbye()
            elif teachchoice=="#":
                print("The program will restart now if you press #. would you rather exit the program?")
                choice=input("* for exiting and # for restarting the program")
                if choice=="#":
                    break
                elif choice=="*":
                    goodbye()
            else:
                invalidandprogramrules()
    elif int(stafforstud)==2:
        while True:
            choicestud=input('''Select your designation
            1.Old student.
            2.Apply for admission.
            #.Go to the previous menu.
            *.Exit the program.
            ''')
            if choicestud=="#":
                print("The program will restart now if you press #. would you rather exit the program?")
                choice=input("* for exiting and # for restarting the program")
                if choice=="#":
                    break
                elif choice=="*":
                    goodbye()
                else:
                    invalidandprogramrules()
            elif choicestud=='*':
                goodbye()
            elif choicestud=="1":
                file1_path=get_files_needed_path("stu.txt")
                stufile=open(file1_path,'r')
                file1_path=get_files_needed_path("names.txt")
                namefile=open(file1_path,'r')
                lines=namefile.readlines()
                index=0
                stu=[]
                for line in lines:
                    if username+"," in line:
                        stu.insert(index,line)
                        index+=1
                        break
                namefile.close()
                if len(stu)==0:
                    studadd=input("your name is not registered with the database. Would you like to apply for an admission")
                    if studadd=='yes' or studadd=='y' or studadd=='1':
                        print("Please select option 2 in the previous menu")
                        print("the program will terminate now.")
                        goodbye()
                    else:
                        print("The program will terminate now.")
                        exit()
                stu=[]
                index=0                        
                rollnumber=input("Enter your Roll Number:")
                lines=stufile.readlines()
                for line in lines:
                    if rollnumber+"," in line:
                        stu.insert(index,line)
                        index+=1
                        break
                stufile.close()
                if len(stu)==0:
                    studadd=input("You are not recognized as an authorised student. Would you like to apply for an admission?")
                    if studadd=='yes' or studadd=='y' or studadd=='1':
                        print("Please select option 2 in the previous menu")
                    else:
                        print("The program will terminate now.")
                        exit()
                elif index==2:
                    print("Your roll number is incorrect. Try again.")
                else:
                    if username.capitalize() in str(stu):
                        linelen=len(stu)
                        for i in range(linelen):
                            print(end=stu[i])
                            logintype="student"
                    else:
                        print("The name entered does not match with the rollnumber. Please try again")
            elif choicestud=="2":
                file1_path=get_files_needed_path("admissions.txt")
                admissionsfile=open(file1_path,"r")
                file1_path=get_files_needed_path("stu.txt")
                stufile=open(file1_path,'r')
                file1_path=get_files_needed_path("admitnames.txt")
                admitnames=open(file1_path,"w")
                lengthadmissions=len(admissionsfile.readlines())
                print(lengthadmissions)
                length=len(stufile.readlines())+lengthadmissions
                print(length)
                name=input("Please enter your full name:")
                admitnames.write(name+"\n")
                rollnumber=str(length+1)
                dob=input("Please enter your date of birth in dd/mm/yyyy format:")
                gen=input("Please enter your gender as Female/Male:")
                rec=name+","+rollnumber+","+dob+","+gen+"\n"
                file1_path=get_files_needed_path("admissions.txt")
                admissionsfile=open(file1_path,"a+")
                admissionsfile.write(rec)
                admissionsfile.close()
                admitnames.close()
                print("Your application has been sent. Please come back in a few days")
                goodbye()
            else:
                invalidandprogramrules()
            if logintype=="student":
                studentconfirm=int(input('''Is the data above correct?
                1.Yes, the above data is related to me and correct.
                2.This is not my data:'''))
                while True:
                    if studentconfirm==1:
                        studentchoice=input('''What else would you like to see?
                        1. My 10th std result
                        2. My attendance
                        3. Teacher remarks
                        #. Go to previous menu
                        *. Exit the program:''')
                        if studentchoice=="#":
                            break
                        elif studentchoice=="*":
                            goodbye()
                        elif studentchoice=="1":
                            file1_path=get_files_needed_path("stu_percentage.txt")
                            percentages=open(file1_path,"r")
                            file1_path=get_files_needed_path("stu.txt")
                            stufile=open("stu.txt","r")
                            stu=[]
                            index=0
                            lines=percentages.readlines()
                            for line in lines:
                                if rollnumber+"," in line:
                                    stu.insert(index,line)
                                    index+=1
                                    break
                            linelen=len(stu)
                            for i in range(linelen):
                                print("Your 10th std percentage is",str(stu[i])[2:-1],"%")
                                print()
                        elif studentchoice=="2":
                            file1_path=get_files_needed_path("attendence.txt")
                            attendence=open(file1_path,"r")
                            file1_path=get_files_needed_path("stu.txt")
                            stufile=open(file1_path,"r")
                            stu=[]
                            index=0
                            lines=attendence.readlines()
                            for line in lines:
                                if rollnumber+":" in line:  
                                    stu.insert(index,line)
                                    index+=1
                                    break
                            linelen=len(stu)
                            for i in range(linelen):
                                print("Your attendence is",str(stu[i])[2:-1])
                        elif studentchoice=="3":
                            file1_path=get_files_needed_path("remarks.txt")
                            remarks=open(file1_path,"r")
                            file1_path=get_files_needed_path("stu.txt")
                            stufile=open(file1_path,"r")
                            stu=[] 
                            index=0
                            lines=remarks.readlines()
                            for line in lines:
                                if username.capitalize()+"," in line:            
                                    stu.insert(index,line)
                                    index+=1
                                    break
                            linelen=len(stu)
                            for i in range(linelen):
                                print("Teacher remarks about you:",str(stu[i]))
                        else:
                            invalidandprogramrules()
                            pass
                    elif studentconfirm==2:
                        print('''Please contact either of the administrators''')
                        print(adminnames)
                        break
                    else:
                        invalidandprogramrules()
                        break
    elif int(stafforstud)==3:
        adminlogin(username)   
        logintype='admin'
        while True:
            if logintype=="admin":
                print('''What would you like to work with?:
                1.Review admission applications
                #.Go back to previous menu
                *.Exit the program:''')
                adminchoices=(input("Enter your choice:"))
                if adminchoices=="1":
                        file_name = get_files_needed_path("admissions.txt")
                        file_name2= get_files_needed_path("admitnames.txt")
                        with open(file_name) as f:
                            for line in f:
                                print(line.strip())
                        with open(file_name) as f:
                            admissionsdata=f.readlines()
                        with open(file_name2) as f:
                            for line in f:
                                print(line.strip())
                        with open(file_name2) as f:
                            admissionnames=f.readlines()
                        adddata=addname=[]
                        adminchoice=input("Would you like to approve any applications?:")
                        if adminchoice=="y":
                            applicationchoice=(input("Enter the rollnumber of the student whose application you want to approve:"))
                            file1_path=get_files_needed_path("names.txt")
                            existingnames=open(file1_path)
                            file1_path=get_files_needed_path("stu.txt")
                            existingstu=open(file1_path)
                            existingdata=len(existingstu.readlines())
                            existingnamesdata=len(existingnames.readlines())
                            index=index1=0
                            for line in admissionsdata:
                                if applicationchoice+"," in line:                # if rollnumber+"," in line:
                                    adddata.insert(index,line)
                                    index+=1
                                    break
                            for line in admissionnames:
                                addname.insert(index,line)
                                index1+=1
                                break    
                            if index==0:
                                print("Invalid entry")
                            print("There are",existingdata,"number of students.")
                            str=adddata[0]
                            print(adddata)
                            str1=addname[0]
                            print(addname)
                            file1_path=get_files_needed_path("names.txt")
                            stuname=open(file1_path,"a")
                            stuname.write(str1)
                            stuname.close()
                            file1_path=get_files_needed_path("stu.txt")
                            stufile=open(file1_path,"a")
                            stufile.write(str)
                            stufile.close()
                            file1_path=get_files_needed_path("admissions.txt")
                            admission123=open(file1_path,"w")
                            admission123.close()
                            file1_path=get_files_needed_path("admitnames.txt")
                            admitnames1=open(file1_path,"w")
                            admitnames1.close()
                        elif adminchoice=="n" or adminchoice=="N" or adminchoice=="No" or adminchoice=="no":
                                pass    
                elif adminchoices=="#":
                    print("The program will restart now if you press #. Would you rather exit the program?")
                    choice=input("* for exiting and # for restarting the program")
                    if choice=="#":
                        break
                    elif choice=="*":
                        goodbye()
                elif adminchoices=="*":
                    goodbye()
                else:
                    invalidandprogramrules()
    else:
        invalid_entry()
