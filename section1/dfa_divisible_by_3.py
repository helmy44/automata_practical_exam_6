class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'0', '1'}
        self.transitions = {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q1', '1': 'q2'},
            'q2': {'0': 'q2', '1': 'q0'}
        }
        self.start_state = 'q0'
        self.accept_states = {'q0'}

    def accepts(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transitions[current_state][symbol]
        return current_state in self.accept_states

# Test cases
print(DFA().accepts("111"))    # True (3 1's)
print(DFA().accepts("101"))    # False (2 1's)
print(DFA().accepts("11111"))  # False (5 1's)
print(DFA().accepts("0"))      # True (0 1's)