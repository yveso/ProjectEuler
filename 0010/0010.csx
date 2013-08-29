#load "../common/PrimeSequence.csx"

var answer = PrimeSequence().TakeWhile(x => x < 2000000).Sum();

Console.WriteLine(answer);