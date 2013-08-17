#load "../common/PrimeFactors.csx"

long number = 600851475143L;

var answer = PrimeFactors(number).Max();

Console.WriteLine(answer);