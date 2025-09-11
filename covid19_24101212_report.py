def normalize_data(n_cases, n_people, scale=1_000_000):
    norm_cases = []
    for idx, n in enumerate(n_cases):
        norm_cases.append(n / n_people[idx] * scale)
    return norm_cases

regions  = ['Seoul', 'Gyeongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu', 'Chungnam', 'Jeonnam', 'Jeonbuk', 'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Sejong']
n_people = [9550227,  13530519, 3359527,     3322373,   2938429,     2630254, 2393626,    2118183,   1838353,   1792476,    1597179,   1536270,   1454679,   1441970, 1124459, 675883,   365309]
n_covid  = [    644,       529,      38,          29,       148,          28,      41,         62,        23,        27,         27,        33,        16,        40,      20,      5,        4] 

sum_people = sum(n_people)
sum_covid  = sum(n_covid)
norm_covid = normalize_data(n_covid, n_people, 1_000_000)


lines1 = []
lines1.append("### Korean Population by Region")
lines1.append(f"* Total population: {sum_people:,}")
lines1.append("")
lines1.append("| Region | New Cases | Ratio (%) |")
lines1.append("| ------ | ---------- | --------- |")

for idx, pop in enumerate(n_people):
    ratio = pop / sum_people * 100
    lines1.append(f"| {regions[idx]} | {pop:,} | {ratio:.1f} |")
    
lines2 = []
lines2.append("### **Korean COVID-19**  new cases by Region")
lines2.append(f"* Total population: {sum_covid:,}")
lines2.append("")
lines2.append("| Region | Population | Ratio (%) |  New Cases/1M |")
lines2.append("| ------ | ---------- | --------- |  ------------ |")

for idx, cases in enumerate(n_people):
    ratio = cases / sum_covid * 100
    lines2.append(f"| {regions[idx]} | {cases:,} | {ratio:.1f} | {norm_covid[idx]:.1f}")
    

report24101212 = "\n".join(lines1) + "\n\n" + "\n".join(lines2)

print(report24101212)

with open("report24101212.md", "w", encoding="utf-8") as f:
    f.write(report24101212)

print(" file report24101212.md saved")