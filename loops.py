## For

#count the no.of even numbers in a list
l=[8,3,4,5,7,6,21,9,45,51,20,14]
c=0
for i in l:
    if i%2==0:
        c+=1
print(c)

l=[0,1,2]
for i in l:
    print(f"For i={i}")
    for i in range(i):
        print("Hii")

city = ['London', 'Paris', 'Mumbai', 'Sydney', 'California']
for i in range(len(city)):
    print(f"I Love {city[i]}")

str="Welcome to Python"
for c in str:
    print(c,end=" ")
print('\n')

for c in range(len(str)):
    print(str[c],end=" ")
print('\n')

for k,v in enumerate(str):
    print(v,end=" ")

#Nested loop
n=['Kamal','Vijay Sethupathi','Rajanikanth ']
m=['Hero','Villain']
for i in n:
    for j in m:
        print(f'{i} acted as a {j}')
    print(" ")

#square of a number
n=int(input())
res=0
for i in range(1,n+1):  #1-5
    for j in range(1,n+1): #1-5
        res+=1
print(res)

#break in for loop
numbers = [5, 9, 7, 13, 8, 1, 11]
for i in numbers:
    if i %2==0:
        print("\nEven value encountered")
        break
    print(i,end=" ")

#pass in for loop
s='Hello World'
for i in s:
    pass
print(f'the last letter in the string is \'{i}\'')

#continue in for loop
country = ['India', 'China', 'UAE', 'UK']
for x in country:
    if x == 'China':
        continue
    print(x,end=" ")

i=1
for i in range(6):
    pass
print(i)  #for loop will update its value

s=[True,True,True,False]
for i in s:
    if not i:
        print("Bye")
    else:
        print("Hi")

i=1
[... for i in range(6)]
print(i) 

for i in range(6):
    ...
print(i)  #once the loop is over we can still access the loop variable
#in the above code, as the loop variable (i) already existed, it was overwritten in each iteration

#But here the loop variable always remains local to the list comprehension. It is never leaked outside
[... for l in range(6)]
print(l)

## While

A while loop repeats a block of code an unknown number of times until a condition is no longer met. for loops, on the other hand, repeat a block of code a fixed number of times.

So, a while loop is useful when you don’t know how many times you want a block of code to execute beforehand.
Eg. Asking a keyword from the user(Each time they enter the wrong one, you continue to prompt them for the correct keyword. And for as long as they enter the wrong keyword, you will not allow them to continue.)

A while loop repeats the block of code based on a given Boolean condition.

count = 0;
while count <5:
    print("You are learning Python\n")
    count += 1
else:
    print('String prined 5 times')    

secret_keyword = "Python"

user_input = input("Please enter the secret keyword: ").capitalize()

while user_input != secret_keyword:
    user_input = input("Please enter the secret keyword: ").capitalize()

Note:If we want to terminate the program, type Control C to escape the infinite loop.

condition = True
while condition:
    user_input = input("Enter 'stop' to end: ")
    if user_input.lower() == 'stop':
        condition = False
    print("Hi")
    if not condition:
        print("Bye")

s = [True, True, True, False]
index = 0
while index < len(s):
    if not s[index]:
        print("Bye")
    print("Hi")
    index += 1

#this creates an infinite loop
# while True:
#     print("I am always true")

#use break to escape from infinite loop
while True:
    print("I am always true")
    break  #the break statement will force the loop to stop when needed.

countdown = 5
while countdown > 0:
    print("Countdown:", countdown)
    countdown -= 1
    if countdown == 0:
        print("Blast off!")

count = 0
while True:
    count += 1
    print("Iteration:", count)
    if count >= 5:
        break
'''
In this example, the loop will continue indefinitely until the count variable reaches a value of 5 or greater. Once the condition count >= 5 is satisfied, the break statement is executed, terminating the loop.
'''

game_over = False
score = 0
while not game_over:
    user_input = input("Type 'exit' to quit: ")
    if user_input.lower() == 'exit':
        game_over = True
    else:
        score += 10
        print("Score:", score)

# Guessing Game
secret_number = 42

while True:
    guess = int(input("Guess the secret number: "))

    if guess == secret_number:
        print("Congratulations! You guessed the secret number!")
        break
    else:
        print("Wrong guess. Try again!")

votes = {'yes': 0, 'no': 0}
while True:
    vote = input("Cast your vote (yes/no), or 'quit' to end: ").lower()
    if vote == 'quit':
        print("Voting closed.")
        break
    elif vote in votes:
        votes[vote] += 1
        print("Vote recorded.")
    else:
        print("Invalid vote. Please vote again.")
print("Voting Results:")
print("Yes:", votes['yes'])
print("No:", votes['no'])

import random

secret_number = random.randint(1, 100)
user_input = None

while user_input != secret_number:
    user_input = int(input("Guess the secret number (or enter 0 to quit): "))
    if user_input == 0:
        print("Exiting the game.")
        break
    elif user_input < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")

users = {'alice': '123', 'bob': '456', 'charlie': '789'}
logged_in = False

while not logged_in:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful. Welcome,", username.capitalize())
        logged_in = True
    else:
        print("Invalid credentials. Try again.")

while True:
    p = input('Please enter a password: ')
    if len(p) >= 8 and p.isalnum():
        has_uppercase = False
        has_lowercase = False
        has_digit = False
        for ch in p:
            if ch.isupper():
                has_uppercase = True
            elif ch.islower():
                has_lowercase = True
            elif ch.isdigit():
                has_digit = True

        if has_uppercase and has_lowercase and has_digit:
            print('Password is valid. Access granted.')
            break
    else:
        print('Invalid password. Please try again.')

num_terms = int(input("Enter the number of terms: "))

# Fibonacci sequence initialization
fib_sequence = [0, 1]

# Generate Fibonacci sequence
while len(fib_sequence) < num_terms:
    next_term = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_term)

# Print Fibonacci sequence
print("Fibonacci Sequence:", ", ".join(str(term) for term in fib_sequence))

