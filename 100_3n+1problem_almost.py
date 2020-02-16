#!/usr/bin/env python

# /* @JUDGE_ID: 1063512 100 Python "Dynamic Programming" */
#
# /* @BEGIN_OF_SOURCE_CODE */


def problema1(n):
    list = [0]
    if n in list:
        return 0
    else:
        list.append(n)
        if n == 1:
            return 1
            if (n % 2):
                return 1 + problema1(3 * n + 1)
            else:
                return 1 + problema1(n / 2)


def problem(n):
    print(n)
    if n == 1: return 0
    if n%2: return 1 + problem(3*n+1)
    return 1 + problem(n/2)

def solve_problem(i, j):
    if i > j: i, j = j, i
    print(i)
    print(problem(i))
    print(type(problem(i)))
    max = problem(i)
    i += 1
    while i < j:
        val = problem(i)
        if (val > max):
            max = val
        i += 1
    print(str(oldi) + " " + str(oldj) + " " + str(max))

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
        solve_problem(int(problem[0]), int(problem[1]))
        # try:
        # except:
        #     pass
