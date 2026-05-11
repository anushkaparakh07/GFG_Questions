#include <cmath>
class Solution {
  public:
    double switchCase(int choice, vector<double> &arr) {
        // code here
        switch(choice){
            case 1:{double r = arr[0];
                    double areaC = M_PI * r * r;
                    return areaC;}
            case 2: {double l = arr[0],b = arr[1];
                    double areaR = l*b;
                    return areaR;}
        }
        return 0;
    }
};
