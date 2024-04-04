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
    class Calculator<T>
    {
        private T variable1;
        private T variable2;
        public Calculator(T var1, T var2)
        {
            variable1 = var1;
            variable2 = var2;
        }
        public void Sum()
        {
            dynamic result = (dynamic)variable1 + (dynamic)variable2;
            Console.WriteLine("Сумма: " + result);
        }
        public void Subtract()
        {
            dynamic result = (dynamic)variable1 - (dynamic)variable2;
            Console.WriteLine("Разность: " + result);
        }
        public void Multiply()
        {
            dynamic result = (dynamic)variable1 * (dynamic)variable2;
            Console.WriteLine("Произведение: " + result);
        }
        public void Divide()
        {
            if (Convert.ToDouble(variable2) == 0)
            {
                Console.WriteLine("Деление на ноль невозможно");
            }
            else
            {
                dynamic result = (dynamic)variable1 / (dynamic)variable2;
                Console.WriteLine("Результат деления: " + result);
            }
        }
    }
    internal class Program
    {
        public static void Main()
        {
            void Menu()
            {
                Console.Write("  Меню:\n1) Работа с целыми;\n2) Работа с вещественными;\n3) Выход.\n  Введите действие: ");
                switch (int.Parse(Console.ReadLine()))
                {
                    case 1:
                        Console.WriteLine("Введите два целых числа:");
                        int numi1 = Convert.ToInt32(Console.ReadLine());
                        int numi2 = Convert.ToInt32(Console.ReadLine());
                        Calculator<int> intCalculator = new Calculator<int>(numi1, numi2);
                        Console.Write("  Операции:\n1) Сумма;\n2) Разность;\n3) Произведение;\n4) Деление;\n  Введите действие: ");
                        switch (int.Parse(Console.ReadLine()))
                        {
                            case 1:
                                intCalculator.Sum();
                                break;
                            case 2:
                                intCalculator.Subtract();
                                break;
                            case 3:
                                intCalculator.Multiply();
                                break;
                            case 4:
                                intCalculator.Divide();
                                break;
                        }
                        break;
                    case 2:
                        Console.WriteLine("Введите два вещественных числа:");
                        double numd1 = Convert.ToDouble(Console.ReadLine());
                        double numd2 = Convert.ToDouble(Console.ReadLine());
                        Calculator<double> doubleCalculator = new Calculator<double>(numd1, numd2);
                        Console.Write("  Операции:\n1) Сумма;\n2) Разность;\n3) Произведение;\n4) Деление;\n  Введите действие: ");
                        switch (int.Parse(Console.ReadLine()))
                        {
                            case 1:
                                doubleCalculator.Sum();
                                break;
                            case 2:
                                doubleCalculator.Subtract();
                                break;
                            case 3:
                                doubleCalculator.Multiply();
                                break;
                            case 4:
                                doubleCalculator.Divide();
                                break;
                        }
                        break;
                    case 3:
                        Environment.Exit(0);
                        break;
                }
            }
            while (true)
            {
                Menu();
            }
        }
    }
}
/*
Необходимо реализовать функции сложения, вычитания, умножения и деления с использованием типов данных целого и вещественного
С использованием обощения - какой тип данных передан, такой и обрабатывается
Вывод результата внутри функции
Это все поместить в класс, который будет иметь две переменные, принимающие нужный тип данных
В main - небольшое меню, включающее 2 пункта: 1) работа с целыми, 2) работа с вещественными
Реализовать все 4 операции
*/