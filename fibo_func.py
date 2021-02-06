from time import perf_counter
from functools import lru_cache
def fibon_iter(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    first_number, second_number = 1, 0
    for i in range(1,n):
        out = first_number + second_number
        first_number, second_number = out, first_number
    return out
def fibon_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibon_rec(n-1) + fibon_rec(n-2)

@lru_cache(100)
def fibon_rec_lru(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibon_rec_lru(n-1) + fibon_rec_lru(n-2)

N = 100
start_time = perf_counter()
result = fibon_iter(N)
end_time = perf_counter()
print('Compute factorial iteratively: {}'.format(result))
print('Time to compute one run: {} s'.format(end_time-start_time))
# start_time = perf_counter()
# print('Compute factorial recursively: {}'.format(fibon_rec(N)))
# print('Time to compute one run: {} s'.format(perf_counter()-start_time))
start_time = perf_counter()
print('Compute factorial recursively with lru_cache: {}'.format(fibon_rec_lru(N)))
print('Time to compute one run: {} s'.format(perf_counter()-start_time))
start_time = perf_counter()
for i in range(100):
    result = fibon_iter(N)
print('Time to compute 100 runs of factorial iteratively: {} s'.format(perf_counter()-start_time))
start_time = perf_counter()
# for i in range(100):
#     result = fibon_rec(N)
# print('Time to compute 100 runs of factorial recursively: {} s'.format(perf_counter()-start_time))
start_time = perf_counter()
for i in range(100):
    result = fibon_rec_lru(N)
print('Time to compute 100 runs of factorial recursively with lru_cache: {} s'.format(perf_counter()-start_time))