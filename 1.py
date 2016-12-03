a = 0
def increment1():
    global a
    a += 1
    return a

def increment2(a):
    return a + 1


print increment1()
print increment2(a)

name_lengths = map(len, ["Mary", "Isla", "Sam"])
print name_lengths

squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
print squares