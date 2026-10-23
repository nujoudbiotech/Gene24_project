import matplotlib.pyplot as plt

genes = {
    "SOX2": 66.15,
    "OCT4": 65.0,
    "KLF4": 72.13,
    "cMYC": 53.03
}

names = list(genes.keys())
values = list(genes.values())

plt.figure()
plt.bar(names, values)
plt.title("Gene24 - GC% of Yamanaka Factors")
plt.ylabel("GC Content %")
plt.xlabel("Genes")
plt.savefig("gc_chart.png")
print("Chart saved as gc_chart.png - 4 factors analyzed")
for n, v in genes.items():
    print(f"{n}: {v}%")