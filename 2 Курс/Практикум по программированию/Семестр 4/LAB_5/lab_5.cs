using Python.Runtime;

namespace MLIntegration
{
    class Program
    {
        static void Main(string[] args)
        {
            Environment.SetEnvironmentVariable("PYTHONNET_PYDLL", @"C:\Users\izgor\AppData\Local\Programs\Python\Python311\python311.dll");

            PythonEngine.Initialize();

            while (true)
            {
                Console.Clear();
                PrintMenu();

                var choice = GetUserChoice();
                if (choice == 7) break;

                var strategy = GetStrategyParams(choice);
                if (strategy == null) continue;

                var predictions = ExecutePythonScript(strategy);
                ProcessResult(strategy.ScriptName, predictions);

                Console.WriteLine("\nНажмите любую клавишу для продолжения...");
                Console.ReadKey();
            }

            PythonEngine.Shutdown();
            Console.WriteLine("Программа завершена.");
        }

        static void PrintMenu()
        {
            Console.WriteLine("Выберите алгоритм классификации:");
            Console.WriteLine("1. CART с генетическим алгоритмом");
            Console.WriteLine("2. CART с алгоритмом роя частиц");
            Console.WriteLine("3. Logit с генетическим алгоритмом");
            Console.WriteLine("4. Logit с алгоритмом роя частиц");
            Console.WriteLine("5. Нейросеть с применением NEAT");
            Console.WriteLine("6. Нейросеть с применением SE-HyperNEAT");
            Console.WriteLine("7. Выход\n");
        }

        static int GetUserChoice()
        {
            Console.Write("Введите номер (1-7): ");
            return int.TryParse(Console.ReadLine(), out int choice) ? choice : 0;
        }

        class StrategyParams
        {
            public string ScriptName { get; }
            public string DataPath { get; }

            public StrategyParams(string script, string data)
            {
                ScriptName = script;
                DataPath = data;
            }
        }

        static StrategyParams GetStrategyParams(int choice)
        {
            return choice switch
            {
                1 => new StrategyParams("strat_1_cart_ga", @"D:\Python\OmGTU\Practicum\LAB_3\x_test_b.csv"),
                2 => new StrategyParams("strat_2_cart_sw", @"D:\Python\OmGTU\Practicum\LAB_3\x_test_b.csv"),
                3 => new StrategyParams("strat_3_logit_ga", @"D:\Python\OmGTU\Practicum\LAB_3\x_test_b.csv"),
                4 => new StrategyParams("strat_4_logit_sw", @"D:\Python\OmGTU\Practicum\LAB_3\x_test_b.csv"),
                5 => new StrategyParams("strat_5_neat", @"D:\Python\OmGTU\Practicum\LAB_3\big_data.csv"),
                6 => new StrategyParams("strat_6_se_neat", @"D:\Python\OmGTU\Practicum\LAB_3\big_data.csv"),
                _ => null
            };
        }

        static int[] ExecutePythonScript(StrategyParams strategy)
        {
            try
            {
                using (Py.GIL())
                {
                    dynamic sys = Py.Import("sys");
                    sys.path.append(@"D:\Python\OmGTU\Practicum\LAB_5\");

                    dynamic script = Py.Import(strategy.ScriptName);
                    dynamic result = script.main(strategy.DataPath);

                    return (result as PyObject)?.As<int[]>();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Ошибка выполнения: {ex.Message}");
                return null;
            }
        }

        static void ProcessResult(string scriptName, int[] predictions)
        {
            Console.WriteLine($"\nРезультаты {scriptName}:");

            if (predictions == null || predictions.Length == 0)
            {
                Console.WriteLine("Нет данных предсказаний");
                return;
            }

            Console.WriteLine($"Первые 10 предсказаний: [{string.Join(", ", predictions[..Math.Min(10, predictions.Length)])}]");
            Console.WriteLine($"Всего предсказаний: {predictions.Length}");
        }
    }
}
