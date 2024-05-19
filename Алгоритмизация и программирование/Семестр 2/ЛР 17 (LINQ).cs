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
            //int[] mass = new int[3];
            //var answer = mass.Where(n => n % 3 == 0).ToArray();
            //foreach (int i in answer) { Console.WriteLine(i); }

            //int[] mass = { 12, 35, 99, 46, 83, 100 };
            //var answer = mass.Where(n => { int suma = 0; while (n > 0) { suma += n % 10; n /= 10; } return suma % 2 == 0; }).ToArray();
            //foreach (int i in answer) { Console.WriteLine(i); }

            void Print(IEnumerable<string> s) { foreach (var o in s) { Console.WriteLine(o); } }
            List<string> mass = new List<string> { "123", "1234", "12345", "124", "4321" };
            var answer = from s in mass
                         where s.Length % 2 == 0
                         select s;
            Print(answer);
            int n = 1;
            while (n < mass.Count) { mass.Remove(mass[n]); n++; }
            Print(answer);
        }
    }
}
/*
Дан массив, состоящий из элементов int типа. Необходимо написать запрос (на LINQ), который выдаёт элементы с последней цифрой кратной 3.

Дан массив, состоящий из элементов int типа. Необходимо написать запрос (на LINQ), который выдаёт элементы с чётной суммой цифр.

Дан массив или список, состоящий из элементов типа string, необходимо составить и выполнить запрос на отбор элементов четной длины.
После выполнения запроса, необходимо удалить каждый второй элемент и выполнить запрос еще раз.
*/