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
using System.IO;
using System.Security.Cryptography;

namespace OmGTU
{
    internal class First
    {
        public static void Main()
        {
            int n = Convert.ToInt32(Console.ReadLine());
            int t = Convert.ToInt32(Console.ReadLine());
            int sum_1 = 0;
            int sum_2 = t;
            for (int i = 0; i < n; i++)
            {
                int a = int.Parse(Console.ReadLine());
                int b = int.Parse(Console.ReadLine());
                sum_1 += a;
                sum_2 = Math.Min(sum_1 + t, sum_2 + b);
            }
            Console.WriteLine(Math.Min(sum_1 + t, sum_2));
        }
    }
}
