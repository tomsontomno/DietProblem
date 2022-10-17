import csv


def csv2list():
    with open('Nutrients.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for i, value_i in enumerate(data):
        for j, value_j in enumerate(value_i):
            if value_j == '':
                data[i][j] = 0
    return data


"""
fields = data[0]
data.pop(0)
rows = data
"""


def list2csv(fields, rows):
    with open('Nutrients.csv', 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)

        write.writerow(fields)
        write.writerows(rows)


def fields2min(data):
    new_fields = []
    for i, value in enumerate(data):
        new_fields.append([value, 0])
    return new_fields


if __name__ == '__main__':
    used_data = csv2list()
    print(used_data)