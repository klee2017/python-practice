sample = [9, 1, 6, 8, 4, 3, 2, 0, 5, 7]

def sel_sort(seq):
    seq = seq.copy()
    seq_len = len(seq)

    min_value = seq[0]
    min_index = 0

    for i in range(seq_len):
        cur_item = sample[i]

        if cur_item < min_value:
            min_value = cur_item
            min_index = i
            
    seq[0], seq[min_index] = seq[min_index], seq[0]
    return seq

result = sel_sort(sample)
print(result)




def sequential_search(seq):
    seq_len = len(seq)
    for i in range(seq_len - 1):
        print('Loop[%d], Current list : %s' % (i, seq))
        min_index = i
        min_val = seq[i]

        for j in range(i,seq_len):
            if seq[j] < min_val:
                min_index = j
                min_val = seq[min_index]
        seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq

sequential_search(sample)


