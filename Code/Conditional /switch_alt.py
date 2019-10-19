# Switch statement is not explicitly defined in Python
# Hence, we implement switch with the help of a dictionary

a = 1

switch = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four"
    }

print(switch.get(a))
