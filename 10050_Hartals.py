
## Main description goes here

week_days = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
free_days = ['Fr', 'Sa']

def solve_halt(halt_sim):
    halts = 0
    n_days, n_parties, party_halts = halt_sim
    for day in range(1, n_days+1):
        if day > 1 and week_days[(day-1)%len(week_days)] not in free_days:
            if 0 in [day%halt for halt in party_halts]:
                halts += 1
    return halts
if __name__ == '__main__':

    problem_input = []
    n_problems = int(input())

    for _ in range(n_problems):
        n_days = int(input())
        n_parties = int(input())
        party_halts = [int(input()) for _ in range(n_parties)]
        problem_input.append([n_days, n_parties, party_halts])

    for halt_sim in problem_input:
        print(solve_halt(halt_sim))
