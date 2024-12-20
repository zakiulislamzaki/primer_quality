import math

def analyze_primer(primer):
    length = len(primer)
    gc_content = calculate_gc_content(primer)
    melting_temp = calculate_melting_temperature(primer)
    return length, gc_content, melting_temp

def calculate_gc_content(sequence):
    return (sequence.count('G') + sequence.count('C')) / len(sequence)

def calculate_melting_temperature(sequence):
    gc_content = calculate_gc_content(sequence)
    return 64.9 + 41 * (gc_content - 0.41)

def assess_primer_pair(primer1, primer2):
    l1, gc1, tm1 = analyze_primer(primer1)
    l2, gc2, tm2 = analyze_primer(primer2)

    print(f"Primer 1:\nLength: {l1}\nGC Content: {gc1:.2f}\nMelting Temperature: {tm1:.2f}")
    print(f"Primer 2:\nLength: {l2}\nGC Content: {gc2:.2f}\nMelting Temperature: {tm2:.2f}")

    if abs(tm1 - tm2) > 5:
        return "Very Bad: Significant Tm difference"
    elif l1 < 18 or l1 > 24 or l2 < 18 or l2 > 24:
        return "Bad: Primer length outside recommended range"
    elif gc1 < 0.4 or gc1 > 0.6 or gc2 < 0.4 or gc2 > 0.6:
        return "Bad: GC content outside recommended range"
    elif primer1 in primer2 or primer2 in primer1:
        return "Bad: Self-complementarity or primer-dimer potential"
    else:
        return "Good: Meets basic primer design criteria"

# Example usage:
primer1 = input("Enter the forward primer: ")
primer2 = input("Enter the reverse primer: ")

quality = assess_primer_pair(primer1, primer2)
print(f"Primer pair quality: {quality}")