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