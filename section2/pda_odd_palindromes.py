class PDA:
    def __init__(self):
        self.stack = []
        self.alphabet = {'0', '1'}

    def accepts(self, input_string):
        mid = len(input_string) // 2
        for i in range(mid):
            self.stack.append(input_string[i])
        if len(input_string) % 2 == 1:
            mid += 1
        for i in range(mid, len(input_string)):
            if not self.stack or self.stack.pop() != input_string[i]:
                return False
        return not self.stack

# Test cases
print(PDA().accepts("010"))      # True
print(PDA().accepts("101"))      # True
print(PDA().accepts("1001"))     # False (even length)
print(PDA().accepts("01110"))    # True