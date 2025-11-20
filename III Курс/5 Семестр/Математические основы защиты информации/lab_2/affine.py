from collections import Counter

class AffineCipherAnalyzer:
    def __init__(self, alphabet=None, common_chars=None):
        self.alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя" if not alphabet else alphabet
        self.common_chars = ['о', 'е', 'а', 'и', 'н', 'т', 'с', 'р', 'в', 'л'] if not common_chars else common_chars
        self.m = len(self.alphabet)
        self.char_to_code = {char: i for i, char in enumerate(self.alphabet)}
        self.code_to_char = {i: char for i, char in enumerate(self.alphabet)}

    def ext_euclid(self, a, m):
        """Вычисление обратного и НОД с помощью расширенного алгоритма Евклида"""
        t0, t1 = 0, 1
        r0, r1 = m, a
        
        while r1 != 0:
            quotient = r0 // r1
            t0, t1 = t1, t0 - quotient * t1
            r0, r1 = r1, r0 - quotient * r1

        inv = None if r0 != 1 else t0 % m
        return inv, r0

    def solve_linear_congruence(self, a, b, m):
        """Решение сравнения a*x ≡ b (mod m)"""
        solutions = []

        a_inv, g = self.ext_euclid(a, m)
        
        if b % g != 0:
            return solutions

        if g == 1:
            if a_inv is not None:
                x0 = (b * a_inv) % m
                solutions.append(x0)
            return solutions

        a1, b1, m1 = a // g, b // g, m // g
        a1_inv, _ = self.ext_euclid(a1, m1)
        
        if a1_inv is not None:
            x0 = (b1 * a1_inv) % m1
            for k in range(g):
                solutions.append(x0 + k * m1)
        
        return solutions

    def solve_system(self, a1, b1, a2, b2, m):
        """Решение системы (a*x + y) mod m = b1, (c*x + y) mod m = b2"""
        solutions = []

        a_diff = (a1 - a2) % m
        b_diff = (b1 - b2) % m

        x_solutions = self.solve_linear_congruence(a_diff, b_diff, m)
        
        for x in x_solutions:
            y = (b1 - a1 * x) % m
            solutions.append((x, y))
        
        return solutions

    def frequency_analysis(self, text):
        """Частотный анализ текста"""
        text = text.lower()
        filtered_text = ''.join(char for char in text if char in self.alphabet)
        
        counter = Counter(filtered_text)
        total_chars = len(filtered_text)
        
        frequencies = {}
        for char, count in counter.items():
            frequencies[char] = count / total_chars

        sorted_chars = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return sorted_chars, frequencies
    
    def decrypt(self, ciphertext, a, b):
        """Расшифрование текста с ключом (a, b)"""
        a_inv = self.ext_euclid(a, self.m)[0]
        if a_inv is None:
            return None
        
        plaintext = []
        for char in ciphertext.lower():
            if char in self.alphabet:
                y = self.char_to_code[char]
                x = (a_inv * (y - b)) % self.m
                plaintext.append(self.code_to_char[x])
            else:
                plaintext.append(char)
        
        return ''.join(plaintext)
    
    def encrypt(self, plaintext, a, b):
        """Шифрование текста с ключом (a, b)"""
        ciphertext = []
        for char in plaintext.lower():
            if char in self.alphabet:
                x = self.char_to_code[char]
                y = (a * x + b) % self.m
                ciphertext.append(self.code_to_char[y])
            else:
                ciphertext.append(char)
        
        return ''.join(ciphertext)
    
    def find_possible_keys(self, ciphertext, top_n=3):
        """Поиск возможных ключей на основе частотного анализа"""
        sorted_chars, _ = self.frequency_analysis(ciphertext)
        
        if len(sorted_chars) < 2:
            return []
        
        cipher_top = [char for char, _ in sorted_chars[:top_n]]
        possible_keys = []
        
        for i in range(min(top_n, len(cipher_top))):
            for j in range(i+1, min(top_n, len(cipher_top))):
                cipher_char1, cipher_char2 = cipher_top[i], cipher_top[j]
                
                for k in range(len(self.common_chars)-1):
                    for l in range(k+1, len(self.common_chars)):
                        plain_char1, plain_char2 = self.common_chars[k], self.common_chars[l]
                        
                        variants = [
                            (plain_char1, cipher_char1, plain_char2, cipher_char2),
                            (plain_char1, cipher_char2, plain_char2, cipher_char1)
                        ]
                        
                        for plain1, cipher1, plain2, cipher2 in variants:
                            x1, x2 = self.char_to_code[plain1], self.char_to_code[plain2]
                            y1, y2 = self.char_to_code[cipher1], self.char_to_code[cipher2]

                            keys = self.solve_system(x1, y1, x2, y2, self.m)
                            
                            for a, b in keys:
                                if self.ext_euclid(a, self.m)[1] == 1:
                                    possible_keys.append((a, b, f"{plain1}->{cipher1}, {plain2}->{cipher2}"))
        
        return possible_keys
    
    def interactive_analysis(self, ciphertext):
        """Интерактивный криптоанализ"""
        print("=== КРИПТОАНАЛИЗ АФФИННОГО ШИФРА ===")
        print(f"Шифртекст: {ciphertext}")
        
        sorted_chars, frequencies = self.frequency_analysis(ciphertext)
        print("\nТоп-10 самых частых букв в шифртексте:")
        for i, (char, count) in enumerate(sorted_chars[:10], 1):
            print(f"{i}. '{char}': {count} раз ({frequencies[char]:.3f})")
        
        print("\nПоиск возможных ключей...")
        possible_keys = self.find_possible_keys(ciphertext, top_n=3)
        
        if not possible_keys:
            print("Не удалось найти возможные ключи. Попробуйте увеличить top_n.")
            return
        
        print(f"\nНайдено {len(possible_keys)} возможных ключей:")
        
        for idx, (a, b, assumption) in enumerate(possible_keys, 1):
            decrypted = self.decrypt(ciphertext, a, b)
            if decrypted:
                print(f"\n--- Ключ {idx}: a={a}, b={b} ({assumption}) ---")
                print(f"Расшифрованный текст: {decrypted}")
                
                filename = f"result_key_{idx}.txt"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Ключ: a={a}, b={b}\n")
                    f.write(f"Предположение: {assumption}\n")
                    f.write(f"Расшифрованный текст:\n{decrypted}")
                print(f"Сохранено в файл: {filename}")
                
                response = input("Осмысленный текст? (y/n/quit): ").lower()
                if response == 'y':
                    print(f"Найден правильный ключ: a={a}, b={b}")
                    return (a, b)
                elif response == 'quit':
                    return None
        
        print("\nПравильный ключ не найден среди предложенных вариантов.")
        return None


def console_interface():
    """Консольный интерфейс для ручного течного тестирования функций"""
    analyzer = AffineCipherAnalyzer()
    
    while True:
        print("\n=== АФФИННЫЙ ШИФР - МЕНЮ ===")
        print("1. Вычисление обратного элемента")
        print("2. Решение сравнения a*x ≡ b (mod m)")
        print("3. Решение системы уравнений")
        print("4. Частотный анализ текста")
        print("5. Выдвижение предположений о соответствии букв")
        print("6. Расшифрование текста")
        print("7. Полный криптоанализ")
        print("0. Выход")
        
        choice = input("Выберите опцию: ")
        
        if choice == "1":
            a = int(input("Элемент a: "))
            m = int(input("Модуль m: "))
            result = analyzer.ext_euclid(a, m)
            print(f"Обратный элемент: {result[0]}")
            
        elif choice == "2":
            a = int(input("Коэффициент a: "))
            b = int(input("Коэффициент b: "))
            m = int(input("Модуль m: "))
            solutions = analyzer.solve_linear_congruence(a, b, m)
            print(f"Решения: {solutions}")
            
        elif choice == "3":
            a1 = int(input("a1: "))
            b1 = int(input("b1: "))
            a2 = int(input("a2: "))
            b2 = int(input("b2: "))
            m = int(input("Модуль m: "))
            solutions = analyzer.solve_system(a1, b1, a2, b2, m)
            for i, (x, y) in enumerate(solutions, 1):
                print(f"Решение {i}: x={x}, y={y}")
                
        elif choice == "4":
            filename = input("Введите название файла: ")
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    text = file.read()
                
                sorted_chars, frequencies = analyzer.frequency_analysis(text)
                print("Топ-10 частых букв:")
                for i, (char, count) in enumerate(sorted_chars[:10], 1):
                    print(f"{i}. '{char}': {count} раз ({frequencies[char]:.3f})")
                    
            except FileNotFoundError:
                print(f"Файл '{filename}' не найден.")
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")

        elif choice == "5":
            filename = input("Введите название файла с шифртекстом: ")
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    ciphertext = file.read()
                
                # Частотный анализ шифртекста
                sorted_chars, frequencies = analyzer.frequency_analysis(ciphertext)
                print("\nТоп-5 самых частых букв в шифртексте:")
                for i, (char, count) in enumerate(sorted_chars[:5], 1):
                    print(f"{i}. '{char}': {count} раз ({frequencies[char]:.3f})")
                
                if len(sorted_chars) >= 2:
                    # Берем две самые частые буквы шифртекста
                    cipher_top1, cipher_top2 = sorted_chars[0][0], sorted_chars[1][0]
                    print(f"\nДве самые частые буквы шифртекста: '{cipher_top1}' и '{cipher_top2}'")
                    
                    # Автоматически выдвигаем предположения на основе частот русского языка
                    print("\nАвтоматические предположения о соответствии букв:")
                    print("На основе частот русского языка:")
                    
                    # Берем различные комбинации частых букв русского языка
                    russian_pairs = [
                        ('о', 'е'), ('о', 'а'), ('о', 'и'), ('е', 'а'),
                        ('е', 'и'), ('а', 'и'), ('о', 'н'), ('е', 'н')
                    ]
                    
                    all_possible_keys = []
                    
                    for plain1, plain2 in russian_pairs:
                        # Два варианта соответствия для каждой пары
                        variants = [
                            (plain1, cipher_top1, plain2, cipher_top2),
                            (plain1, cipher_top2, plain2, cipher_top1)
                        ]
                        
                        for plain_char1, cipher_char1, plain_char2, cipher_char2 in variants:
                            x1, x2 = analyzer.char_to_code[plain_char1], analyzer.char_to_code[plain_char2]
                            y1, y2 = analyzer.char_to_code[cipher_char1], analyzer.char_to_code[cipher_char2]
                            
                            keys = analyzer.solve_system(x1, y1, x2, y2, analyzer.m)
                            
                            for a, b in keys:
                                if analyzer.ext_euclid(a, analyzer.m)[1] == 1:
                                    assumption = f"открытый '{plain_char1}' -> шифр '{cipher_char1}', открытый '{plain_char2}' -> шифр '{cipher_char2}'"
                                    key_info = (a, b, assumption)
                                    if key_info not in all_possible_keys:
                                        all_possible_keys.append(key_info)
                    
                    if all_possible_keys:
                        print(f"\nНайдено {len(all_possible_keys)} возможных ключей на основе частотного анализа:")
                        
                        for i, (a, b, assumption) in enumerate(all_possible_keys[:10], 1):  # Ограничиваем вывод первыми 10
                            print(f"\n--- Предположение {i} ---")
                            print(f"Соответствие: {assumption}")
                            print(f"Ключ: a={a}, b={b}")
                            
                            # Пробуем расшифровать
                            decrypted = analyzer.decrypt(ciphertext, a, b)
                            if decrypted:
                                print(f"Пример расшифровки: {decrypted[:80]}...")
                                
                                # Сохраняем результат
                                filename_out = f"auto_hypothesis_{i}.txt"
                                with open(filename_out, 'w', encoding='utf-8') as f:
                                    f.write(f"Автоматическое предположение {i}\n")
                                    f.write(f"Соответствие букв: {assumption}\n")
                                    f.write(f"Ключ шифрования: a={a}, b={b}\n")
                                    f.write(f"Расшифрованный текст:\n{decrypted}")
                                print(f"Сохранено в файл: {filename_out}")
                        
                        if len(all_possible_keys) > 10:
                            print(f"\n... и еще {len(all_possible_keys) - 10} предположений")
                            
                        print("\nВсе предположения сохранены в файлы auto_hypothesis_*.txt")
                    else:
                        print("Не удалось найти подходящие ключи для автоматических предположений.")
                        print("Возможно, нужно рассмотреть другие комбинации частых букв.")
                else:
                    print("Текст слишком короткий для анализа (нужно как минимум 2 различные буквы).")
                    
            except FileNotFoundError:
                print(f"Файл '{filename}' не найден.")
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")

        elif choice == "6":
            filename = input("Введите название файла с шифртекстом: ")
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    ciphertext = file.read()
                
                a = int(input("Ключ a: "))
                b = int(input("Ключ b: "))
                decrypted = analyzer.decrypt(ciphertext, a, b)
                print(f"Расшифрованный текст: {decrypted}")

                output_filename = f"decrypted_{filename}"
                with open(output_filename, 'w', encoding='utf-8') as f:
                    f.write(decrypted)
                print(f"Результат сохранен в файл: {output_filename}")
                
            except FileNotFoundError:
                print(f"Файл '{filename}' не найден.")
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")

        elif choice == "7":
            filename = input("Введите название файла с шифртекстом: ")
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    ciphertext = file.read()
                analyzer.interactive_analysis(ciphertext)
            except FileNotFoundError:
                print(f"Файл '{filename}' не найден.")
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")
                    
        elif choice == "0":
            break
            
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    console_interface()
