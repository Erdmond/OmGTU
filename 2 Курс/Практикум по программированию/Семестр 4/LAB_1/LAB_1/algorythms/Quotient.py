import mmh3

class QuotientFilter:
    def __init__(self, size):
        self.size = size
        self.table = [{'occupied': False, 'continuation': False, 'shifted': False, 'remainder': None}
                      for _ in range(size)]
        self.r_bits = 8
        self.r_mask = (1 << self.r_bits) - 1

    def _hash(self, x):
        h = mmh3.hash(str(x), signed=False)
        q, r = divmod(h, 1 << self.r_bits)
        q = q % self.size
        return q, r

    def _increment(self, i):
        return (i + 1) % self.size

    def insert(self, x):
        q, r = self._hash(x)
        self.table[q]['occupied'] = True
        if self.table[q]['remainder'] is None:
            self.table[q]['remainder'] = r
            self.table[q]['shifted'] = False
            self.table[q]['continuation'] = False
            return
        pos = q
        while self.table[pos]['shifted']:
            pos = self._increment(pos)
            if pos == q:
                raise Exception("Фильтр заполнен")
        insert_pos = pos
        while True:
            if self.table[insert_pos]['remainder'] is None:
                break
            if r < self.table[insert_pos]['remainder']:
                break
            insert_pos = self._increment(insert_pos)
            if insert_pos == q:
                raise Exception("Фильтр заполнен")
        curr = insert_pos
        prev_entry = {'occupied': False, 'continuation': False, 'shifted': False, 'remainder': None}
        while True:
            self.table[curr], prev_entry = prev_entry, self.table[curr]
            if curr != q:
                self.table[curr]['shifted'] = True
            curr = self._increment(curr)
            if prev_entry['remainder'] is None:
                break

        self.table[insert_pos] = {'occupied': False,
                                  'continuation': (insert_pos != q),
                                  'shifted': (insert_pos != q),
                                  'remainder': r}

    def lookup(self, x):
        q, r = self._hash(x)
        if not self.table[q]['occupied']:
            return False
        pos = q
        while True:
            if self.table[pos]['remainder'] is None:
                return False
            if self.table[pos]['remainder'] == r:
                return True
            pos = self._increment(pos)
            if pos == q:
                return False
