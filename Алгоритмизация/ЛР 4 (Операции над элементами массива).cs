using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;

namespace OmGTU
{
    internal class First
    {
        static void Main(string[] args)
        {
            /*
            int n, i, y;
            n = Convert.ToInt32(Console.ReadLine());
            int[] e = new int[n];
            for (i = 0; i < n; i++)
            {
                e[i] = Convert.ToInt32(Console.ReadLine());
            }
            y = e[0];
            foreach (int x in e)
            {
                if ((x > y) && (x % 2 == 0)) y = x;
            }
            Console.WriteLine("Максимальное среди чётных: " + y);
            */

            /*
            int n, i, y, num, k;
            n = Convert.ToInt32(Console.ReadLine());
            k = 0;
            int[] e = new int[n];
            for (i = 0; i < n; i++)
            {
                e[i] = Convert.ToInt32(Console.ReadLine());
            }
            foreach (int x in e)
            {
                if (x > 0) num = x;
                else num = -x;
                do
                {
                    y = num % 10;
                    if (y == 5) { k++; break; }
                    num = num / 10;
                } while (num > 0);
            }
            Console.WriteLine(k);
            */

            /*
            int n, i, num, mink, mink1, k;
            n = Convert.ToInt32(Console.ReadLine());
            int[] e = new int[n];
            for (i = 0; i < n; i++)
            {
                e[i] = Convert.ToInt32(Console.ReadLine());
            }
            if (e[0] > 0) num = e[0];
            else num = -e[0];
            k = e[0];
            mink = 0;
            do
            {
                mink += num % 10;
                num = num / 10;
            } while (num > 0);
            foreach (int x in e)
            {
                if (x > 0) num = x;
                else num = -x;
                mink1 = 0;
                do
                {
                    mink1 += num % 10;
                    num = num / 10;
                } while (num > 0);
                if (mink1 < mink) { k = x; mink = mink1; }
            }
            Console.WriteLine(k + " " + mink);
            */
        }
    }
}
