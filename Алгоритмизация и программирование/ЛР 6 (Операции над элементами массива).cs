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
            int n, m;
            m = Convert.ToInt32(Console.ReadLine());
            n = Convert.ToInt32(Console.ReadLine());
            int[,] mass = new int[n, m];
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    mass[i, j] = Convert.ToInt32(Console.ReadLine());
                }
            }



            int k1;
            k1 = 0;
            foreach (int i in mass)
            {
                if (i % 5 == 0) k1++;
            }
            Console.WriteLine("Количество элементов, кратных 5: " + k1);



            int k2, suma1, proizv1;
            k2 = 0;
            for (int i = 0; i < n; i++)
            {
                suma1 = 0;
                proizv1 = 1;
                for (int j = 0; j < m; j++)
                {
                    suma1 += mass[i, j];
                    proizv1 = proizv1 * mass[i, j];
                }
                if (suma1 > proizv1) k2++;
            }
            Console.WriteLine("Количество строк, в которых сумма больше произведения: " + k2);




            int[] minim = new int[m];
            for (int i = 0; i < m; i++)
            {
                minim[i] = mass[0, i];
            }
            for (int i = 1; i < n; i++)
            {
                for (int j = 1; j < m; j++)
                {
                    if (mass[i, j] < minim[j]) minim[j] = mass[i, j];
                }
            }
            Console.Write("Минимальные элементы каждого столбца равны: ");
            foreach (int i in minim) Console.Write(i + " ");
            Console.WriteLine("");



            int proizv2;
            proizv2 = 1;
            foreach (int i in mass)
            {
                if ((i % 2 == 0) && (i >= 0)) proizv2 = proizv2 * i;
            }
            Console.WriteLine("Произведение неотрицательных кратных элементов массива равно: " + proizv2);



            int k3, sum2, pro2, nul;
            int[,] five = new int[n, 3];
            k3 = 0;
            for (int i = 0; i < n - 1; i++)
            {
                nul = 0;
                pro2 = 1;
                sum2 = 0;
                for (int j = 0; j < m; j++)
                {
                    if (mass[i, j] == 0) nul++;
                    pro2 = pro2 * mass[i, j];
                    sum2 += mass[i, j];
                }
                five[i, 0] = nul;
                five[i, 1] = pro2;
                five[i, 2] = sum2;
            }
            for (int i = 0; i < n; i++)
            {
                for (int j = i; (j < n - 1); j++)
                {
                    if ((five[i, 0] == five[j, 0]) && (five[i, 1] == five[j, 1]) && (five[i, 2] == five[j, 2])) k3++;
                }
            }
            Console.WriteLine("Количество пар строк, состоящих из одних элементов равно: " + k3);
        }
    }
}