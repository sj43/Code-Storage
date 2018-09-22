try:
    file = open('test.txt','rb')
except (IOError, EOFError) as e:
    print('An IOError occured. {}'.format(e.args[-1]))


try:
    file = open('test.txt','rb')
except Exception:
    raise
