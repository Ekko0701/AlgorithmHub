n = input()
decimal_value = int(n, 2)  
octal_str = oct(decimal_value).replace("0o", "") 

print(octal_str)