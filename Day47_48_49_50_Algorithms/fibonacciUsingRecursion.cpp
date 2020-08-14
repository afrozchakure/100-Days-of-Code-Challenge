//Complete this function
long long fibonacci(int n)
{
    //Your code here
    if(n == 1 || n == 2)
        return 1;
    else{
        return fibonacci(n-1) + fibonacci(n-2);
    }
}
