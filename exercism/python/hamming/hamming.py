def distance(strand_a, strand_b):
    
    split_strand_a = [i for i in strand_a]
    split_strand_b = [i for i in strand_b]

    print(split_strand_b)
    print(split_strand_a)
    if len(split_strand_b) != len(split_strand_a):
        raise ValueError("length mismatches")
    diff_count = 0
    for starnd_index in range(len(strand_a)):
        if split_strand_a[starnd_index] is not split_strand_b[starnd_index]:
            diff_count += 1
    return diff_count
