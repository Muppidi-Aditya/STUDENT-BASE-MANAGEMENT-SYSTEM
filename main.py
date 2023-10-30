print("Enter the login id")
loginid = input()
loginstar = len(loginid) - 4
loginidcover = loginid[0:2]+"*"*loginstar+loginid[-2::]
if loginid == "aditya9296" :
    print("Login id : %s"%(loginidcover))
    password = input("Enter the password : ")
    if password == "am9296" :
        print("You are succesfully been into the code")
        print("Enter how many students are there in you class")
        s = {}
        s1 = {}
        l1 = []
        srev = {}
        count = 0
        numofstudents = int(input())
        for i in range(numofstudents) :
            nameofstudent = input("Enter the name of the student : ")
            marksofstudent = int(input("Enter the marks of the student : "))
            s.update({nameofstudent:marksofstudent})
            s1.update({nameofstudent:marksofstudent})
            l1.append(marksofstudent)
            srev.update({marksofstudent:nameofstudent})
    else :
        print("You entered the wrong password , you dont have access to the code")
    highestintheclass = max(s,key = s.get)
    highestmarks = max(s.values())
    print("%s is the student to get the highest marks in the class , he got %dmarks"%(highestintheclass,highestmarks))
    lowestintheclass = min(s,key = s.get)
    lowestmarks = min(s.values())
    print("%s is the student to get the least marks in the class , he got %dmarks"%(lowestintheclass,lowestmarks))
    s.pop(highestintheclass)
    secondhighintheclass = max(s,key = s.get)
    secondmarks = max(s.values())
    print("%s is the student to get second highest in the class with %dmarks"%(secondhighintheclass,secondmarks))
    s.pop(secondhighintheclass)
    thirdhighestintheclass = max(s,key = s.get)
    thirdmarks = max(s.values())
    print("%s is the student to score third highest in the class , he got %dmarks"%(thirdhighestintheclass,thirdmarks))
    leng = len(l1)
    print("The students failed in the exam")
    
    for x in range(leng) :
        intl = int(l1[x])
        keyfind = l1[x]
        if intl < 35 :
            print(srev.get(keyfind))
            count = count + 1
    print("There are %d failures in the counducted exam"%(count))
    print("Thank You")
    print("Done by :-M Aditya\nRA2211003011363")
else :
    print("You entered an incorect login id try , you dont have access to the code")