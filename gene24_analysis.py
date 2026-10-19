# Gene24 Stem Cell Marker Analysis
import matplotlib.pyplot as plt

stem_cells = [95, 92, 96, 94, 98]
differentiated = [5, 8, 3, 2, 6]

avg_stem = sum(stem_cells)/len(stem_cells)
avg_diff = sum(differentiated)/len(differentiated)

print("=== Gene24 Analysis ===")
print(f"Stem Cells avg: {avg_stem}%")
print(f"Differentiated avg: {avg_diff}%")
print("Conclusion: Gene24 is a Stem Cell Marker!")

plt.bar(["Stem Cells", "Differentiated"], [avg_stem, avg_diff], color=['#00C49A', '#FF6B6B'])
plt.ylabel("Gene24 Expression %")
plt.title("Gene24 is a Stem Cell Marker")
plt.savefig("gene24_chart.png")
print("Chart saved: gene24_chart.png")