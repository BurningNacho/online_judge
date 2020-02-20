
def solve_problem(n_jumpers, jumpers):
    jumped = [0]*n_jumpers
    for i in range(n_jumpers-1):
        if jumped[abs(jumpers[i]-jumpers[i+1])]:
            return 'Not jolly'
        jumped[abs(jumpers[i]-jumpers[i+1])] = 1
    return 'Jolly'


if __name__ == '__main__':

    problem_input = []
    line = input()
    while line:
        if not(line == ''): problem_input.append([int(i) for i in line.strip().split()])
        try: line = input()
        except: line = ''
    for problem in problem_input:
        try: print(solve_problem(problem[0], problem[1:]))
        except: print('Not jolly')
