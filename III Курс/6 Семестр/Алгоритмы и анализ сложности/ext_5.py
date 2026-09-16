import heapq

def kmp(text, pattern):
    n, m = len(text), len(pattern)

    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and text[i] != pattern[j]:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self):
        self.char2code = {}
        self.code2char = {}
        self.root = None

    def encode(self, text):
        self.char2code.clear()
        self.code2char.clear()

        freq = self._freq_dict(text)
        self.root = self._build_tree(freq)
        self._build_codes(self.root)

        return "".join(self.char2code[c] for c in text)

    def decode(self, encoded):
        result = []
        node = self.root

        for bit in encoded:
            node = node.left if bit == "0" else node.right
            if node.char is not None:
                result.append(node.char)
                node = self.root

        return "".join(result)

    def _freq_dict(self, text):
        freq = {}
        for c in text:
            freq[c] = freq.get(c, 0) + 1
        return freq

    def _build_tree(self, freq):
        heap = []
        for char in freq:
            heapq.heappush(heap, Node(char, freq[char]))

        if len(heap) == 1:
            only = heapq.heappop(heap)
            root = Node(None, only.freq)
            root.left = only
            return root

        while len(heap) > 1:
            n1 = heapq.heappop(heap)
            n2 = heapq.heappop(heap)

            merged = Node(None, n1.freq + n2.freq)
            merged.left = n1
            merged.right = n2

            heapq.heappush(heap, merged)

        return heap[0]

    def _build_codes(self, root):
        stack = [(root, "")]

        while stack:
            node, code = stack.pop()

            if node.char is not None:
                self.char2code[node.char] = code or "0"
                self.code2char[code or "0"] = node.char

            if node.right:
                stack.append((node.right, code + "1"))
            if node.left:
                stack.append((node.left, code + "0"))


if __name__=='__main__':
    text_kmp = "dfgyc@dfgmmbdfvdfgycdfgycdfgvc"
    pattern_kmp = "dfgyc"

    print(f"Результат Кнута-Морриса-Пратта: {kmp(text_kmp, pattern_kmp)}")

    hc = HuffmanCoding()

    text_huffman = "Чтобы расшифровать закодированную строку необходимо идти по дереву, сворачивая в соответствующую каждому биту сторону до тех пор, пока не будет достигнут лист. Например, если есть строка «101 11 101 11» и дерево, получается строка «pepe». На практике, при реализации данного алгоритма сразу после построения дерева строится таблица Хаффмана. Данная таблица — это связный список или массив, который содержит каждый символ и его код, так как это делает кодирование более эффективным. Как правило, для кодирования используется таблица Хаффмана, а для декодирования — дерево Хаффмана."
    encoded = hc.encode(text_huffman)

    print("Исходный текст:", text_huffman)
    print("Закодировано:", encoded)

    print("\nСловарь кодов:")
    for ch in sorted(hc.char2code, key=lambda x: len(hc.char2code[x])):
        print(repr(ch), "->", hc.char2code[ch])

    print("\nДекодировано:", hc.decode(encoded))
