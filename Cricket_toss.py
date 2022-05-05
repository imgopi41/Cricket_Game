
# $$$$$$$$$$$$ Toss $$$$$$$$$$$$$$$$$

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