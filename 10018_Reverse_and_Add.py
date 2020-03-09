
## Main description goes here


def is_palindrome(n):
    nl = len(n)
    if nl > 1:
        if nl%2 == 0: return n[:int(nl/2)] == n[int(nl/2):][::-1]
        return n[:int(nl/2)] == n[int(nl/2)+1:][::-1]
    return True

def reverse_add(number):
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
        reverse_add(str(problem))
        # print()
        # try:
        # except: print('Not jolly')
