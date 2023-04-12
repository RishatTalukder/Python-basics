def collatz(end):
    values = []
    for i in range(1, end + 1):
        while True:
            if i not in values:
                values.append(i)
            # print(i)
            if i == 1:
                break
            elif i % 2 == 0:
                i = i // 2
            else:
                i = 3 * i + 1

            if i in values:
                break

    return values


value_list = collatz(100000)
print(sorted(value_list))
print(len(value_list))
