# Python program to find sum of primes
# in range from 1 to n.

def sumOfPrimes(n):
	# list to store prime numbers
	prime = [True] * (n + 1)
	p = 2
	while p * p <= n:
		# If prime[p] is not changed, then
		# it is a prime
		if prime[p] == True:
			# Update all multiples of p
			i = p * 2
			while i <= n:
				prime[i] = False
				i += p
		p += 1
	sum = 0
	for i in range (2, n + 1):
		if(prime[i]):
			sum += i
	return sum

n = 11
print(sumOfPrimes(n))

