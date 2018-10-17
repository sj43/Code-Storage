while True:
    my_seq = []
    for _ in range(4):
        my_seq.append(int(input()))
    if all(element == -1 for element in my_seq):
        break
    else:
        ari_rate = 0
        geo_rate = 1
        prev_v = 0
        for element in my_seq:
            if element != -1:
                if prev_v == 0:
                    prev_v = element
                else:
                    ari_rate = element - prev_v
                    geo_rate = element / prev_v
            else:
