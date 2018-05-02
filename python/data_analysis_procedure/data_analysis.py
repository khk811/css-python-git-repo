
# coding: utf-8

# In[76]:

from functools import reduce
import pickle
import math #square root



def average(scores):
    return reduce(lambda a,b: a + b,scores)/len(scores)
                  
                  
def variance(scores, arvg):
    return reduce(lambda a,b: a + b, map(lambda s: (s-avrg)**2, scores)) / len(scores)


    


# In[77]:

def evaluateClass(avrg, std_dev):
    if avrg <50 and std_dev >20:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > 50 and std_dev >20:
        print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
    elif avrg < 50 and std_dev <20:
        print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
    elif avrg > 50 and std_dev <20:
        print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")
        


# In[78]:

f = open("class_A.bin", "rb")


# In[79]:

item_ = []
while True:
    try: 
        data = pickle.load(f)
    except EOFError:
        break
    item_.append(data)
    

f.close()
    
print(item_)
type(item_)        


# In[80]:

#soc = map(lambda a:  ,item_)
#print(soc)


# In[81]:

scores = []

for i in item_:
    for value in i.values():
        scores.append(value)
scores


# In[82]:

avrg = round(average(scores), 1)
avrg


# In[83]:

vari = variance(scores, avrg)
vari


# In[84]:

std_dev = round(math.sqrt(vari), 1)
std_dev


# In[85]:

print("\n")

print('*' * 50)
print("A반 성적 분석 결과")
print('*' * 50)
print("A반의 평균은 {0}점이고 분산은 {1}이며, 따라서 표준편차는 {2}이다".format(avrg, variance, std_dev))
print('*' * 50)
print("A반 종합 평가")
print('*' * 50)

print('\n')


# In[86]:

evaluateClass(avrg, std_dev)


# In[ ]:




# In[ ]:




# In[ ]:



