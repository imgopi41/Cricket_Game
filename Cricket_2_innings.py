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