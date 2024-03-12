#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print(f"{len(sys.argv) - 1:d} arguments:")
    for w in range(1, len(sys.argv)):
        print(f"{w:d}: {sys.argv[w]}")
