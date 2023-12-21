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

namespace OmGTU
{
    internal class First
    {
        public static void Main()
        {
            string obraz = Convert.ToString(Console.ReadLine());
            string vvod = null;
            while (true)
            {
                string kusok = Convert.ToString(Console.ReadLine());
                if (kusok == "") { break; }
                else { vvod += kusok; }
            }
            while (vvod.Contains(obraz)) { vvod = vvod.Replace(obraz, "^"); }
            Console.WriteLine(vvod.Count(e => e == '^'));
        }
    }
}