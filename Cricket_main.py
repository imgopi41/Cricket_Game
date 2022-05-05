import random

$$$$$$$$$$$$$ Toss $$$$$$$$$$$$$$$$$

print("\nWelcome to You v/s Computer Cricket game")
toss = input("\nChoose HEADS or TAILS: ").upper()

random_opt = random.randint(1,2)
random_pc = random.randint(1,2)

user_choice = 0
pc_choice = 0

if random_opt == 1 and toss == "HEADS":
    print("\nYou have won the toss")
    user_choice = input("\nChoose to bat or bowl: ").lower()

elif random_opt == 2 and toss == "TAILS":
    print("\nYou have won the toss")
    user_choice = input("\nChoose to bat or bowl: ").lower()

else:
    print("\nYou have lost the toss")

    if random_pc == 1:
        pc_choice = "bat"
        print("\nComputer choose to",pc_choice)

    elif random_pc == 2:
        pc_choice = "bowl"
        print("\nComputer choose to",pc_choice)

# $$$$$$$$$$$$$$ First innings $$$$$$$$$$$$$$$$$$$$

runs_1 = 0
wickets_1 = 0
balls_1 = 0

while wickets_1 != 2 and balls_1 != 12:

    user_input = int(input("Choose the number from (1 to 6): "))
    pc_input = random.randint(1, 6)

    if user_input < 1 or user_input > 6:
        print("\nPlease choose number from 1 to 6 only")

    else:
        print("\nYour choice",user_input,"\nComputer choice",pc_input)

        if user_input == pc_input:
            wickets_1 = wickets_1 + 1

        else:
            if user_choice == "bat" or pc_input == "bowl":
                bat_first = "You"
                bowl_first = "Computer"
                runs_1 += user_input


            elif user_choice =="bowl" or pc_input == "bat":
                bat_first = "Computer"
                bowl_first = "You"
                runs_1 += pc_input

        print("\nScore =", runs_1, "/", wickets_1)

        balls_1 += 1

        if balls_1 == 6:
            print("\nOne over compeleted")

        elif balls_1 == 12:
            print("\nTwo over's compeleted")

        print("Balls Remaining is",12 - balls_1)

print("\nScore Card: You v/s Computer")
print("Total runs is",runs_1)
print("Total wickets is",wickets_1)
print("Target",runs_1+1)
print("\n",bowl_first,"need",runs_1+1,"runs To win the match")

# $$$$$$$$$$$$$ Second innings $$$$$$$$$$$$$$$$

runs_2 = 0
wickets_2 = 0
balls_2 = 0

while balls_2 != 12 and wickets_2 !=2 and runs_2 <= runs_1:

    user_input = int(input("\nChoose the number from (1 to 6): "))
    pc_input = random.randint(1,6)

    if user_input < 1 and user_input > 6:
        print("\nPlease choose the number from 1 to 6")

    else:
        print("Your choice is: ",user_input,"\nComputer choice: ",pc_input)

        if user_input == pc_input:
            wickets_2 = wickets_2+1


        else:
            if bat_first == "Computer":
                runs_2 += user_input
                bat_second = "You"

            elif bat_first == "You":
                runs_2 += pc_input
                bat_second = "Computer"

        print("\nScore =",runs_2,"/",wickets_2)

        balls_2 = balls_2 + 1

        if balls_2 == 6:
            print("First over completed")

        elif balls_2 ==12:
            print("Two over's completed")

        if wickets_2 != 2 and runs_2 <= runs_1 and balls_2 <= 11:
            print("To win",runs_1 -runs_2+1,"runs needed from",12-balls_2,"balls")

print("\nEnd of the innings")

print("\nScore: You v/s Computer")
print("Runs =",runs_2)
print("Wickets =",wickets_2)

print("\nResult")


$$$$$$$$$$$$$$$$$$$ Result $$$$$$$$$$$$$$$$

if runs_1 > runs_2:

    if bat_first == "You":
        print("Congratulations! You won the Match by", runs_1 - runs_2, "runs.")

    else:
        print("Better luck next time! The Computer won the Match by", runs_1 - runs_2, "runs.")

elif runs_2 > runs_1:

    if bat_second == "You":
        print("Congratulations! You won the Match by", 2 - wickets_2, "wickets.")

    else:
        print("Better luck next time! The Computer won the Match by", 2 - wickets_2, "wickets.")

else:
    print("\nDraw match")















