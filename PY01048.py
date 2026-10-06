def count_ways(n):
    while n % 2 == 0:
        n //= 2
    
    total_odd_divisors = 1
    d = 3
    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                count += 1
                n //= d
            total_odd_divisors *= (count + 1)
        d += 2
        
    if n > 1:
        total_odd_divisors *= 2

    return total_odd_divisors - 1

T = int(input())
results = []
for i in range(T):
    n = int(input())
    results.append(str(count_ways(n)))
    
print("\n".join(results))