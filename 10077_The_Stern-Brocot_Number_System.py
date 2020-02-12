## /external/100/10077.pdf

## ini 0/1; 1/1; 1/0 3 positions
## a/b is input
## a/b < x/y(middle) to determine if greater(middle goes to left) or bigger(middle goes right)
## a*y < x*b


class positions:

    def __init__(self):
        self.pos = [[0,1], [1,1], [1,0]]

    def right(self):
        self.pos[2] = list(self.pos[1])
        self.pos[1][0] = self.pos[0][0] + self.pos[1][0]
        self.pos[1][1] = self.pos[0][1] + self.pos[1][1]

    def left(self):
        self.pos[0] = list(self.pos[1])
        self.pos[1][0] = self.pos[2][0] + self.pos[1][0]
        self.pos[1][1] = self.pos[2][1] + self.pos[1][1]

    def mid_0(self):
        return self.pos[1][0]
    def mid_1(self):
        return self.pos[1][1]


def L_or_R(a, b, x, y):
    if (a*y < x*b):
        return 'R'
    else:
        return 'L'


def SBT(a, b):
    mat = positions()
    estados = ''
    while not(a==mat.mid_0() and b==mat.mid_1()):
        movement = L_or_R(a, b, mat.mid_0(), mat.mid_1())
        if movement == 'L':
            mat.left()
            estados += 'R'
        if movement == 'R':
            mat.right()
            estados += 'L'
            # print(estados)
    if estados:
        print(estados)


if __name__ == '__main__':

    tosolve=[]
    line = input()
    while line:
        if not(line == 'none'):
            tosolve.append(line.strip().split())
        try:
            line = input()
        except:
            line = ''
    for pair in tosolve:
        try:
            SBT(int(pair[0]),int(pair[1]))
        except:
            pass
