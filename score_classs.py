def read_data(filename):
    # TODO) Read `filename` as a list of integers
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = [p.strip() for p in line.split(',')]
            if len(parts) < 2:
                continue
            m = int(parts[0]);  f = int(parts[1])
            data.append((m, f))
    return data

def calc_weighted_average(data_2d, weight):
    # TODO) Calculate the weighted averages of each row of `data_2d`
    average = []
    for m, f in data_2d:
       avg = weight[0]*m + weight[1]*f
       average.append(avg)
    return average

def analyze_data(data_1d):
    # если список пустой
    if not data_1d:
        return float('nan'), float('nan'), float('nan'), float('nan'), float('nan')

    # Среднее
    mean = sum(data_1d) / len(data_1d)

    # Дисперсия (генеральная: делим на n)
    var = sum((x - mean) ** 2 for x in data_1d) / len(data_1d)

    # Медиана
    sorted_data = sorted(data_1d)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        median = float(sorted_data[mid])
    else:
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2

    # Минимум и максимум
    min_val = min(data_1d)
    max_val = max(data_1d)

    return mean, var, median, min_val, max_val


if 'name' == '__main__':
    import os
    data = read_data(os.path.join('data', 'class_score_en.csv'))
    if data and len(data[0]) == 2:
        average = calc_weighted_average(data, [40/125, 60/100])

        with open('class_score_analysis.md', 'w', encoding='utf-8') as report:
            report.write('# Class Score Analysis\n\n')
            report.write('## Individual Score\n\n')
            report.write('| Midterm | Final | Average |\n')
            report.write('|---:|---:|---:|\n')
            for (m_score, f_score), a_score in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')

            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m for m,_ in data],
                'Final'  : [f for _,f in data],
                'Average': average}
            for name, column in data_columns.items():
                
                mean, var, median, min_, max_ = analyze_data([float(x) for x in column])
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean:.3f}**\n')
                report.write(f'  * Variance: {var:.3f}\n')
                report.write(f'  * Median: **{median:.3f}**\n')
                report.write(f'  * Min/Max: ({min_:.3f}, {max_:.3f})\n')
