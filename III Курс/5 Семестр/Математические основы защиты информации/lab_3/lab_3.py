import math
import re
from collections import Counter
import matplotlib.pyplot as plt

class TextAnalyzer:
    def __init__(self):
        self.alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'[^а-яё]', '', text)
        return text
    
    def calculate_k_grams(self, text, k):
        k_grams = []
        for i in range(len(text) - k + 1):
            k_gram = text[i:i + k]
            k_grams.append(k_gram)
        return k_grams
    
    def calculate_entropy(self, text, k):
        if len(text) < k:
            return 0

        k_grams = self.calculate_k_grams(text, k)

        k_gram_counts = Counter(k_grams)
        total_k_grams = len(k_grams)

        entropy = 0
        for count in k_gram_counts.values():
            probability = count / total_k_grams
            entropy -= probability * math.log2(probability)
        
        return entropy
    
    def analyze_text(self, text):
        processed_text = self.preprocess_text(text)
        
        results = {}

        for k in range(1, 6):
            entropy = self.calculate_entropy(processed_text, k)
            normalized_entropy = entropy / k
            
            results[k] = {
                'H_k': entropy,
                'H_k/k': normalized_entropy
            }
        
        return results
    
    def plot_results(self, results):
        k_values = list(results.keys())
        h_k_over_k = [results[k]['H_k/k'] for k in k_values]
        
        plt.figure(figsize=(10, 6))
        plt.plot(k_values, h_k_over_k, 'bo-', linewidth=2, markersize=8)
        plt.xlabel('k (размер k-граммы)')
        plt.ylabel('H_k(T)/k')
        plt.title('Зависимость нормированной энтропии от размера k-граммы')
        plt.grid(True, alpha=0.3)

        for k, value in zip(k_values, h_k_over_k):
            plt.annotate(f'{value:.3f}', (k, value), textcoords="offset points", 
                        xytext=(0,10), ha='center')
        
        plt.xticks(k_values)
        plt.tight_layout()
        plt.show()

def main():
    analyzer = TextAnalyzer()

    with open(f'MFoIS/lab_3/{input('Введите название файла с текстом для анализа: ')}.txt', 'r', encoding='utf-8') as file:
        try:
            text = file.read()
        except Exception():
            print('Ошибка!')

    results = analyzer.analyze_text(text)
    
    with open(f'MFoIS/lab_3/out.txt', 'w', encoding='utf-8') as file:
        print("Энтропия для первых 5-ти k-грамм открытого текста:")
        print("|  k  |   H_k    |   H_k/k    |")

        file.writelines(["|  k  |   H_k    |   H_k/k    |", "\n"])
        for k in range(1, 6):
            h_k = results[k]['H_k']
            h_k_over_k = results[k]['H_k/k']
            print(f"|  {k}  |  {h_k:.4f}  |   {h_k_over_k:.4f}   |")
            file.writelines([f"|  {k}  |  {h_k:.4f}  |   {h_k_over_k:.4f}   |", "\n"])

        print("\nПОСТРОЕНИЕ ГРАФИКА...")
        analyzer.plot_results(results)

if __name__ == "__main__":
    main()