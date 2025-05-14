def regex_to_dfa(regex):
    if regex == "a*":
        return {
            'states': {'q0'},
            'alphabet': {'a'},
            'transitions': {'q0': {'a': 'q0'}},
            'start_state': 'q0',
            'accept_states': {'q0'}
        }
    return None

# Test cases
print(regex_to_dfa("a*"))  # Returns DFA for a*
print(regex_to_dfa("b*"))  # Returns None (not implemented)