class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        if self.stop < self.pointer and self.step > 0:
            raise StopIteration
        elif self.stop > self.pointer and self.step < 0:
            raise StopIteration
        else:
            return self.pointer


a = Iterator(0, 5, 2)

for i in a:
    print(i)