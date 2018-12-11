# Write a Python script to concatenate following dictionaries to create a new one. Go to the editor
# Sample Dictionary : 
# dic1={1:10, 2:20} 
# dic2={3:30, 4:40} 
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic1)
print(dic2)
print(dic3)

print(dic4)