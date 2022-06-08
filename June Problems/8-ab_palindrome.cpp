#include<string>
using namespace std;

class Solution {
public:
    bool isPalin(const string &s) {
        int i = 0, j = s.size() - 1;
        while (i < j) {
            if (s[i++] != s[j--]) {
                return false;
            }
        }
        return true;
    }
    
    int removePalindromeSub(string s) {
        return (isPalin(s)) ? 1 : 2;
    }
};