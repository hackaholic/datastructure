import sys

def randomarr(n, filen):
    import random
    f = open(filen, "w")
    for x in range(n):
        f.write(str(random.randint(0, n)) + "\n")
    f.close()

if __name__ == '__main__':
    randomarr(int(sys.argv[1]), sys.argv[2])
