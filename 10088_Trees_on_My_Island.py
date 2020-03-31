import math

def lattice_p(x1,y1,x2,y2):
    return math.gcd(x2-x1, y2-y1)-1
def determinant(x1, y1, x2, y2):
    return x1*y2-x2*y1
def poligonArea(vertices):
    area = 0
    lattice = 0
    i = -1
    for v_x, v_y in vertices:
        area += determinant(int(vertices[i][0]), int(vertices[i][1]) ,int(v_x), int(v_y))
        lattice += lattice_p(int(vertices[i][0]), int(vertices[i][1]) ,int(v_x), int(v_y))
        i += 1
    return int(abs(area)/2-(lattice/2 + len(vertices)/2)+1)

if __name__ == '__main__':

    problem_input = []
    n_vertices = int(input())
    while n_vertices:
        problem_input.append([n_vertices, [input().split() for _ in range(n_vertices)]])
        n_vertices = int(input())

    for problem in problem_input:
        print(poligonArea(problem[1]))
