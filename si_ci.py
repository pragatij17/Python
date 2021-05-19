def simple_interest(p, r, t): 
    si = (p * r * t)/100
    return si
def compound_interest(p, r, t, n):
    amount = p*(pow((1+r/n),(n*t)))
    ci = amount-p
    return ci

p=int(input('The principal is: '))
t=float(input('The time period is: '))
r=float(input('The rate of interest is: '))
n=int(input('Number of times: '))
print(simple_interest(p, r, t))
print(compound_interest(p, r, t, n))