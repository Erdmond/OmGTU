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
            // Ввод значений.
            int n = Convert.ToInt32(Console.ReadLine());
            int m = Convert.ToInt32(Console.ReadLine());
            int[,] mass = new int[n, m];

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    mass[i, j] = Convert.ToInt32(Console.ReadLine());
                }
            }

            // 1 Задание.
            string[] max_chet_str = new string[n];
            for (int i = 0; i < n; i++)
            {
                int max_chet = mass[i, 0];
                int y = 0;
                while ((max_chet % 2 != 0) && (y != m - 1))
                {
                    max_chet = mass[i, y];
                    y++;
                }
                for (int j = 0; j < m; j++)
                {
                    if ((mass[i, j] > max_chet) && (mass[i, j] % 2 == 0)) { max_chet = mass[i, j]; }
                }
                if (max_chet % 2 == 0) { max_chet_str[i] = Convert.ToString(max_chet); }
                else { max_chet_str[i] = "N"; }
            }
            foreach (string s in max_chet_str) { Console.Write(s + " "); }
            Console.WriteLine();

            // 2 Задание.
            int[] nenull = new int[m];
            for (int i = 0; i < m; i++)
            {
                int k = 0;
                for (int j = 0; j < n; j++)
                {
                    if (mass[j, i] != 0) { k++; }
                }
                nenull[i] = k;
            }
            foreach (int s in nenull) { Console.Write(s + " "); }
            Console.WriteLine();

            // 3 Задание.
            int m1 = 0;
            int[,] mass_peresbor = new int[n, m];
            if (m % 2 == 0) { m1 = m; }
            else
            {
                m1 = m - 1;
                for (int i = 0; i < n; i++) { mass_peresbor[i, m - 1] = mass[i, m - 1]; }
            }
            for (int i = 0; i < m1; i += 2)
            {
                for (int j = 0; j < n; j++)
                {
                    mass_peresbor[j, i] = mass[j, i + 1];
                    mass_peresbor[j, i + 1] = mass[j, i];
                }
            }
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    Console.Write(mass_peresbor[i, j] + " ");
                }
                Console.WriteLine();
            }
        }
    }
}
/*
для заданного массива размерность n×m определить 
1)  максимальный среди чётных элементов в каждой строке
2) количество ненулевых элементов в каждом столбце
3) программу преобразования массива по следующему принципу
первый столбец меняется с элементами второго столбца
третий столбец меняется с четвёртым и так далее
ограничения: 
заполнение массива функцией, как и все остальное
 */