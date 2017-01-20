class Machine:

    def __init__(self):
        self.registers = dict.fromkeys(['a','b','c','d'], 0)
        self.pp = 0

    def is_register(self, x):
        return x in self.registers.keys()

    def cpy(self, x, y):
        assert self.is_register(y)
        self.registers[y] = self.registers[x] if self.is_register(x) else int(x)
        self.pp += 1

    def inc(self, x):
        assert self.is_register(x)
        self.registers[x]+=1
        self.pp += 1

    def dec(self, x):
        assert self.is_register(x)
        self.registers[x]-=1
        self.pp += 1

    def jnz(self, x, y):
        print "testing {} to be zero, registers: {}".format(x, self.registers)
        not_zero = self.registers[x] != 0 if self.is_register(x) else int(x) != 0
        if not_zero:
            self.pp += int(y)
        else:
            self.pp += 1

    def execute(self, command_str):
        parts = command_str.split()
        if parts[0] == 'cpy':
            [_,x,y] = parts
            self.cpy(x,y)
        elif parts[0] == 'inc':
            [_,x] = parts
            self.inc(x)
        elif parts[0] == 'dec':
            [_,x] = parts
            self.dec(x)
        elif parts[0] == 'jnz':
            [_,x,y] = parts
            self.jnz(x,y)

    def execute_program(self, commands):
        self.pp = 0
        while self.pp in range(len(commands)):
            self.execute(commands[self.pp])
            if self.registers['a'] < 0:
                break
        self.print_registers()

    def print_registers(self):
        print self.registers

m = Machine()
m.registers['c'] = 1
program = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 17 c
cpy 18 d
inc a
dec d
jnz d -2
dec c
jnz c -5""".split("\n")

m.execute_program(program)
