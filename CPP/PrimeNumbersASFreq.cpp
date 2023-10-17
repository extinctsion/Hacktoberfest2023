// C++ program to print all primes between 1
// to N in reverse order using Sieve of
// Eratosthenes
#include <bits/stdc++.h>
using namespace std;

void primeNumbersReversed(int n)
{
	// Create a boolean array "prime[0..n]" and
	// initialize all entries it as true. A value
	// in prime[i] will finally be false if i
	// is Not a prime, else true.
	bool prime[n + 1];
	memset(prime, true, sizeof(prime));

	for (int p = 2; p * p <= n; p++) {

		// If prime[p] is not changed, then
		// it is a prime
		if (prime[p] == true) {

			// Update all multiples of p
			for (int i = p * 2; i <= n; i += p)
				prime[i] = false;
		}
	}

	// Print all prime numbers in reverse order
	for (int p = n; p >= 2; p--)
		if (prime[p])
			cout << p << " ";
}

// Driver Program
int main()
{
	// static input
	int N = 25;

	// to display
	cout << "Prime number in reverse order" << endl;

	if (N == 1)
		cout << "No prime no exist in this range";
	else
		Reverseorder(N); // calling the function

	return 0;
}
