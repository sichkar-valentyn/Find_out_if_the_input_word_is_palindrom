# Imlementing the task
# Find out if the input word is palindrom

dna = input().lower()  # Putting word in low case

# First way to check - is usinf loop
i = 0
j = len(dna) - 1
palindrom = True
while i < j:
    if dna[i] != dna[j]:
        palindrom = False
        break # stop the loop
    i += 1
    j -= 1
if palindrom:
    print('Yes')
else:
    print('No')

# Another way to check - slicing of strings
dna_revers = dna[::-1]
if dna == dna_revers:
    print('Yes')
else:
    print('No')
