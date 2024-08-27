from fun_fake_math import divide as fake_divide
from fun_true_math import divide as true_divide

res1 = fake_divide(1, 2)
res2 = fake_divide(5, 0)
res3 = true_divide(5, 2)
res4 = true_divide(7, 0)

print(res1)
print(res2)
print(res3)
print(res4)
