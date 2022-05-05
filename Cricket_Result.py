# $$$$$$$$$$$$$$$$$$$$  Result $$$$$$$$$$$$$$$$$$

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


