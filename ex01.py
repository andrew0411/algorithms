i=list(map(int,input().split()))
print(max(i)*100) if len(set(i))==3 else print(10000+1000*i[0]) if len(set(i))==1 else \
(print(1000+100*list(set(i))[0]) if i.count(list(set(i))[0])==2 else print(1000+100*list(set(i))[1]))
