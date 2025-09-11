# covid19_statistics.py

def normalize_data(n_cases, n_people, scale=1_000_000):
    """cases per scale people (e.g., per 1M)"""
    return [c / p * scale for c, p in zip(n_cases, n_people)]

def md_table(headers, rows):
    """return a Markdown table string"""
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["-" * len(h) for h in headers]) + " |")
    for r in rows:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)

# ====== YOUR DATA (вставь полные списки без троеточий) ======
regions  = ['Seoul','Gyeonggi','Busan','Gyeongnam','Incheon','Gyeongbuk','Daegu','Chungnam',
            'Jeonnam','Jeonbuk','Chungbuk','Gangwon','Daejeon','Gwangju','Ulsan','Jeju','Sejong']
n_people = [9550227,13530519,3359527,3322373,2938429,2630254,2393626,2118183,
            1838353,1792476,1597719,1536270,1454679,1441970,1124459,675883,365309]  # 2021-08
n_covid  = [644,529,38,29,148,28,41,62,23,27,27,33,16,40,20,5,4]                    # 2021-09-21
# ============================================================

sum_people = sum(n_people)
sum_covid  = sum(n_covid)
per_million = normalize_data(n_covid, n_people, 1_000_000)

# ---------- Table 1: Population ----------
pop_rows = []
for r, p in zip(regions, n_people):
    ratio = p / sum_people * 100
    pop_rows.append([
        r,
        f"{p:,}",          # Population
        f"{ratio:,.1f}"    # Ratio %
    ])

section1 = []
section1.append("### Korean Population by Region")
section1.append(f"* Total population: {sum_people:,}")
section1.append("")
section1.append(md_table(["Region", "Population", "Ratio (%)"], pop_rows))


# ---------- Print to console ----------
print("\n".join(section1))
print()

# ---------- Save to Markdown file ----------
report = "\n".join(section1) + "\n\n"
with open("report.md", "w", encoding="utf-8") as f:
    f.write(report)

print("\nSaved Markdown to: report.md")