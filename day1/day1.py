nums = {'1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5':'five',
        '6':'six',
        '7':'seven',
        '8':'eight',
        '9':'nine'}

def find_first(str_value):
    for i in range(len(str_value)):
        if str_value[i].isnumeric():
            return str_value[i]
        
        str_so_far = str_value[:i+1]
        for num in nums:
            if nums[num] in str_so_far:
                return int(num)

def find_last(str_value):
    str_value_rev = str_value[::-1]
    for i in range(len(str_value_rev)):
        if str_value_rev[i].isnumeric():
            return str_value_rev[i]
        
        str_so_far = str_value[-(i+1):]
        for num in nums:
            if nums[num] in str_so_far:
                return int(num)
        
test = "seven82683\n"

cal_val = int(f"{find_first(test.strip())}{find_last(test.strip())}")
print(cal_val)

with open("day1\input.txt") as f:
    lines = f.readlines()
    total_sum = 0
    for line in lines:
        line.strip()
        cal_val = int(f"{find_first(line.strip())}{find_last(line.strip())}")
        total_sum += cal_val

    print(total_sum)