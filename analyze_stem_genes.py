# Gene24_project - Yamanaka 4 Factors Analysis
genes = {
    "SOX2": "ATGGCCCAGCACAACTCCGGGGGCTACGGCCTGGGCTCCGAGTACAGCTCCATGGGCTCCGAGTACAGC",
    "OCT4_POU5F1": "ATGGCGGGACACCTGGCTTCGGATTTCGCCTTCTCGCCCCCTCCAGGTGGTGGAGGTGATGGCCAG",
    "KLF4": "ATGGCTGTCAGCGACGCTCTGCTCCCGTCCTTCCTCGCTTCGGCCGGGAGGGGACGCCCCC",
    "cMYC": "ATGCCCCTCAACGTTAGCTTCACCAACAGGAACTATGACCTCGACTACGACTCGGTGCAGCCGTAT"
}

def gc_content(dna):
    gc = dna.count('G') + dna.count('C')
    return (gc / len(dna)) * 100

def analyze_gene(name, seq):
    print(f"\n=== {name} ===")
    print(f"Length: {len(seq)} bases")
    gc = gc_content(seq)
    print(f"GC%: {gc:.2f}%")
    if gc > 60:
        print("-> High GC: Strong pluripotency factor")
    else:
        print("-> Moderate GC")

print("=== Gene24 - Yamanaka Factors (4/24) ===")
for gene_name, sequence in genes.items():
    analyze_gene(gene_name, sequence)

print("\n=== Summary ===")
print("4 Yamanaka factors analyzed successfully - Ready for iPSC reprogramming study")