## 01
secret_number = 10
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("guess my secret number: "))
    guess_count +=1
    if guess == secret_number:
        print ("you guessed right!!!")
        break
else:
    print("you missed it!")

