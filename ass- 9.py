
# coding: utf-8

# Sets in python.
# 
# unordered collection of elements using{}.
# 
# maintains uniqueness of elements
# 
# doesnt support indexing for acessing element
# 
# does supports mathematical sets operation(union,intersection,diff. and symmetry.
# 

# In[3]:


names={'Ali','Naimat','Fahad'}

unique_names =set(names)
unique_names.add('hadi')
unique_names.remove('hadi')
print(unique_names)


# In[1]:


num1 = {1,2,3,4,4,5,6,7,8,9}
num2 = {1,3,4,5,6,7,8,1}

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)
print(num1 ^ num2)


# Functions in python

# In[1]:


def greet(f_name,last_name):
    print(f"hi there {f_name} {last_name}")
    
    greet(Ali,hasnat)


# In[4]:


def increment(num,by):
    return num*by

increment(2,by=5)


# In[24]:


#secret msg (aka cypher) and encoded msg

def cypher(message,shift):
    encrypted_msg= ""
    for char in message:
        if char.isalpha():
            alphabets='abdcdefghijklmnopqrstuvwxyz'
            if char.isupper():
                alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            position= alphabets.find(char)
            shifted_position = (position+shift)%26
            encrypted_chr =alphabets[shifted_position]
            encrypted_msg += encrypted_chr
        else:
            encrypted_msg +=char
    return encrypted_msg
message =input("Enter your message")
shift=int(input("by how many char ou wants to shift your charcater"))

print(cypher(message, shift))



# In[ ]:


# Dictonaries converter









# In[ ]:


#Weigth conerter
def weigth(mass)















