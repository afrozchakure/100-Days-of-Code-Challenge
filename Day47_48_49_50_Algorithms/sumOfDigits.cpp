int sumOfDigits(int n)
{
    int sum = 0;
    if(n == 0)
        return 0;
    while(n > 0)
    {
        sum += n%10;
        n = n / 10;
    }
    return sum;
    //Your code here
}
