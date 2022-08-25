import random as r

# Sets score to 0
score = 0
# dictionary
questions = {}

# Randomly generates maths questions with number between 0 and 12
# Equation is randomly picked out of (+, *)
for i in range(20):
    int_a = r.randint(0, 12)
    int_b = r.randint(0, 12)
    equation = ['+', '*']
    equation_value = r.choice(equation)
    question = str(int_a)+" "+equation_value+" "+str(int_b)
    answer = str(eval(question))
    question += ": "

    # adds the question to questions dictionary
    questions.update({question: answer})

# Iterates through the questions in the dictionary and response respectively
for q in questions.keys():
    user_answer = input(q)
    if questions.get(q) == user_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
# Outputs the users score
print("You got "+str(score)+" right!")
