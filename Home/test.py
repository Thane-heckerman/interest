one_month = {'vcb': 2 , 'tcb': 3 , 'bidv': 4 , 'vietin': 5 }
two_month = {'vcb': 4 , 'tcb': 5 , 'bidv': 6 , 'vietin': 7 }
lowest1 = min(one_month.items(), key=lambda x: x[1])
lowest = min(two_month.items(), key=lambda x: x[1])
print(id(one_month))
print(id(two_month))

#done