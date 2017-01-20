from collections import defaultdict

class Bot:

    def __init__(self, number):
        self.values = []
        self.number = number

    def set_value(self, v):
        self.values.append(v)
        self.values.sort()

    def has_values(self):
        return len(self.values) == 2

    def get_low(self):
        low = self.values[0]
        self.values = self.values[1:]
        return low

    def get_high(self):
        high = self.values[-1]
        self.values = self.values[:-1]
        return high

    def compares_correct_values(self):
        return len(self.values) == 2 and self.values[0] == 17 and self.values[1] == 61


bots = dict()
outputs = dict()

bots.values()

def get_bot(num):
    if not num in bots:
        bots[num] = Bot(num)
    return bots[num]

with open('input10.txt','r') as file_h:
    lines = file_h.readlines()

commands = [ line for line in lines if line.split()[0] == 'bot' ]
values = [ line for line in lines if line.split()[0] == 'value' ]

for value_line in values:
    parts = value_line.split()
    get_bot(int(parts[-1])).set_value(int(parts[1]))

executable_commands = [ command for command in commands if get_bot(int(command.split()[1])).has_values() ]
executed_commands = set()

while len(executable_commands) > 0:
    print "executable commands = {}".format(len(executable_commands))
    for command_line in executable_commands:
        #print command_line
        parts = command_line.split()
        bot = get_bot(int(parts[1]))
        if parts[5] == 'bot':
            bot_low = get_bot(int(parts[6]))
            bot_low.set_value(bot.get_low())
        else:
            print "out to {}".format(parts[6])
            outputs[int(parts[6])] = bot.get_low()

        if parts[-2] == 'bot':
            bot_high = get_bot(int(parts[-1]))
            bot_high.set_value(bot.get_high())
        else:
            print "out to {}".format(parts[-1])
            outputs[int(parts[-1])] = bot.get_high()
        executed_commands.add(command_line)

    for bot in bots.values():
        if bot.compares_correct_values():
            print "found!"
            print bot.number

    executable_commands = [ command for command in commands if get_bot(int(command.split()[1])).has_values() and not command in executed_commands ]

print outputs
