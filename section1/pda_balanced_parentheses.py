class PDA:
    def __init__(self):
        self.stack = []
        self.alphabet = {'(', ')'}

    def accepts(self, input_string):
        for symbol in input_string:
            if symbol == '(':
                self.stack.append(symbol)
            elif symbol == ')':
                if not self.stack:
                    return False
                self.stack.pop()
        return not self.stack

# Test cases
print(PDA().accepts("()"))     # True
print(PDA().accepts("(())"))   # True
print(PDA().accepts("(()"))    # False
print(PDA().accepts(")("))     # False