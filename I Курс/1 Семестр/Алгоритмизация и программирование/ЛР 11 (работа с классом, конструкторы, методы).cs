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
using System.IO;
using System.Security.Cryptography;
using OmGTU;

namespace OmGTU
{
    public class Family
    {
        public string FIO { get; set; }
        public string Sex { get; set; }
        public int Year_Birth { get; set; }
        public string FIO_Mother { get; set; }
        public string FIO_Father { get; set; }
        public int[] Schools { get; set; }
        public Family(string fio, string sex, int year_birth, string fio_mother, string fio_father, int[] schools)
        {
            FIO = fio;
            Sex = sex;
            Year_Birth = year_birth;
            FIO_Mother = fio_mother;
            FIO_Father = fio_father;
            Schools = schools;
        }
        public void Mono_School_Kids(Family i)
        {
            if (i.Schools.Length == 1) { Console.WriteLine("\t" + i.FIO); }
        }
    }
    internal class First
    {
        public static void Main()
        {
            Family[] Families = new Family[11];
            Families[0] = new Family("Ерёмин Вадим Сергеевич", "М", 2005, "Ерёмина Валерия Жынсымбаевна", "Ерёмин Сергей Павлович", new int[3] { 386, 1, 3 });
            Families[1] = new Family("Ерёмина Валерия Жынсымбаевна", "Ж", 1985, "Тулиева Саннар Раиловна", "Тулиев Жынсымбай Маилович", new int[2] { 6, 23 });
            Families[2] = new Family("Ерёмин Сергей Павлович", "М", 1982, "Ерёмина Елена Юрьевна", "Ерёмин Павел Ильич", new int[1] { 3 });
            Families[3] = new Family("Данилов Егор Дмитриевич", "М", 2005, "Данилова Евгения Александровна", "Данилов Дмитрий Иванович", new int[2] { 386, 6 });
            Families[4] = new Family("Данилов Глеб Дмитриевич", "М", 2005, "Данилова Евгения Александровна", "Данилов Дмитрий Иванович", new int[1] { 6 });
            Families[5] = new Family("Данилова Евгения Александровна", "Ж", 1985, "Нестерова Анна Алексеевна", "Нестеров Александр Константинович", new int[3] { 1, 6, 7 });
            Families[6] = new Family("Данилов Дмитрий Иванович", "М", 1980, "Данилова Анастасия Петровна", "Колдун Иван Викторович", new int[2] { 8, 6 });
            Families[7] = new Family("Нестерова Анна Алексеевна", "М", 1965, "Макарова Ольга Иосифовна", "Макаров Алексей Григорьевич", new int[1] { 6 });
            Families[8] = new Family("Нестеров Александр Константинович", "Ж", 1964, "Нестерова Наталья Богдановна", "Нестеров Константин Владимирович", new int[5] { 78, 5, 23, 1, 10 });
            Families[9] = new Family("Данилова Анастасия Петровна", "Ж", 1960, "Данилова Марина Витальевна", "Данилов Пётр Михайлович", new int[1] { 5 });
            Families[10] = new Family("Колдун Иван Викторович", "М", 1961, "Колдун Софья Романовна", "Колдун Виктор Ринатович", new int[2] { 64, 8 });
            int Kids_Count = 0;
            string Parents_Max_Kids = null;
            int Max_Kids = 0;
            for (int i = 0; i < Families.Length; i++)
            {
                string Parents = Families[i].FIO_Mother + " и " + Families[i].FIO_Father;
                int Count_Kids = 0;
                for (int j = i + 1; j < Families.Length; j++)
                {
                    if (Families[j].FIO_Mother == Families[i].FIO_Mother && Families[j].FIO_Father == Families[i].FIO_Father)
                        Count_Kids++;
                }
                if (Count_Kids > Max_Kids)
                {
                    Max_Kids = Count_Kids;
                    Parents_Max_Kids = Parents;
                }
            }
            Console.WriteLine($"   >>> ВЫБОРКИ ЧЛЕНОВ СЕМЕЙ ПО ПАРАМЕТРАМ <<<\n1) Родители с наибольшим количеством детей:\n\t{Parents_Max_Kids}");
            Console.Write("Введите год, по которому необходимо выполнить отбор рождённых детей: ");
            int e = Convert.ToInt32(Console.ReadLine());
            foreach (Family o in Families) { if (o.Year_Birth == e) { Kids_Count++; } }
            Console.WriteLine($"2) Количество детей, рождённых в {e} году:\n\t{Kids_Count}");
            int Most_Popular_School = 0;
            int Max_Students = 0;
            foreach (Family o in Families)
            {
                foreach (int j in o.Schools)
                {
                    int Students = 0;
                    foreach (Family y in Families)
                    {
                        bool flag = false;
                        foreach (int u in y.Schools) { if (u == j) { flag = true; break; } }
                        if (flag) { Students++; }
                    }
                    if (Students > Max_Students) { Max_Students = Students; Most_Popular_School = j; }
                }
            }
            Console.WriteLine($"3) Наиболее популярная школа:\n\t{Most_Popular_School}");
            Console.WriteLine("4) Дети, которые учились лишь в одной школе:");
            foreach (Family o in Families) { o.Mono_School_Kids(o); }
            Console.ReadLine();
        }
    }
}
/*
## ПРИМЕР ВЫВОДА ПРОГРАММЫ ЧЕРЕЗ КОНСОЛЬ
    >>> ВЫБОРКИ ЧЛЕНОВ СЕМЕЙ ПО ПАРАМЕТРАМ <<<
1) Родители с наибольшим количеством детей:
        Данилова Евгения Александровна и Данилов Дмитрий Иванович
Введите год, по которому необходимо выполнить отбор рождённых детей: 2005
2) Количество детей, рождённых в 2005 году:
        3
3) Наиболее популярная школа:
        6
4) Дети, которые учились лишь в одной школе:
        Ерёмин Сергей Павлович
        Данилов Глеб Дмитриевич
        Нестерова Анна Алексеевна
        Данилова Анастасия Петровна
Для продолжения нажмите любую клавишу . . .
*/
