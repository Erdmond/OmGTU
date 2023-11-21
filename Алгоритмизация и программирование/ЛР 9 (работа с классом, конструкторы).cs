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

namespace OmGTU
{
    public class Gruppa
    {
        public string FullName { get; set; }
        public int YearOfBirth { get; set; }
        public string Group { get; set; }

        public Gruppa(string fullName, int yearOfBirth, string group)
        {
            FullName = fullName;
            YearOfBirth = yearOfBirth;
            Group = group;
        }

        public void Info()
        {
            Console.WriteLine("Имя: " + FullName + ", Год рождения: " + YearOfBirth + ", Группа: " + Group);
        }

        public static void Main()
        {
            Console.WriteLine("Введите количество людей в группе:");
            int count = Convert.ToInt32(Console.ReadLine());

            // Создаем и заполняем массив из экземпляров класса Gruppa
            Gruppa[] people = new Gruppa[count];

            for (int i = 0; i < count; i++)
            {
                Console.WriteLine("Введите ФИО, год рождения и группу через пробел для человека номер " + (i + 1));
                string input = Console.ReadLine();
                string[] data = input.Split(' ');

                string fullName = string.Join(" ", data.Take(3));
                int yearOfBirth = int.Parse(data[3]);
                string group = data[4];

                people[i] = new Gruppa(fullName, yearOfBirth, group);
            }

            Console.WriteLine("Введите год по которому требуется отобрать людей:");
            int year_otbor = Convert.ToInt32(Console.ReadLine());

            // Метод выборки по году рождения
            Console.WriteLine("Люди, родившиеся в " + year_otbor + ":");
            var BornIn = people.Where(person => person.YearOfBirth == year_otbor);
            foreach (var person in BornIn)
            {
                person.Info();
            }

            Console.WriteLine("Введите группу по которой необходимо отобрать людей:");
            string gruppa_otbor = Convert.ToString(Console.ReadLine());

            // Метод выборки по группе
            Console.WriteLine("Люди из группы " + gruppa_otbor + ":");
            var InGroup = people.Where(person => person.Group == gruppa_otbor);
            foreach (var person in InGroup)
            {
                person.Info();
            }
        }
    }
}
/*
Создать массив из экземпляров класса со следующей структурой:
ФИО, год роджения, группа.

В классе должен быть реализованы:
1) Конструкторы свойства - геттеры, сеттеры
2) Метод выборки по году рождения и метод выборки по группе
*/