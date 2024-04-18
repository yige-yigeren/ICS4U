class Quadratic:
    def __init__(self, A=1, B=1, C=1):
        self.A = A
        self.B = B
        self.C = C
        if A == 0:
            print('Invalid input: A cannot be 0')
            exit(1)
        # calculate the vertex form
        self.a = A
        self.h = -B / (2 * A)
        self.k = C - A * self.h ** 2

    def Display(self, form='standard'):
        if form == 'standard':
            print(f'{self.A}x^2 + {self.B}x + {self.C}')
        elif form == 'vertex':
            print(f'{self.a}(x - {self.h})^2 + {self.k}')
    
    def Diraction(self):
        if self.A > 0:
            return 'Up'
        else:
            return 'Down'
    
    def Vertex(self):
        return (self.h, self.k)
    
    def Xintercept(self):
        if self.B ** 2 - 4 * self.A * self.C < 0:
            return []
        elif self.B ** 2 - 4 * self.A * self.C == 0:
            x = -self.B / (2 * self.A)
            return [x]
        else:
            x1 = (-self.B + (self.B ** 2 - 4 * self.A * self.C) ** 0.5) / (2 * self.A)
            x2 = (-self.B - (self.B ** 2 - 4 * self.A * self.C) ** 0.5) / (2 * self.A)
            return [x1, x2]
    
    def Yintercept(self):
        return self.C
    
    def add(self, other):
        if isinstance(other, Quadratic):
            new_A = self.A + other.A
            new_B = self.B + other.B
            new_C = self.C + other.C
            return Quadratic(new_A, new_B, new_C)
        else:
            print("The input is not a Quadratic object.")
            return None
        
a = Quadratic(1, 2, 1)
a.Display('standard')
a.Display('vertex')
print(a.Diraction())
print(a.Vertex())
print(a.Xintercept())
print(a.Yintercept())
b = Quadratic(1, 4, 4)
b.Display('standard')
b.Display('vertex')
print(b.Diraction())
print(b.Vertex())
print(b.Xintercept())
print(b.Yintercept())
c = a.add(b)
c.Display('standard')
c.Display('vertex')
print(c.Diraction())
print(c.Vertex())
print(c.Xintercept())
print(c.Yintercept())