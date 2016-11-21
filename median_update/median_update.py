#!/bin/python
def median(a,x):
    num_set = []
    
    for i in xrange(len(x)):
        calc_pass = False
        
        if a[i] == 'a':
            
            if len(num_set) < 1:
                num_set.append(x[i])
                calc_pass = True
                
            else:
                
                j = 0
                l = len(num_set)
                switch = True
                
                while switch:
                    if x[i] < num_set[j]:
                        switch = not switch
                        num_set = num_set[:j] + [x[i]] + num_set[j:]
                    j += 1
                    if j == l and switch:
                        switch = not switch
                        num_set.append(x[i])
                    
                calc_pass = True
        else:
            
            if len(num_set) > 1:
                try:
                    loc = num_set.index(x[i])
                    del num_set[loc]
                    calc_pass = True
                except ValueError:
                    pass
            else:
                pass
        
        if calc_pass:
            if len(num_set) % 2 == 1:
                print num_set[len(num_set) / 2]
            else:
                pos = len(num_set) / 2
                average = (num_set[pos] + num_set[pos - 1])
                if str(average/2.0)[-1] == "0":
                    print average/2
                else:
                    print average/2.0
        else:
            print "Wrong!"
            
            
N = input()
s = []
x = []
for i in range(0, N):
    tmp = raw_input().strip().split(' ')
    s.append(tmp[0])
    x.append(int(tmp[1]))
    
median(s,x)