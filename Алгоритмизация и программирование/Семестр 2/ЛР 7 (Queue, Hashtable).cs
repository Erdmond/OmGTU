using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.Linq;
using System.Net.Configuration;
using System.Runtime.InteropServices;
using System.Runtime.Remoting.Metadata.W3cXsd2001;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Threading;
using System.Xml.Linq;
using System.Xml.Schema;
using System.IO;
using System.Security.Cryptography;
using OmGTU;
using System.Diagnostics;
using System.Collections;
using System.Collections.ObjectModel;

namespace OmGTU
{
    public class Call
    {
        public string Number { get; set; }
        public string Date { get; set; }
        public string Time { get; set; }
        public int Minutes { get; set; }
        public Call(string number, string date, string time, int minutes)
        {
            Number = number;
            Date = date;
            Time = time;
            Minutes = minutes;
        }
    }
    internal class Program
    {
        public static void Main()
        {
            Queue<Call> queue = new Queue<Call>();
            Console.WriteLine("Вводите данные, для завершения ввода введите X");
            while (true) { string input = Convert.ToString(Console.ReadLine()); if (input == "X") { break; } var d = input.Split(); queue.Enqueue(new Call(d[0], d[1], d[2], Convert.ToInt32(d[3]))); }
            Dictionary<string, int> num_d = new Dictionary<string, int>();
            Hashtable num_h = new Hashtable();
            Dictionary<string, int> mon_d = new Dictionary<string, int>();
            Hashtable mon_h = new Hashtable();
            while (queue.Count > 0)
            {
                string num = queue.Peek().Number;
                string date = queue.Peek().Date;
                int min = queue.Dequeue().Minutes;
                if (num_d.ContainsKey(num))
                {
                    num_d[num] += min;
                    num_h[num] = (int)num_h[num] + min;
                }
                else
                {
                    num_d.Add(num, min);
                    num_h.Add(num, min);
                }
                if (mon_d.ContainsKey(date))
                {
                    mon_d[date] += min;
                    mon_h[date] = (int)num_h[date] + min;
                }
                else
                {
                    mon_d.Add(date, min);
                    mon_h.Add(date, min);
                }
            }
            Console.WriteLine("Номер:\t\tСловарь:\tХэш-таблица:");
            foreach (string a in num_d.Keys)
            {
                Console.WriteLine($"{a}\t\t{num_d[a]}\t\t{num_h[a]}");
            }
            Console.WriteLine("Дата:\t\tСловарь:\tХэш-таблица:");
            foreach (string a in mon_d.Keys)
            {
                Console.WriteLine($"{a}\t\t{mon_d[a]}\t\t{mon_h[a]}");
            }
        }
    }
}
/*
На вход подаются данные в виде номера телефона, даты разговора, времени начала разговора, кол-ва минут
1) Необходимо выдать месячный отчёт по общей сумме минут каждого номера
Условия: данные ровно за один месяц, данные подаются в очередь,
чтобы подсчитать сумму минут необходимо с помощью словаря и хеш-таблицы (в качестве ключа - номер телефона, в качестве значения - кол-во минут),
на выходе выдать данные из словаря и из хеш-таблицы

2) Необходимо подсчитать суммарное время за каждую дату
Условия: данные ровно за один месяц, данные подаются в очередь,
чтобы подсчитать сумму минут необходимо с помощью словаря и хеш-таблицы (в качестве ключа - дата, в качестве значения - кол-во минут),
на выходе выдать данные из словаря и из хеш-таблицы
*/