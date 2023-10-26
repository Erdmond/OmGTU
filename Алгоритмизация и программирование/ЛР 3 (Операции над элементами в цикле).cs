using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OmGTU
{
    internal class First
    {
        static void Main(string[] args)
        {
            /*
            int n, x, y, z, i;
            z = 0;
            n = Convert.ToInt32(Console.ReadLine());
            x = Convert.ToInt32(Console.ReadLine());
            for (i = 0; i < (n - 1); i++)
            {
                y = Convert.ToInt32(Console.ReadLine());
                if ((x > 0) && (y < 0) || (x < 0) && (y > 0))
                {
                    z++;
                }
                x = y;
            }
            Console.WriteLine(z);
            */

            /*
            int n, i, x, y, z, c;
            c = 0;
            n = Convert.ToInt32(Console.ReadLine());
            x = Convert.ToInt32(Console.ReadLine());
            y = Convert.ToInt32(Console.ReadLine());
            for (i = 0; i < (n-2); i++)
            {
                z = Convert.ToInt32(Console.ReadLine());
                if ((x > y) && (z > y))
                {
                    c++;
                }
                x = y;
                y = z;
            }
            Console.WriteLine(c);
            */

            /*
            int n, i, x, y, maxc, c;
            maxc = 1;
            c = 1;
            n = Convert.ToInt32(Console.ReadLine());
            x = Convert.ToInt32(Console.ReadLine());
            for (i = 0; i < (n-1); i++)
            {
                y = Convert.ToInt32(Console.ReadLine());
                if (x == y)
                {
                    c++;
                }
                else
                {
                    c = 1;
                }
                if (c > maxc)
                {
                    maxc = c;
                }
                x = y;
            }
            Console.WriteLine(maxc);
            */

            /*
            int n, i, x, y, c, minc;
            c = 0;
            n = Convert.ToInt32(Console.ReadLine());
            minc = n + 1;
            x = Convert.ToInt32(Console.ReadLine());
            for (i = 0; i < (n-1); i++)
            {
                y = Convert.ToInt32((Console.ReadLine()));
                if (x < 0)
                {
                    c++;
                    if (y > 0)
                    {
                        if (c < minc)
                        {
                            minc = c;
                        }
                        c = 0;
                    }
                    if ((i == n-2) && (y < 0))
                    {
                        c++;
                        if (c < minc)
                        {
                            minc = c;
                        }
                    }
                }
                else
                {
                    if (i == n-2)
                    {
                        minc = 1;
                    }
                }
                x = y;
            }
            if (minc == n+1)
            {
                Console.WriteLine("Нет отрицательных элементов.");
            }
            else
            {
                Console.WriteLine(minc);
            }
            */
        }
    }
}
