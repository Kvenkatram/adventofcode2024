#!/usr/bin/env python3

import re

def mul_it_over(text:str):

    matches = re.findall(r"mul\(\d+,\d+\)", text)
    answer = 0
    for match in matches:
        str_values = re.findall(r"\d+", match)
        values = [ int(x) for x in str_values]
        answer += (values[0] * values[1])
    
    return answer


def do_dont(text:str):
    
    new_text = re.sub(r"don't\(\).*?do\(\)|don't\(\).*?$", "", text)
    return mul_it_over(new_text)
    


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.read().replace("\n","")
    
    
    part_1 = mul_it_over(content)
    print("Part 1 Answer: {}".format(part_1))
    part_2 = do_dont(content)
    print("Part 2 Answer: {}".format(part_2))