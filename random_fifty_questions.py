'''
Here are functions that can 
help generate random fifty yin questions and answers
'''

# %%
from helper import recite_yin 

# %%
test_num = input("Enter the number of time you want to do the test: ")
if test_num == '':
    test_num = 10
else:
    test_num = int(test_num)

# repeat test for test num times
for i in range(test_num):
    recite_yin(['empty'])
# %%
