import pandas as pd
import time
import random  
import sys  

quiz_started = False  

def sub():
    print("\t\t\t\t\t\t\t ✨✨⭐ WELCOME!!! ✨✨⭐ ") 
    global user_name                       
    user_name = input("👩‍💻 Enter your name: ")
    print()
    print(f'🌟 Welcome {user_name} to the online quiz platform 🌟')

    start_quiz = input('Are you excited for the quiz? 🤔 (yes/no) ').lower()
    if start_quiz == 'yes':
        print('🚀 Great! Let\'s get started ')
    else:
        print('😔 Okay, no worries. Try once you will be entertained.')
        print('🚀 Let\'s get started ')
        time.sleep(3)
    
    while True:  
        print("\nChoose the subject for the quiz")
        print("1. 🐍 PYTHON\n2. 💾 FDS\n3. 🖥 C Language")
        subject = input("Enter your choice: ")
        try:
            subject = int(subject)
            if subject == 1:
                return level1()
            elif subject == 2:
                return level2()
            elif subject == 3:
                return level3()
            else:
                print("Invalid choice. Please enter a valid subject number.")
        except ValueError:
            subject = subject.lower()  
            if subject == 'python':
                return level1()
            elif subject == 'fds':
                return level2()
            elif subject == 'c language':
                return level3()
            else:
                print("Invalid choice. Please enter a valid subject.")

def level1():
    print("\nChoose the level of questions")
    print("1. 🟢 EASY\n2. 🟡 MEDIUM\n3. 🔴 HARD")
    lev = input("Enter your choice (1 for Easy, 2 for Medium, 3 for Hard): ")
    return select_questions("PYTHON", lev)

def level2():
    print("\nChoose the level of questions")
    print("1. 🟢 EASY\n2. 🟡 MEDIUM\n3. 🔴 HARD")
    lev = input("Enter your choice (1 for Easy, 2 for Medium, 3 for Hard): ")
    return select_questions("FDS", lev)

def level3():
    print("\nChoose the level of questions")
    print("1. 🟢 EASY\n2. 🟡 MEDIUM\n3. 🔴 HARD")
    lev = input("Enter your choice (1 for Easy, 2 for Medium, 3 for Hard): ")
    return select_questions("C", lev)

def accept(subject):
    print()
    print("📚 Read the instructions carefully before starting the quiz 📚\n")
    time.sleep(1)
    print("🌟 Instructions:")
    time.sleep(1)
    print("1. There are a total of 10 questions.")
    time.sleep(1)
    print("2. Each question is mandatory.")
    time.sleep(1)
    print("3. Each question has a weightage of 1 mark each.")
    time.sleep(1)
    print("4. Total marks: 10")
    time.sleep(1)
    print("5. Answer each question by entering the corresponding option (A/B/C/D).")
    time.sleep(1)
    print("6. You have to solve all the questions within 10 minutes ")
    time.sleep(1)
    print("7. Take a note that after 10 minutes you quiz will be over")
    time.sleep(1)
    print("8. Have fun and good luck!")
    time.sleep(1)
    
    print()
    start = input("Press '1' or 'start' to begin the quiz: ")
    if start == '1' or start == 'start':  
        return pd.read_excel(df, f"{subject}")

def select_questions(subject, level):
    while True:
        level = level.lower()  
        if level == '1' or level == 'easy':
            return accept(f"{subject}-EASY")
        elif level == '2' or level == 'medium':
            return accept(f"{subject}-MEDIUM")
        elif level == '3' or level == 'hard':
            return accept(f"{subject}-HARD")
        else:
            print("Invalid choice. Please enter a valid level.")
            level = input("Enter your choice (1 for Easy, 2 for Medium, 3 for Hard): ")

df = 'datasetpython.xlsx'  

while True:
    if not quiz_started:  
        quiz = sub()  
        quiz_started = True  
    timelimit = 60  

    if quiz is not None: 
        while True:
            start_time = time.time()  
            correct = 0
            incorrect = 0
            cl = ['Sr.No.', 'Question', 'A', 'B', 'C', 'D']

            quiz = quiz.sample(frac=1).reset_index(drop=True)
            
            for index, row in quiz.iloc[0:10].iterrows():  
                if time.time() - start_time > timelimit:
                    print("Time limit exceeded. You cannot answer any more questions.")
        
                    break  
                
                print()
                print(f'📝 Question {index+1}: {row[cl[1]]}')
                print("\tA", row[cl[2]])
                print("\tB", row[cl[3]])
                print("\tC", row[cl[4]])
                print("\tD", row[cl[5]])

                while True:
                    a = input("Enter your answer (A/B/C/D): ").strip().upper()
                    if a not in ['A', 'B', 'C', 'D']:
                        print("Invalid Choice. Please choose A, B, C, or D.")
                    else:
                        break
                        
                if a == row['Answer']:
                    correct += 1
                else:
                    incorrect += 1

            end_time = time.time()
            total_time = end_time - start_time
            average_time = total_time / 10
            print()
            print()
            print("It's time to see how you did!")
            print("⌛⌛⌛")
            time.sleep(2)
            print()
            print()
            print(f"🕑 Total time taken to complete the quiz is {total_time:.2f} seconds")
            time.sleep(2)
            print(f'🕑 Average time taken to answer each question is {average_time:.2f} seconds')
            time.sleep(2)
            
            print(f"👩‍💻 Out of {len(quiz)} questions,")
            print(f"{correct} questions were answered correctly, and {incorrect} questions were answered incorrectly.")
            percentage = (correct / len(quiz)) * 100
            time.sleep(2)
    
            print(f" 🌟 Your percentage score is {percentage:.2f}%")
        
            time.sleep(2)
            if percentage >= 80 :
                print(f"🎉 Congratulations, {user_name}! You are a genius student! 🎉")
            elif percentage >= 60:
                print(f"👍 Well done, {user_name}! You are a good student! 👍")
            elif percentage >= 40:
                print(f"📚 Keep trying, {user_name}! You are an average student. 📚")
            else:
                print(f"😔 {user_name}, you need to work harder! You are a poor student. 😔")
            
            print("Do you want to check the answer key ❓")
            answer_key = input("Enter YES or NO: ").strip().upper()
            if answer_key == 'YES':
                for index, row in quiz.iterrows():
                    print()
                    print(f'📝 Question {index+1}: {row[cl[1]]}')
                    print("\tA", row[cl[2]])
                    print("\tB", row[cl[3]])
                    print("\tC", row[cl[4]])
                    print("\tD", row[cl[5]])
                    print("Correct answer is ", row['Answer'])

            play_again = input("Do you want to play again? Enter YES or NO: ").strip().upper()
            if play_again == 'NO':
                print("Thank you for using this quiz 😊")
                print("🌟Visit again and Enjoy !!!")
                sys.exit()  
            elif play_again == 'YES':
                quiz_started = False 
                break  
