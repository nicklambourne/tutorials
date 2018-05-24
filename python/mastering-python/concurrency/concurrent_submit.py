from concurrent import futures


def factorise(n):
    if n == 1:
        return 1, []

    found = []

    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            if all(i % j != 0 for j in found):
                found.append(i)

    if not found:
        return n, [n]

    return n, found

if __name__ == '__main__':
    with futures.ProcessPoolExecutor() as pool:
        fs = [pool.submit(factorise, x) for x in range(1, 10001)]
        for f in futures.as_completed(fs):
            try:
                number, factors = f.result()
            except ValueError:
                continue
            print('{}: {}'.format(number, factors))
