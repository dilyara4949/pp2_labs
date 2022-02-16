'''Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F - 32)'''

fahr = int(input())
toCel = lambda x : (5/9) * (x - 32)

print(toCel(fahr))