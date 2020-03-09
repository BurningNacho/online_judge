
## Main description goes here


def carry_count(a, b):
    a = f"{'0'*(len(b)-len(a))}{a}"[::-1]
    b = f"{'0'*(len(a)-len(b))}{b}"[::-1]
    carry_count = carry = 0
    for numa, numb in zip(a,b):
        carry = int((int(numa)+int(numb)+carry)/10)
        if carry: carry_count += 1
    return carry_count


if __name__ == '__main__':

    problem_input = []
    line = input()
    while line != '0 0':
        if not(line == ''): problem_input.append(line.strip())
        try: line = input()
        except: line = '0 0'
    for problem in problem_input:
        carries = carry_count(problem.split()[0], problem.split()[1])
        if carries > 1: print(f'{carries} carry operations.')
        else: print(f'{carries or "No"} carry operation.')
        # print()
        # try:
        # except: print('Not jolly')
