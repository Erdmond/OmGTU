import math
from itertools import combinations

class RSACryptoAnalyzer:
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
            raise ValueError("Обратный элемент не существует")
        return x % m

    def sieve_primes_up_to(self, limit):
        if limit < 2:
            return []
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if sieve[i]:
                step = i
                start = i * i
                sieve[start:limit+1:step] = [False] * (((limit - start) // step) + 1)
        return [i for i, is_prime in enumerate(sieve) if is_prime]

    def generate_prime_products(self, n):
        sqrt_n = int(math.isqrt(n))
        primes = self.sieve_primes_up_to(sqrt_n)
        prime_products = []
        for i in range(len(primes) - 2):
            prod = primes[i] * primes[i+1] * primes[i+2]
            if prod <= sqrt_n:
                prime_products.append((primes[i], primes[i+1], primes[i+2]))
        for p in primes:
            prime_products.append((p,))
        return prime_products

    def _factorize_small_number(self, n):
        factors = []
        temp = n
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                factors.append(d)
                temp //= d
            d += 1 if d == 2 else 2
        if temp > 1:
            factors.append(temp)
        return factors

    def advanced_trial_division(self, n):
        print(f"Пробные деления числа {n}...")
        factors = []
        temp_n = n

        while temp_n % 2 == 0:
            print("Найден множитель 2")
            factors.append(2)
            temp_n //= 2
        while temp_n % 3 == 0:
            print("Найден множитель 3")
            factors.append(3)
            temp_n //= 3

        if temp_n == 1:
            return factors

        prime_products = self.generate_prime_products(temp_n)

        for product in prime_products:
            product_value = math.prod(product)
            g = math.gcd(temp_n, product_value)
            if 1 < g < temp_n:
                print(f"НОД({temp_n}, {product_value}) = {g}")
                gcd_factors = self._factorize_small_number(g)
                for f in gcd_factors:
                    print(f"Найден множитель {f}")
                factors.extend(gcd_factors)

                while temp_n % g == 0:
                    temp_n //= g
                while temp_n % 2 == 0:
                    print("Найден множитель 2")
                    factors.append(2)
                    temp_n //= 2
                while temp_n % 3 == 0:
                    print("Найден множитель 3")
                    factors.append(3)
                    temp_n //= 3

                if temp_n == 1:
                    break

        if temp_n > 1:
            print(f"Добиваем остаток {temp_n} обычным делением")
            small_factors = self._factorize_small_number(temp_n)
            for f in small_factors:
                print(f"Найден множитель {f}")
            factors.extend(small_factors)

        factors.sort()
        print(f"Все найденные множители: {factors}")
        return factors

    def trial_division_factorization(self, n):
        print("Начало факторизации методом пробных делений...")
        all_factors = self.advanced_trial_division(n)

        if not all_factors:
            raise ValueError("Не удалось разложить число на множители")

        prod = 1
        for f in all_factors:
            prod *= f
        if prod != n:
            raise ValueError("Найденные множители не дают исходное число")

        if len(all_factors) == 2:
            p, q = all_factors
            print(f"Факторизация завершена: p={p}, q={q}")
            return p, q

        print("Найдено более двух множителей, перебор комбинаций...")
        m = len(all_factors)
        for r in range(1, m + 1):
            for comb in combinations(range(m), r):
                p = 1
                for idx in comb:
                    p *= all_factors[idx]
                q = n // p
                if p * q == n:
                    p, q = min(p, q), max(p, q)
                    print(f"Подобраны p={p}, q={q}")
                    return p, q

        raise ValueError("Не удалось выделить два сомножителя p и q")

    def euler_phi(self, p, q):
        return (p - 1) * (q - 1)

    def binary_exponentiation(self, a, d, n):
        result = 1
        base = a % n
        while d > 0:
            if d & 1:
                result = (result * base) % n
            base = (base * base) % n
            d >>= 1
        return result

    def blocks_to_numbers(self, blocks):
        numbers = []
        for block in blocks:
            temp = block
            block_numbers = []
            while temp > 0:
                block_numbers.insert(0, temp % 100)
                temp //= 100
            clean = []
            for num in block_numbers:
                if num != 0 or (clean and num >= 10):
                    clean.append(num)
            numbers.extend(clean)
        while numbers and numbers[0] == 0:
            numbers.pop(0)
        return numbers

    def numbers_to_text(self, numbers):
        return ''.join([self.code_to_char.get(num, '*') for num in numbers])

    def crack_rsa(self, e, n, ciphertext):
        print("=== НАЧАЛО КРИПТОАНАЛИЗА RSA ===")
        print(f"Открытый ключ: e={e}, n={n}")
        print(f"Шифртекст: {ciphertext}\n")

        try:
            p, q = self.trial_division_factorization(n)
        except ValueError as ve:
            print(f"Ошибка факторизации: {ve}")
            return None, None, None, None

        print(f"p = {p}, q = {q}")
        phi_n = self.euler_phi(p, q)
        print(f"φ(n) = {phi_n}")

        try:
            d = self.modular_inverse(e, phi_n)
        except ValueError:
            print("Ошибка: обратный элемент для e по модулю φ(n) не существует")
            return p, q, None, None

        print(f"Закрытый ключ d = {d}")
        ciphertext_list = ciphertext if isinstance(ciphertext, list) else [ciphertext]
        decrypted_blocks = [self.binary_exponentiation(block, d, n) for block in ciphertext_list]
        print(f"Дешифрованные блоки: {decrypted_blocks}")

        numbers = self.blocks_to_numbers(decrypted_blocks)
        print(f"Коды символов: {numbers}")

        plaintext = self.numbers_to_text(numbers)
        print(f"Расшифрованный текст: '{plaintext}'")

        return p, q, d, plaintext


def main():
    analyzer = RSACryptoAnalyzer()
    e = 251 # input("Введите e: ")
    n = 44923 # input("Введите N: ")
    raw = input("Введите шифртекст или путь к файлу: ")
    if '.' in raw and not raw.replace('.', '', 1).isdigit():
        with open(raw, mode='r', encoding='utf-8') as file:
            C = list(map(int, file.read().split()))
    else:
        C = list(map(int, raw.split()))
    p, q, d, plaintext = analyzer.crack_rsa(e, n, C)
    if p is not None:
        print("\n=== РЕЗУЛЬТАТЫ ===")
        print(f"p={p}, q={q}, d={d}")
        print(f"Расшифровка: {plaintext}")

if __name__ == "__main__":
    main()
