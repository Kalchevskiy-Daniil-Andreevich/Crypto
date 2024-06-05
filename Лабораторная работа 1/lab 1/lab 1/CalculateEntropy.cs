using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_1
{
	internal class CalculateEntropy
	{
		// Кол-во появлений символов в строке
		public static Dictionary<char, int> GetSymbolAppearances(string str)
		{
			var symblAppear = new Dictionary<char, int>();
			foreach (char c in str)
			{
				if (!symblAppear.ContainsKey(c))
					symblAppear.Add(c, 1);
				else
					symblAppear[c] += 1;
			}
			return symblAppear;
		}


		// Энтропия Шеннона
		public static double GetShannonEntropy(string str)
		{
			var symblAppear = GetSymbolAppearances(str);
			var entropyCulc = 0d;
			foreach (var item in symblAppear)
			{
				var P = (double)item.Value / str.Length;
				entropyCulc -= P * Math.Log2(P);
			}
			return Math.Round(entropyCulc, 3);
		}


		// Количество информации
		public static double GetInformationAmount(string ABC, string str)
		{
			if (IsBinaryAlphabet(ABC))
				return str.Length;
			var informAmount = GetShannonEntropy(ABC) * str.Length;
			return Math.Round(informAmount, 3);
		}


		// Эффективная энтропия
		public static double GetEffectiveEntropy(string ABC, double p)
		{
			var q = 1 - p;
			if (IsBinaryAlphabet(ABC) && (p == 0 || q == 0))
				return 1;
			if (!IsBinaryAlphabet(ABC) && p == 1)
				return 0;
			return 1 - (-p * Math.Log2(p) - q * Math.Log2(q));
		}


		// Количество информации при наличии вероятности ошибки
		public static double GetInformationAmount(string ABC, string str, double p)
		{
			var informAmount = GetShannonEntropy(ABC) * str.Length * GetEffectiveEntropy(ABC, p);
			return Math.Round(informAmount, 3);
		}


		// Проверить, является ли алфавит бинарным
		private static bool IsBinaryAlphabet(string ABC) => GetSymbolAppearances(ABC).Count == 2;


		// Вспомогательный метод для чтения текста из файла
		public static string ReadFromFile(string fileName)
		{
			var pathToFolder = "../../../ABC/";
			var filePath = Path.Combine(pathToFolder, fileName);
			var text = "";
			using (var sr = new StreamReader(filePath))
				text = sr.ReadToEnd().ToLower();
			return text;
		}
	}
}
