import sys

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # 1. insert value
        self.heap.append(value)

        # 2. heapify: compare x with x // 2
        idx = len(self.heap) - 1
        while idx > 0:
            parent_idx = (idx-1) // 2
            if self.heap[parent_idx] > self.heap[idx]:
                self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
                idx = parent_idx
            else:
                break
    
    def pop(self):
        if len(self.heap) == 0:
            return 0
        else:
            # 1. swap first and last
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            # 2. remove last
            val = self.heap.pop()
            # 3. sort
            self.sort()
            return val
        
    def sort(self):
        _idx = 0

        while len(self.heap) > 0:
            _next = _idx
            for x in [2*_idx+1, 2*_idx+2]:
                if x < len(self.heap) and self.heap[x] < self.heap[_next]:
                    _next = x   

            if _next != _idx:
                self.heap[_idx], self.heap[_next] = self.heap[_next], self.heap[_idx]
                _idx = _next
            else:
                break


n = int(sys.stdin.readline())
mh = MinHeap()

ans = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        ans.append(mh.pop())
    else:
        mh.insert(x)

print('\n'.join([str(x) for x in ans]))