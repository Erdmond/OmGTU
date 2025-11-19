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
            void print(HashSet<int> e)
            {
                foreach (int i in e) { Console.WriteLine(i); }
            }
            HashSet<int> a = new HashSet<int>();
            HashSet<int> b = new HashSet<int>();
            HashSet<int> c = new HashSet<int>();
            HashSet<int> inter = new HashSet<int>(a);
            inter.IntersectWith(b);
            inter.IntersectWith(c);
            HashSet<int> uni = new HashSet<int>(a);
            uni.UnionWith(b);
            uni.UnionWith(c);
            HashSet<int> dop_a = new HashSet<int>(a);
            HashSet<int> dop_b = new HashSet<int>(b);
            HashSet<int> dop_c = new HashSet<int>(c);
            dop_a.ExceptWith(uni);
            dop_b.ExceptWith(uni);
            dop_c.ExceptWith(uni);
            Console.WriteLine("\nОбъединене:");
            print(uni);
            Console.WriteLine("\nПересечение:");
            print(inter);
            Console.WriteLine("\nДополнение 1 множества:");
            print(dop_a);
            Console.WriteLine("\nДополнение 2 множества:");
            print(dop_b);
            Console.WriteLine("\nДополнение 3 множества:");
            print(dop_c);
        }
    }
}