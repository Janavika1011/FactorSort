def factor(num):
    i=1
    count=0
    while i*i <=num:
        if num%i==0:
            if num/i==i:
                count+=1
            else:
                count+=2
        i+=1
    return count