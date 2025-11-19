using System;
using System.Collections.Generic;
using System.Collections;
namespace OmGTU
{
    internal class Program
    {
        public static void Main()
        {
            void Polish()
            {
                Console.WriteLine("Задайте выражение в формате польской записи:");
                string[] input = Convert.ToString(Console.ReadLine()).Split();
                Stack stack = new Stack();
                foreach (string c in input)
                {
                    if (int.TryParse(c, out _))
                    {
                        stack.Push(c);
                    }
                    else if (c == "/")
                    {
                        while (stack.Count > 1)
                        {
                            double operand2 = Convert.ToDouble(stack.Pop());
                            double operand1 = Convert.ToDouble(stack.Pop());
                            if (operand2 == 0) { Console.WriteLine("Деление на ноль!"); return; }
                            stack.Push(operand1 / operand2);
                        }
                    }
                    else if (c == "*")
                    {
                        while (stack.Count > 1)
                        {
                            double operand2 = Convert.ToDouble(stack.Pop());
                            double operand1 = Convert.ToDouble(stack.Pop());
                            stack.Push(operand1 * operand2);
                        }
                    }
                    else if (c == "+")
                    {
                        while (stack.Count > 1)
                        {
                            double operand2 = Convert.ToDouble(stack.Pop());
                            double operand1 = Convert.ToDouble(stack.Pop());
                            stack.Push(operand1 + operand2);
                        }
                    }
                    else if (c == "-")
                    {
                        while (stack.Count > 1)
                        {
                            if (stack.Count == 2)
                            {
                                double operand2 = Convert.ToDouble(stack.Pop());
                                double operand1 = Convert.ToDouble(stack.Pop());
                                stack.Push(operand1 - operand2);
                            }
                            else
                            {
                                double operand2 = Convert.ToDouble(stack.Pop());
                                double operand1 = Convert.ToDouble(stack.Pop());
                                stack.Push(operand1 + operand2);
                            }
                        }
                    }
                    else { Console.WriteLine("Неверная запись!"); return; }
                }
                if (stack.Count == 1) { Console.WriteLine($"Ответ: {stack.Pop()}"); }
                else { Console.WriteLine("Неверная запись!"); }
            }

            void Brackets()
            {
                Console.WriteLine("Введите выражение, содержащее скобки:");
                string input = Convert.ToString(Console.ReadLine());
                Stack<char> stack = new Stack<char>();
                foreach (char c in input)
                {
                    if (c == '(' || c == '[' || c == '{') { stack.Push(c); }
                    else if (c == ')' && (stack.Count == 0 || stack.Pop() != '(')) { Console.WriteLine("Неверное расположении скобок!"); return; }
                    else if (c == ']' && (stack.Count == 0 || stack.Pop() != '[')) { Console.WriteLine("Неверное расположении скобок!"); return; }
                    else if (c == '}' && (stack.Count == 0 || stack.Pop() != '{')) { Console.WriteLine("Неверное расположение скобок!"); return; }
                }
                if (stack.Count == 0) { Console.WriteLine("Ошибок нет."); }
                else { Console.WriteLine("Неверное расположение скобок!"); return; }
            }

            int Menu()
            {
                Console.WriteLine("  Меню:");
                Console.WriteLine("1) Информация об авторе");
                Console.WriteLine("2) Запуск алгоритма решения польской записи");
                Console.WriteLine("3) Запуск алгоритма проверки корректности скобок");
                Console.WriteLine("4) Выход");
                Console.Write("  Введите номер действия: ");
                return int.Parse(Console.ReadLine());
            }

            while (true)
            {
                switch (Menu())
                {
                    case 1:
                        Console.WriteLine("Выполнил студент 1 курса группы ФИТ-232 Изгородин Илья");
                        break;
                    case 2:
                        Polish();
                        break;
                    case 3:
                        Brackets();
                        break;
                    case 4:
                        Environment.Exit(1);
                        break;
                    default:
                        Console.WriteLine("Неверный ввод");
                        Menu();
                        break;
                }
            }
        }
    }
}