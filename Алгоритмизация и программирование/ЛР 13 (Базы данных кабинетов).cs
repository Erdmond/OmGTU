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

namespace OmGTU
{
    public class Menu
    {
        public void Show_Menu(ref List<Classes> s, Classes r, ref bool t)
        {
            Console.Write("Меню:\n\t1) Создание базы данных;\n\t2) Добавление элементов в базу данных;\n\t3) Изменение базы;\n\t4) Выборка по кол-ву посадочных мест;\n\t5) Выборка по наличию проеткоров;\n\t6) Выборка по наличию ПК и кол-ву посадочных мест;\n\t7) Выборка по этажу;\n\t8) Вывод всей базы данных;\n\t9) Выход.\nДля выбора действия введите его номер: ");
            int x = int.Parse(Console.ReadLine());
            if (x == 1)
            {
                r.Create_Base(ref s, r);
                Console.WriteLine("База успешно создана, производится возврат к меню.\n");
            }
            else if (x == 2)
            {
                r.Add_To_Base(ref s, r);
                Console.WriteLine("Элемент успешно добавлен, производится возврат к меню.\n");
            }
            else if (x == 3)
            {
                r.Edit_Base(ref s, r);
                Console.WriteLine("Элемент успешно отредактирован, производится возврат к меню.\n");
            }
            else if (x == 4)
            {
                r.Selection_By_Count(s, r);
                Console.WriteLine("Выборка совершена, производится возврат к меню.\n");
            }
            else if (x == 5)
            {
                r.Selection_By_Proj(s, r);
                Console.WriteLine("Выборка совершена, производится возврат к меню.\n");
            }
            else if (x == 6)
            {
                r.Selection_By_Pc_Count(s, r);
                Console.WriteLine("Выборка совершена, производится возврат к меню.\n");
            }
            else if (x == 7)
            {
                r.Selection_By_Floor(s, r);
                Console.WriteLine("Выборка совершена, производится возврат к меню.\n");
            }
            else if (x == 8)
            {
                r.All_Base(ref s);
                Console.WriteLine("Информация выведена, производится возврат к меню.\n");
            }
            else if (x == 9)
            {
                Console.WriteLine("Программа завершена.");
                t = false;
            }
            else
            {
                Console.WriteLine("Произошла ошибка.");
            }
        }
    }
    public class Classes
    {
        public int Num { get; set; }
        public int Count { get; set; }
        public bool Proj { get; set; }
        public bool Pc { get; set; }
        public Classes(int n, int c, bool p, bool pc) { Num = n; Count = c; Proj = p; Pc = pc; }
        public void Add_To_Base(ref List<Classes> x, Classes r)
        {
            bool f = false;
            int n = 0;
            int c = 0;
            bool p = false;
            bool pc = false;
            do
            {
                try
                {
                    Console.Write("Введите номер кабинета трёхзначным числом: ");
                    n = int.Parse(Console.ReadLine());
                    if (n < 100 || n > 999) { Console.WriteLine("Ошибка формата данных. Попробуйте снова."); continue; }
                    Console.Write("Введите кол-во посадочных мест: ");
                    c = int.Parse(Console.ReadLine());
                    Console.Write("Введите 1 если присутствует проектор, 0 если нет: ");
                    p = Convert.ToBoolean(int.Parse(Console.ReadLine()));
                    Console.Write("Введите 1 если присутствует ПК, 0 если нет: ");
                    pc = Convert.ToBoolean(int.Parse(Console.ReadLine()));
                    Console.WriteLine();
                    f = true;
                }
                catch (FormatException e)
                {
                    Console.WriteLine("Ошибка формата данных. Попробуйте снова.");
                    f = false;
                }
                catch (Exception e)
                {
                    Console.WriteLine("Ошибка формата данных. Попробуйте снова.");
                    f = false;
                }
            } while (!f);
            Classes a = new Classes(n, c, p, pc);
            x.Add(a);
        }
        public void Create_Base(ref List<Classes> x, Classes r)
        {
            Console.Write("Количество элементов базы: ");
            int s = int.Parse(Console.ReadLine());
            x = new List<Classes>();
            for (int i = 0; i < s; i++)
            {
                r.Add_To_Base(ref x, r);
            }
        }
        public void Edit_Base(ref List<Classes> x, Classes r)
        {
            Console.Write("Номер кабинета, который необходимо изменить: ");
            int y = int.Parse(Console.ReadLine());
            for (int i = 0; i < x.Count; i++)
            {
                bool q = false;
                if (x[i].Num == y)
                {
                    q = true;
                    bool f = false;
                    do
                    {
                        try
                        {
                            Console.Write("Введите новый номер кабинета трёхзначным числом: ");
                            int n = int.Parse(Console.ReadLine());
                            if (n < 100 || n > 999) { Console.WriteLine("Ошибка формата данных. Попробуйте снова."); continue; }
                            x[i].Num = n;
                            Console.Write("Введите новое кол-во посадочных мест: ");
                            x[i].Count = int.Parse(Console.ReadLine());
                            Console.Write("Введите 1 если теперь присутствует проектор, 0 если нет: ");
                            x[i].Proj = Convert.ToBoolean(int.Parse(Console.ReadLine()));
                            Console.Write("Введите 1 если теперь присутствует ПК, 0 если нет: ");
                            x[i].Pc = Convert.ToBoolean(int.Parse(Console.ReadLine()));
                            Console.WriteLine();
                            f = true;
                        }
                        catch (FormatException e)
                        {
                            Console.WriteLine("Ошибка формата данных. Попробуйте снова.");
                            f = false;
                        }
                        catch (Exception e)
                        {
                            Console.WriteLine("Ошибка формата данных. Попробуйте снова.");
                            f = false;
                        }
                    } while (!f);
                }
                if (q == false) { Console.WriteLine("Не найдено таких кабинетов, возврат в меню."); }
            }
        }
        public void Selection_By_Count(List<Classes> x, Classes r)
        {
            Console.Write("Кол-во посадочных мест: ");
            int w = int.Parse(Console.ReadLine());
            foreach (Classes i in x)
            {
                if (i.Count == w)
                {
                    i.Info(i);
                }
            }
        }
        public void Selection_By_Proj(List<Classes> x, Classes r)
        {
            Console.Write("Наличие проектора (1 - есть, 0 - нет): ");
            bool o = Convert.ToBoolean(Console.ReadLine());
            foreach (Classes i in x)
            {
                if (o)
                {
                    i.Info(i);
                }
            }
        }
        public void Selection_By_Pc_Count(List<Classes> x, Classes r)
        {
            Console.Write("Наличие ПК (1 - есть, 0 - нет): ");
            bool o = Convert.ToBoolean(Console.ReadLine());
            Console.Write("Кол-во посадочных мест: ");
            int v = int.Parse(Console.ReadLine());
            foreach (Classes i in x)
            {
                if (o & i.Count == v)
                {
                    i.Info(i);
                }
            }
        }
        public void Selection_By_Floor(List<Classes> x, Classes r)
        {
            Console.Write("Этаж: ");
            Char v = Convert.ToChar(Console.ReadLine());
            foreach (Classes i in x)
            {
                if (Convert.ToString(i.Num)[0] == v)
                {
                    i.Info(i);
                }
            }
        }
        public void All_Base(ref List<Classes> x)
        {
            foreach (Classes c in x)
            {
                c.Info(c);
            }
        }
        public void Info(Classes c)
        {
            Console.WriteLine("---");
            Console.WriteLine($"Номер кабинета: {c.Num};");
            Console.WriteLine($"Кол-во посадочных мест: {c.Count};");
            if (c.Proj == true) { Console.WriteLine("В кабинете есть проектор;"); }
            else { Console.WriteLine("В кабинете нет проектора;"); }
            if (c.Pc == true) { Console.WriteLine("В кабинете есть компьютеры.;"); }
            else { Console.WriteLine("В кабинете нет компьютеров.;"); }
        }
    }
    internal class First
    {
        public static void Main()
        {
            bool u = true;
            Classes r = new Classes(0, 0, false, false);
            List<Classes> Cabinet = new List<Classes>();
            Menu menu = new Menu();
            while (u)
            {
                menu.Show_Menu(ref Cabinet, r, ref u);
            }
        }
    }
}
/* 2 класса: 1 - класс меню (создание базы, добавление элементов базы, модификация эл-в по номеру кабинета, выборка каб-в с кол-м посадочных мест >= заданному, выборка кабинетов с проектором, выборка кабинетов с компьютерами и кол-вом посадочных мест >= заданному, вывод всей информации базы, выборка кабнетов на одном этаже, выход);
 *           2 - класс кабинетов (номер, кол-во посадочных мест, наличие проектора, наличие ПК); предусмотреть после пункта меню возврат в основное, предусмотреть проверку данных (если база не заполненна, то выборки делать нельзя)*/