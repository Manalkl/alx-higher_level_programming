#!/usr/bin/python3

import sys

def main():
    arguments = sys.argv[1:]
    result = sum(int(arg) for arg in arguments)
    print(result)

if __name__ == "__main__":
    main()
