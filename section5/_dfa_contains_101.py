class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'0', '1'}
        self.transitions = {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q2', '1': 'q1'},
            'q2': {'0': 'q0', '1': 'q3'},
            'q3': {'0': 'q3', '1': 'q3'}
        }
        self.start_state = 'q0'
        self.accept_states = {'q3'}

    def accepts(self, input_string):
        state = self.start_state
        for symbol in input_string:
            state = self.transitions[state][symbol]
        return state in self.accept_states

# Test cases
print(DFA().accepts("0101"))   # True
print(DFA().accepts("101"))    # True
print(DFA().accepts("111"))    # False
print(DFA().accepts("00100"))  # False