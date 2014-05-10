#r "System.Numerics"
#load "../../../common/ToDigits.csx"
using System.Numerics;

var x = ToDigits(new BigInteger(Math.Pow(2, 1000))).Sum();


Console.WriteLine(x);