#This game is rock-paper-scissors game. This is the beginner level project.
import random
import time

computer_point=0
player_point=0

choices=["Rock","Paper","Scissors"]

print("Welcome to the Rock-Paper-Scissors Game...")

ascii_art=["⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣄⣀⡀",
"⠀⢠⣶⠟⠉⠁⠀⣠⠉⠉⠛⠳⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠉⠀⠈⠙⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⢰⡿⠁⠀⣀⣠⠞⠁⠀⠀⠀⠀⠀⠉⠻⣶⡶⠶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀",
"⣠⡶⠟⠛⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠈⢿⡄⠀⢠⣴⠶⠶⠶⣦⣄⠀⠀⠀⠀⠀⠀⠀⣠⣾⠋⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⣀⣀⣀⡀⠀⠀⠀",
"⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣶⠈⣿⡀⠘⣷⠀⢸⡇⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⢀⣼⠏⢀⣠⡶⠟⠋⠉⠉⠛⢷⣄⠀",
"⠸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢀⣀⡀⠹⣧⠀⢻⡄⠸⣧⠀⠀⠀⠀⠀⢻⡇⠀⠀⣠⡿⠃⠀⠀⠀⠀⠀⢠⣾⣧⠾⠛⠉⠀⠀⠀⠀⠀⠀⢈⣿⠀",
"⠀⣼⡿⠶⠦⠤⠤⠤⠀⠀⠀⠀⠀⠀⢠⣤⡶⠶⠞⠛⢋⡁⠀⣿⠀⢸⡧⠀⢻⣇⠀⠀⠀⠀⠘⣇⣴⡾⠋⠀⠀⠀⠀⠀⠀⣰⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠋⠀",
"⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠟⠃⢀⣿⢀⣾⠁⠀⠀⣿⡇⠀⠀⠀⠀⠟⠁⠀⠀⠀⠀⠀⠀⠀⣸⠋⠀⠀⠀⠀⠀⠀⠀⣀⣴⠿⠋⠁⠀⠀⠀",
"⢸⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⢀⣿⡛⠛⠁⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⢀⣤⠾⠋⣀⣠⣤⣤⣤⣄⡀",
"⠈⠻⣶⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⠀⠀⠀⠂⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠛⠛⠛⠉⠉⠁⠀⠀⠙⣿",
"⠀⠀⠀⢹⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠟⠋⠀⠀⠀⠀⠀⠀⢀⣼⡇⠀⠀⠀⢀⣴⡄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠏",
"⠀⠀⠀⠀⠙⠿⣶⣤⣤⣀⣀⣠⣤⣴⡶⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠉⣷⠀⢀⣴⡿⠋⠀⢀⣴⠿⠁⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⢀⣠⣴⠾⠛⠉⠁⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣀⣀⣀⡀⠀⠀⠀⠀⠀⠁⣷⠀⢻⣧⠈⠁⢀⣤⡾⠋⠁⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⢀⣤⠶⠿⣶⣤⡶⠟⠛⠉⠉⠉⢉⡉⠙⠛⢷⣦⡀⠀⠀⠀⠹⣇⠀⠹⣷⡀⠉⠁⣤⣴⠶⠛⠋⠀⠀⠀⠀⠀⠀⣀⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⣰⡟⠁⢠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠙⢿⡄⠀⠀⠀⠹⣧⡀⠈⢿⣦⡀⠁⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⣰⡏⠀⣰⡟⠀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣄⣸⣇⠀⠀⠀⠀⠈⠻⣦⣄⣈⣻⡷⠶⣶⣶⡶⠶⠾⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⢠⡟⠀⣰⡟⠀⣄⠈⠉⠛⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠳⠶⠶⠶⠶⣤⣭⣭⣋⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⢸⡇⢀⣿⠁⢠⠛⠿⢶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠘⣷⣼⣇⠀⠘⢷⣄⡀⠈⠙⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠈⠉⢿⡆⠀⠀⠙⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠒⠒⠶⢶⣶⣶⣤⣤⣤⣤⣤⣀⣀⣀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠘⢿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣦⣀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠉⠛⠲⢶⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠶⣦⣤⣄⣠⣤⣤⠶⠟⠋⠉⠛⠳⢶⣤⣀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⣦⣄⡀⣀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"]
for line in ascii_art:
    print(line)



while True:
    answer = input("Do you wanna start (yes,no) : ")
    if answer.lower()=="yes":

        while computer_point < 3 and player_point < 3:
            computer_choice=choices[random.randint(0,2)]
            print("------------------------------------------------------------------")
            player_choice=input("Write your choice (Rock,Paper or Scissors) : ")

            if player_choice.lower()=="rock" and computer_choice.lower()=="rock":
                print("Player Chocice :",player_choice,)
                print("Computer Choice :",computer_choice)
                print("There is no winner. Equals!")

            elif player_choice.lower()=="rock" and computer_choice.lower()=="paper":
                print("Player Chocice :",player_choice,)
                print("Computer Choice :",computer_choice)
                print("Computer wins!")
                computer_point+=1

            elif player_choice.lower()=="rock" and computer_choice.lower()=="scissors":
                print("Player Chocice :",player_choice,)
                print("Computer Choice :",computer_choice)
                print("Player wins!")
                player_point+=1

            elif player_choice.lower() == "paper" and computer_choice.lower() == "paper":
                print("Player Chocice :", player_choice, )
                print("Computer Choice :", computer_choice)
                print("There is no winner. Equals!")

            elif player_choice.lower() == "paper" and computer_choice.lower() == "rock":
                print("Player Chocice :", player_choice, )
                print("Computer Choice :", computer_choice)
                print("Player wins!")
                player_point += 1

            elif player_choice.lower() == "paper" and computer_choice.lower() == "scissors":
                print("Player Chocice :", player_choice, )
                print("Computer Choice :", computer_choice)
                print("Computer wins!")
                computer_point += 1

            elif player_choice.lower() == "scissors" and computer_choice.lower() == "scissors":
                print("Player Chocice :", player_choice, )
                print("Computer Choice :", computer_choice)
                print("There is no winner. Equals!")

            elif player_choice.lower() == "scissors" and computer_choice.lower() == "rock":
                print("Player Chocice :", player_choice, )
                print("Computer Choice :", computer_choice)
                print("Computer wins!")
                computer_point += 1

            elif player_choice.lower() == "scissors" and computer_choice.lower() == "paper":
                print("Player Chocice :", player_choice, )
                print("Computer Choice :", computer_choice)
                print("Player wins!")
                player_point += 1

            print("Score : ", player_point, "-", computer_point)
            if (computer_point <3 and player_point <3):
                print("Next turn coming. Please Wait...")
            time.sleep(1.25)

        if computer_point >player_point:
            print("Computer Won the game")
        else:
            print("Player Won")
        print("The game is restarting now...")
        print("-----------------------------------------------------------------")

    elif answer.lower()=="no":
        print("The game is shutting down, please wait...")
        time.sleep(1)
        print("The game shutted down!")
        break