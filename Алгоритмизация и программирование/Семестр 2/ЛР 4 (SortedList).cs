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
            Console.WriteLine("1 - Создать SortedList");
            Console.WriteLine("2 - Добавить элемент");           // Add()
            Console.WriteLine("3 - Изменить элемент");           // SortedList[x] = newLine
            Console.WriteLine("4 - Удалить элемент");            // Remove()
            Console.WriteLine("5 - Найти индекс по ключу");      // IndexOfKey()
            Console.WriteLine("6 - Найти индекс по значению");   // IndexOfValue()
            Console.WriteLine("7 - Найти значение по индексу");  // GetByIndex()
            Console.WriteLine("8 - Найти ключ по значению");     // GetKey()
            Console.WriteLine("9 - Вывести SortedList");
            Console.WriteLine("10 - Выйти из программы");
            Console.Write("\nВведите номер действия: ");
            int result = int.Parse(Console.ReadLine());
            return result;
        }
    }
    internal class Program
    {
        public static void Main()
        {
            void WriteCollection(SortedList t) { foreach (DictionaryEntry o in t) { Console.WriteLine(o.Key + ": " + o.Value); } }
            int i = 0;
            SortedList Collection = new SortedList();
            while (true)
            {
                switch (Menu.Show_Menu())
                {
                    case 1:
                        Collection = new SortedList();
                        Console.Write("Введите количество элементов, которое необходимо внести в лист: ");
                        i = int.Parse(Console.ReadLine());
                        Console.Write("Введите ключ, после введите значение: ");
                        for (int j = 0; j < i; j++) { Collection.Add(Console.Read(), Console.ReadLine()); }
                        WriteCollection(Collection);
                        break;
                    case 2:
                        Console.Write("Введите ключ и значение элемента который необходимо добавить: ");
                        Collection.Add(Console.Read(), Console.ReadLine());
                        WriteCollection(Collection);
                        break;
                    case 3:
                        Console.Write("Введите ключ элемента значение которого необходимо заменить: ");
                        i = int.Parse(Console.ReadLine());
                        Console.Write("Введите новый элемент: ");
                        Collection[i] = Console.ReadLine();
                        WriteCollection(Collection);
                        break;
                    case 4:
                        Console.Write("Введите индекс элемента который необохдимо удалить: ");
                        i = int.Parse(Console.ReadLine());
                        Collection.Remove(i);
                        WriteCollection(Collection);
                        break;
                    case 5:
                        Console.Write("Введите ключ для которого необходимо найти индекс: ");
                        Console.WriteLine(Collection.IndexOfKey(Console.ReadLine()));
                        break;
                    case 6:
                        Console.Write("Введите значение для которого необходимо найти индекс: ");
                        Console.WriteLine(Collection.IndexOfValue(Console.ReadLine()));
                        break;
                    case 7:
                        Console.Write("Введите индекс для которого необходимо найти значение: ");
                        i = int.Parse(Console.ReadLine());
                        Console.WriteLine(Collection.GetByIndex(i));
                        break;
                    case 8:
                        Console.Write("Введите значение для которого нужно найти ключ: ");
                        Console.WriteLine(Collection.GetKey(Collection.IndexOfValue(Console.ReadLine())));
                        break;
                    case 9:
                        WriteCollection(Collection);
                        break;
                    case 10:
                        Environment.Exit(0);
                        break;
                }
            }
        }
    }
}