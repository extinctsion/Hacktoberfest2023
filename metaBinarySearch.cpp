// C++ implementation of above approach

#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

// Function to show the working of Meta binary search
int bsearch(vector<int> A, int key_to_search)
{
    int n = (int)A.size();
    // Set number of bits to represent largest array index
    int lg = log2(n-1)+1; 

    //while ((1 << lg) < n - 1)
        //lg += 1;

    int pos = 0;
    for (int i = lg ; i >= 0; i--) {
        if (A[pos] == key_to_search)
            return pos;

        // Incrementally construct the
        // index of the target value
        int new_pos = pos | (1 << i);

        // find the element in one
        // direction and update position
        if ((new_pos < n) && (A[new_pos] <= key_to_search))
            pos = new_pos;
    }

    // if element found return pos otherwise -1
    return ((A[pos] == key_to_search) ? pos : -1);
}

// Driver code
int main(void)
{

    vector<int> A = { -2, 10, 100, 250, 32315 };
    cout << bsearch(A, 10) << endl;

    return 0;
}

// This implementation was improved by Tanin
