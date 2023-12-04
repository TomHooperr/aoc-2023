
def find_num_end(line, start):
    current = start
    while (line[current+1].isnumeric()):
        current += 1
    return current

def adj_special_char(lines, line_idx, num_start, num_end):
    # iterate over adjacent lines and check for special chars
    for i in range(-1, 2):

        # check list bounds
        curr_line_idx = line_idx + i
        if curr_line_idx < 0:
            curr_line_idx = 0
        elif curr_line_idx >= len(lines):
            curr_line_idx = len(lines) - 1

        # check line bounds
        line_start = 0 if num_start-1 < 0 else num_start-1
        line_end = len(lines[curr_line_idx]) if num_end+2 > len(lines[curr_line_idx]) else num_end + 2

        line = lines[curr_line_idx][line_start:line_end].strip()
        line = line.replace(".", "")

        if any(not c.isnumeric() for c in line):
            # special char found
            return True
    
    return False

def find_gear_coords(lines):
    gear_coords = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "*":
                # store bounds of adj cells surrounding gear
                gear_coords.append((i-1, i+1, j-1, j+1))
    return gear_coords

def find_adjacent_parts(gear, part_coords: dict):
    adj_parts = []
    for k, v in part_coords.items():
        if (k[0] >= gear[0] and k[0] <= gear[1]):
            # part is within adjacent rows
            for i in range(k[1], k[2]+1):
                if (i >= gear[2] and i <= gear[3]):
                    # part is within adjacent columns
                    adj_parts.append(v)
                    break
    return adj_parts
                    

with open("day3\input.txt") as f:
    lines = f.readlines()

    total = 0
    part_coords = {}

    for i in range(len(lines)):
        end = 0
        for j in range(len(lines[i])):
            if end > 0:
                if (not lines[i][j].isnumeric()):
                    end = 0
                    continue
            elif (lines[i][j].isnumeric()):
                start = j
                end = find_num_end(lines[i], j)
                num = int(lines[i][start: end+1])

                if (adj_special_char(lines, i, start, end)):
                    total += num
                    part_coords[(i, start, end)] = num

    gear_coords = find_gear_coords(lines)

    gear_ratio_sum = 0
    for gear in gear_coords:
        adj_parts = find_adjacent_parts(gear, part_coords)
        if (len(adj_parts) == 2):
            gear_ratio_sum += (adj_parts[0] * adj_parts[1])

    print(total) # sum of part numbers
    print(gear_ratio_sum) # sum of gear ratios
                