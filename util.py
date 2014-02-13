def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')
        for block in blocks(f):
            print block
    else:
         print 'usage: util.py filename'
