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
using System.Security.Policy;

namespace OmGTU
{
    public class Employee
    {
        public int Num { get; set; }
        public string Fio { get; set; }
        public string Post { get; set; }
        public int Pay { get; set; }
        public string Category { get; set; }
        public int Quantity { get; set; }
        public int Price { get; set; }

        public Employee(int num, string fio, string post, int pay, string category, int quantity, int price)
        {
            Num = num;
            Fio = fio;
            Post = post;
            Pay = pay;
            Category = category;
            Quantity = quantity;
            Price = price;
        }
    }

    internal class Program
    {
        static void Main()
        {
            List<Employee> employees = new List<Employee>() { };

            // Кол-во рабочих, которые получают ЗП < сумма выработанной продукции
            int workersWithLowerPay = employees.Count(e => e.Pay < e.Quantity * e.Price);
            Console.WriteLine($"1) Количество рабочих с ЗП меньше выработки: {workersWithLowerPay}");

            // Кол-во произведённой продукции по каждой категории (в количественном и денежном эквиваленте)
            var productsByCategory = employees
                .GroupBy(e => e.Category)
                .Select(g => new
                {
                    Category = g.Key,
                    TotalQuantity = g.Sum(e => e.Quantity),
                    TotalValue = g.Sum(e => e.Quantity * e.Price)
                });
            Console.WriteLine("\n2) Произведенная продукция по категориям:");
            foreach (var item in productsByCategory)
            {
                Console.WriteLine($"{item.Category}: количество - {item.TotalQuantity}, стоимость - {item.TotalValue}");
            }

            // Общий суммарный объём произведённой продукции
            int totalQuantity = employees.Sum(e => e.Quantity);
            decimal totalValue = employees.Sum(e => e.Quantity * e.Price);
            Console.WriteLine($"\n3) Общий объем продукции: количество - {totalQuantity}, стоимость - {totalValue}");

            // Кол-во сотрудников, получающих > 50% от суммы производимого ими продукта
            int highPaidWorkers = employees.Count(e => e.Pay > 0.5m * e.Quantity * e.Price);
            Console.WriteLine($"\n4) Количество сотрудников с ЗП > 50% от выработки: {highPaidWorkers}");
        }
    }
}