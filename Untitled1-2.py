#!/usr/bin/env python
# coding: utf-8

# In[1]:


inputlist = [[0, 5], [1, 6], [7, 3], [9, 2], [3, 5]]
inputlist.sort()
st, en = ([i[0] for i in inputlist], [i[0] + i[1] for i in inputlist])

# In[2]:


# initialise
heap_list = []
heap_size = 0
counters = 0
N = len(st)


# In[3]:


def insert(val):
    global heap_size
    heap_list.append(val)
    heap_size += 1
    bh(heap_list)


def delete():
    global heap_size
    global heap_list

    lastElement = heap_list[heap_size - 1]
    heap_list[0] = lastElement
    heap_size = heap_size - 1
    bh(heap_list)


def heapify(A, k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        heapify(A, smallest)


def min_heap_val():
    return heap_list[0]


def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def bh(arr):
    n = int((len(arr) // 2) - 1)
    for k in range(n, -1, -1):
        heapify(arr, k)


# In[4]:


for i in range(N):
    if heap_size > 0 and min_heap_val() < st[i]:
        delete()
        insert(en[i])
    else:
        counters = counters + 1
        insert(en[i])
print('Counters Required: ' + str(counters))

# In[ ]:
