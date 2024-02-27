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
    public class Menu
    {
        public static int Show_Menu()
        {
            Console.WriteLine("\t\tМеню:");
            Console.WriteLine("1 - Создать Array");
            Console.WriteLine("2 - Найти элемент больше чем");            // Find
            Console.WriteLine("3 - Изменить элемент");                    // Array[x] = newObject
            Console.WriteLine("4 - Уменьшить размер");                    // Array.Resize()
            Console.WriteLine("5 - Подсчитать кол-во элементов");         // Count()
            Console.WriteLine("6 - Бинарный поиск элемента");             // BinarySearch()
            Console.WriteLine("7 - Копировать элементы");                 // CopyTo()
            Console.WriteLine("8 - Поиск индекса элемента");              // IndexOf
            Console.WriteLine("9 - Найти последний элемент больше чем");  // FindLast()         
            Console.WriteLine("10 - Развернуть порядок");                 // Reverse()
            Console.WriteLine("11 - Сортировать элементы");               // Sort()
            Console.WriteLine("12 - Вывести Array");                      // WriteArray(Array)
            Console.WriteLine("13 - Выйти из программы");
            Console.Write("\nВведите номер действия: ");
            int result = int.Parse(Console.ReadLine());
            return result;
        }
    }
    internal class Program
    {
        public static void Main()
        {
            void WriteArray(Array a) { for (int p = 0; p < a.Length; p++) { Console.WriteLine(a.GetValue(p)); } }
            Array Collection = Array.CreateInstance(typeof(Int32), 1);
            Collection.SetValue(2, 0);
            int i = 0;
            while (true)
            {
                switch (Menu.Show_Menu())
                {
                    case 1:
                        Console.Write("Введите количество элементов, которое необходимо внести в массив: ");
                        i = int.Parse(Console.ReadLine());
                        Collection = new int[i];
                        for (int j = 0; j < i; j++) { Collection.SetValue(int.Parse(Console.ReadLine()), i); }
                        WriteArray(Collection);
                        break;
                    case 2:
                        Console.Write("Введите больше какого числа должен быть найденный элемент: ");
                        i = int.Parse(Console.ReadLine());
                        int[] Collect = new int[Collection.Length];
                        Collection.CopyTo(Collect, 0);
                        Console.WriteLine(Array.Find(Collect, x => x == i));
                        break;
                    case 3:
                        Console.Write("Введите номер элемента который необходимо заменить: ");
                        i = int.Parse(Console.ReadLine());
                        Console.WriteLine("Введите новый элемент: ");
                        Collection.SetValue(int.Parse(Console.ReadLine()), i); ;
                        WriteArray(Collection);
                        break;
                    case 4:
                        Console.Write("Введите кол-во элементов которые необходимо урезать: ");
                        i = int.Parse(Console.ReadLine());
                        int[] res = new int[Collection.Length - i];
                        Collection.CopyTo(res, 0);
                        Collection = res;
                        WriteArray(Collection);
                        break;
                    case 5:
                        Console.Write("Введите элемент кол-во которого необходимо посчитать: ");
                        i = int.Parse(Console.ReadLine());
                        Collect = new int[Collection.Length];
                        Collection.CopyTo(Collect, 0);
                        Console.WriteLine($"Количество элементов {i} в массиве: {Array.FindAll(Collect, x => x == i).Length}");
                        break;
                    case 6:
                        Array.Sort(Collection);
                        Console.Write("Введите элемент который необходимо найти: ");
                        i = int.Parse(Console.ReadLine());
                        Console.WriteLine($"Индекс элемента {i} в массиве: {Array.BinarySearch(Collection, i)}");
                        break;
                    case 7:
                        Console.Write("Введите с индекс с которого нужно скопировать элементы: ");
                        i = int.Parse(Console.ReadLine());
                        int[] CopyArray = new int[Collection.Length - i];
                        Collection.CopyTo(CopyArray, 0);
                        WriteArray(CopyArray);
                        break;
                    case 8:
                        Console.Write("Введите элемент индекс которого необходимо найти: ");
                        i = int.Parse(Console.ReadLine());
                        Console.WriteLine($"Индекс элемента {i}: {Array.IndexOf(Collection, i)}");
                        break;
                    case 9:
                        Console.Write("Введите больше какого числа должен быть найденный элемент: ");
                        i = int.Parse(Console.ReadLine());
                        Collect = new int[Collection.Length];
                        Collection.CopyTo(Collect, 0);
                        Console.WriteLine(Array.FindLast(Collect, x => x > i));
                        break;
                    case 10:
                        Array.Reverse(Collection);
                        WriteArray(Collection);
                        break;
                    case 11:
                        Array.Sort(Collection);
                        WriteArray(Collection);
                        break;
                    case 12:
                        WriteArray(Collection);
                        break;
                    case 13:
                        Environment.Exit(0);
                        break;
                }
            }
        }
    }
}