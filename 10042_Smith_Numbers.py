
## Main description goes here
import math
def primeFactors(n):
    factors = []
    while n%2==0:
        # if n in primes.keys(): return factors+primes[n] ## List of solutions?
        factors.append(2)
        n=n/2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n%i == 0:
            factors.append(int(i))
            n=n/i
    if n > 2:
        factors.append(int(n))
    return factors


if __name__ == '__main__':

    n_cases = int(input())
    problem_cases = [int(input()) for _ in range(n_cases)]
    for case in problem_cases:
        while 1:
            case += 1
            my_l = primeFactors(case)
            if len(my_l) > 1:
                num_sum = sum([int(i) for i in str(case)])
                l_sum = 0
                # l_sum = sum([sum([i for in in str(elem)]) for elem in my_l])
                for elem in my_l:
                    for i in str(elem):
                        l_sum += int(i)

                if num_sum == l_sum: break
        print(case)
        # print('')
        # print(f'SUM:{num_sum} \t\t CASE:{case}')
        # print(f'SUM:{l_sum} \t PRIME_F:{my_l}')
        # print('')
        # input()
        # primes = list(set(primes))
        # print(primes)
        # input()
