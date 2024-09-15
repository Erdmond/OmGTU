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
    interface InterMath
    {
        double Sum(double a, double b);
        double Raz(double a, double b);
        double Umn(double a, double b);
        double Del(double a, double b);
        double Kor(double a);
        double Sin(double a);
        double Cos(double a);
    }
    class MathOperations : InterMath
    {
        public double Sum(double a, double b) { return a + b; }
        public double Raz(double a, double b) { return a - b; }
        public double Umn(double a, double b) { return a * b; }
        public double Del(double a, double b) { if (b != 0) return a / b; else throw new DivideByZeroException("Деление на 0 невозможно!"); }
        public double Kor(double a) { if (a >= 0) return Math.Sqrt(a); else throw new Exception("Нет реального корня из отрицательного числа!"); }
        public double Sin(double a) { return Math.Sin(a); }
        public double Cos(double a) { return Math.Cos(a); }
    }
    internal class Program
    {
        public static void Main()
        {
            void Menu() { Console.Write("  Выберите математическую операцию:\n1) Сложение\n2) Вычитание\n3) Умножение\n4) Деление\n5) Извлечение корня\n6) Sin\n7) Cos\n  "); }
            InterMath math = new MathOperations();
            Func<double, double, double> SumDelegate = math.Sum;
            Func<double, double, double> RazDelegate = math.Raz;
            Func<double, double, double> UmnDelegate = math.Umn;
            Func<double, double, double> DelDelegate = math.Del;
            Func<double, double> KorDelegate = math.Kor;
            Func<double, double> SinDelegate = math.Sin;
            Func<double, double> CosDelegate = math.Cos;
            Menu();
            string[] a;
            switch (Convert.ToInt32(Console.ReadLine()))
            {
                case 1:
                    Console.Write("Введите числa: ");
                    a = Console.ReadLine().Split();
                    Console.WriteLine($"Результат операции: {SumDelegate(Convert.ToDouble(a[0]), Convert.ToDouble(a[1]))}");
                    break;
                case 2:
                    Console.Write("Введите числa: ");
                    a = Console.ReadLine().Split();
                    Console.WriteLine($"Результат операции: {RazDelegate(Convert.ToDouble(a[0]), Convert.ToDouble(a[1]))}");
                    break;
                case 3:
                    Console.Write("Введите числa: ");
                    a = Console.ReadLine().Split();
                    Console.WriteLine($"Результат операции: {UmnDelegate(Convert.ToDouble(a[0]), Convert.ToDouble(a[1]))}");
                    break;
                case 4:
                    Console.Write("Введите числa: ");
                    a = Console.ReadLine().Split();
                    Console.WriteLine($"Результат операции: {DelDelegate(Convert.ToDouble(a[0]), Convert.ToDouble(a[1]))}");
                    break;
                case 5:
                    Console.Write("Введите число: ");
                    a = Console.ReadLine().Split();
                    Console.WriteLine($"Результат операции: {KorDelegate(Convert.ToDouble(a[0]))}");
                    break;
                case 6:
                    Console.Write("Введите число: ");
                    a = Console.ReadLine().Split();
                    Console.WriteLine($"Результат операции: {SinDelegate(Convert.ToDouble(a[0]))}");
                    break;
                case 7:
                    Console.Write("Введите число: ");
                    a = Console.ReadLine().Split();
                    Console.WriteLine($"Результат операции: {CosDelegate(Convert.ToDouble(a[0]))}");
                    break;
                default:
                    Console.WriteLine("Неверный выбор операции.");
                    return;
            }
        }
    }
}
/*
Необходимо написать программу в которой будет список делегатов для мат. операций сложения,
вычитания, умножения, деления, извлечения корня, нахождения sin, cos.
Пользователь выбирает тип математической операции и в зависимости от операции вводит или одно или два числа.
Результат выводится. Необходимо создать интерфейс, который будет содержать методы для всех делегатов.
*/