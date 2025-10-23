# 在此文件中实现 PrimeList 函数
def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔
    参数:     N - 正整数
    返回:     str - 包含所有小于 N 的质数的字符串
    """
    primes = int(input())
    for num in range(1, N):
        is_prime = True
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return " ".join(primes)
