

def pick_winner_2(ballots, candidates_left):
    value_counts = [0]*(n_candidates)
    for candidate in [int(ballot[0]) for ballot in ballots]:
        value_counts[candidate-1] += 1

    # if True in [i in value_counts for i in range(int(len(ballots)+1/2)+1,len(ballots)+1)]:
    if max(value_counts) >= int(candidates_left/2) + 1:
        return [value_counts.index(max(value_counts)) + 1]

    # min_val = min(list(filter(lambda num: num != 0, value_counts)))
    min_val = min([i for i in value_counts if i != 0])
    if value_counts.count(min_val) != candidates_left:
        for _ in range(value_counts.count(min_val)):
            ballots = [ballot[1:] if int(ballot[0]) == (value_counts.index(min_val) + 1) and len(ballot) else ballot for ballot in ballots]
            ballots = [ballot for ballot in ballots if int(ballot[0]) != (value_counts.index(min_val) + 1) and len(ballot)]
            # for ballot in ballots:
            #     if min_val in ballot:
            #         print('hehe')
            #     else:
            candidates_left -= 1
            value_counts[value_counts.index(min_val)] = -1
            # if len(ballots[value_counts.index(min_val)]) > 1:
            #     ballots[value_counts.index(min_val)][0] = ballots[value_counts.index(min_val)][1]
            # ballots = [ballot.replace(str(value_counts.index(min_val)+1), '') for ballot in ballots if len(ballot)>1]
        return pick_winner_2(ballots, candidates_left)

    return list(set([ballot[0] for ballot in ballots]))


def pick_winner(ballots):
    value_counts = {}
    for candidate in ballots[0]:
        value_counts[candidate] = 0
    for candidate in [ball[0] for ball in ballots]:
        value_counts[candidate] += 1

    max_val = max(value_counts, key=value_counts.get)
    if value_counts[max_val] > int(len(ballots) / 2):
        return list(max_val)

    min_val = min(value_counts.values())
    min_vals = [key for key in value_counts if value_counts[key] == min_val]

    if max_val in min_vals:
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
        candidates = int(input())
        candidates = [input() for candidate in range(candidates)]

        ballots = []
        ballot = input()
        while ballot:
            # ballots.append(ballot.replace(' ', ''))
            ballots.append(ballot.split())
            try:
                ballot = input()
            except:
                break
        cases.append([candidates,ballots])

    cases.reverse()

    while len(cases):
        candidates, ballots = cases.pop()
        global n_candidates
        n_candidates = len(candidates)
        for winner in pick_winner_2(ballots, len(candidates)):
            print(candidates[int(winner)-1])
        if cases:
            print()
