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
            int x, bel, k, m, y;
            k = Convert.ToInt32(Console.ReadLine());
            m = Convert.ToInt32(Console.ReadLine());
            bel = Convert.ToInt32(Console.ReadLine());
            x = 0;
            int[] mouse = new int[k];
            for (int i = 0; i < mouse.Length; i++) { mouse[i] = 1; }
            while (mouse.Count(j => j == 1) > 1)
            {
                x += m;
                Console.WriteLine(x);
                if (mouse[(x % k)] == 1) { mouse[(x % k)] = 0; }
                else
                {
                    while (mouse[(x % k)] == 0) { x++; }
                    mouse[(x % k)] = 0;
                    x += 1;
                }
            }
            y = Array.IndexOf(mouse, 1);
            Console.WriteLine((k + bel - y) % k);

            /* Дано К мышек, 1 белая, кот начинает съедать каждую M-ную (например 3), 
            необходимо определить с какой мышки кот должен съедать каждую М-ную, чтобы в конце осталась одна белая мышка
            Полный перебор использовать нельзя */
        }
    }
}
