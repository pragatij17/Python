def simple_interest(p, r, t): 
    si = (p * r * t)/100
    return si
def compound_interest(p, r, t):
    amount = p*(pow((1+r/100),t))
    ci = amount-p
    return ci

p=int(input('The principal is: '))
t=float(input('The time period is: '))
r=int(input('The rate of interest is: '))
print(simple_interest(p, r, t))
print(compound_interest(p, r, t))