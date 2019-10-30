def parent():
    some = [0]

    def use_some(new_val):
        some.append(new_val)
        print(some)

    return use_some

val = parent()

for i in range(1, 5):
    val(i)

