
## Main description goes here
import math

def solve_problem(r):
    Rsq = r*r
    A1 = math.pi*Rsq/3-(math.sqrt(3)-1)*Rsq
    A2 = ((0.25*math.pi*Rsq-Rsq/2)*2-A1)*2
    A3 = Rsq-A1-A2
    return f'{A1:.3f} {A2:.3f} {A3:.3f}'

if __name__ == '__main__':
    problem_input = []
    line = input()
    while line:
        problem_input.append(float(line))
        try: line = input()
        except: break
    for problem in problem_input:
        print(solve_problem(problem))
