n = int(input());
list_new = input().split()
print(" ".join([str(list_new.index(str(i))+1) for i in range(1,n+1)]))