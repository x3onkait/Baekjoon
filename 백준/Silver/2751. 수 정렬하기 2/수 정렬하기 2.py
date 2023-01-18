from collections import deque
import sys

def get_values():
    
    _qty    = int(input())
    data    = []

    for _seq in range(_qty):
        data.append(int(sys.stdin.readline()) + 10000001)

    return data


# Conduct sorting with a radix sort algorithm
def radix_sort(number_list):
    
    buckets   = [deque() for _ in range(10)]

    max_value = max(number_list)
    queue     = deque(number_list)
    digit     = 1                       # Radix sort does sorting with its digit

    while max_value >= digit:

        # putting numbers into the bucket
        while queue:
            number  = queue.popleft()
            buckets[(number // digit) % 10].append(number)

        # sort
        for bucket in buckets:
            while bucket:
                queue.append(bucket.popleft())

        digit *= 10

    return list(queue)

data = radix_sort(get_values())

for _data in data:
    print(_data - 10000001)             # THIS PROBLEM MAY GIVE NEGATIVE VALUES!!!!!!!!!