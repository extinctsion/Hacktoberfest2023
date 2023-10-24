// C++ program to find all string
// which are greater than given length k

#include <bits/stdc++.h>
using namespace std;

// function find string greater than
// length k
void string_k(string s, int k)
{
	// create an empty string
	string w = "";
	// iterate the loop till every space
	for (int i = 0; i < s.size(); i++) {
		if (s[i] != ' ')

			// append this sub string in
			// string w
			w = w + s[i];
		else {

			// if length of current sub
			// string w is greater than
			// k then print
			if (w.size() > k)
				cout << w << " ";
			w = "";
		}
	}
}

// Driver code
int main()
{
	string s = "geek for geeks";
	int k = 3;
	s = s + " ";
	string_k(s, k);
	return 0;
}

// This code is contributed by
// Manish Shaw (manishshaw1)
