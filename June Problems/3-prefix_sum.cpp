#include<vector>
using namespace std;

class NumMatrix {
public:
    vector<vector<int>> sums;

    NumMatrix(vector<vector<int>>& matrix): 
    sums(matrix.size(), vector<int> (matrix[0].size(), 0))
    {
        int m = matrix.size(), n = matrix[0].size(), cumu = 0;
        for (int i = 0; i < m; ++i) {
            cumu = 0;
            for (int j = 0; j < n; ++j) {
                cumu += matrix[i][j];
                sums[i][j] = cumu;
                if (i != 0) {
                    sums[i][j] += sums[i-1][j];
                }
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = sums[row2][col2];
        
        if(row1 > 0)
            sum -= sums[row1-1][col2];
        if(col1 > 0)
            sum -= sums[row2][col1-1];
        if(row1 > 0 && col1 > 0)
            sum += sums[row1-1][col1-1];
        
        return sum;
    }
};