choice1 = input(
    "you finaly arrive temple that has a tresure in side will you risk your life for tresure you can still go away/n wanna go away? Y or N"
)
if choice1 == "Y":
    print(
        "you are smart than i though. you ddint go and lived long life but you had a always regret for not trying /nGame over"
    )
if choice1 != "Y":
    choice2 = input(
        "you are in the temple now and suddenly the enterence closed there is omly two ways now you can go right or left "
    )
    if choice2 == "right":
        print(
            "you choose to go right you entered the room and eaten by a giant snake /nGame Over"
        )
    else:
        choice3 = input("now you see three gates what will you choose 1 , 2 , 3 ")
        if choice3 == 1:
            print("you have found the tresure")
        if choice3 == 2:
            print("gate crashed on you Game Over")
        else:
            print(
                "You find chest you opended that chesst while you thinking i found the tresure but in side of it therew as a snake and eat you Game Over"
            )
