import copy

x = 123

n = 1
if x < 0:
    n = -1
    x = -x

x_ = copy.deepcopy(x)
ws = 0
while int(x_):
    x_ = x_ / 10
    ws += 1

num_ = 0
num__ = 0
for i in range(ws):
    num = x % pow(10, i)
    num_ = num * (pow(10, (ws - i)))
    x -= num_
    num__ += num_
print(num_ * n)
