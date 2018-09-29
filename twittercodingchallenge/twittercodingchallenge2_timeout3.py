# Complete the closest function below.
def closest(s, queries):
    result = []
    char_to_index = {}
    # make dictionary
    for idx, ch in enumerate(s):
        if ch in char_to_index:
            char_to_index[ch].append(idx)
        else:
            new_list = []
            new_list.append(idx)
            char_to_index[ch] = new_list

    # solve for every query
    for que in queries:
        min_distance = -1
        removed = False
        if char_to_index[s[que]]:
            temp_list = char_to_index[s[que]]
            idx = temp_list.index(que)
            if que in temp_list:
                temp_list.remove(que)
                removed = True
            if temp_list:
                min_distance = min(
                    temp_list, key=lambda x: abs(x - que))
            if min_distance == que:
                min_distance = -1
            if removed:
                temp_list.insert(idx, que)
        result.append(min_distance)
    return result
