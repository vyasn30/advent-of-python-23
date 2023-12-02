import json

NUM_MAP = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9",
    }
SPELLS = [*NUM_MAP]


def search_for_puzzle_1(input_string: str):
    # Searching only for digits like 1, 2, 4, 8 etc
    pos_dict = {}
    for num in range(1, 10):
        indices = [index for index in range(len(input_string)) if input_string.startswith(str(num), index)]
        for val in indices:
            pos_dict[val] = num
    
    return pos_dict

def search_for_puzzle_2(input_string: str):
    # Searching for digits and words like one two three

    pos_dict = {}

    # digit
    for num in range(1, 10):
        indices = [index for index in range(len(input_string)) if input_string.startswith(str(num), index)]
        for val in indices:
            pos_dict[val] = num

    # print(pos_dict)

    #word
    for spell in SPELLS:
        indices = [index for index in range(len(input_string)) if input_string.startswith(spell, index)]
        if indices == []:
            continue
        for val in indices:
            pos_dict[val] = int(NUM_MAP[spell])

    # print(pos_dict)
    return pos_dict

def return_cal(pos_dict):
    first = min([*pos_dict])
    last = max([*pos_dict])

    return str(pos_dict[first]) + str(pos_dict[last])
    
def sum_call():
    with open("data/trebuchet.txt") as fp:
        # cals = [int(return_cal(line)) for line in fp]
        # print(cals)
        cals = []
        ans_dict = {}

        for line in fp:
            pos_dict = search_for_puzzle_2(line)
            ans = return_cal(pos_dict)
            cals.append(ans)
            ans_dict[line] = ans

        cals = [int(val) for val in cals]

    ans = 0
    for val in cals:
        ans+=val
       
    return ans

if __name__ == "__main__":
    # with open('data/trebuchet.txt') as fp:
        # for line in fp:
    # print("ggdone3nbmsthreefourninefiveoneightpr")
    # print(return_cal(search("m2")))
    print(sum_call())