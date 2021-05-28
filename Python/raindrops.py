def convert(number):
    Pling, Plang, Plong = "", "", ""
    num = number
    if number%3==0:
        Pling, num = 'Pling', ''
    if number%5==0:
        Plang, num = 'Plang', ''
    if number%7==0:
        Plong, num= 'Plong', ''
            
    return f"{num}{Pling}{Plang}{Plong}"
    