
print("\n\n**********Welcome to the Quiz Game!!************")
print("\n_______Choose one of the following answers____________\n")
general_questions=[{"question":"Which country is konown as LAND OF RISING SUN ?","answer":"A"},
                   {"question":"What is the largest desert in world?","answer":"C"},
                   {"question":"Which continent is known has dark continent","answer":"D"},
                   {"question":"Which planet is known as the BLUE PLANET?","answer":"B"},
                   {"question":"What is the capital of India?","answer":"D"}
                   ]
options=[["A.Japan","B.Russia","C.Taiwan","D.China"],
         ["A.Sahara Desert","B.Thar Desert","C.Antarctica Desert","D.Great Baisn Desret"],
         ["A.Asia","B.Antarctica","C.Europe","D.Africa"],
         ["A.Venus","B.Earth","C.Mars","D.Jupiter"],
         ["A.Mumbai","B.Hyderabad","C.Jaipur","D.Delhi"]]

score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return  True
    else:
        return   False
        
for question_num in range(len(general_questions)):
    print("\n***********************\n")
    print(general_questions[question_num]["question"])
    for i in options[question_num]:
         print(i) 
    guess=input("Enter your answer(A/B/C/D):").upper()
    is_correct=check_answer(guess,general_questions[question_num]["answer"]) 
    if is_correct:
              print("Correct answer!")
              score +=1
    else:
              print("Wrong answer!")
              print(f"Correct answer is {general_questions[question_num]['answer']}")          
print("Your total score is:",score)   
if score>=3:
    print("\nCongratulations!,You got a very good score.\n")
else:
    print("\nBetter Luck Next Time.\n")     