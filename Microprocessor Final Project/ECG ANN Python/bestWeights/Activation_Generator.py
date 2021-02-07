import math
import csv
import numpy as np
file_name = ""
fraction_bits = 8
total_bits = 32
pres = 2

def GenerateSigmoidValues():
       Map = open("Sigmoid_map.txt", 'w')
       i = -4.0
       increment = 1.0/(2**(fraction_bits))
       n = 0
       A = []
       while i < 4.0:
              x =  (1/float(1+math.exp(-1*i)))
              print(i , x ,ConvertToBinary(x, fraction_bits))
              Map.write(str(i))
              Map.write("\t")
              Map.write(ConvertToBinary(x, total_bits))
              Map.write("\n")
              A.append(x)
              i += increment
              n += 1
       Map.close()
       print(n)
       return A

def ConvertToBinary(j, bits):
       num = ''
       k = 0
       neg = 0
       if (j < 0):
              neg = True
              j = j*-1
       else:
              neg = False
       a = int(j)
       j = round(j-a, 10)       
       while k < fraction_bits:
              j *= 2
              if j >= 1:
                     num = num+'1'
                     j  -= 1
              else:
                     num += '0'
              k += 1
       i = fraction_bits
       while i < bits:
              if int(a) % 2 == 0:
                     num = '0' + num
              else:
                     num = '1' + num
              a = int(a/2) 
              i += 1
       if (neg):
              num = TwoCompl(num, bits)
       return num

def ConvertToDecimal(j, bits):
       k = bits - 1
       num = 0.0
       power = -1*fraction_bits
       neg = 0
       number = j
       if j[0] == '1':
              neg = 1
              j = TwoCompl(j, bits)
       while k >= 0:
              if j[k] == '1':
                     num = num +(2**(power))
              k = k - 1
              power += 1
       if (neg):
              num = num*-1
       return num


def TwoCompl(binary, bits):
       first_1 = 0
       for i in range(len(binary)):
              if first_1:
                     binary = binary[:(bits-1)-i]+str(int(not(int(binary[(bits-1)-i]))))+binary[(bits)-i:]
              else:
                     if binary[(bits-1)-i] == '1':
                            first_1 = 1
       return binary

def main():
       A = GenerateSigmoidValues()      
       B = []
       C = []
       for a in A:
              x = ConvertToBinary(a, fraction_bits)
              B.append(x)
              y = ConvertToDecimal(x, fraction_bits)
              C.append(y)
       MIF = open("Sigmoid_LUT.mif", 'w')
       n = 0
       for b in B:
              print(b)
              MIF.write(b)
              MIF.write("\n")
              n += 1
       MIF.close()
       print(n)
       
no_bits = 32
arr = []

'''
with open('BW2.csv', newline='') as f:
       reader = csv.reader(f)
       for row in reader:
              numb = float(row[0])
              BNum = ConvertToBinary(numb, no_bits)
              arr.append(BNum)
arr1 = np.array(arr)
np.savetxt("Binary/BBW2.csv", arr1,fmt='%s' , newline=',\n')
'''
x1 = ConvertToBinary(0.02163647 , no_bits)
x2 = ConvertToBinary(0.01123784, no_bits)
x3 = ConvertToDecimal(x1, no_bits)
x4 = ConvertToDecimal(x2, no_bits)

print(x1,x2)
print(x3,x4)