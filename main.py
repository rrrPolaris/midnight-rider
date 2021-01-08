# main.py
# Midnight Rider
# A text adventure game that is riveting.
# IGN gives it 4 stars out of 100.

import random
import sys
import textwrap
import time


INTRODUCTION = """
WELCOME TO MIDNIGHT RIDER
WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.
THE GOVERNMENT WANTS IT FOR THEIR GAIN.
WE CAN'T LET THAT HAPPEN.
ONE GOAL: SURVIVAL... and THE CAR.
REACH THE END BEFORE THE MAN GON GETCHU.
"""
win = """
You press the botton to open the gate.
This is not the first time you have done this
so you know how to time it
Just as the doors close,you slide right in to HQ
you know you did the right thing,the government would have torn the car apart
Theyt do not know its secrets
that it holds the key to different worlds
As you take a couple of steps away from the car
it makes a strange sound
It changes it shape
You have seen it before only on TV
Bumblebee???
-----Game Over-----"""

CHOICES = """
    ----
    A. eat some tofu
    B. moving at a moderate speed
    C. Speed ahead a full throttle.
    D. Stop for fuel at a refuelling station.
       (No food available)
    E. Status check
    Q. QUIT
    ----
"""
def type_text_output(text):
    for char in textwrap.dedent(text):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
def main():
    type_text_output(INTRODUCTION)

    # CONSTANTS
    MAX_FUEL_LEVEL = 50
    MAX_TOFU_LEVEL = 3
    moderate_speed = 80
    Max_distance_traveled = 100
    Tofu_Chance = 0.3

    # Variables
    done = False

    km_traveled = 0
    agents_distance = -20.0
    turns = 0                   # amount of turns taken
    tofu = 3                    # 3 is max tofu
    fuel = 50                   # 50 is a full tank
    hunger = 0                  # hunger increases with num

    while not done:
        #Fido
        if random.randrange() <Tofu_Chance:
            #Fido pops up say something and refills tofu
            tofu = MAX_TOFU_LEVEL
            print()
            print("Your tofu is magically refilled")
            print("\You are welcome! \" a voice says")
            print("It is Fido")
            print("He is using his tofu cooking skills")

        #showing hunger
        if hunger > 35:
            print("Your stomach rumbles.You need to eat something soon")
        elif hunger > 20:
            print("*****Your hunger is small but manageble")

        #check if reached the end game
        while not done:
            # TODO: Check if reached END GAME
            # Check if reached END GAME
            if km_traveled > Max_distance_traveled:
                # WIN
                # Print win scenario (typing way)
                time.sleep(2)
                type_text_output(win)

                # Break from while loop
                break


        # Give the player their choices
        print(CHOICES)
        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.? ")

        if users_choice =="a":
            #Eat
            if tofu > 0:
                tofu -= 1
                hunger = 0
                print()
                print("----soybean goodness")
                print("----Your hunger is stated")
                print()
            else :
              print()
              print("----You have none left.")
              print()

        elif users_choice == "b":
            #Drive moderately
            player_speed_now =moderate_speed
            player_distance_now = random.randrange(8,14)
            agents_distance_now = random.randrange(4,10)
            #Burn fuel
            fuel -= random.randrange(4,7)
            #Player distance traveled
            km_traveled += player_distance_now
            #agents' distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)
            print()
            print(f"-------- You sped ahead {player_distance_now} kms!")
            print()

        elif users_choice == "c":
            # Drive Fast
            player_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(5, 11)

            # Player distance traveled
            km_traveled += player_distance_now

            # Agent's distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)

            # Feedback to Player
            print()
            print(f"-------- You sped ahead {player_distance_now} kms!")
            print()
        elif users_choice == "d":
            # Refuel
            # Fill the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give the user feedback
            print()
            print("-------- You filled the fuel tank.")
            print("-------- The agents got closer...")
            print()
        elif users_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkms traveled: {km_traveled} kms")
            print(f"\tFuel left: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} kms behind you.")
            print(f"\tYou have {tofu} tofu left.")
            print("\t------\n")
        elif users_choice == "q":
            done = True

        #increase hunger
        if users_choice not in ["a", "e"]:
           hunger += random.randrange(5,13)
        # Pause
        time.sleep(1)
    # Outroduction
    print("Thanks for playing! Please play again. =)")
if __name__ == '__main__':
    main()
