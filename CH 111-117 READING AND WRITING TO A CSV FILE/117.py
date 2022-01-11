"""
117
Create a simple maths quiz that will ask the user for their name and then generate two
random questions. Store their name, the questions they were asked, their answers and
their final score in a .csv file. Whenever the program is run it should add to the .csv file
and not overwrite anything.
"""
import random

print("Hello\n"
      "we are going to generate a series of five questions for you")
# USERNAME
userName = input("What's your name: ")

# score
score = 0

# GENERATE QUESTIONS 1
# numbers
anum1 = random.randint(10, 30)
anum2 = random.randint(10, 30)
# answer
aans = anum2 + anum1
# posting the quiz to user
print(f"{anum1} + {anum2} = ")
auserQuiz = int(input("answer: "))

# user score
if auserQuiz == aans:
    score += 1
    print("correct")
else:
    print("oops!")

# GENERATE QUESTIONS 2
# numbers
bnum1 = random.randint(10, 30)
bnum2 = random.randint(10, 30)
# answer
bans = bnum2 + bnum1
# posting the quiz to user
print(f"{bnum1} + {bnum2} = ")
buserQuiz = int(input("answer: "))
# user score
if buserQuiz == bans:
    score += 1
    print("correct")
else:
    print("oops!")


# STORE INTO A CSV FILE
file = open("Winners.csv", "a")
data = str(userName + "," + str(anum1) + "," + str(anum2) + "," + str(auserQuiz) + "," + str(bnum1) + "," + str(bnum2) + ","
           + str(buserQuiz) + "," + str(score) + "\n")
file.write(data)
file.close()

