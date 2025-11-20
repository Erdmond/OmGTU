import random

class RSACrypto:
    def __init__(self):
        self.char_to_code = {
            'А': 10, 'Б': 11, 'В': 12, 'Г': 13, 'Д': 14, 'Е': 15, 'Ж': 16, 'З': 17,
            'И': 18, 'Й': 19, 'К': 20, 'Л': 21, 'М': 22, 'Н': 23, 'О': 24, 'П': 25,
            'Р': 26, 'С': 27, 'Т': 28, 'У': 29, 'Ф': 30, 'Х': 31, 'Ц': 32, 'Ч': 33,
            'Ш': 34, 'Щ': 35, 'Ъ': 36, 'Ы': 37, 'Ь': 38, 'Э': 39, 'Ю': 40, 'Я': 41, ' ': 99
        }
        self.code_to_char = {v: k for k, v in self.char_to_code.items()}
        
    def integer_square_root(self, m):
        x = m
        while True:
            y = (x + m // x) // 2
            if y < x:
                x = y
            else:
                return x
    
    def binary_exponentiation(self, a, d, n=None):
        result = 1
        base = a
        
        if n is not None:
            base = base % n
            while d > 0:
                if d % 2 == 1:
                    result = (result * base) % n
                base = (base * base) % n
                d = d // 2
        else:
            while d > 0:
                if d % 2 == 1:
                    result = result * base
                base = base * base
                d = d // 2
        
        return result
    
    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        
        gcd, x1, y1 = self.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        
        return gcd, x, y
    
    def modular_inverse(self, a, m):
        gcd, x, y = self.extended_gcd(a, m)
        if gcd != 1:
            raise ValueError(f"Обратный элемент не существует для a={a}, m={m}")
        return x % m
    
    def text_to_numbers(self, text):
        text = text.upper().replace('Ё', 'Е')
        numbers = [self.char_to_code[char] for char in text if char in self.char_to_code]
        return numbers
    
    def numbers_to_text(self, numbers):
        text = ''.join([self.code_to_char[num] if num in self.code_to_char else '*' for num in numbers])
        return text
    
    def split_into_blocks(self, numbers, n):
        blocks = []
        current_value = 0
        
        for num in numbers:
            num_digits = len(str(num))
            multiplier = 10 ** num_digits
            
            new_value = current_value * multiplier + num
            
            if new_value < n:
                current_value = new_value
            else:
                if current_value > 0:
                    blocks.append(current_value)
                current_value = num
        
        if current_value > 0:
            blocks.append(current_value)
        
        return blocks
    
    def blocks_to_numbers(self, blocks):
        numbers = []
        for block in blocks:
            temp = block
            block_numbers = []

            while temp > 0:
                block_numbers.insert(0, temp % 100)
                temp = temp // 100

            clean_numbers = []
            for num in block_numbers:
                if num != 0 or (clean_numbers and num >= 10):
                    clean_numbers.append(num)
            
            numbers.extend(clean_numbers)

        while numbers and numbers[0] == 0:
            numbers.pop(0)

        return numbers
    
    def is_coprime(self, a, b):
        return self.extended_gcd(a, b)[0] == 1
    
    def generate_random_e(self, phi, max_attempts=1000):
        attempts = 0
        while attempts < max_attempts:
            min_e = phi // 2 + 1
            max_e = phi - 1
            
            if min_e >= max_e:
                min_e = 3
                
            e = random.randint(min_e, max_e)
            
            if self.is_coprime(e, phi):
                return e
            attempts += 1
        
        raise ValueError(f"Не удалось найти подходящее e после {max_attempts} попыток")
    
    def generate_key_pairs(self, p, q, num_pairs=3):
        n = p * q
        phi = (p - 1) * (q - 1)
        
        key_pairs = []
        used_e_values = set()

        for _ in range(num_pairs):
            e = self.generate_random_e(phi)
            while e in used_e_values:
                e = self.generate_random_e(phi)
            
            used_e_values.add(e)
            d = self.modular_inverse(e, phi)

            if e != d:
                key_pairs.append((e, d, n))
        
        return key_pairs
    
    def generate_key_by_e(self, p, q, e):
        n = p * q
        phi = (p - 1) * (q - 1)

        if e <= 1 or e >= phi:
            raise ValueError(f"e должно быть в диапазоне 1 < e < φ(n) = {phi}")
        
        d = self.modular_inverse(e, phi)
        return (e, d, n)
    
    def encrypt_rsa(self, message, e, n):
        numbers = self.text_to_numbers(message)
        print(f"Текст как числа: {numbers}")

        blocks = self.split_into_blocks(numbers, n)
        print(f"Блоки для шифрования: {blocks}")

        encrypted_blocks = []
        for block in blocks:
            encrypted_block = self.binary_exponentiation(block, e, n)
            encrypted_blocks.append(encrypted_block)
        
        return encrypted_blocks
    
    def decrypt_rsa(self, encrypted_blocks, d, n):
        decrypted_blocks = []
        for block in encrypted_blocks:
            decrypted_block = self.binary_exponentiation(block, d, n)
            decrypted_blocks.append(decrypted_block)
        
        print(f"Расшифрованные блоки: {decrypted_blocks}")

        numbers = self.blocks_to_numbers(decrypted_blocks)
        text = self.numbers_to_text(numbers)
        
        return text

def main():
    rsa = RSACrypto()

    p, q = 139, 277
    # p, q = map(int, input('Через пробел введите p и q: ').split())

    n = p * q
    phi = (p - 1) * (q - 1)
    
    print(f"Параметры RSA:")
    print(f"p = {p}, q = {q}")
    print(f"n = p * q = {n}")
    print(f"φ(n) = (p-1)*(q-1) = {phi}")
    print()

    print("РЕЖИМЫ ГЕНЕРАЦИИ КЛЮЧЕЙ:")
    print("1 - Автоматическая генерация нескольких пар (случайные большие e)")
    print("2 - Генерация по заданному e")
    
    mode = input("Выберите режим (1/2): ")
    print()
    
    key_pairs = []
    
    if mode == '1':
        pairs = int(input('Введите количество пар ключей: '))
        
        print("ГЕНЕРАЦИЯ ПАР КЛЮЧЕЙ...")
        key_pairs = rsa.generate_key_pairs(p, q, num_pairs=pairs)
        
        if not key_pairs:
            print("Не удалось сгенерировать ни одной пары ключей!")
            return
            
        print(f"Успешно сгенерировано {len(key_pairs)} пар ключей:")
        for i, (e, d, n) in enumerate(key_pairs, 1):
            print(f"Пара ключей #{i}:")
            print(f"  Открытый ключ (e, n): ({e}, {n})")
            print(f"  Закрытый ключ (d, n): ({d}, {n})")
            print(f"  Размер e: {len(str(e))} цифр")
            print(f"  Проверка: e * d mod φ(n) = {e * d % phi}")
            print()
            
    elif mode == '2':
        try:
            e_input = int(input('Введите желаемое значение e: '))
            e, d, n = rsa.generate_key_by_e(p, q, e_input)
            key_pairs = [(e, d, n)]
            
            print("СГЕНЕРИРОВАНА ПАРА КЛЮЧЕЙ:")
            print(f"Открытый ключ (e, n): ({e}, {n})")
            print(f"Закрытый ключ (d, n): ({d}, {n})")
            print(f"Размер e: {len(str(e))} цифр")
            print(f"Проверка: e * d mod φ(n) = {e * d % phi}")
            print()
            
        except ValueError as ve:
            print(f"ОШИБКА: {ve}")
            print(f"Рекомендации:")
            print(f"- e должно быть в диапазоне 1 < e < {phi}")
            print(f"- e должно быть взаимно просто с {phi}")
            print(f"- Попробуйте простое число или число без общих делителей с {phi}")
            return

    if input('Для чтения из файла введите 1, 0 для ручного ввода: ') == '1':
        name = input('Введите название файла: ')
        with open(f'MFoIS/lab_4/{name}.txt', 'r', encoding='utf-8') as file:
            test_message = file.read()
    else:
        test_message = input('Введите строку для шифрования: ')
    
    print("ПРОЦЕСС ШИФРОВАНИЯ:")
    if len(key_pairs) > 1:
        print("Доступные пары ключей:")
        for i, (e, d, n) in enumerate(key_pairs, 1):
            print(f"{i}: e = {e} (размер: {len(str(e))} цифр)")
        key = int(input('Выберите пару ключей: '))
    else:
        key = 1
    
    e, d, n = key_pairs[key - 1]
    encrypted_blocks = rsa.encrypt_rsa(test_message, e, n)
    print(f"Зашифрованные блоки: {encrypted_blocks}")
    with open(f'MFoIS/lab_4/encoded_blocks.txt', 'w', encoding='utf-8') as file:
        file.write(', '.join([str(block) for block in encrypted_blocks]))
    print()
    
    print("ПРОЦЕСС РАСШИФРОВАНИЯ:")
    if len(key_pairs) > 1:
        print("Доступные пары ключей:")
        for i, (e, d, n) in enumerate(key_pairs, 1):
            print(f"{i}: e = {e} (размер: {len(str(e))} цифр)")
        key = int(input('Выберите пару ключей: '))
    else:
        key = 1
    
    e, d, n = key_pairs[key - 1]
    decrypted_message = rsa.decrypt_rsa(encrypted_blocks, d, n)
    print(f"Расшифрованное сообщение: '{decrypted_message}'")
    with open(f'MFoIS/lab_4/decoded_text.txt', 'w', encoding='utf-8') as file:
        file.write(decrypted_message)
    print()

if __name__ == "__main__":
    main()