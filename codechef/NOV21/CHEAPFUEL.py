
# cook your dish here

t = int(input())
while t:
    n = list(map(int, input().split()))
    final_price_petrol = n[0] + (n[2] * n[4])
    final_price_diesel = n[1] + (n[3] * n[4])
    if final_price_petrol < final_price_diesel:
        print("PETROL")
    elif final_price_petrol > final_price_diesel:
        print("DIESEL")
    else:
        print("SAME PRICE")
    t -= 1