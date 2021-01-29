import timeit

class CustomException(Exception):
    def __init__(self,a=""):
        message = a
        super().__init__(message)


def fibo_rec(n):
    if n==0 or n==1:
        return n
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=int(input("Zadej n pro výpočet Fibonacciho: "))
    if n<0:
        raise CustomException("N musí být >=0!")
    else:
        start_time = timeit.timeit()
        fibo_n=[]
        for my_counter in range(n+1):
            if my_counter<2:
                fibo_n.append(my_counter)
            else:
                temp=fibo_n[my_counter-1]+fibo_n[my_counter-2]
                fibo_n.append(temp)

        end_time = timeit.timeit()

        print("Doba výpočtu Fibonacciho iterací:",(end_time-start_time))

        print("Fibonacci iterací: ",fibo_n[n])

        start_time = timeit.timeit()
        fibo_n2=int(fibo_rec(n))
        end_time = timeit.timeit()
        print("Doba výpočtu Fibonacciho rekurzí:",(end_time - start_time))
        print("Fibonacci rekurzí: ",fibo_n2)