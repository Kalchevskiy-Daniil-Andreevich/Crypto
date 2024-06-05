using lab_1;
using System.Security.Claims;

var franceLanguage = CalculateEntropy.ReadFromFile("franceLanguage.txt");
var bulgarianLanguage = CalculateEntropy.ReadFromFile("bulgarianLanguage.txt");
var binary = CalculateEntropy.ReadFromFile("binary.txt");
var myFIO = CalculateEntropy.ReadFromFile("myFIO.txt");
var myFIOInASCII = CalculateEntropy.ReadFromFile("myFIOInASCII.txt");

Console.WriteLine("\n==========================================");
Console.WriteLine($"Entropy of Language (france):      {CalculateEntropy.GetShannonEntropy(franceLanguage)}");
Console.WriteLine($"Entropy of Language (bulgarian):  {CalculateEntropy.GetShannonEntropy(bulgarianLanguage)}");
Console.WriteLine($"Entropy of Language (binary):      {CalculateEntropy.GetShannonEntropy(binary)}");

Console.WriteLine("\n================  P = 0  =================");
Console.WriteLine($"Information Amount (france):       {CalculateEntropy.GetInformationAmount(franceLanguage, myFIO)}");
Console.WriteLine($"Information Amount (bulgarian):   {CalculateEntropy.GetInformationAmount(bulgarianLanguage, myFIO)}");
Console.WriteLine($"Information Amount (ASCII):        {CalculateEntropy.GetInformationAmount(myFIOInASCII, myFIOInASCII)}");

Console.WriteLine("\n===============  P = 0.1  ================");
Console.WriteLine($"Information Amount (france):       {CalculateEntropy.GetInformationAmount(franceLanguage, myFIO, 0.1)}");
Console.WriteLine($"Information Amount (bulgarian):   {CalculateEntropy.GetInformationAmount(bulgarianLanguage, myFIO, 0.1)}");
Console.WriteLine($"Information Amount (ASCII):        {CalculateEntropy.GetInformationAmount(myFIOInASCII, myFIOInASCII, 0.1)}");

Console.WriteLine("\n===============  P = 0.5  ================");
Console.WriteLine($"Information Amount (france):       {CalculateEntropy.GetInformationAmount(franceLanguage, myFIO, 0.49)}");
Console.WriteLine($"Information Amount (bulgarian):   {CalculateEntropy.GetInformationAmount(bulgarianLanguage, myFIO, 0.49)}");
Console.WriteLine($"Information Amount (ASCII):        {CalculateEntropy.GetInformationAmount(myFIOInASCII, myFIOInASCII, 0.5)}");

Console.WriteLine("\n================  P = 1  =================");
Console.WriteLine($"Information Amount (france):       {CalculateEntropy.GetInformationAmount(franceLanguage, myFIO, 1)}");
Console.WriteLine($"Information Amount (bulgarian):   {CalculateEntropy.GetInformationAmount(bulgarianLanguage, myFIO, 1)}");
Console.WriteLine($"Information Amount (ASCII):        {CalculateEntropy.GetInformationAmount(myFIOInASCII, myFIOInASCII, 1)}");


foreach (var item in CalculateEntropy.GetSymbolAppearances(bulgarianLanguage))
{
	Console.WriteLine($"{item.Key}-{item.Value}");
}