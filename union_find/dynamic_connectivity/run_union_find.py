import sys
from weighted_quick_union import UnionFind
# from quick_union import UnionFind
# from quick_find import UnionFind
# from union_find import UnionFind


def main():
    N = int(sys.argv[1])
    uf = UnionFind(N)
    print("Input queries in format\nU a b\nC a b\nX for exit")
    input_string = ""
    while(input_string != "X"):
        input_string = input()
        if "U " in input_string:
            a, b = map(int, input_string.split()[1:])
            uf.union(int(a), int(b))
            uf.print()
        if "C " in input_string:
            a, b = map(int, input_string.split()[1:])
            if uf.connected(int(a), int(b)):
                print("{} and {} are connected".format(a, b))
            else:
                print("{} and {} are not connected".format(a, b))


if __name__ == "__main__":
    main()
