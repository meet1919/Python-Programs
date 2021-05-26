import time

def calcu():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

start = time.time()
prod = calcu()
end = time.time()

print('The final number is %s digits long'%(len(str(prod))))
print('Time elasped in this calculation is %s seconds'%(end-start))