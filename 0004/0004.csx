#load "../common/IsPalindrome.csx"

int answer = 0;

for (int x = 100; x <= 999; x++)
{
  for (int y = 100; y <= 999; y++)
  {
    int product = x * y;
    if(IsPalindrome(product) && product > answer)
    {
      answer = product;
    }
  }
}

Console.WriteLine(answer);