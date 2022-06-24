def zeros(num: int) -> int:
    count = 0
    for x in range(1, num + 1):
        n = 0
        while x % 5 == 0:
            x /= 5
            n += 1
        count += n
    return count if num != 0 else 0