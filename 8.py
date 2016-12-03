# def zero(s):
#     if s[0] == '0':
#         return s[1:]

# def one(s):
#     if s[0] == 1:
#         return s[1:]

# def rule_sequence(s,rules):
#     for rule in rules:
#         s = rule(s)
#         if s == None:
#             break

#     return s

###

def rule_sequence(s, rules):
    if s == None or not rules:
        return s
    else:
        return rule_sequence(rules[0](s), rules[1:])
