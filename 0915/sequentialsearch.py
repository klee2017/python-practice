def seq_srch(s, key):
    index = 0
    while (index < len(s)):
        cur_char = s[index]
        if cur_char == key:
            return index
        index += 1
    return -1

search_char = 'f'
result1 = seq_srch('league of legend', search_char)
print(result1)


def seq_sr(s, key):
    for i, cur_char in enumerate(list(s)):
        if cur_char == key:
            return i
    return -1


search_char = 'f'
result2 = seq_sr('league of legend', search_char)
print(result2)
s_ch = 'z'
result3 = seq_sr('league of legend', s_ch)
print(result3)
