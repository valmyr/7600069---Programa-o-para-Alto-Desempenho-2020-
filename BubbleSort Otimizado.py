#BubbleSort Otimizado
import time
import random
tempoInicial = time.time()
def BubbleSort(v):
       for i in range(len(v)):
              flag = 0
              for j in range(1,len(v)-i):
                     if(v[i] < v[j]):
                        v[i],v[j] = v[j], v[i]
                        flag = 1
              if(flag):
                 break
       return v
v = [random.randint(1,10000) for i in range(1000000)]
BubbleSort(v)
print(time.time()-tempoInicial)
