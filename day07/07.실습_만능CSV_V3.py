def read_csv(filename):
    fp = open(filename, "r", encoding="utf-8")
    data = fp.read()
    fp.close()
    elements = []

    # print(data)
    # print('-'*50)

    rows = data.split("\n")
    # print(rows[0])
    keys = rows[0].split(',')
    for idx in range(len(keys)):
        keys[idx] = keys[idx].strip()
        # print(keys[idx])
    # print(keys[1])

    element = {}

    for row in rows[1:]:
        fields = row.split(",")
        print('an',type(fields))
        for idx in range(len(keys)):
            key = keys[idx]
            field = fields[idx].strip()
            element[key] = field

        elements.append(element)
    return elements

filename = "./data/JB_Finance_Group.csv"
result = read_csv(filename)

print(result)