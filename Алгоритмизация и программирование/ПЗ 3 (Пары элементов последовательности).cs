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
            int n, x, y, i, suma, maxsum;
            n = Convert.ToInt32(Console.ReadLine());
            suma = maxsum = 0;
            int[] par = new int[n * 2];
            int[] ost = new int[n];
            for (i = 0; i < n * 2; i++)
            {
                par[i] = Convert.ToInt32(Console.ReadLine());
            }
            for (i = 0; i < n * 2; i = i + 2)
            {
                x = par[i];
                y = par[i + 1];
                suma += Math.Max(x, y);
                ost[(i / 2)] = Math.Abs(x - y);
            }
            Array.Sort(ost);
            if (suma % 3 == 0) Console.WriteLine(suma);
            else
            {
                for (i = 0; i < n; i++)
                {
                    suma = suma - ost[i];
                    if ((suma % 3 == 0) && (suma > maxsum))
                    {
                        maxsum = suma;
                        break;
                    }
                }
            }
            if (maxsum != 0) Console.WriteLine(maxsum);
            else Console.WriteLine("Ошибка.");
        }
    }
}
