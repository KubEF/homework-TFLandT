public static (int, int) DiagNumberAndStart(int k)
{
    var n = 1; 
    var count = 1;
    while (count < k)
    {
        n++;
        count += n;
    }
    return (n, count - n + 1);
}
static int J(int k)
{
    var (diagNum, diagStart) = DiagNumberAndStart(k);
    return k - diagStart + 1;
}
static int I(int k)
{
    var (diagNum, diagStart) = DiagNumberAndStart(k);
    return diagNum + 1 - (k - diagStart + 1);
}