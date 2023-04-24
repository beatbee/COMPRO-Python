dna = input("DNA: ")
i = 0
ans = 0
new = []
for a in dna:
    if a == 'A': new.append('U')
    if a == 'C': new.append('G')
    if a == 'G': new.append('C')
    if a == 'T': new.append('A')
rna = ''.join(new)
while(i<len(rna)):
    if rna[i:i+3] == 'AUG':
        ans+=1
        i+=3
    if ans>0:
        if rna[i:i+3] == 'UAA' or rna[i:i+3] == 'UGA' or rna[i:i+3] == 'UAG':
            break
        i+=3
        ans+=1
    else:
        i+=1
print(f'{ans} Amino acid(s)')
"""
DNA: CGTACAACGCGGACAAGCGTACCTGCATCTACAAA
8 Amino acid(s)
"""

