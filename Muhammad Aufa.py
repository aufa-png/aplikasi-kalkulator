def penjumlahan (a,b):
    return a+b
def pengurangan (a,b):
    return a-b
def perkalian (a,b):
    return a*b
def pembagian (a,b):
        return a/b
    
while True:
        a = int (input ("masukan angka pertama :"))
        b = int (input ("masukan angka kedua :"))
        
        print ("pilih operasi \n"\
               "1. penjumlahan\n"\
               "2. pengurangan\n"\
               "3. perkalian\n"\
               "4. pembagian\n"\
               "5. keluar")
        pilih =int(input("pilih operasi 1,2,3,4,5:"))
        if pilih == 1:
            print(a, "+",b,"=",penjumlahan (a,b))
            
        elif pilih == 2:
            print(a, "-",b,"=",pengurangan (a,b))
            
        elif pilih == 3:
            print(a, "*",b,"=",perkalian (a,b))
            
        elif pilih == 4:
            print(a, "/",b,"=",pembagian (a,b))
            
        elif pilih == 5:
            break
        else:
            print ("invalid input")
        
        