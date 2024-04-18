import random
class Fraction:
    # define the constructor
    def __init__(self, numerator=1, denominator=1):
        if denominator == 0:
            print('Invalid input: denominator cannot be 0')
            exit(1)
        elif denominator//1 != denominator or numerator//1 != numerator:
            print('Invalid input: numerator and denominator must be integers')
            exit(1)
        self.numerator = numerator
        self.denominator = denominator
    
    # reduce the fraction
    def reduce(self):
        for i in range(min(abs(self.numerator), abs(self.denominator)), 1, -1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                self.numerator = self.numerator // i
                self.denominator = self.denominator // i
        return self

    # check if the fraction is equal to another fraction
    def equal(self, other):
        if self.numerator * other.denominator == self.denominator * other.numerator:
            return True
        else:
            return False
    
    # convert the fraction to a string
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    
    # Add, subtract, multiply, divide four operations
    def add(self, other):
        new = Fraction()
        new.numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new.denominator = self.denominator * other.denominator
        return new
    
    def subtract(self, other):
        new = Fraction()
        new.numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new.denominator = self.denominator * other.denominator
        return new
    
    def multiply(self, other):
        new = Fraction()
        new.numerator = self.numerator * other.numerator
        new.denominator = self.denominator * other.denominator
        return new
    
    def divide(self, other):
        new = Fraction()
        new.numerator = self.numerator * other.denominator
        new.denominator = self.denominator * other.numerator
        return new
    
    # generate a simple fraction
    def generate():
        while True:
            n1 = random.randint(1,15)
            n2 = random.randint(2,15)
            f = Fraction(n1, n2).reduce()
            if f.numerator%f.denominator != 0 or f.denominator != 1:
                break
        return f

# test Part
print('Please type the answer as n/d in most simplly.\nIf you want stop please type \'quit\'')
questions = 0
correct = 0
while True: # loop of the quiz
    while True: # generate questions loop
        f1 = Fraction.generate()
        f2 = Fraction.generate()
        type = random.choice(['add', 'subtract', 'multiply', 'divide']) # choice the type of the question
        answer = getattr(f1, type)(f2) # get the answer of type

        # check if the answer is an integer (too simple)
        if answer.numerator % answer.denominator != 0 or answer.numenator != 0: 
            # simplify the answer proper fraction
            answer = answer.reduce()
            break
    # question generate loop end
    # ask the question
    print(f'Question: {f1} {type} {f2} = ?')
    inputanswer = input('Please type the answer:')

    if inputanswer == 'quit': # check if the user want to quit
        break
    questions += 1
    if inputanswer == answer.__str__():
        print('Correct')
        correct += 1
    else:
        print(f'Incorrect, the answer is {answer}')
print (f'You have answered {correct} questions correctly out of {questions} questions')
exit()