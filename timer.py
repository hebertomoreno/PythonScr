import time, math, openpyxl

start = time.time()
print("hello")
sw = 0
end = time.time() + 0.1
while (math.floor(end-start) < 50):
    if (((end-start) % 5) == 0) :
        print(math.floor(end - start))
        end = time.time() + 0.1
    else:
        end = time.time()
