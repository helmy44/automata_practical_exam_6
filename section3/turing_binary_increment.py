class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape[::-1])
        self.position = 0
        self.state = 'start'

    def step(self):
        if self.state == 'start':
            while self.position < len(self.tape):
                if self.tape[self.position] == '0':
                    self.tape[self.position] = '1'
                    return
                elif self.tape[self.position] == '1':
                    self.tape[self.position] = '0'
                    self.position += 1
            self.tape.append('1')

    def run(self):
        self.step()
        return ''.join(reversed(self.tape))

# Test cases
print(TuringMachine("1").run())   # "10"
print(TuringMachine("0").run())   # "1"
print(TuringMachine("111").run()) # "1000"