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
            StreamReader reader1 = new StreamReader("file1.txt");
            StreamReader reader2 = new StreamReader("file2.txt");
            StreamWriter writer = new StreamWriter("merged_file.txt");
            string line1 = reader1.ReadLine();
            string line2 = reader2.ReadLine();
            while (line1 != null || line2 != null)
            {
                if (line1 == null || (line2 != null && string.Compare(line1, line2) > 0))
                {
                    writer.WriteLine(line2);
                    line2 = reader2.ReadLine();
                }
                else
                {
                    writer.WriteLine(line1);
                    line1 = reader1.ReadLine();
                }
            }
        }
    }
}
/*
даны два файла с отсортированными данными необходимо сформировать выходной файл, который является слиянием двух файлов,
данные в выходном файле тоже должны быть отсортированы, ограничения: нельзя считывать данные в промежуточные списки -> надо брать попеременно
*/