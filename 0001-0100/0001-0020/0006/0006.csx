

public int SumOfSquares(int number)
{
  return
    Enumerable.Range(1, number)
    .Select(x => x * x)
    .Sum();
}

public int SquaredSum(int number)
{
  int sum = number * (number + 1) / 2;
  return sum * sum;
}

var answer = SquaredSum(100) - SumOfSquares(100);

Console.WriteLine(answer);