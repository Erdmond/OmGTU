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
            int hour_rise = Convert.ToInt32(Console.ReadLine());
            int min_rise = Convert.ToInt32(Console.ReadLine());
            int hour_dawn = Convert.ToInt32(Console.ReadLine());
            int min_dawn = Convert.ToInt32(Console.ReadLine());

            float v = float.Parse(Console.ReadLine());
            int pauses = Convert.ToInt32(Console.ReadLine());
            float[] s_pauses = new float[pauses];
            for (int i = 0; i < s_pauses.Length; i++) { s_pauses[i] = float.Parse(Console.ReadLine()); }
            int rise_min = hour_rise * 60 + min_rise;
            int dawn_min = hour_dawn * 60 + min_dawn;
            float[] s = new float[10];
            Console.WriteLine();
            for (int i = pauses - 1; i >= 1; i--)
            {
                s[i] = s_pauses[i] - s_pauses[i - 1];
            }
            float time_now = rise_min;
            foreach (float i in s)
            {
                if (time_now + (i / v) * 60 <= dawn_min)
                {
                    time_now += i / v * 60;
                    Console.WriteLine((int)(time_now / 60) + "." + (int)(time_now % 60));
                }
                else
                {
                    Console.Write(Array.IndexOf(s, i) + " ");
                    time_now = rise_min;
                }
            }
            Console.WriteLine();
            Console.WriteLine((int)(time_now / 60) + "." + (int)(time_now % 60));
        }
    }
}