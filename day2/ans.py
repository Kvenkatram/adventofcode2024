#!/usr/bin/env python3

def is_safe(report:list):
    
    if sorted(report) != report and sorted(report) != report[::-1]:
        return False
    
    for index, item in enumerate(report[:-1]):       
        diff = abs(item - report[index+1])
        if diff == 0 or diff > 3:
            return False

    return True


def problem_dampen(report) -> bool:

    for index, item in enumerate(report):
        copy_report = report.copy()
        copy_report.pop(index)
        if is_safe(copy_report):
            return True
    
    return False


if __name__ == "__main__":
    
    # Part 1 and part 2
    safe = 0
    pd = 0
    with open("input.txt") as fd:
        for line in fd:
            report_str = line.split()
            report = [int(item) for item in report_str]
            safe_report = is_safe(report)
            if safe_report:
                safe += 1
            elif problem_dampen(report):
                pd += 1
                
            
    
    print("Number of safe reports: {}".format(safe))
    print("Number of safe reports with problem damping: {}".format(safe + pd))

            


