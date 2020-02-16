
## Main description goes here


def solve_problem(line):
    print(line)



if __name__ == '__main__':

    problem_input = []
    line = input()
    while line:
        if not(line == ''):
            problem_input.append(line.strip().split())
        try:
            line = input()
        except:
            line = ''
    for problem in problem_input:
        try:
            solve_problem(problem)
        except:
            pass
