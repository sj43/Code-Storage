def parChecker(symbolString):
    s = []
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.append(symbol)
        else:
            if len(s) == 0:
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and len(s) == 0:
        return True
    else:
        return False


def matches(open_bracket, close_bracket):
    opens = "([{"
    closers = ")]}"
    if open_bracket in opens and close_bracket in closers:
        return opens.index(open_bracket) == closers.index(close_bracket)
    return False



for _ in xrange(input()):
    string = str(raw_input().strip().split())
    string = string[2: -2]
    if parChecker(string):
        print 'YES'
    else:
        print 'NO'
