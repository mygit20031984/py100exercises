d = {"a": 1, "b": 2, "c": 3}

d.pop("c")
d.pop("b")
print(d)


d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)