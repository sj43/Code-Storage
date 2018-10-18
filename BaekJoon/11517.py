while True:
    my_seq = input().split()
    my_seq = [int(s) for s in my_seq]
    if my_seq == [-1, -1, -1, -1]:
        break
    else:
        # find necessary info
        negative_index = my_seq.index(-1)
        for i in range(len(my_seq) - 1):
            if my_seq[i + 1] != -1 and my_seq[i] != -1:
                geo_rate = my_seq[i + 1] / my_seq[i]
                ari_rate = my_seq[i + 1] - my_seq[i]
                break
        ari = False
        geo = False

        # check for ari
        if negative_index == 0:
            my_seq[0] = my_seq[1] - ari_rate
        else:
            my_seq[negative_index] = my_seq[negative_index - 1] + ari_rate
        check = []
        check.append(my_seq[0])
        for k in range(3):
            check.append(check[k] + ari_rate)
        if check == my_seq:
            if 0 < my_seq[negative_index] <= 10000:
                ari = True

        # check for geo
        if negative_index == 0:
            my_seq[0] = my_seq[1] / geo_rate
        else:
            my_seq[negative_index] = my_seq[negative_index - 1] * geo_rate
        check = []
        check.append(my_seq[0])
        for k in range(3):
            check.append(check[k] * geo_rate)
        if check == my_seq:
            if 0 < my_seq[negative_index] <= 10000:
                geo = True

        # print
        j = negative_index
        if j == 0:
            if ari:
                print(int(my_seq[j + 1] - ari_rate))
            elif geo:
                val = my_seq[j + 1] / geo_rate
                if int(val) != val:
                    print(-1)
                else:
                    print(int(my_seq[j + 1] / geo_rate))
            else:
                print(-1)
        else:
            if ari:
                print(int(my_seq[j - 1] + ari_rate))
            elif geo:
                val = my_seq[j - 1] * geo_rate
                if int(val) != val:
                    print(-1)
                else:
                    print(int(my_seq[j - 1] * geo_rate))
            else:
                print(-1)
