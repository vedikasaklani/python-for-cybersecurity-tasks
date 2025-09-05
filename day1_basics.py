#a student record management system, to revise basic python programming 
#covers basics like looping, conditionals, functions, flags etc
students={}
def add_student():
    grd=str(input("Enter class: "))
    id=int(input("Enter ID: "))
    name=str(input("Enter name: "))
    marks=float(input("Enter marks: "))
    if(grd not in students):
        students[grd]={}
    students[grd][id]=[name, marks]

def search_by_name():
    src=str(input("Enter the name to be searched: "))
    found=False
    for key, value in students.items():
        for j in value.values():
            if(src==j[0]):
                print(src, " found in class", key)
                found=True
            elif(src in j[0]):
                print(j[0], "found in class", key)
                found=True
    if(not found): print("Not found!")

def search_by_id():
    src=int(input("Enter the ID to search: "))
    found=False
    for key, value in students.items():
        for i in value.keys(): 
            if i==src:
                print("Found", src,",",value[i][0], "in class ", key)
                found=True
    if(not found):
        print(src, " not found!")

def find_all_avg():
    avg={}
    for key, value in students.items():
        avg[key]=0
        for i in value.values():
            avg[key]+=i[1];
        avg[key]=avg[key]/len(students[key])
    for key, value in avg.items():
        print("Average of", key, " is ",value," .")
while(True):
    print("Choose from the following options: ")
    print("1. Enter a new student")
    print("2. Search a student by name")
    print("3. Search a student by ID")
    print("4. Find average of all classes")
    print("Choose any other key to exit.")
    choice=str(input("Enter your choice: "))
    if(choice=="1"):
        add_student()

    elif choice=="2":
        search_by_name()

    elif choice=="3":
        search_by_id()

    elif choice=="4":
        find_all_avg()

    else:
        break
