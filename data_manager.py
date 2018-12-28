import csv


def select_data(filename, col_nums, dlm=','):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=dlm)
        selected_data = []
        next(csv_reader)  # skip headers

        for row in csv_reader:
            selected_data.append([item
                                  for num, item in enumerate(row)
                                  if num in col_nums])

    return selected_data
