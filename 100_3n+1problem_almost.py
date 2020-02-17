import time


def prob(n):
    # print(n)
    if n in vals.keys(): return vals[n]
    if n == 1: return 1
    if n%2: return 1 + prob((3*n)+1)
    return 1 + prob(int(n/2))

def prob_v2(n):
    cycle = [n]
    while n != 1:
        if n in vals.keys(): return cycle[:-1] + vals[n]
        if n%2: n = (3*n) + 1
        else: n = int(n/2)
        cycle.append(n)
    return cycle

vals = {1:[1]}


def solve_problem(i, j):
    if i > j: bot, top = j, i
    else: bot, top = i, j
    if bot not in vals.keys():
        vals[bot] = prob_v2(bot)
    max = len(vals[bot])
    for nums in range(bot,top):
        if nums not in vals.keys():
            vals[nums] = prob_v2(nums)
        val = len(vals[nums])
        if val > max: max = val
    # print(vals[i+1])
    print(f'{i} {j} {max}')

if __name__ == '__main__':
    initime = time.time()
    problem_input = []
    line = input()
    while line:
        if line: problem_input.append(line.strip().split())
        try: line = input()
        except: line = ''
    for problem in problem_input:
        solve_problem(int(problem[0]), int(problem[1]))
        # try:
        # except:
        #     pass
    print(f'\nTotal time:{time.time() - initime}')
