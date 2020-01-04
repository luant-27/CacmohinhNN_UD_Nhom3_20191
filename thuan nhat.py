#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math


# In[2]:


def nhap_he_thong():
    print("Nhập các thông số của hệ thống thuần nhất(LƯU Ý: λ<nμ)")
    ex = True
    while ex: 
        n = np.int(input('Số kênh phục vụ: n= '))
        λ = np.float(input('Cường độ dòng yêu cầu: λ= '))
        μ = np.float(input('Cường độ dòng phục vụ: μ= '))
        if (λ < n*μ):
            ex = False
        else:
            print("nhập lại:")
    anpha = λ/μ
    return n,anpha,λ


# In[3]:


def nhap_chi_phi():
    Cc = np.float(input('Giá trị tổn thất khi 1 yêu cầu chờ($/đơn vị tgian): Cc= '))
    Ckb = np.float(input('Chi phí 1 kênh phục vụ($/đơn vị tgian): Ckb= '))
    Ckr = np.float(input('Tổn thất khi 1 kênh rỗi($/đơn vị tgian): Ckr= '))
    Cpv = np.float(input('Số tiền thu về khi phục vụ 1 y/c($)3: Cpv= '))
    return Cc,Ckb,Ckr,Cpv


# In[4]:


def tinh_P0(n, anpha):
    tong = 0
    for k in range(n+1):
        tong = tong + math.pow(anpha,k)/math.factorial(k)
    P0 = 1/(tong + math.pow(anpha,n+1)/(math.factorial(n)*(n-anpha)))
    return P0


# In[5]:


def tinh_Pc(n,anpha,P0):
    Pc = P0*(math.pow(anpha,n)/math.factorial(n))*(n/(n-anpha))     #2.20
    return Pc


# In[6]:


def hangcho_tgiancho_TB(n,anpha,P0,λ):
    Mc = P0*math.pow(anpha,n+1)/(math.factorial(n-1)*math.pow(n-anpha,2))
    Tc = Mc/λ
    return Mc,Tc


# In[7]:


def kenh_roi_TB(n,anpha,P0):
    sum=0
    for k in range(n+1):
        sum=sum+(n-k)*math.pow(anpha,k)/math.factorial(k)
    Nr = P0* sum
    return  Nr


# In[8]:


def tonthat_hieuqua(n,anpha,λ,Mc,Nr):
    Cc,Ckb,Ckr,Cpv = nhap_chi_phi()
    G = (Mc*Cc + (n-Nr)*Ckb + Nr*Ckr)
    E = λ*Cpv - G
    return G,E


# In[9]:


n,anpha, λ = nhap_he_thong()
P0 = tinh_P0(n, anpha)
print("1,Xác suất hệ thống rỗi: Pr= ",P0)
Pc = tinh_Pc(n,anpha,P0)
print("2,Xác suất một yêu cầu phải chờ: Pc= ",Pc)
print("3,Xác suất một yêu cầu được phục vụ ngay: Ppvn= ",1-Pc)
Mc,Tc = hangcho_tgiancho_TB(n,anpha,P0,λ)
print("4,Độ dài hàng chờ trung bình: Mc= ",Mc)
print("5, Thời gian chờ trung bình của 1 yêu cầu: Tc= ", Tc)
Nr = kenh_roi_TB(n,anpha,P0)
print("6,Số kênh rỗi trung bình: Nr= ",Nr)
print("7,Số kênh bận trung bình: Nb= ", n-Nr)


# In[10]:


G,E = tonthat_hieuqua(n,anpha,λ,Mc,Nr)
print("8,Chi phí tổn thất của hệ thống: G={}($/đvt/gian)".format(G))
print("9,Hiệu quả kinh tế của mô hình E = {}($/đvtg)".format(E))






