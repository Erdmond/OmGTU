#include <stdio.h>
#include <Windows.h>
#include <string.h>

int main()
{
    // оглашение хэндла консольного ввода
    HANDLE input = GetStdHandle(STD_INPUT_HANDLE);
    // оглашение хэндла консольного вывода
    HANDLE output = GetStdHandle(STD_OUTPUT_HANDLE);
    // оглашение хэндла файла
    HANDLE file = CreateFile("file.txt", GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    // oглашение длинны введённых данных
    DWORD lenght;
    // оглашение буфера для хранения вводимых значений
    char buffer[255];

    // вывод хэндлов ввода и вывода
    printf("Input handle - %d, output handle - %d\n\n", input, output);
    // вывод уведомления о вводе
    WriteFile(output, "Input text: ", strlen("Input text: "), NULL, NULL);
    // ввод данных в буфер
    ReadFile(input, buffer, 255, &lenght, NULL);
    // вывод значений в буфере
    WriteFile(output, buffer, lenght, NULL, NULL);
    // ожидание ввода для завершения программы
    getchar();
    return 0;
}

// lab1_w.exe < input.txt > output.txt