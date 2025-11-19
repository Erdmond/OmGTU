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
            Console.WriteLine();
            int[][] mn = new int[n][];
            int max_m = 0;
            int sum_dlin = 1;
            int r = 0;
            int k = 0;



            for (int i = 0; i < n; i++)
            {
                int m = Convert.ToInt32(Console.ReadLine());
                if (max_m < m) { max_m = m; }
                sum_dlin += m;
                mn[i] = new int[m];
                for (int j = 0; j < m; j++)
                {
                    mn[i][j] = Convert.ToInt32(Console.ReadLine());
                }
                Console.WriteLine();
            }



            int[] per = new int[max_m];
            int[] obj = new int[sum_dlin];



            r = 0;
            foreach (int[] i in mn)
            {
                foreach (int j in i)
                {
                    if (!Array.Exists(obj, elem => elem == j))
                    {
                        obj[r] = j;
                        r++;
                    }
                }
            }



            r = 0;
            foreach (int i in obj)
            {
                k = 0;
                foreach (int[] j in mn)
                {
                    if (Array.Exists(j, elem => elem == i)) { k++; }
                }
                if (k == n) { per[r] = i; r++; }
            }



            Console.WriteLine("Множество пересечения:");
            foreach (int i in per)
            {
                if (i != 0) { Console.Write(i + " "); }
            }
            Console.WriteLine();



            Console.WriteLine("Множество объединения:");
            foreach (int i in obj)
            {
                if (i != 0) { Console.Write(i + " "); }
            }
            Console.WriteLine();



            Console.WriteLine("Множества дополнений:");
            foreach (int[] j in mn)
            {
                foreach (int i in obj)
                {
                    if ((!Array.Exists(j, elem => elem == i)) && (i != 0)) { Console.Write(i + " "); }
                }
                Console.WriteLine();
            }
        }
    }
}

/* Дано n множеств int типа. Кол-во элементов в каждом множестве различно. Хранить мн-ва в ступенчатом массиве. Определить:
 * 1. Мн-во пересечения
 * 2. Мн-во объединения
 * 3. Определить дополнения каждому множеству относительно объединения */