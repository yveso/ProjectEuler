public Stack<int> ToDigits(BigInteger number)
{
    var stack = new Stack<int>();
    do
    {
        stack.Push((int)(number % 10));
        number /= 10;
    } while (number > 0);
    return stack;
}