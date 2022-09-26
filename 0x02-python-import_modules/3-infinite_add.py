#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv)
    sum = 0
    if number > 1:
        for i in range(1, number):
            sum += int(sys.argv[i])
        print("{}".format(sum))
    else:
        print("{}".format(sum))
