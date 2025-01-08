import csv
import re
#function to load csv file
def load_csv(filename):
    data = []
    try:
        with open(filename, mode ="r") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"File{filename} not found")
    return data
#to write data in csv file
def write_csv(filename,data):
    with open(filename, mode ="w",newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(data)
#function to validate the password strength
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]",password):#for checking atleast one uppercase letter
        return False
    if not re.search(r"\d",password):#for checking atleast one integer
        return False
    if not re.search(r"#@_$%",password):#for atleast one special character
        return False
    return True
#function to check if the user is unique
def is_unique_user(username,filename):
    data = load_csv(filename)

    for user in data:
        if user[0] == username:
            return False #shows that the username already exists
        return True
#functions that admin performs
def add_user():
    username = input("Enter username")
    password = input("Enter password")
    #to check for the unique username
    if not is_unique_user(username,'users.csv'):
        print("Username already exists! Try again")
    else:
        print("User added successfully")
#validate password
    if not validate_password(password):
        print("Password must be atleast of 8 characters,include one digit and one special character")
        #add new user to csv file
        users = load_csv('users.csv')
        users.append([username,password,'50%'])
        write_csv('users.csv',users)
        print(f"User{username} added successfully")
#function for adding or updating questions
def add_update_questions():
    question_id = len(load_csv('questions.csv'))+1
    questions = load_csv('questions.csv')
#adding question
    question_num = 1
    while question_num < 10:
            que=input(f"enter question no. {question_num}")
            choice = questions[question_num-1]
            print(choice)
            answer = input(" ")
            question_num +=1
            questions.append([str(question_num),que])
            write_csv("questions.csv",questions)
        #adding options
            print("Enter 4 options (A,B,C,D):")
            options = []
            for option in ['A','B','C','D']:
                option_text = input(f"{option}:")
                options.append(option+option_text)
            #ensuring of exact 4 options
            if len(options)!=4:
                print("Error! You should provide only 4 options")
            #Enter correct answer
            correct_answer = input("Enter correct answer[A,B,C or D]").upper()
            #validate correct answer
            if not correct_answer in['A','B','C','D']:
                print("Error!Please enter correct answer") 

            #marking the answer with []using dict method
                options_dict ={'A':options[0],'B':options[1],'C':options[2],'D':options[3]}
                options_line = [str(question_id)] +options_dict.values()
            #ensure only one correct answer
                options_line = [f"[{opt}]" if opt == correct_answer else opt for opt in options_line]
                write_csv('questions.csv',add_update_questions)
                write_csv('options.csv',options)
                print("Questions and options added/updated successfully!!")
    #for viewing participant results
def view_participant_results():
    users = load_csv('users.csv')
    print("Username | Score")
    for user in users[1:]:
        if len(user)>=3:
            print(f"{user[0]} - Score:{user[2]}")
        else:
            print(f"Invalid data for user:{user[0]}")
#participant functions
def participant_login():
    username = input("Enter username")
    password = input("Enter password")
    #loading users

    users = load_csv("users.csv")
    for user in users:
        if user[0] == username:
            if user[1] == password:
                print("Login successful")
                return username
            else:
                print("Wrong password! enter the correct password")
                return
            print("Please ask the administrator for registration")
            return None
#for quiz related functions
def take_quiz(username):
    questions = load_csv("questions.csv")
    options = load_csv("options.csv")
    score = 0
    for i in range (len(options)-1):
        if i < len(options):
            print("Index{i} out of range")
        else:
            #option_line :options[i]
            #quiz logic
            
         for i in enumerate(questions[1:],start =1):
                print(i)
                print(f"question{i}:question{1}")
                option_line =options[1]
                print(f"A :{option_line[1]}")
                print(f"B :{option_line[2]}")
                print(f"C :{option_line[3]}")
                print(f"D :{option_line[4]}")
        answer = input("Enter answer (A/B/C/D):").upper()
        #validate answer
        if answer not in ['A','B','C','D']:
            print("Enter the answers from the options [A/B/C/D]")
            continue
                 
        #validating the correct answer against the other options
        if f"{answer}" in options[1:]:
            answer=options[1:].index(f"{answer}")  # Find the correct answer
        else:
            print(f"Error! the answer {answer} is not in options")    
            
            #to check the total number of questions
        total_questions = len(questions)-1
        #import pdb;pdb.set_trace()
        if score!=0: 
            percentage = (total_questions/score)*100
        else:
            percentage = 0
            return
            #print("Score is 0 cannot calculate the percentage")
        result = f"{percentage}%"
        print("You are passed",result)
        #saving score in user's csv file
        users = load_csv('users.csv')
        for user in users:
            if user[0] == username:
             user[2] == result
        write_csv('users.csv',users)  
#main program
def admin_main():
    while True:
        print("1.Admin login")
        print("2.Participant login")
        print("3 Exit") 
        choice=input("Enter your choice")

        if choice == "1":
            admin_username = input("Enter username")
            admin_password = input("Enter password")
            if admin_username == 'Meena' and admin_password == 'Meena123':
                while True:
                    print("\nAdmin Menu")
                    print("1 Add new user")
                    print("2 Add/update questions")
                    print("3 View participant results")
                    print("4 Exit")
                    choice = input("Enter your choice")
                    if choice == "1":
                        add_user()
                    elif choice == "2":
                        add_update_questions()
                    elif choice == "3":
                        view_participant_results()
                    elif choice == "4":
                        break
                    else:
                        print("Invalid choice!!")
        elif choice == "2":
            username = participant_login()
            if username:
                take_quiz(username)
        elif choice == "3":
            break
        else:
            print("Invalid choice!!")
if __name__ == "__main__":
    admin_main()                        




                              




































 




          





