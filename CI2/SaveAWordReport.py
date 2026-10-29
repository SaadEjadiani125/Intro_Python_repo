with open("text.txt", encoding="utf-8") as file:
    line = file.read().lower()
for p in ".,!?":
    line = line.replace(p, "")
sep = line.split()
 
counts = {}
for i in sep:
    counts[i] = counts.get(i, 0) + 1
 
with open("report.txt", "w", encoding="utf-8") as out:
    out.write(f"Words: {len(sep)}\n")
    out.write(f"Unique: {len(counts)}\n")
    for i in sorted(counts):
        out.write(f"{i:<10}{counts[i]}\n")
print("Report saved")