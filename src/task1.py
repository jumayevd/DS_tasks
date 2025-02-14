import time

def kwargsAcceptFun(**kwargs):
   
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwargsAcceptFun(name = "Doniyor", age=20, country="Uzbekistan")



def decorator_1(func):
   
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)  
        end_time = time.time()  
        execution_time = end_time - start_time  
        print(f"{func.__name__} call executed in {execution_time:.4f} sec")
        return result 
    return wrapper


def kwargsAcceptFun(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    kwargsAcceptFun(name="Doniyor", age=20, city="Tashkent")
