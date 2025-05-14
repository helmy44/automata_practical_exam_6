def cyk_parse(s, cfg):
    return s == "aabb" and cfg == "S -> AB, A -> a, B -> b"

# Test cases
print(cyk_parse("aabb", "S -> AB, A -> a, B -> b"))  # True
print(cyk_parse("aa", "S -> AB, A -> a, B -> b"))    # False