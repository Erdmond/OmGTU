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
            int n = Convert.ToInt32(Console.ReadLine());
            int m = Convert.ToInt32(Console.ReadLine());
            int k = Convert.ToInt32(Console.ReadLine());
            int n1 = Convert.ToInt32(Console.ReadLine());
            int m1 = Convert.ToInt32(Console.ReadLine());
            if ((n1 > n) || (m1 > m) || ((k == 0) && ((n1 != n) || (m1 != m)))) { Console.WriteLine("Некорректные входные данные"); return; }



            int[] krug = new int[n + m];
            for (int i = 0; i < (n + m); i++) { krug[i] = 1; }



            int x = 1;
            while (krug.Count(elem => elem == 1) > (n1 + m1))
            {
                if (krug[x % (n + m)] == 1) { krug[x % (n + m)] = 0; }
                else
                {
                    while (krug[x % (n + m)] != 1)
                    {
                        x++;
                    }
                    krug[x % (n + m)] = 0;
                }
                x += k;
            }
            foreach (int i in krug) { Console.Write(i + " "); }
            Console.WriteLine();



            for (int i = 0; i < (n + m); i++)
            {
                if ((krug[i] == 1) && (n1 != 0)) { krug[i] = 2; n1 -= 1; }
                else
                {
                    if ((krug[i] == 1) && (m1 != 0)) { krug[i] = 3; m1 -= 1; }
                }
            }



            x = 0;
            while (krug.Count(elem => elem == 2) < n)
            {
                if (krug[x] == 0) { krug[x] = 2; }
                x++;
            }



            x = 0;
            while (krug.Count(elem => elem == 3) < m)
            {
                if (krug[x] == 0) { krug[x] = 3; }
                x++;
            }



            string[] mouses = new string[n + m];
            for (int i = 0; i < n + m; i++)
            {
                if (krug[i] == 2) { mouses[i] = "СЕР"; }
                if (krug[i] == 3) { mouses[i] = "БЕЛ"; }
            }


            if (krug[0] == 3) { Console.WriteLine("Некорректные входные данные."); }
            else { { foreach (int i in krug) { Console.Write(i + " "); } Console.WriteLine(); foreach (string i in mouses) { Console.Write(i + " "); } } }
        }
    }
}