using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Configuration;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;

namespace OmGTU
{
    internal class First
    {
        static void Main(string[] args)
        {
            int m, min, max, end1, end2, flag3, flag4, indmax, indmin;

            end1 = -1;
            flag3 = flag4 = 1;
            m = Convert.ToInt32(Console.ReadLine());

            int[] mass = new int[m];
            for (int i = 0; i < m; i++) mass[i] = Convert.ToInt32(Console.ReadLine());

            min = mass.Min();
            max = mass.Max();
            indmin = Array.IndexOf(mass, min);
            indmax = Array.IndexOf(mass, max);

            for (int i = 0; i < m; i++)
            {
                if (mass[i] % min == 0) { end1 = i + 1; }
                break;
            }

            end2 = Array.LastIndexOf(mass, 0);

            if ((indmax == indmin) || (indmax + 1 == indmin) || (indmax == indmin + 1)) flag3 = 5;
            else
            {
                for (int i = Math.Min(indmax, indmin) + 1; i < Math.Max(indmax, indmin) - 1; i++)
                {
                    if (mass[i] <= mass[i + 1]) flag3 = 0;
                    break;
                }
            }

            for (int i = 0; i < m; i++)
            {
                if (mass[i] % (i + 1) != 0) { flag4 = 0; }
            }

            int[] end5 = new int[(m - 1)];
            for (int i = 0; i < m - 1; i++)
            {
                end5[i] = mass[i] + mass[(i + 1)];
            }

            if (end1 == -1) Console.WriteLine("1) Нет подходящего элемента.");
            else Console.WriteLine("1) " + end1 + ".");

            if (end2 == -1) Console.WriteLine("2) Нет подходящего элемента.");
            else Console.WriteLine("2) " + end2 + ".");

            if (flag3 == 5) Console.WriteLine("3) Между min и max значениями нет элементов.");
            if (flag3 == 0) Console.WriteLine("3) Элементы между min и max не образуют убывающей последовательности.");
            if (flag3 == 1) Console.WriteLine("3) Элементы между min и max образуют убывающую последовательность.");

            if (flag4 == 1) Console.WriteLine("4) Все элементы кратны номеру, под которым они идут.");
            else Console.WriteLine("4) Не все элементы кратны номеру, под которым они идут.");

            Console.Write("5) ");
            foreach (int i in end5) Console.Write(i + " ");
            Console.WriteLine();
        }
    }
}
