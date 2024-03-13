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
            // Оглашение словаря данных
            Dictionary<string, List<string[]>> Calls_for_date = new Dictionary<string, List<string[]>>();

            // Функция вывода меню с выбором
            int Menu()
            {
                Console.Write("  Меню:\n1) Добавить данные\n2) Поиск самого востребованного номера\n3) Поиск самого длинного суммарного разговора\n4) Выход из программы\n  ");
                return int.Parse(Console.ReadLine());
            }

            // Функция внесения данных
            void AddToData()
            {
                Console.WriteLine("Вводите данные, чтобы прекратить ввод введите 'x':");
                while (true)
                {
                    string[] s = Console.ReadLine().Split();
                    if (s[0] == "x") { break; }
                    if (!Calls_for_date.ContainsKey(s[2])) { Calls_for_date[s[2]] = new List<string[]>(); }
                    Calls_for_date[s[2]].Add(new string[3] { s[0], s[1], s[3] });
                }
            }

            // Функция поиска самого вызываемого номера за дату
            void More_Call(string num)
            {
                foreach (string i in Calls_for_date.Keys)
                {
                    Console.WriteLine($"Наиболее вызываемые номера за {i} для номера {num}:");
                    List<string> most_num = new List<string>();
                    Dictionary<string, int> num_k = new Dictionary<string, int>();
                    foreach (string[] j in Calls_for_date[i])
                    {
                        if (j[0] == num)
                        {
                            if (!num_k.ContainsKey(j[1]))
                            {
                                num_k[j[1]] = 1;
                            }
                            else
                            {
                                num_k[j[1]]++;
                            }
                        }
                    }
                    int max_k = num_k.Max(x => x.Value);
                    foreach (string j in num_k.Keys)
                    {
                        if (num_k[j] == max_k) { Console.WriteLine(j); }
                    }
                }
            }

            // Функция поиска наиболее продолжительного суммарного разговора
            void More_Time(string num)
            {
                foreach (string i in Calls_for_date.Keys)
                {
                    Console.WriteLine($"Наиболее долгие разговоры за {i} для номера {num}:");
                    List<string> most_num = new List<string>();
                    Dictionary<string, int> num_k = new Dictionary<string, int>();
                    foreach (string[] j in Calls_for_date[i])
                    {
                        if (j[0] == num)
                        {
                            if (!num_k.ContainsKey(j[1]))
                            {
                                num_k[j[1]] = int.Parse(j[2]);
                            }
                            else
                            {
                                num_k[j[1]] += int.Parse(j[2]);
                            }
                        }
                    }
                    int max_k = num_k.Max(x => x.Value);
                    foreach (string j in num_k.Keys)
                    {
                        if (num_k[j] == max_k) { Console.WriteLine($"{j} {max_k}"); }
                    }
                }
            }

            // Программа
            while (true)
            {
                switch (Menu())
                {
                    case 1:
                        AddToData();
                        break;
                    case 2:
                        Console.Write("Напишите номер, для которго необходимо проводить отбор: ");
                        More_Call(Convert.ToString(Console.ReadLine()));
                        break;
                    case 3:
                        Console.Write("Напишите номер, для которго необходимо проводить отбор: ");
                        More_Time(Convert.ToString(Console.ReadLine()));
                        break;
                    case 4:
                        Environment.Exit(0);
                        break;
                }
            }
        }
    }
}
/*
100 200 21.12 10
100 200 21.12 5
500 100 21.12 15
100 500 22.12 3
500 300 22.12 10
100 200 22.12 3
100 600 23.12 10
100 200 23.12 30
*/