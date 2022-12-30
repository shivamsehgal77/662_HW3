#!/usr/bin/env python
# coding: utf-8

# # HOMEWORK - 03

# 
# # 1. Position Kinematics - Panda  [3.5 points]

# In[1]:


from sympy import *
from IPython.display import Image,display,HTML
init_printing()

theta,d,a,alpha=symbols('theta,d,a,alpha')
d_1,d_3,d_5,d_7,a_3=symbols('d_1,d_3,d_5,d_7,a_3')
theta_1,theta_2,theta_3,theta_4,theta_5,theta_6,theta_7=symbols('theta_1,theta_2,theta_3,theta_4,theta_5,theta_6,theta_7')
Rot_z_theta=Matrix([[cos(theta),-sin(theta),0,0],
                    [sin(theta),cos(theta),0,0],
                    [0,0,1,0],
                    [0,0,0,1]])
Trans_z_d=Matrix([[1,0,0,0],
                  [0,1,0,0],
                  [0,0,1,d],
                  [0,0,0,1]])
Trans_x_a=Matrix([[1,0,0,a],
                  [0,1,0,0],
                  [0,0,1,0],
                  [0,0,0,1]])
Rot_x_alpha=Matrix([[1,0,0,0],
                   [0,cos(alpha),-sin(alpha),0],
                   [0,sin(alpha),cos(alpha),0],
                   [0,0,0,1]])



# # ROTATION MATRIX COMPUTATION

# In[2]:


A=Rot_z_theta*Trans_z_d*Trans_x_a*Rot_x_alpha


# # ROTATION MATRIX COMPUTATION FOR EACH JOINT

# In[3]:


A_1=A.subs({theta:theta_1,d:d_1,a:0,alpha:pi/2})
A_2=A.subs({theta:theta_2,d:0,a:0,alpha:-pi/2})
A_3=A.subs({theta:theta_3,d:d_3,a:a_3,alpha:-pi/2})
A_4=A.subs({theta:theta_4,d:0,a:-a_3,alpha:pi/2})
A_5=A.subs({theta:theta_5,d:d_5,a:0,alpha:pi/2})
A_6=A.subs({theta:theta_6,d:0,a:a_3,alpha:pi/2})
A_7=A.subs({theta:theta_7,d:d_7,a:0,alpha:0})


# In[4]:


A_1


# In[5]:


A_2


# In[6]:


A_3


# In[7]:


A_4


# In[8]:


A_5


# In[9]:


A_6


# In[10]:


A_7


# # THE FINAL TRANFORMATION OF EF WRT ORIGIN

# In[11]:


Transformation=A_1*A_2*A_3*A_4*A_5*A_6*A_7
Transformation


# ## TRANSFOMATION RESULTS FOR GEOMETRICALLY KNOW CONFIGRATIONS

# ### Theta2 is rotated by pi/2

# In[12]:


T_1=Transformation.subs({theta_1:0,
theta_2:pi/2,
theta_3:0,
theta_4:0,
theta_5:0,
theta_6:0,
theta_7:0})
T_1


# ### All angles are zero home configration
# 

# In[13]:


T_1=Transformation.subs({theta_1:0,
theta_2:0,
theta_3:0,
theta_4:0,
theta_5:0,
theta_6:0,
theta_7:0})
T_1


# ### Theta3 is rotated by pi/2

# In[14]:


T_1=Transformation.subs({theta_1:0,
theta_2:0,
theta_3:pi/2,
theta_4:0,
theta_5:0,
theta_6:0,
theta_7:0})
T_1


# ### Theta4 is rotated by pi/2

# In[15]:


T_1=Transformation.subs({theta_1:0,
theta_2:0,
theta_3:0,
theta_4:pi/2,
theta_5:0,
theta_6:0,
theta_7:0})
T_1


# ### Theta5 is rotated by pi/2

# In[16]:


T_1=Transformation.subs({theta_1:0,
theta_2:0,
theta_3:0,
theta_4:0,
theta_5:pi/2,
theta_6:0,
theta_7:0})
T_1


# ### Theta6 is rotated by pi/2

# In[17]:


T_1=Transformation.subs({theta_1:0,
theta_2:0,
theta_3:0,
theta_4:0,
theta_5:0,
theta_6:pi/2,
theta_7:0})
T_1


# ### Theta7 is rotated by pi/2

# In[18]:


T_1=Transformation.subs({theta_1:0,
theta_2:0,
theta_3:0,
theta_4:0,
theta_5:0,
theta_6:0,
theta_7:pi/2})
T_1


# ### Theta 7 is roated by pi/2

# In[19]:


T_1=Transformation.subs({theta_1:0,
theta_2:0,
theta_3:0,
theta_4:0,
theta_5:0,
theta_6:0,
theta_7:pi/2})
T_1


# In[ ]:




