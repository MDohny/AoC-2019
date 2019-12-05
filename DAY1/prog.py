#DAY 1
#Change the DIFFICULTY constant to either "easy" or "hard" to switch between difficulties

import math

#Constants
FILE_PATH = "input.txt"
DIFFICULTY = "hard"

with open(FILE_PATH, "r") as input_file:
    input_parsed = input_file.readlines()

if(DIFFICULTY == "easy"):
    total_fuel = 0
    for i in range(len(input_parsed)):
        current_fuel = math.floor((int(input_parsed[i]))  / 3) - 2
        total_fuel += current_fuel

    print(total_fuel)

elif(DIFFICULTY == "hard"):
    total_fuel = 0
    for i in range(len(input_parsed)):
        current_fuel = math.floor((int(input_parsed[i]))  / 3) - 2
        total_current_fuel = current_fuel
        while(current_fuel > 0):
            current_fuel = math.floor((current_fuel  / 3)) - 2
            if(current_fuel > 0):
                total_current_fuel += current_fuel
        total_fuel += total_current_fuel

    print(total_fuel)
