input_string = input("Sonlarni prober bilan kiriting: ")
list  = input_string.split()
a=''
for i in range(0,len(list)):
   a=a+' '+str(i)
print('Siz kiritgan sonlar:')
print(a)
sum = 0
for num in list:
    sum += int (num)
print("O'rtacha qiymat: %.2f"%(sum/len(list)))