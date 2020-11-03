from solver import Solution


def main():
    tests = [["ab+c.aba.*.bac.+.+* 3 2", "YES"], ["acb..bab.c.*.ab.ba.+.+*a. 3 0", "NO"],
              ["ab+ 3 0", "NO"], ["ab.* 4 2", "YES"]]

    for test in tests:
        print(test)
        lang = test[0].split()[0]
        k = int(test[0].split()[1])
        l = int(test[0].split()[2])
        ans = test[1]

        s = Solution(lang, k, l)
        if s.solve() == ans:
            print("Test passed.")
        else:
            print("Test didn't pass.")


if __name__ == "__main__":
    main()
