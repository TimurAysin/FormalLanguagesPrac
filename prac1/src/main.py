from solver import Solution


def main():
    s = input().split()
    lang = s[0]
    k = int(s[1])
    l = int(s[2])

    solver = Solution(lang, k, l)
    print(solver.solve())


if __name__ == "__main__":
    main()
