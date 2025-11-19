import string # вспомогательная библиотека для работы со строками
import os

ALPHABET = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# функция форматирования текста
def M(text):
    return text.translate(str.maketrans('', '', string.punctuation + ' ')).lower().replace('ё', 'е')

# функция кодирования букв в числа
def A(M):
    return [ALPHABET.find(letter) if letter in ALPHABET else letter for letter in M]

# функция шифрования символа
def E(x, k):
    return (x + k) % len(ALPHABET)

# функция дешифрования символа
def D(x, k):
    return (x - k) % len(ALPHABET)

# функция декодирования чисел в буквы
def A_1(Y):
    return ''.join([ALPHABET[num] if isinstance(num, int) else num for num in Y])

# функция-конвеер для шифровки
def encode(text, key):
    formatted_text = M(text)
    numeric_text = A(formatted_text)
    encoded_numeric_text = [E(letter, key) if isinstance(letter, int) else letter for letter in numeric_text]
    encoded_text = A_1(encoded_numeric_text)

    return encoded_text

# функция-конвеер для дешифровки
def decode(text, key):
    numeric_text = A(text)
    decoded_numeric_text = [D(letter, key) if isinstance(letter, int) else letter for letter in numeric_text]
    decoded_text = A_1(decoded_numeric_text)

    return decoded_text

# вывод меню
def menu():
    print('  Меню:')
    print('1. Шифрование с произвольным ключом')
    print('2. Расшифровка с произвольным ключом')
    print('3. Расшифровка с перебором ключей')
    print('4. Выход\n')
    return input('  Ваш выбор: ')


if __name__ == '__main__':
    while True:
        os.system('cls')

        match menu():
            case '1': # шифровка с известным ключом
                os.system('cls')

                text = input('  Введите открытый текст:\n')
                key = input('  Введите ключ:\n')

                if not key.isdigit():
                    print('Ключ должен быть числом!')
                    break
                
                key = int(key)

                if key // len(ALPHABET) > 0:
                    print(f'Ваш ключ {key}, но уникальных ключей для алфавита всего {len(ALPHABET) - 1}.\nВаш ключ соответствует шифровке с ключом {key % len(ALPHABET)}')

                result = encode(text, key)

                print('\n  Зашифрованный текст:')
                print(result)

                with open('Зашифрованный текст.txt', 'w', encoding='utf-8') as file:
                    file.write(f'Ключ: {str(key)}\n')
                    file.write(f'Текст: {result}')
                print('\n  Зашифрованный текст сохранён в Зашифрованный текст.txt')
                
                input('\nEnter для продолжения...')

            case '2': # дешифровка с известным ключом
                os.system('cls')

                text = input('  Введите закрытый текст:\n')
                key = input('  Введите ключ:\n')

                if not key.isdigit():
                    print('Ключ должен быть числом!')
                    break

                key = int(key)

                if key // len(ALPHABET) > 0:
                    print(f'Ваш ключ {key}, но уникальных ключей для алфавита всего {len(ALPHABET) - 1}.\nВаш ключ соответствует дешифровке с ключом {key % len(ALPHABET)}')

                key = int(key)

                result = decode(text, key)

                print('\n  Расшифрованный текст:')
                print(result)

                with open('Расшифрованный текст.txt', 'w', encoding='utf-8') as file:
                    file.write(f'Ключ: {str(key)}\n')
                    file.write(f'Текст: {result}')
                print('\n  Расшифрованный текст сохранён в Расшифрованный текст.txt')
                
                input('\nEnter для продолжения...')

            case '3': # дешифровка с неизвестным ключом
                os.system('cls')

                text = input('  Введите закрытый текст:\n')

                for key in range(len(ALPHABET) - 1):
                    result = decode(text, key)

                    print(f'Ключ: {key}')

                    print('\n  Расшифрованный текст:')
                    print(result)

                    choice = input('\n1. Продолжить перебор\n2. Заверишть перебор\n  Ваш выбор:')
                
                    if choice == '2':
                        with open('Расшифрованный текст.txt', 'w', encoding='utf-8') as file:
                            file.write(f'Ключ: {str(key)}\n')
                            file.write(f'Текст: {result}')
                        print('\n  Расшифрованный текст сохранён в Расшифрованный текст.txt')

                        break
                    elif choice == '1':
                        continue
                    else:
                        print('Введена неизвестная команда, перебор будет продолжен.')

                input('\nEnter для продолжения...')

            case '4':
                quit()

            case _:
                print('Ошибочный ввод!')
