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
    public class Product
    {
        public int Article { get; set; }
        public string Name { get; set; }
        public string Category { get; set; }
        public int Quantity { get; set; }
        public int Price { get; set; }
        public string Warehouse { get; set; }

        public Product(int article, string name, string category, int quantity, int price, string warehouse)
        {
            Article = article;
            Name = name;
            Category = category;
            Quantity = quantity;
            Price = price;
            Warehouse = warehouse;
        }
    }

    internal class Program
    {
        static void Main()
        {
            List<Product> products = new List<Product>()
            {
                new Product(1, "Ноутбук", "Электроника", 10, 1000, "Склад A"),
                new Product(2, "Мышь", "Электроника", 20, 20, "Склад A"),
                new Product(3, "Клавиатура", "Электроника", 15, 50, "Склад B"),
                new Product(4, "Стол", "Мебель", 5, 200, "Склад B"),
                new Product(5, "Стул", "Мебель", 12, 50, "Склад A"),
                new Product(6, "Лампа", "Электроника", 8, 30, "Склад B"),
            };

            // Объем товара в денежном эквиваленте по каждому складу
            var warehouseVolumes = products
                .GroupBy(p => p.Warehouse)
                .Select(g => new { Warehouse = g.Key, TotalValue = g.Sum(p => p.Price * p.Quantity) });
            Console.WriteLine("Объем товара в денежном эквиваленте по каждому складу:");
            foreach (var item in warehouseVolumes)
            {
                Console.WriteLine($"{item.Warehouse}: {item.TotalValue}");
            }

            // Максимальная цена по каждой категории
            var maxPricesByCategory = products
                .GroupBy(p => p.Category)
                .Select(g => new { Category = g.Key, MaxPrice = g.Max(p => p.Price) });
            Console.WriteLine("\nМаксимальная цена по каждой категории:");
            foreach (var item in maxPricesByCategory)
            {
                Console.WriteLine($"{item.Category}: {item.MaxPrice}");
            }

            // Средняя цена товара по каждому складу и по всем складам
            var avgPricesByWarehouse = products
                .GroupBy(p => p.Warehouse)
                .Select(g => new { Warehouse = g.Key, AveragePrice = g.Average(p => p.Price) });
            Console.WriteLine("\nСредняя цена товара по каждому складу:");
            foreach (var item in avgPricesByWarehouse)
            {
                Console.WriteLine($"{item.Warehouse}: {Math.Round(item.AveragePrice, 2)}");
            }
            double overallAvgPrice = products.Average(p => p.Price);
            Console.WriteLine($"\nСредняя цена товара по всем складам: {Math.Round(overallAvgPrice)}");

            // Определение самого дешевого товара
            Product cheapestProduct = products.OrderBy(p => p.Price).First();
            Console.WriteLine($"\nСамый дешевый товар: {cheapestProduct.Name} ({cheapestProduct.Price})");

            // Вывод данных по складу с наименьшей суммарной стоимостью товаров
            var cheapestWarehouse = warehouseVolumes.OrderBy(w => w.TotalValue).First();
            Console.WriteLine("\nДанные по складу с наименьшей суммарной стоимостью товаров:");
            var productsInCheapestWarehouse = products.Where(p => p.Warehouse == cheapestWarehouse.Warehouse);
            foreach (var product in productsInCheapestWarehouse)
            {
                Console.WriteLine($"- {product.Name} ({product.Quantity} шт., {product.Price} за шт.)");
            }
        }
    }
}

/*
Даны сведения о товарах на складах компании (поля: артикул товара
наименование товара, категория товара, кол-во товара(на данном складе),
цена за единицу, склад размещения)
 
С помощью запросов узнать:
- объем товара в денежном эквиваленте по каждом складу
- максимальную цену по каждой категории
- среднюю цену товара по каждому складу и по всем складам (всех товаров на складе)
- определить самый дешевый товар
- вывести данные по складу, в котором наименьшая суммарная стоимость товаров (вывести все данные)
*/