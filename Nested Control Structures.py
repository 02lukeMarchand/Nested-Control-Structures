'''
Programmer: Luke Marchand
Date: 10.15.19
Program: Double For Loop

This program will nest a For Loop inside of another
For Loop
'''

for i in range (3):
    print ("Outer for loop: " + str(i))
    for l in range (2):
        print ("     Inner For Loop: " + str(l))

print ("\n________________________________\n\n")

'''
Programmer: Luke Marchand
Date: 10.22.19
Program: Average Test Scores

This program will ask for the test scores for multiple people
and reports the average test score for each portion
'''

numOfPeople = int(input("How many people took the test: "))
testPerPerson = int(input("How many tests are going to be averaged: "))

for i in range (numOfPeople):
    name = input("Enter name: ")
    sum = 0
    for i in range (testPerPerson):
        score = int(input("     Enter a Score: "))
        sum = sum + score

    average = float(sum/testPerPerson)
    print (name + " got an average of " + str(round(average, 2)) + "\n")