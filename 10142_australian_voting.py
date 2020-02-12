
def pick_winner(ballots):
    # print(ballots)
    value_counts = {}
    for candidate in ballots[0]:
        value_counts[candidate] = 0
    for candidate in [ball[0] for ball in ballots]:
        value_counts[candidate] += 1

    max_val = max(value_counts, key=value_counts.get)
    if value_counts[max_val] > int(len(ballots) / 2):
        # print('max')
        return list(max_val)

    min_val = min(value_counts.values())
    min_vals = [key for key in value_counts if value_counts[key] == min_val]

    if max_val in min_vals:
        # print('min')
        return min_vals

    for i, ballot in enumerate(ballots):
        for val in min_vals:
            ballots[i] = ballots[i].replace(str(val), '')
    return pick_winner(ballots)

if __name__ == '__main__':
    n_cases = int(input())
    cases = []
    input()

    for case in range(n_cases):
        n_candidates = int(input())
        candidates = [input() for candidate in range(n_candidates)]

        ballots = []
        ballot = input()
        while ballot:
            ballots.append(ballot.replace(' ', ''))
            ballot = input()
        cases.append(candidates)
        cases.append(ballots)

    cases.reverse()

    while len(cases):
        candidates = cases.pop()
        ballots = cases.pop()
        for winner in pick_winner(ballots):
            print(candidates[int(winner)-1])
        print()
