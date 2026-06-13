from analisys.funcs import *
import heapq

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


text = "я очень люблю алгоритмы, души в них не чаю"

hc = HuffmanCoding()

t1, encoded = measure_time(hc.encode, text)
t2, decoded = measure_time(hc.decode, encoded)

print("Исходный текст:", text)
print("Закодировано:", encoded)

print("\nСловарь кодов:")
for ch in sorted(hc.char2code, key=lambda x: len(hc.char2code[x])):
    print(repr(ch), "->", hc.char2code[ch])

print("\nДекодировано:", decoded)
print("\nВремя кодирования:", f"{t1:.6f} сек")
print("Время декодирования:", f"{t2:.6f} сек")

assert decoded == text
