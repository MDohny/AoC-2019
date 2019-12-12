#DAY 1
#Change the DIFFICULTY constant to either "easy" or "hard" to switch between difficulties

FILE_PATH = "test.txt"
DIFFICULTY = "easy"
with open(FILE_PATH, "r") as input_file:
    input_wires = input_file.readlines()
    wire_1_string = input_wires[0].split(",")
    wire_2_string = input_wires[1].split(",")

if(DIFFICULTY == "easy"):
    for i in range(len(wire_1_string)):
        current_wire_1_move = wire_1_string[i]
        current_wire_1_dir = current_wire_1_move[0]
        current_wire_1_dist = int(''.join(char for char in current_wire_1_move if char.isdigit()))
        current_wire_1_coords = []
        if(current_wire_1_dir == "R"):
            for j in range(current_wire_1_dist + 1):
                current_coords = [j, 0]
                current_wire_1_coords.append(current_coords)
        elif(current_wire_1_dir == "L"):
            for j in range(current_wire_1_dist + 1):
                current_coords = [-j, 0]
                current_wire_1_coords.append(current_coords)
        elif(current_wire_1_dir == "U"):
            for j in range(current_wire_1_dist + 1):
                current_coords = [0, j]
                current_wire_1_coords.append(current_coords)
        elif(current_wire_1_dir == "D"):
            for j in range(current_wire_1_dist + 1):
                current_coords = [0, -j]
                current_wire_1_coords.append(current_coords)

        print(current_wire_1_coords[-1])

        for j in range(len(wire_2_string)):
            current_wire_2_move = wire_2_string[j]
            current_wire_2_dir = current_wire_2_move[0]
            current_wire_2_dist = int(''.join(char for char in current_wire_2_move if char.isdigit()))
            current_wire_2_coords = []
            if(current_wire_2_dir == "R"):
                for x in range(current_wire_2_dist + 1):
                    current_coords = [x, 0]
                    current_wire_2_coords.append(current_coords)
            elif(current_wire_2_dir == "L"):
                for x in range(current_wire_2_dist + 1):
                    current_coords = [-x, 0]
                    current_wire_2_coords.append(current_coords)
            elif(current_wire_2_dir == "U"):
                for y in range(current_wire_2_dist + 1):
                    current_coords = [0, y]
                    current_wire_2_coords.append(current_coords)
            elif(current_wire_2_dir == "D"):
                for y in range(current_wire_2_dist + 1):
                    current_coords = [0, -y]
                    current_wire_2_coords.append(current_coords)

        break







