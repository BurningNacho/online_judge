
def my_island(n_vertices, vertices):
    # x_vertices = [int(v[0]) for v in vertices]
    # y_vertices = [int(v[1]) for v in vertices]
    # print(vertices)
    # print(f'{x_vertices} {y_vertices}')
    max_x = 0
    max_y = 0
    for v_x, v_y in vertices:
        if int(v_x) > max_x: max_x = int(v_x)
        if int(v_y) > max_y: max_y = int(v_y)
    # print(f'{max_x} {max_y}')

    island_planning = [[0]*(max_y+1)]*(max_x+1)

    for row in island_planning:
        print(''.join([str(pos) for pos in row]))

    print()
    for v_x, v_y in vertices:
        island_planning[int(v_x)][int(v_y)] = 1

    for row in island_planning:
        print(''.join([str(pos) for pos in row]))

    print(f'{max_x} {max_y}')
    pass

if __name__ == '__main__':

    problem_input = []
    n_vertices = int(input())
    while n_vertices:

        problem_input.append([n_vertices, [input().split() for i in range(n_vertices)]])
        # print(problem_input)
        n_vertices = int(input())

    for problem in problem_input:
        my_island(problem[0], problem[1])
