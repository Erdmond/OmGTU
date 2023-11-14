using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.Linq;
using System.Net.Configuration;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;

namespace OmGTU
{
    internal class First
    {
        static void Main(string[] args)
        {
            string s_or = Convert.ToString(Console.ReadLine());
            string s_re = "";
            int max_poly = 0;



            for (int i = 0; i < s_or.Length; i++)
            {
                s_re = s_or[i] + s_re;
            }



            for (int i = 0; i < s_or.Length; i++)
            {
                for (int j = 0; j < s_re.Length; j++)
                {
                    string poly = "";
                    if (s_or[i] == s_re[j])
                    {
                        for (int k = 0; Math.Max(j, i) + k < s_re.Length; k++)
                        {
                            if (s_or[i + k] == s_re[j + k])
                            {
                                poly = poly + s_or[i + k];
                            }
                            else { break; }
                        }
                    }
                    if (poly.Length > max_poly) { max_poly = poly.Length; Console.WriteLine(poly); }
                }
            }



            Console.WriteLine(max_poly);
        }
    }
}
/* На вход строка, определить наибольшую длину подстроки полиндрома */