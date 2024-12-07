#!/usr/bin/env python3

def is_safe(report:list) -> bool:
    
    is_increasing = True
    if report[0] > report[1]:
        is_increasing = False

    for index, item in enumerate(report[:-1]):
        if is_increasing:
            if item > report[index+1]:
                return False
        else:
            if item < report[index+1]:
                return False
                
        diff = abs(item - report[index+1])
        if diff == 0 or diff > 3:
            return False

    return True


    
    


if __name__ == "__main__":
    
    # Part 1 and part 2
    safe = 0
    safe_with_problem_damp = 0
    with open("input.txt") as fd:
        for line in fd:
            report_str = line.split()
            report = [int(item) for item in report_str]
            if is_safe(report):
                safe += 1
    
    print("Number of safe reports: {}".format(safe))

            


