# Эта программа выводит ступенчатую комбинацию.
NUM_STEPS = 6
 
for r in range(NUM_STEPS):
    for c in range(r):
        print(' ', end='')
    print('#')