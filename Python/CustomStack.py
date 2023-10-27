class CustomStack:
    def __init__(self, maxSize):
        self.st = []
        self.max = maxSize

    def push(self, x):
        if len(self.st) != self.max:
            self.st.append(x)

    def pop(self):
        if not self.st:
            return -1
        return self.st.pop()

    def increment(self, k, val):
        temp = []
        while self.st:
            temp.append(self.st.pop())
        
        for i in range(k):
            if not temp:
                break
            self.st.append(temp.pop() + val)
        
        while temp:
            self.st.append(temp.pop())
