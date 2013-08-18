public string ReverseNumber(int number)
{
  var asArray = number.ToString().ToCharArray();
  Array.Reverse(asArray);
  return new string(asArray);
}

public bool IsPalindrome(int number)
{
  return number.ToString() == ReverseNumber(number);
}