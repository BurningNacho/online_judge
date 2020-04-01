
## Main description goes here
import math

def solve_problem(a,b,c):
    try:
        s = (a+b+c)/2
        return f'{math.sqrt((s-a)*(s-b)*(s-c)/s):.3f}'
    except: return '0.000'

if __name__ == '__main__':
    problem_input = []
    line = input()
    while line:
        problem_input.append(line)
        try: line = input()
        except: break
    for problem in problem_input:
        line = problem.split()
        print(f'The radius of the round table is: {solve_problem(float(line[0]), float(line[1]), float(line[2]))}')
