def match(w, s):
    if (w, s) in cache:
        return cache[(w, s)]
    
    while s < len(S) and w < len(W) and (W[w] == '?' or W[w] == S[s]):
        cache[(w, s)] = match(w + 1, s + 1)
        return cache[(w, s)]
        
    if w == len(W):
        cache[(w, s)] = (s == len(S))
        return cache[(w, s)]
    
    if W[w] == '*':
        if match(w + 1, s) or (s < len(S) and match(w, s + 1)):
            cache[(w, s)] = True
            return True

    cache[(w, s)] = False
    return False


for _ in xrange(input()):
    W = raw_input().strip()
    answers = []
    for _ in xrange(input()):
        S = raw_input().strip()
        cache = {}
        if match(0, 0):
            answers.append(S)
    answers.sort()
    for ans in answers:
        print ans
