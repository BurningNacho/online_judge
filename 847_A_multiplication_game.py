
def multiplication_game(number):
    iterations = 1
    number = str(int(number) + int(number[::-1]))
    while not is_palindrome(number):
        number = str(int(number) + int(number[::-1]))
        iterations += 1
    print(f'{iterations} {number}')

if __name__ == '__main__':

    problem_input = []
    input()
    line = input()
    while line != '':
        if not(line == ''): problem_input.append(line.strip())
        try: line = input()
        except: line = ''
    for problem in problem_input:
        multiplication_game(problem)
        # print()
        # try:
        # except: print('Not jolly')
