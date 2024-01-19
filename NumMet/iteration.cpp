#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;
double func(double x)
{
    return x * x * x + 3 * x - 1;
}
void num_method(double x, double y)
{
    int count = 0;
    double temp1 = x, temp2 = y, temp3 = 0;
    int signx = ((func(x) > 0) ? 1 : -1), signy = ((func(y) > 0) ? 1 : -1);
    while (count != 8)
    {
        temp3 = (temp1 + temp2) / 2.0;
        if (func(temp3) > 0)
        {
            if (signx == -1)
                temp2 = temp3;
            else
                temp1 = temp3;
        }
        else
        {
            if (signx == -1)
                temp1 = temp3;
            else
                temp2 = temp3;
        }
        count++;
    }
    printf("x = %.8f\nF(x) = %.8f", temp3, func(temp3));
}
int main()
{
    double x, y;
    cin >> x >> y;
    num_method(x, y);
}