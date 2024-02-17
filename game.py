import random


def game():
    i = 0
    while(i<10):
        my_inp = str(input("Enter 0 for stone, 1 for paper and 2 for scissor : "))

        
        print("Player : ", my_inp)
        choice = random.randint(0, 2)

        if choice == 0:
            computer = "rock"
        elif choice == 1:
            computer = "paper"
        elif choice == 2:
            computer = "scissors"

        print("Computer : ", computer)


        if my_inp == computer:
            print(f"Both players selected {my_inp}. It's a tie!")
        elif my_inp == "rock":
            if computer == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif my_inp == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif my_inp == "scissors":
            if computer == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        i += 1


       


game()

