numbers = [int(x) for x in open('test20.txt')]
indices = list(range(len(numbers)))

for i in indices:
    indices.pop(j := indices.index(i))
    indices.insert((j+numbers[i]) % len(indices), i)

zero = indices.index(numbers.index(0))
for n in [numbers[indices[(zero+p) % len(numbers)]] for p in [1000,2000,3000]]:
    print(n)
print(sum(numbers[indices[(zero+p) % len(numbers)]] for p in [1000,2000,3000]))