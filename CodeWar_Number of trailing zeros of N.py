def zeros(num: int) -> int:
    if num != 0:
        count = 0
        for x in range(1, num + 1):
            if (str(x).endswith("0")):
                count += 1
            elif (str(x).endswith("5")):
                n = 0
                while x % 5 == 0:
                    x /= 5
                    n += 1
                count += n
        return count
    else:
        return 0