# Gene24_project - Analysis of SOX2 & OCT4
genes = {
    "SOX2": "ATGGCCCAGCACAACTCCGGGGGCTACGGCCTGGGCTCCGAGTACAGCTCCATGGGCTCCGAGTACAGC",
    "OCT4_POU5F1": "ATGGCGGGACACCTGGCTTCGGATTTCGCCTTCTCGCCCCCTCCAGGTGGTGGAGGTGATGGCCAG"
}

def gc_content(dna):
    gc = dna.count('G') + dna.count('C')
    return (gc / len(dna)) * 100

def analyze_gene(name, seq):
    print(f"\n=== {name} ===")
    print(f"Length: {len(seq)} bases")
    print(f"GC%: {gc_content(seq):.2f}%")
    if gc_content(seq) > 60:
        print("-> High GC: Strong transcription factor")

print("=== Stem Cell Gene Analysis ===")
for gene_name, sequence in genes.items():
    analyze_gene(gene_name, sequence)