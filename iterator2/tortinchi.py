import csv


def convert_comma_to_dot(func):
    def wrapper(file):
        new_rows = []
        rows = func(file)
        for row in rows:
            new_row = [col.replace(',', '.') for col in row]
            new_rows.append(new_row)
        return new_rows

    return wrapper


@convert_comma_to_dot
def read_csv(file):
    rows = []
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


def save_csv(file, rows):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)


input_file = 'countries of the world.csv'
output_file = 'countries of the world_converted.csv'

rows = read_csv(input_file)
save_csv(output_file, rows)
