using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.Linq;
using System.Net.Configuration;
using System.Runtime.InteropServices;
using System.Runtime.Remoting.Metadata.W3cXsd2001;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Threading;
using System.Xml.Linq;
using System.Xml.Schema;
using System.IO;
using System.Security.Cryptography;
using OmGTU;
using System.Diagnostics;
using System.Collections;
using System.Collections.ObjectModel;
namespace OmGTU
{
    internal class Program
    {
        public static void Main()
        {
            SortedDictionary<char, int> symbols = new SortedDictionary<char, int>();
            StreamReader file = new StreamReader("file_name.txt");
            string line = file.ReadLine();
            while (line != null)
            {
                foreach (char i in line)
                {
                    if (!symbols.ContainsKey(i)) { symbols[i] = 1; }
                    else { symbols[i]++; }
                }
                line = file.ReadLine();
            }
            Console.WriteLine("Самый(е) частвый символ:");
            foreach (char i in symbols.Keys) { if (symbols[i] == symbols.Values.Max()) { Console.WriteLine(i); } }
            Console.WriteLine($"Количество уникальных символов: {symbols.Count}");
            Console.WriteLine("Отсортированный список всех символов:");
            foreach (char i in symbols.Keys) { Console.WriteLine(i); }
        }
    }
}
/*
Дан входной файл из символов (латинские буквы) необходимо:
опредилить символ, который встречается чаще всего
кол-во уникальных символов
выдать список символов, с помощью которых составлена последовательность в файле (в алф порядке)
Ограничения: данные считывать в массивы, списки и др. элементы коллекций (нельзя для хранения исходных данных, для обработки можно)
Строк может быть несколько, в строку считывать можно
*/