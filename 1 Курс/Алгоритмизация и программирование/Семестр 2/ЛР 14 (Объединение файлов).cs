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
        static void Main()
        {
            StreamReader reader1 = null;
            StreamReader reader2 = null;
            StreamWriter writer = null;
            try
            {
                reader1 = new StreamReader("file1.txt");
                reader2 = new StreamReader("file2.txt");
                writer = new StreamWriter("output.txt");
                string line1 = reader1.ReadLine();
                string line2 = reader2.ReadLine();

                while (line1 != null || line2 != null)
                {
                    int num1 = line1 != null ? int.Parse(line1) : int.MaxValue;
                    int num2 = line2 != null ? int.Parse(line2) : int.MaxValue;
                    if (num1 <= num2)
                    {
                        writer.WriteLine(num1);
                        line1 = reader1.ReadLine();
                    }
                    else
                    {
                        writer.WriteLine(num2);
                        line2 = reader2.ReadLine();
                    }
                }
            }
            finally
            {
                if (reader1 != null) reader1.Close();
                if (reader2 != null) reader2.Close();
                if (writer != null)
                {
                    writer.Flush();
                    writer.Close();
                }
            }
        }
    }
}
/*
даны два файла с отсортированными данными необходимо сформировать выходной файл, который является слиянием двух файлов,
данные в выходном файле тоже должны быть отсортированы, ограничения: нельзя считывать данные в промежуточные списки -> надо брать попеременно
*/