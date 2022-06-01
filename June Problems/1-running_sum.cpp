#include<vector>

class Solution
{
public:
    std::vector<int> runningSum(std::vector<int> &nums)
    {
        int R = 0;
        for (int i = 0; i < nums.size(); ++i) {
            R += nums[i];
            nums[i] = R;
        }
        return nums;
    }
};