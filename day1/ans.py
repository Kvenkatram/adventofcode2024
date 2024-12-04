#!/usr/bin/env python3
def get_lists(file_name = "input.txt"):
    "Read input file and return sorted lists 1 & 2"
    
    list_1 = []
    list_2 = []
    with open(file_name) as fd:
        for line in fd:
            num_1, num_2 = line.split()
            list_1.append(int(num_1))
            list_2.append(int(num_2))
    
    return sorted(list_1), sorted(list_2)

def get_lists_part_2(file_name = "input.txt"):

    "Read input file and return left list and number of collisions between left and right list"
    left_list = []
    right_list = []
    collisions = {}
    with open(file_name) as fd:
        for line in fd:
            str_1, str_2 = line.split()
            num_1 = int(str_1)
            num_2 = int(str_2)
            left_list.append(num_1)
            right_list.append(num_2)
            if num_1 not in collisions:
                collisions[num_1] = 0
    
    for item in right_list:
        if item in collisions:
            collisions[item] += 1

    return left_list, collisions



if __name__ == "__main__":

    "Part 1"
    list_1, list_2 = get_lists()
    difference = 0
    for item_1, item_2 in zip(list_1, list_2):
        difference += abs(item_1 - item_2)
    
    print("Difference score is {}".format(difference))

    "Part 2"
    similarity = 0
    left_list, collisions = get_lists_part_2()
    for item in left_list:
        similarity += item*collisions[item]
    
    print("Similarity score is {}".format(similarity))



