import random
length=int(input("Enter the length of the integer: "))
min=("9"*(length-1))
max=("9"*length)
min=int(min)+1
max=(int(max))
num=random.randint(min,max)


print(f"I have generated a {length}- digit number with unique digits. Try to  guess it")
guess_count=0
hint=0
while True:
    guess=int(input("Guess: "))
    guess_count+=1
    bull_count=0
    for i in range(length):
        if str(num)[i]==str(guess)[i]:
            bull_count+=1
    print(f"bulls {bull_count}")

    cow_count=0
    for i in str(guess):
        if i in str(num):
            
                cow_count+=1
            
    print(f"cows {cow_count}")

    if cow_count==length and bull_count==length:
        print("Correct number guessed")
        break
    if guess_count>= 15+length:
        print("Game lose")
        break
    if guess_count>15 and guess_count< 15+length:
        hint+=1
        print(f"The number at {hint} position is {str(num)[hint-1]}")
