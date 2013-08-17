public List<long> PrimeFactors(long number)
{
  var primeFactors = new List<long>();
  long i = 2;
  while(i <= number)
  {
    if (number % i == 0)
    {
      number /= i;
      primeFactors.Add(i);
    }
    else
    {
      i++;
    }
  }
  
  return primeFactors;
}