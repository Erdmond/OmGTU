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
using System.Xml.Linq;
using System.Xml.Schema;

namespace OmGTU
{
    public class Biblioteki
    {
        public string Raion { get; set; }
        public string Adres { get; set; }
        public int Knigi { get; set; }
        public int Posititeli { get; set; }
        public string FIOruk { get; set; }

        public Biblioteki(string raion, string adres, int knigi, int posetiteli, string fioruk)
        {
            Raion = raion;
            Adres = adres;
            Knigi = knigi;
            Posititeli = posetiteli;
            FIOruk = fioruk;
        }

        public void Info()
        {
            Console.WriteLine("  Район: " + Raion + "\n Адрес: " + Adres + "\n Количество книг: " + Knigi + "\n Количество посетителей: " + Posititeli + "\n ФИО руководителя: " + FIOruk);
        }

        public void Rai(Biblioteki Biblioteki, string Rai_Otb)
        {
            if (Biblioteki.Raion == Rai_Otb) { Biblioteki.Info(); }
        }

        public void Pos(Biblioteki Biblioteki, int Pos_Otb)
        {
            if (Biblioteki.Posititeli > Pos_Otb) { Biblioteki.Info(); }
        }

        public void Kni(Biblioteki Biblioteki, int Kni_Otb)
        {
            if (Biblioteki.Knigi >= Kni_Otb) { Biblioteki.Info(); }
        }

        public void Fio(Biblioteki Biblioteki, string Fio_Otb)
        {
            if (Biblioteki.FIOruk == Fio_Otb) { Biblioteki.Info(); }
        }
    }
    internal class First
    {
        public static void Main()
        {
            Biblioteki[] Biblioteki = new Biblioteki[7];
            Biblioteki[0] = new Biblioteki("Советский", "пр. Мира 11", 7913, 112, "Алябьев Александр Иванович");
            Biblioteki[1] = new Biblioteki("Советский", "ул. Химиков 20", 2574, 90, "Федотова Ольга Юрьевна");
            Biblioteki[2] = new Biblioteki("Центральный", "ул. Ленина 46", 10275, 170, "Казаков Макар Геннадьевич");
            Biblioteki[3] = new Biblioteki("Центральный", "ул. Пушкина 78", 9086, 230, "Девятерикова Наталья Ивановна");
            Biblioteki[4] = new Biblioteki("Куйбышевский", "ул. Звездова 34", 1075, 73, "Женихин Иван Юрьевич");
            Biblioteki[5] = new Biblioteki("Первомайский", "ул. Тюленина 89", 3460, 102, "Петин Сергей Павлович");
            Biblioteki[6] = new Biblioteki("Первомайский", "ул. Заозерная 25", 8532, 87, "Астюхина Анна Григорьевна");

            Console.WriteLine("Введите район, библиотеки которого необходимо найти.");
            string Rai_Otb = Convert.ToString(Console.ReadLine());
            Console.WriteLine("Список нужных библиотек:");
            foreach (Biblioteki i in Biblioteki) { i.Rai(i, Rai_Otb); }

            Console.WriteLine("Введите количество посетителей, больше которого должно быть количество посетителей отобранных библиотек.");
            int Pos_Otb = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Список нужных библиотек:");
            foreach (Biblioteki i in Biblioteki) { i.Pos(i, Pos_Otb); }

            Console.WriteLine("Введите количество книг, больше которого должно быть количество книг отобранных библиотек.");
            int Kni_Otb = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Список нужных библиотек:");
            foreach (Biblioteki i in Biblioteki) { i.Kni(i, Kni_Otb); }

            Console.WriteLine("Введите ФИО руководителя библиотеки, информацию о которой необходимо найти.");
            string Fio_Otb = Convert.ToString(Console.ReadLine());
            Console.WriteLine("Список нужных библиотек:");
            foreach (Biblioteki i in Biblioteki) { i.Fio(i, Fio_Otb); }
        }
    }
}
/*
Библиотека с характеристиками: район, адрес, кол-во книг, кол-во посетителей, ФИО руководителя.
В мэйне массив со сведениями со всеми библиотеками г. Омска.
Выборка по району, выборку по кол-ву посетителей превышающих заданное, выборку по кол-ву книг не менее заданного, поиск информации библиотеки по ФИО руководителя.
*/