def read_data(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split(',')
                if len(parts) == 2:
                    midterm = int(parts[0].strip())
                    final = int(parts[1].strip())
                    data.append((midterm, final))
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error reading file: {e}")
    return data

def calc_weighted_average(data_2d, weight):
    average = []
    for midterm, final in data_2d:
        weighted_avg = (midterm * weight[0]) + (final * weight[1])
        average.append(weighted_avg)
    return average

def analyze_data(data_1d):
    n = len(data_1d)
    if n == 0:
        return 0, 0, 0, 0, 0

    sorted_data = sorted(data_1d)
    min_val = sorted_data[0]
    max_val = sorted_data[-1]
    mean = sum(data_1d) / n
    variance = sum((x - mean) ** 2 for x in data_1d) / n

    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    
    return mean, variance, median, min_val, max_val

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2:
        average = calc_weighted_average(data, [40/125, 60/100])

        with open('class_score_analysis.md', 'w') as report:
            report.write('### Individual Score\n\n')
            report.write('| Midterm | Final | Average |\n')
            report.write('| ------- | ----- | ------- |\n')
            for ((m_score, f_score), a_score) in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')

            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m_score for m_score, _ in data],
                'Final': [f_score for _, f_score in data],
                'Average': average }
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean:.3f}**\n')
                report.write(f'  * Variance: {var:.3f}\n')
                report.write(f'  * Median: **{median:.3f}**\n')
                report.write(f'  * Min/Max: ({min_:.3f}, {max_:.3f})\n')