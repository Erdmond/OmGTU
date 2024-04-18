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
    struct Person
    {
        public int Year;
        public string City;
        public string Country;
    }
    internal class Program
    {
        public static void Main()
        {
            List<Person> people = new List<Person>();
            string[] lines = File.ReadAllLines("data.txt");
            foreach (string line in lines)
            {
                string[] parts = line.Split(',');
                Person person = new Person
                {
                    Year = int.Parse(parts[0]),
                    City = parts[1],
                    Country = parts[2]
                };
                people.Add(person);
            }

            var groupByYear = people.GroupBy(p => p.Year);
            List<string> File_1 = new List<string>();
            foreach (var group in groupByYear)
            {
                foreach (Person person in group)
                {
                    File_1.Add(person.Year.ToString() + person.City + person.Country);
                }
            }
            File.WriteAllLines(@"D:\File_1.txt", File_1);

            var groupByCity = people.GroupBy(p => p.City);
            List<string> File_2 = new List<string>();
            foreach (var group in groupByCity)
            {
                foreach (Person person in group)
                {
                    File_2.Add(person.Year.ToString() + person.City + person.Country);
                }
            }
            File.WriteAllLines(@"D:\File_2.txt", File_2);

            var groupByCountry = people.GroupBy(p => p.Country);
            List<string> File_3 = new List<string>();
            foreach (var group in groupByCountry)
            {
                foreach (Person person in group)
                {
                    File_3.Add(person.Year.ToString() + person.City + person.Country);
                }
            }
            File.WriteAllLines(@"D:\File_3.txt", File_3);

            Console.WriteLine("Введите страну для вывода данных:");
            string country = Console.ReadLine();
            foreach (var group in groupByCountry)
            {
                foreach (Person person in group)
                {
                    if (person.Country == country)
                    {
                        Console.WriteLine(person.Year.ToString() + person.City + person.Country);
                    }
                }
            }
        }
    }
}
/*
Задачка по алгоритмизации на структуры и файлы. 
В файле хранятся данные следующей структуры:
-год рождения
-город рождения
-страна рождения
Задание: необходимо создать 3 выходных файла. 
*1 файл: данные сгруппированы по году рождения (без разницы, по возрастанию или убыванию), 
*2 файл: сгруппировать по городам
*3 файл: вывести данные тех, кто родился в определенной стране. Страна запрашивается пользователем.
*/