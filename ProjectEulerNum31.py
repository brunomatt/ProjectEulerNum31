# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
import time
start = time.time()

answer = 8    #homogenuous options, ie 1 two pound coin, two one pound coins, 4 50 pence coins, etc.

for a in range(0,2):
    for b in range(0,4):
        if 100*a + 50*b < 200:
            for c in range(0,10):
                if 100*a + 50*b + 20*c < 200:
                    for d in range(0,20):
                        if 100*a + 50*b + 20*c + 10*d < 200:
                            for e in range(0,40):
                                if 100*a + 50*b + 20*c + 10*d + 5*e < 200:
                                    for f in range(0,100):
                                        if 100*a + 50*b + 20*c + 10*d + 5*e + 2*f < 200:
                                            for g in range(0,199):
                                                if 100*a + 50*b + 20*c + 10*d + 5*e + 2*f + g == 200:
                                                    answer += 1
                                        elif 100*a + 50*b + 20*c + 10*d + 5*e + 2*f == 200:
                                            answer += 1
                                elif 100*a + 50*b + 20*c + 10*d + 5*e == 200:
                                    answer += 1
                        elif 100*a + 50*b + 20*c + 10*d == 200:
                            answer += 1
                elif 100*a + 50*b + 20*c == 200:
                    answer += 1
        elif 100*a + 50*b == 200:
            answer += 1

print(answer)

stop = time.time()
print('Time: ', stop - start)