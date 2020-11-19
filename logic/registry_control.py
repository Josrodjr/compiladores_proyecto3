# according to arm asm target is r1 throug r10 for general purpose
# not using 10 cuz of the luls

import copy

avail_registers = {
    'r1': 0,
    'r2': 0,
    'r3': 0,
    'r4': 0,
    'r5': 0,
    'r6': 0,
    'r7': 0,
    'r8': 0,
    'r9': 0
}

class reg_controller():
    registers = 0

    def __init__(self):
        self.registers = copy.deepcopy(avail_registers)

    def find_available(self):
        found = 0
        for i in range(1,10):
            # check the value in self registers
            if self.registers['r'+str(i)] == 0:
                found = 'r'+str(i)
                break
        return found

    def reserve(self, reg):
        if reg in self.registers:
            self.registers[reg] = 1

    def free(self, reg):
        if reg in self.registers:
            self.registers[reg] = 0


    def pop(self):
        found = 0
        for i in reversed(range(1,10)):
            # check backwards the last intem in list
            if self.registers['r'+str(i)] == 1:
                found = 'r'+str(i)
                self.registers[found] = 0
                break
        return found
# test
# controller = reg_controller()

# controller.reserve('r1')
# controller.free('r1')

# a = controller.find_available()
# print(a)

# print(controller.pop())