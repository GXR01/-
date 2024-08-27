class Solution {
    public int mySqrt(int x)
    {
        if(x==0)
            return 0;
        return (int)sqrt(x,x);
    }
  
    public static double sqrt(double i, int x)
    {
        double res = (x/i+i)/2;
        if(i==res)
            return i;
        else
          return sqrt(res,x);
    }
}