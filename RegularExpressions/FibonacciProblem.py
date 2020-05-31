'''
Let's learn some new Python concepts! You have to generate a list of the first  fibonacci numbers,  being the first number. 
Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.
'''

cube = lambda x: x*x*x# complete the lambda function 

def fibonacci(n):
    lst=list()
    #lst.append(0)
    #lst.append(1)
    for i in range(n):
        #print(i)
        if(i==0):
         lst.append(0) 
        elif(i==1):
         lst.append(1)
        else:  
         #print(i)  
         #print(lst[i-1])  
         #print(lst[i-2])
         lst.append(lst[i-1] + lst[i-2])
    return lst;     
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))