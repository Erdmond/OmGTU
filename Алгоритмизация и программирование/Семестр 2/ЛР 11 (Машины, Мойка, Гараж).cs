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
    class Car
    {
        public string Model { get; set; }
        public string Dirty { get; set; }
        public Car(string model, string dirty)
        {
            Model = model;
            Dirty = dirty;
        }
    }
    class CarWash
    {
        public static void WashDirtyCar(Car car)
        {
            if (car.Dirty == "Грязная") { car.Dirty = "Чистая"; Console.WriteLine("Машина вымыта."); }
            else { Console.WriteLine("Машина и так чистая."); }
        }
    }
    class Garage
    {
        public List<Car> Cars_in_garage { get; set; }
        public Garage(List<Car> cars)
        {
            Cars_in_garage = cars;
        }
        public static void Garage_add(Garage gar, Car car)
        {
            gar.Cars_in_garage.Append(car);
        }
    }

    internal class Program
    {
        public static void Main()
        {
            Garage garage = new Garage(new List<Car>());
            int Menu() { Console.Write("  Выберите действие:\n1) Добавить машины в гараж\n2) Помыть машины в гараже\n3) Выйти из программы\n  "); return int.Parse(Console.ReadLine()); }
            while (true)
            {
                switch (Menu())
                {
                    case 1:
                        Console.WriteLine("Перечислите машины, чтобы зывершить ввод отправьте x:");
                        string[] o = null;
                        while (o[0] != "x") { o = Console.ReadLine().Split(); Garage.Garage_add(garage, new Car(o[0], o[1])); }
                        break;
                    case 2:
                        foreach (Car c in garage.Cars_in_garage) { CarWash.WashDirtyCar(c); }
                        break;
                    case 3:
                        Environment.Exit(0);
                        break;
                }
            }
        }
    }
}
/*
Разработать программу, которая реализует взаимодействие следующих классов:
автомобиль, гараж (гараж это коллекция автомобилей), мойка (независимое предприятие, только принимает автомобили).
Необходимо выполнить помывку всех автомобилей, делегируя выполнение работы мойке.
*/