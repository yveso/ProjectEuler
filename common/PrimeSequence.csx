public IEnumerable<long> PrimeSequence()
{
  yield return 2;
  long itter = 3;
  while(true)
  {
    long numberToCheck = itter;
    itter += 2;
    long sqrt = (long)Math.Sqrt(numberToCheck);
    bool divisorFound = false;
    for(long i = 3; i <= sqrt; i += 2)
    {
      if (numberToCheck % i == 0)
      {
        divisorFound = true;
        break;
      }
    }
    if (!divisorFound)
    {
      yield return numberToCheck;
    }
  }
}