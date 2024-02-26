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
    }
}