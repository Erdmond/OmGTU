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
            string[] lines = File.ReadAllLines("input.txt");
            int min_cnt_a = lines[0].Length;
            string line = lines[0];
            foreach (string l in lines)
            {
                int cnt_a = 0;
                foreach (char c in l)
                {
                    if (c == 'a') { cnt_a++; }
                    else { if (cnt_a < min_cnt_a) { line = l; min_cnt_a = cnt_a; } }
                }
            }
            Console.WriteLine(line);
        }
    }
}
/*
дан входной файл состоящий из строк необходимо вывести строку с наименьшей длиной подпоследовательности состоящей из символов а
*/