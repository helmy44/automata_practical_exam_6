def dfa_equivalent(dfa1, dfa2):
    return dfa1 == dfa2

# Test cases
print(dfa_equivalent({'states': 2}, {'states': 2}))  # True
print(dfa_equivalent({'states': 2}, {'states': 3}))  # False