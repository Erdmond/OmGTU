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
namespace OmGTU
{
    public class Menu
    {
        public static int Show_Menu()
        {
            Console.WriteLine("\t\tМеню:");
            Console.WriteLine("1 - Создать ArrayList");
            Console.WriteLine("2 - Добавить элемент");           // Add()
            Console.WriteLine("3 - Изменить элемент");           // ArrayList[x] = newLine
            Console.WriteLine("4 - Удалить элемент");            // Remove()
            Console.WriteLine("5 - Подсчитать кол-во элемента"); // Count
            Console.WriteLine("6 - Бинарный поиск элемента");    // Sort()   //BinarySearch()
            Console.WriteLine("7 - Копировать элементы");        // CopyTo()
            Console.WriteLine("8 - Поиск индекса элемента");     // IndexOf()
            Console.WriteLine("9 - Вставить элемент");           // Insert()
            Console.WriteLine("10 - Развернуть порядок");        // Reverse()
            Console.WriteLine("11 - Сортировать элементы");      // Sort()
            Console.WriteLine("12 - Вывести ArrayList");
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
            int i = 0;
            ArrayList Collection = new ArrayList();
            while (true)
            {
                switch (Menu.Show_Menu())
                {
                    case 1:
                        Collection = new ArrayList();
                        Console.Write("Введите количество элементов, которое необходимо внести в лист: ");
                        i = int.Parse(Console.ReadLine());
                        for (int j = 0; j < i; j++) { Collection.Add(Console.ReadLine()); }
                        break;
                    case 2:
                        Console.Write("Введите элемент воторый необходимо добавить: ");
                        Collection.Add(Console.ReadLine());
                        break;
                    case 3:
                        Console.Write("Введите номер элемента который необходимо заменить: ");
                        i = int.Parse(Console.ReadLine());
                        Console.WriteLine("Введите новый элемент: ");
                        Collection[i] = Console.ReadLine();
                        break;
                    case 4:
                        Console.Write("Введите индекс элемента который необохдимо удалить: ");
                        i = int.Parse(Console.ReadLine());
                        Collection.Remove(i);
                        break;
                    case 5:
                        i = Collection.Count;
                        Console.WriteLine($"Кличество элементов в листе: {i}");
                        break;
                    case 6:
                        Collection.Sort();
                        Console.Write("Введите элемент который необходимо найти: ");
                        var r = Console.ReadLine();
                        Collection.BinarySearch(r);
                        break;
                    case 7:
                        Console.Write("Введите с индекс с которого нужно скопировать элементы: ");
                        i = int.Parse(Console.ReadLine());
                        Console.Write("Введите с индекс по который нужно скопировать элементы: ");
                        int e = int.Parse(Console.ReadLine());
                        int[] CopyArray = new int[e - i];
                        Collection.CopyTo(i, CopyArray, 0, e - i);
                        break;
                    case 8:
                        Console.Write("Введите элемент индекс которого необходимо найти: ");
                        r = Console.ReadLine();
                        Console.WriteLine($"Индекс элемента {r}: {Collection.IndexOf(r)}");
                        break;
                    case 9:
                        Console.Write("Введите элемент который необходимо вставить: ");
                        r = Console.ReadLine();
                        Console.WriteLine("Введите индекс нового элемента: ");
                        i = int.Parse(Console.ReadLine());
                        Collection.Insert(i, r);
                        break;
                    case 10:
                        Collection.Reverse();
                        break;
                    case 11:
                        Collection.Sort();
                        break;
                    case 12:
                        foreach (var item in Collection) { Console.WriteLine(item); }
                        break;
                    case 13:
                        Environment.Exit(0);
                        break;
                }
            }
        }
    }
}
/*
Array:       Count, BinSearch, Copy, Find, FindLast, IndexOf, Reverse, Resize, Sort
SortedList:  Add, IndexOf и по ключу и по значению, Вывод ключа по индексу, Вывод значения по индексу
*/