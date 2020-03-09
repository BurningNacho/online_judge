
## Main description goes here

erdos = 'Erdos, P.'

def erdos_numb(erdos_list):
    papers = erdos_list[0]
    candidates = erdos_list[1]
    candidate_rank = {candidate: infinity for candidate in candidates}
    for paper in papers:
        if erdos in paper:
            for candidate in paper:



    return erdos_list

if __name__ == '__main__':

    problem_input = []
    n_problems = int(input())

    for _ in range(n_problems):
        n_papers, n_candidates = input().split()
        papers = [input().split(':')[0] for _ in range(int(n_papers))]
        candidates = [input().split(':') for _ in range(int(n_candidates))]

        problem_input.append([papers, candidates])

    for sim in problem_input:
        print(erdos_numb(sim))
