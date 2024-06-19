
def read_data(file, start_line, end_line):
    with open(file, 'r') as data:
        rows = []
        for i, current_row in enumerate(data, start=1):
            if start_line <= i <= end_line:
                rows.append(current_row[1:-2].strip().split(', '))
            elif i > end_line:
                break
    return rows
