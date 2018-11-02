# Day2
# Asked by Uber

# input: [1,2,3,4,5], output: [120,60,40,30,24]
# input: [3,2,1] output: [2,3,6]
# follow up: what if you can't use division?


lst = list(map(int, input().split()))


# 1. naive solution
# first obtain product of all elements, and call it product_all.
# then iterate through each element in lst and perform product_all / element, then
# append to end of a new list
# note: need to take care of edge case involving 0.


def naive_product_all_else(lst):
    result = []
    zeros = []
    product_all = 1
    for count, element in enumerate(lst):
        if element == 0:
            zeros.append(count)
        else:
            product_all *= element
    if len(zeros) > 1:
        return [0] * len(result)
    elif len(zeros) == 1:
        for count, element in enumerate(lst):
            if element == 0:
                result.append(product_all)
            else:
                result.append(0)
        return result
    else:
        for count, element in enumerate(lst):
            result.append(int(product_all / element))
        return result


# print(naive_product_all_else(lst))


# 2. without division
# naive way to do solve this without division would be to simply brute force:
# just manually multiply all other elements together for each element in lst.
# But this would be very inefficient timewise. Better way to do this
# would be to rotate lst to the right and multiply to out 1-initialized result list.

def rotate_product_all_else(lst):
    result = [1] * len(lst)
    lst2 = list(lst)
    for i in range(len(lst) - 1):
        temp = lst2[0]
        lst2.pop(0)
        lst2.append(temp)
        for j in range(len(result)):
            result[j] *= lst2[j]
    return result


print(rotate_product_all_else(lst))
