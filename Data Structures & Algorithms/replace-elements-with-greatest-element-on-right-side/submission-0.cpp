class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int left = 0;

        while (left < arr.size() - 1) {
            int right = arr.size() - 1;
            int biggest = 0;
            while (right > -1 and right > left) {
                if (arr[right] > biggest) { 
                    biggest = arr[right]; 
                }
                right--;
            }
            arr[left] = biggest; 
            left++;
        }
        arr[arr.size() - 1] = -1; 
        return arr;
    }
};