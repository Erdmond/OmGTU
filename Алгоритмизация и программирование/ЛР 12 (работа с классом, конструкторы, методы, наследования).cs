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
using System.Xml.Linq;
using System.Xml.Schema;
using System.IO;
using System.Security.Cryptography;
using OmGTU;

namespace OmGTU
{
    public class Animals
    {
        public string Name { get; set; }
        public int Year_Of_Birth { get; set; }
        public Animals(string n, int y) { Name = n; Year_Of_Birth = y; }
    }
    class Dog : Animals
    {
        public string Breed { get; set; }
        public string Color { get; set; }
        public Dog(string n, int y, string b, string c) : base(n, y) { Breed = b; Color = c; }
        public void Info() { Console.WriteLine($"Имя: " + Name + "\n  Год рождения: " + Year_Of_Birth + "\n  Порода: " + Breed + "\n  Окрас: " + Color); }
        public void Selection(Dog i, string c) { if (i.Breed == c) { i.Info(); } }
    }
    class Cat : Animals
    {
        public string Breed { get; set; }
        public string Color { get; set; }
        public Cat(string n, int y, string b, string c) : base(n, y) { Breed = b; Color = c; }
        public void Info() { Console.WriteLine($"Имя: " + Name + "\n  Год рождения: " + Year_Of_Birth + "\n  Порода: " + Breed + "\n  Окрас: " + Color); }
        public void Selection(Cat i, string c) { if (i.Color == c) { i.Info(); } }
        public void Swap(Cat i, string a) { i.Breed = a; }
    }
    internal class First
    {
        public static void Main()
        {
            Dog[] Dogs = new Dog[Convert.ToInt32(Console.ReadLine())];
            for (int i = 0; i < Dogs.Length; i++) { string n = Console.ReadLine(); int y = int.Parse(Console.ReadLine()); string b = Console.ReadLine(); string c = Console.ReadLine(); Dogs[i] = new Dog(n, y, b, c); }
            Cat[] Cats = new Cat[Convert.ToInt32(Console.ReadLine())];
            for (int i = 0; i < Cats.Length; i++) { string n = Console.ReadLine(); int y = int.Parse(Console.ReadLine()); string b = Console.ReadLine(); string c = Console.ReadLine(); Cats[i] = new Cat(n, y, b, c); }
            string Selection_Breed_Dogs = Console.ReadLine();
            string Selection_Color_Cats = Console.ReadLine();
            string Swap_Breed_Before = Console.ReadLine();
            string Swap_Breed_After = Console.ReadLine();
            foreach (Cat c in Cats) { c.Selection(c, Selection_Color_Cats); }
            foreach (Dog d in Dogs) { d.Selection(d, Selection_Breed_Dogs); }
            foreach (Cat c in Cats) { if (c.Breed == Swap_Breed_Before) { c.Swap(c, Swap_Breed_After); } }
        }
    }
}
/* 
класс Животные(Имя, Год рождения), наследники Собаки(Порода, Окрас), Кошечки(Порода, Окрас)
предусмотреть: заполнение массивом на наследников, выборка собак по породе, выборка кошечек по окрасу, смена породы у кошечек
*/

/* 

# Тестовый ввод:
3
Бобик
2022
Ротвеллер
Чёрный
Наташа
2009
Хаски
Серый
Рекс
2010
Бульдог
Рыжий
3
Тина
2016
Манчкин
Рыжий
Егор
2005
Сфинкс
Розовый
Санбой
2024
Русская Голубая
Серый
Хаски
Розовый
Русская Голубая
Вислоухая
*/