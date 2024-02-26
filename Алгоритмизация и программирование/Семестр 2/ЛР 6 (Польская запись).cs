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
using System.Net;
using System.Diagnostics.Eventing.Reader;

namespace OmGTU
{
    internal class Program
    {
        public static void Main()
        {
            string[] input = Convert.ToString(Console.ReadLine()).Split();
            Stack stack = new Stack();
            foreach (string c in input)
            {
                if (int.TryParse(c, out _))
                {
                    stack.Push(c);
                }
                else if (c == "/" && stack.Count >= 2)
                {
                    double operand2 = Convert.ToDouble(stack.Pop());
                    double operand1 = Convert.ToDouble(stack.Pop());
                    if (operand2 == 0) { Console.WriteLine("Деление на ноль!"); return; }
                    stack.Push(operand1 / operand2);
                }
                else if (c == "*" && stack.Count >= 2)
                {
                    double operand2 = Convert.ToDouble(stack.Pop());
                    double operand1 = Convert.ToDouble(stack.Pop());
                    stack.Push(operand1 * operand2);
                }
                else if (c == "+" && stack.Count >= 2)
                {
                    double operand2 = Convert.ToDouble(stack.Pop());
                    double operand1 = Convert.ToDouble(stack.Pop());
                    stack.Push(operand1 + operand2);
                }
                else if (c == "-" && stack.Count >= 2)
                {
                    double operand2 = Convert.ToDouble(stack.Pop());
                    double operand1 = Convert.ToDouble(stack.Pop());
                    stack.Push(operand1 - operand2);
                }
                else { Console.WriteLine("Неверная запись!"); return; }
            }
            if (stack.Count == 1) { Console.WriteLine(stack.Pop()); }
            else { Console.WriteLine("Неверная запись!"); }
        }
    }
}