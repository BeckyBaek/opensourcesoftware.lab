def read_data(filename):
    data = []
    with open(filename, 'r') as fi:
        for line in fi.readlines():
            try:
                values = [int(word) for word in line.split(',')]
                data.append(values)
            except ValueError as ex:
                print(f'A line is ignored.(message: {ex})')
    return data
    

def calc_weighted_average(data_2d, weight):
    # TODO) Calculate the weighted averages of each row of `data_2d`
    averages = []
    for row in data_2d:
        weighted_average = sum(val * w for val, w in zip(row, weight))
        averages.append(weighted_average)
    return averages

def analyze_data(data_1d):
    # TODO) Derive summary of the given `data_1d`
    # Note) Please don't use NumPy and other libraries. Do it yourself.
    mean = 0
    var = 0
    median = 0
    mean = sum(data_1d)/ len(data_1d)
    var = sum((x - mean) ** 2 for x in data_1d) / len(data_1d)
    data_1d_sorted = sorted(data_1d)
    n = len(data_1d_sorted)
    if n % 2 == 0:
        median = (data_1d_sorted [ n // 2 -1] + data_1d_sorted[n // 2]) / 2
    else:
        median = data_1d_sorted[n // 2]
    #min_data = min(data_1d)
    #max_data = max(data_1d)
    return mean, var, median, data_1d_sorted[0], data_1d_sorted[-1]

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    print(f"data: {data}")
    if data and len(data[0]) == 2: # Check 'data' is valid
        average = calc_weighted_average(data, [40/125, 60/100])
        print(f"average: {average}")

        # Write the analysis report as a markdown file
        with open('class_score_analysis.md', 'w') as report:
            report.write('### Individual Score\n\n')
            report.write('| Midterm | Final | Total |\n')
            report.write('| ------- | ----- | ----- |\n')
            for ((m_score, f_score), a_score) in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')

            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m_score for m_score, _ in data],
                'Final'  : [f_score for _, f_score in data],
                'Average': average }
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean:.3f}**\n')
                report.write(f'  * Variance: {var:.3f}\n')
                report.write(f'  * Median: **{median:.3f}**\n')
                report.write(f'  * Min/Max: ({min_:.3f}, {max_:.3f})\n')
