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
using OmGTU;
using System.Diagnostics;

namespace OmGTU
{
    internal class First
    {
        public static void Main()
        {
            for (int i = 106732567; i < 152673837; i++)
            {
                bool flag = true;
                if (((int)Math.Sqrt(i) * (int)Math.Sqrt(i)) != i)
                {
                    continue;
                }
                int delit = 0;
                int max_del = 0;
                for (int j = 2; j < (int)(Math.Sqrt(i) - 1); j++)
                {
                    if (i % j == 0)
                    {
                        delit += 2;
                        max_del = i / j;
                    }
                    if (delit > 2)
                    {
                        flag = false;
                        break;
                    }
                }
                if (flag && delit == 2)
                {
                    Console.WriteLine($"{i} {max_del}");
                }
            }
        }
    }
}