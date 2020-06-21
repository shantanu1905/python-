import random

lower = "qwertyuioplkjhgfdsazxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
symbols = "!@#$%&*_-\/?"

all = lower + upper +numbers + symbols

length = 10
password ="".join(random.sample(all,length))
print(password)
