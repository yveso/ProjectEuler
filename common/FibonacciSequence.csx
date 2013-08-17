public IEnumerable<int> FibonacciSequence()
{
  int x = 1, y = 2, temp;
  
  yield return x;
  
  while(true)
  {
    temp = x;
    x = y;
    y += temp;
    
    yield return x;
  }
}