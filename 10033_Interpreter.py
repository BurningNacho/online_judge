

class custom_interpreter:
    def __init__(self, RAM):
        self.regs = ['000' for _ in range(10)]
        self.instructions = 0
        self.ram = RAM

    def instruction(self, i): # i [Xd/nsa]
        i = str(i)
        self.instructions += 1
        if int(i) == 0:  return 1, 0
        if i == '100':
            return 0, self.instructions
        if i[0] == '2': # set register d to n (between 0 and 9)
            self.regs[int(i[1])] = i[2]
            return 1, 0
        if i[0] == '3': # means add n to register d
            self.regs[int(i[1])] = (int(self.regs[int(i[1])]) + int(i[2]))%1000
            return 1, 0
        if i[0] == '4': # means multiply register d by n
            self.regs[int(i[1])] = (int(self.regs[int(i[1])]) * int(i[2]))%1000
            return 1, 0
        if i[0] == '5': # means set register d to the value of register s
            self.regs[int(i[1])] = self.regs[int(i[2])]
            return 1, 0
        if i[0] == '6': # means add the value of register s to register d
            self.regs[int(i[1])] = (int(self.regs[int(i[1])]) + int(self.regs[int(i[2])]))%1000
            return 1, 0
        if i[0] == '7': # means multiply register d by the value of register s
            self.regs[int(i[1])] = (int(self.regs[int(i[1])]) * int(self.regs[int(i[2])]))%1000
            return 1, 0
        if i[0] == '8': # means set register d to the value in RAM whose address is in register a
            self.regs[int(i[1])] = self.ram[int(self.regs[int(i[2])])]
            return 1, 0
        if i[0] == '9': # means set the value in RAM whose address is in register a to that of register s
            self.ram[int(self.regs[int(i[2])])] = self.regs[int(i[1])]
            return 1, 0
        if i[0] == '0': # means goto the location in register d unless register s contains 0
            if int(self.regs[int(i[2])]) == 0:
                return 1, 0
            return 1, self.regs[int(i[1])]

    def run(self):
        i = 0
        iter = 0
        running = 1
        while running:
            # print(f'next instruction # {i}')
            running, iter = self.instruction(self.ram[i])
            i += 1
            if iter: i = int(iter)
        return f'{self.instructions}'


def solve_problem(problem):
    CI = custom_interpreter(problem)
    val = CI.run()
    return val

if __name__ == '__main__':

    n_cases = int(input())
    problem_input = [[] for _ in range(n_cases)]
    line = input()
    for i in range(n_cases):
        line = input()
        while line != '':
            problem_input[i].append(line)
            try: line = input()
            except: break

    for problem in problem_input:
        problem.extend([0 for _ in range(1000-len(problem))])
        print(solve_problem(problem))
        if problem != problem_input[-1]:
            print()
