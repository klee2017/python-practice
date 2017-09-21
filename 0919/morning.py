try:
    def mymax(seq):
        seq = seq.copy()
        seq_len = len(seq)
        max_value = seq[0]
        max_index = 0
        for i in range(seq_len):
            cur_item = seq[i]
            if cur_item > max_value:
                max_value = cur_item
                max_index = i
                return max_value
except:
    print('Invalid arguments')

sample = [9, 1, 6, 8, 11, 4, 3, 10, 2, 0, 5, 7]
result = mymax(sample)
print(result)

