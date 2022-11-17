#!/usr/bin/env python
# coding: utf-8

# # Python class

# In[1]:


print('Hello World')


# In[2]:


type('Hello world')


# In[3]:


type("a")


# In[4]:


a = 5 


# In[5]:


type(a)


# In[6]:


range(10)


# In[7]:


type(a==5)


# In[8]:


range(0,10)


# In[9]:


list(range(0,10))


# In[10]:


list(range(3,10)) ##list number from 3 -9


# In[11]:


list(range(3,10,2))##list number from 3 -9 by skipping 1 num in between 


# In[12]:


list(range(10,3))# its gives an empty list


# In[13]:


list(range(3,10,-1))


# In[14]:


list(range(3,10.5))


# In[15]:


list(range(-10,-3))


# In[16]:


"anand"+"rajesh"


# In[17]:


a=input("Enter a number:")


# In[18]:


a


# In[19]:


type(a)


# In[20]:


num1=input("Enter 1st number:")
num2=input("Enter 2nds number:")

sum=num1+num2
print(sum)


# In[21]:


num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nds number:"))

sum=num1+num2
print(sum) 


# In[22]:


print(sum)


# In[23]:


sum


# ## Design a Basic calculator

# In[24]:


num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))

sum = num1+num2
diff = num1-num2
mult = num1*num2
div = num1/num2
mod = num1%num2
flr = num1//num2
pwr = num1**num2

print(sum)  
print(diff)  
print(mult)  
print(div)  
print(mod)
print(flr)
print(pwr)


# In[25]:


a=2
a**2


# In[26]:


pow(3,5)


# In[27]:


pow('anand',3)


# In[28]:


'anand'*3


# In[29]:


list("anand")


# In[31]:


a=list('INDEPENDENCE')


# In[32]:


a


# In[33]:


len(a)


# In[34]:


a[5]


# In[35]:


a[:5]


# In[36]:


a[11]


# In[37]:


a[::2]


# In[38]:


a[-2]


# In[39]:


a[0:12:3]


# In[40]:


a[::-1]


# In[41]:


b=a[::-1]


# In[42]:


b


# In[43]:


a='hello how are you ramya'
b=a[::-1]


# In[44]:


a


# In[45]:


b


# In[46]:


a="Swastik"


# In[47]:


a[3]


# In[48]:


len(a)


# In[49]:


a[3]='m'


# In[50]:


str_to_list=list(a)


# In[51]:


str_to_list


# In[52]:


empty_list=[]#create empty list


# In[53]:


empty_list


# In[54]:


list_object=['sehnaz',23,11,22,45,'Akash',65]


# In[55]:


list_object


# In[56]:


list_object=['sehnaz',23,11,22,45,'Akash',65,['Goutam','anand']]


# In[57]:


list_object


# In[58]:


list_object[-1]


# In[59]:


list_object.append('Rama')


# In[60]:


list_object


# In[61]:


list_object.insert(3,'Menal')


# In[62]:


list_object


# ## task for you all
# ## list=[2,3,4,5,6,7,8,9,123,13,14,15,16]
# ## I want all my even number in one list and all my odd number in another list

# In[63]:


num_list=[2,3,4,5,6,7,8,9,123,13,14,15,16]


# In[64]:


type(num_list)


# In[65]:


num_list


# In[66]:


len(num_list)


# In[67]:


a=[]
b=[]


# In[68]:


a


# In[69]:


b


# In[70]:


for i in range(len(num_list)):
    if (num_list[i]%2==0):
        a.append(num_list[i])
    else:
        b.append(i)


# In[71]:


a,b


# In[72]:


c=[]
d=[]


# In[74]:


for i in num_list:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)


# In[75]:


c


# In[76]:


d


# In[77]:


'a' in 'anand'


# In[78]:


'Akash' in list_object


# In[79]:


str_object="asdjdfhuhgjhndmkjhdfjhdfhufhdjhjfhhu43438485jkhj12j3hjh43jj6hj7nj8n9mn5jwwedd"


# In[80]:


str_object.find('w')# index of 1st occurance


# In[81]:


str_object.find('33')# number not exist


# In[82]:


str_object.split('j')


# In[83]:


str_object.split('m')


# In[84]:


str_object.partition('j')


# In[85]:


text="INDIA is my country"


# In[86]:


text.center(50,'#')


# In[87]:


text.center(50,'*')


# In[88]:


text


# In[89]:


s= [1,3,4,5,5]


# In[90]:


s


# In[91]:


s.append([3,5,6,7])# append list inside the list


# In[92]:


s


# In[93]:


s.append(['Kumar',55,'Hello'])


# In[94]:


s


# In[95]:


s.extend([6,7,8,9,'Rama'])


# In[96]:


s


# In[97]:


var = input("Please input your name: ")


# In[98]:


'my name is {}'.format(var)


# In[99]:


print("My name is",var)


# In[101]:


list(34)


# In[102]:


list('34')


# In[103]:


a= [1,2,3,4,5,6,7,8]
b= ['Anand','Manisha',"Ramya","Anil"]
c= [23,34,45,67,88,89]

d = [a,b,c]


# In[104]:


d


# In[105]:


b[2]


# In[106]:


d[1][-2]


# In[107]:


d[2][-4]


# In[108]:


list_num =[24,45,67,32,90]


# In[109]:


[i*2 for i in list_num] # list comprehentin


# In[ ]:




