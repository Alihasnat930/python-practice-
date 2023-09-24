
# coding: utf-8

# Agrs in functions

# In[27]:


def multiply(*numbers):
    for number in numbers:
        print(numbers)
    multiply(3,5)




# In[ ]:


def sales_calculation(*sales): #pass tuples in single *
    total=0
    for sale in sales:
        


    
    
    daily_sale = [1500.3,2500]


# In[14]:


def save_user_info(**users): # pass dictoinary in **
    for user,info in users.items():
        print(user,info)
    
user_info={
    'id':1, 
    'user':'Ali',
    'age':19
}
    
print(save_user_info(**user_info))
    
    


# In[30]:


# dictoinary output
def save_user_info(**users):
    for user,info in users.items():
        return(user,info)
        
print(save_user_info({id:1,user:'Ali',age:19})


# In[25]:


# Product inventory dictoinary via user.input

def product_inventory():
    {
        'Hand wash':40
        'bags'= 1000
        'flowes'= 500
    }

    print(product_inventory)







# In[10]:


#fezz buss user input 
def fezz_buss(num):
    if num%3:
        print("buss")
        if num%5:
            print("Buzzz")
            if num%3 and num%5:
                 print("Fezz buss")
                    
num=int(input("Enter num"))
print(num)
    
    
    
    
    
    

