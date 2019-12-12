#DAY 1
#Change the DIFFICULTY constant to either "easy" or "hard" to switch between difficulties

FILE_PATH = "input.txt"
DIFFICULTY = "easy"

with open(FILE_PATH, "r") as input_file:
    input_parsed = input_file.read()
    input_split = input_parsed.split(',')

if(DIFFICULTY == "easy"):
    input_split[1] = 12
    input_split[2] = 2


    values = [int(x) for x in input_split]
    output = 0
    for i in range(0,len(values),4):
        op_code = values[i]
        if(op_code == 99):
            print("Program halted...")
            break
        else:
            input_position_1 = values[i + 1]
            input_position_2 = values[i + 2]
            output_position = values[i + 3]

            value_at_position_1 = values[input_position_1]
            value_at_position_2 = values[input_position_2]

            if(op_code == 1):
                values[output_position] = value_at_position_1 + value_at_position_2
                #print(values[output_position])
            elif(op_code == 2):
                values[output_position] = value_at_position_1 * value_at_position_2
                #print(values[output_position])
    output = values[0]
    print(output)

elif(DIFFICULTY == "hard"):
    expected_output = 19690720
    values = [int(x) for x in input_split]
    values_copy = values.copy()

    answer = 0
    done = False
    while(not done):
        for i in range(100):
            noun = i
            for j in range(100):
                verb = j
                values[1] = noun
                values[2] = verb
                for k in range(0,len(values),4):
                    op_code = values[k]
                    if(op_code == 99):
                        print("Program halted...")
                        break
                    else:
                        input_position_1 = values[k + 1]
                        input_position_2 = values[k + 2]
                        output_position = values[k + 3]

                        value_at_position_1 = values[input_position_1]
                        value_at_position_2 = values[input_position_2]

                        if(op_code == 1):
                            values[output_position] = value_at_position_1 + value_at_position_2
                            #print(values[output_position])
                        elif(op_code == 2):
                            values[output_position] = value_at_position_1 * value_at_position_2
                            #print(values[output_position])
                current_output = values[0]
                if(current_output == expected_output):
                    answer = (100 * noun) + verb
                    print(answer)
                    done = True
                else:
                    values = values_copy[:]
