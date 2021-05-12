print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

if age >= 13:
    print("Pog! You are old enough to play!")

    wants_to_play = input("Do you want to play? (yes/no) ").lower()
    if wants_to_play == "yes":
        print("Let's play!")

        health = 10

        print("You are starting with", health, "health.")

        left_or_right = input("First choice... Left or Right? (left/right) ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... "
                        "Do you swim across or go around? (across/around) ")

            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5
                print("You now have", health, "health.")

            ans = input("You notice a house and a river. Which do you go to? (river/house) ")
            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health.")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived...")
                    print("Congrats", name + ". You have won the game!")
            else:
                print("You fell in the river and lost 10 health.")
                print("You now have 0 health and you lost the game...")

        else:
            print("You fell down and lost 10 health.")
            print("You now have 0 health and you lost the game...")

    else:
        print("ait")

else:
    print("ur trash kid get rekt lmao")
