#load "../../../common/FibonacciSequence.csx"

var answer =
  FibonacciSequence()
  .TakeWhile(x => x < 4000000)
  .Where(x => x % 2 == 0)
  .Sum();

Console.WriteLine(answer);