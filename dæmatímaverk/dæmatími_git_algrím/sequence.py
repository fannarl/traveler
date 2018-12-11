#reglan bakvið þetta sequence 1, 2, 3, 6, 11, 20, 37 er 1+2 =3, 1+2+3=6,2+3+6=11,3+6+11=20,6+11+20=37,11+20+37=58.
#Búa til for loopu til að finna þetta út

int_1 = 0
int_2 = 0
int_3 = 0
newest_int = 0
#length of sequence
n = int(input("Enter the length of the sequence: ")) # Do not change this line

for n in range (0, n):
#harðkóða upphafspunktana   
    if n == 0:
        int_1 = 1
        print(int_1)
    elif n == 1:
        int_2 = 2
        print(int_2)
    elif n == 2:
        int_3 = 3
        print(int_3)
#eftir að fyrstu 3 af sequencinu eru kominn þá getur algrímið tekið við        
    else:
        newest_int = int_1 + int_2 + int_3 
        print(newest_int)

        int_1 = int_2
        int_2 = int_3
        int_3 = newest_int

