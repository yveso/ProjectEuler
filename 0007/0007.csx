#load "../common/PrimeSequence.csx"

var answer = PrimeSequence().Take(10001).Max();

Console.WriteLine(answer);