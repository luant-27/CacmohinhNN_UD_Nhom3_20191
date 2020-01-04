#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math


# In[2]:


def nhap_he_thong():
    print("Nhập các thông số của hệ thống chờ hạn chế")
    n = np.int(input('Số kênh phục vụ: n= '))
    m = np.int(input('Độ dài hàng chờ: m= '))
    λ = np.float(input('Cường độ dòng yêu cầu: λ= '))
    μ = np.float(input('Cường độ dòng phục vụ: μ= '))
    anpha = λ/μ
    return n,anpha,λ,m


# In[3]:


def nhap_chi_phi():
    Cc = np.float(input('Giá trị tổn thất khi 1 yêu cầu chờ($/đơn vị tgian): Cc= '))
    Ckb = np.float(input('Chi phí 1 kênh phục vụ($/đơn vị tgian): Ckb= '))
    Ckr = np.float(input('Tổn thất khi 1 kênh rỗi($/đơn vị tgian): Ckr= '))
    Cpv = np.float(input('Số tiền thu về khi phục vụ 1 y/c($)3: Cpv= '))
    Ctc = np.float(input('Tổn thất khi từ chối phục vụ($/đơn vị tgian): Ctc='))
    return Cc,Ckb,Ckr,Cpv,Ctc


# In[4]:


def tinh_P0(n, anpha,m):
    tong = 0
    if (anpha/n == 1):
        for k in range(n+1):
            tong = tong + math.pow(anpha,k)/math.factorial(k)
        P0 = 1/(tong + (m*math.pow(anpha,n)/(math.factorial(n))))
        return P0
    else:
        for k in range(n+1):
            tong = tong + math.pow(anpha,k)/math.factorial(k)
        P0 = 1/(tong + ((math.pow(anpha,n)/math.factorial(n))*(anpha/n*(1-math.pow(anpha/n,m))/(1-anpha/n))))
        return P0 
        


# In[5]:


def tinh_Pc(n,anpha,P0,m):
    tong = 0
    for k in range(m):
        tong = tong + pow(anpha/n,k)
    Pc = math.pow(anpha,n)/math.factorial(n) * tong * P0
    return Pc


# In[6]:


def tinh_Ptc(n,anpha,P0,m):
    Ptc = math.pow(anpha,n)/math.factorial(n) * math.pow(anpha/n,m) * P0
    return Ptc


# In[7]:


def kenh_ban_TB(n,anpha,P0,m):
    sum1=0
    for k in range(n+1):
        sum1=sum1+k*math.pow(anpha,k)/math.factorial(k)
    sum2=0
    for k in range(1,m+1):
        sum2=sum2+math.pow(anpha,n)/math.factorial(n)*math.pow(anpha/n,k)
    Nb = P0*(sum1 + n*sum2)
    return  Nb


# In[8]:


def hangcho_tgiancho_TB(n,anpha,P0,λ,m):
    tong = 0
    for k in range(m+1):
        tong=tong+k*math.pow(anpha/n,k)
    Mc = P0*math.pow(anpha,n)/math.factorial(n)*tong
    Tc = Mc/λ
    return Mc,Tc


# In[9]:


def tonthat_hieuqua(n,anpha,λ,Mc,Nb,Ptc,Cc,Ckb,Ckr,Cpv,Ctc ):
    G = λ*Ptc*Ctc + Mc*Cc + Nb*Ckb + (n-Nb)*Ckr
    E = λ*Cpv - G
    return G,E


# In[10]:


def loinhuan_toiuu(G,E,n,anpha,λ,Cc,Ckb,Ckr,Cpv,Ctc,m):
    tempE = E
    tempG = G
    n= n+1
    P0 = tinh_P0(n, anpha,m)
    Pc = tinh_Pc(n,anpha,P0,m)
    Ptc = tinh_Ptc(n,anpha,P0,m)
    Mc,Tc = hangcho_tgiancho_TB(n,anpha,P0,λ,m)
    Nb = kenh_ban_TB(n,anpha,P0,m)
    G,E = tonthat_hieuqua(n,anpha,λ,Mc,Nb,Ptc,Cc,Ckb,Ckr,Cpv,Ctc)
    if ( tempE < E):
        while (tempE < E):
            tempE = E
            tempG = G
            n= n+1
            P0 = tinh_P0(n, anpha,m)
            Pc = tinh_Pc(n,anpha,P0,m)
            Ptc = tinh_Ptc(n,anpha,P0,m)
            Mc,Tc = hangcho_tgiancho_TB(n,anpha,P0,λ,m)
            Nb = kenh_ban_TB(n,anpha,P0,m)
            G,E = tonthat_hieuqua(n,anpha,λ,Mc,Nb,Ptc,Cc,Ckb,Ckr,Cpv,Ctc)
        return G, E,n
    else:
        n= n-2
        P0 = tinh_P0(n, anpha,m)
        Pc = tinh_Pc(n,anpha,P0,m)
        Ptc = tinh_Ptc(n,anpha,P0,m)
        Mc,Tc = hangcho_tgiancho_TB(n,anpha,P0,λ,m)
        Nb = kenh_ban_TB(n,anpha,P0,m)
        G,E = tonthat_hieuqua(n,anpha,λ,Mc,Nb,Ptc,Cc,Ckb,Ckr,Cpv,Ctc)
        while(E>tempE):
            tempE = E
            tempG = G
            n = n -1
            P0 = tinh_P0(n, anpha,m)
            Pc = tinh_Pc(n,anpha,P0,m)
            Ptc = tinh_Ptc(n,anpha,P0,m)
            Mc,Tc = hangcho_tgiancho_TB(n,anpha,P0,λ,m)
            Nb = kenh_ban_TB(n,anpha,P0,m)
            G,E = tonthat_hieuqua(n,anpha,λ,Mc,Nb,Ptc,Cc,Ckb,Ckr,Cpv,Ctc)
        return tempG, tempE,n
    


# In[11]:


n,anpha,λ,m = nhap_he_thong()
P0 = tinh_P0(n, anpha,m)
print("1,Xác suất hệ thống rỗi: Pr= ",P0)
Pc = tinh_Pc(n,anpha,P0,m)
print("2,Xác suất một yêu cầu phải chờ: Pc= ",Pc)
Ptc = tinh_Ptc(n,anpha,P0,m)
print("3,Xác suất một yêu cầu bị từ chối: Ptc= ",Ptc)
print("4,Xác suất một yêu cầu được phục vụ ngay: Ppvn= ",1-Pc-Ptc)
Mc,Tc = hangcho_tgiancho_TB(n,anpha,P0,λ,m)
print("5,Độ dài hàng chờ trung bình: Mc= ",Mc)
print("6, Thời gian chờ trung bình của 1 yêu cầu: Tc= ", Tc)
Nb = kenh_ban_TB(n,anpha,P0,m)
print("7,Số kênh rỗi trung bình: Nr= ",n - Nb)
print("8,Số kênh bận trung bình: Nb= ",Nb)


# In[12]:


Cc,Ckb,Ckr,Cpv,Ctc = nhap_chi_phi()
G,E = tonthat_hieuqua(n,anpha,λ,Mc,Nb,Ptc,Cc,Ckb,Ckr,Cpv,Ctc)
print("9,Chi phí tổn thất của hệ thống: G={}($/đvt/gian)".format(G))
print("10,Hiệu quả kinh tế của mô hình E = {}($/đvtg)".format(E))


# In[13]:


G,E,n = loinhuan_toiuu(G,E,n,anpha,λ,Cc,Ckb,Ckr,Cpv,Ctc,m)
print("11,Để hệ thống hiệu quả nhất cần {} kênh phục vụ, lợi nhuận tối ưu {}($/đvt/gian), chi phí tối ưu {}($/đvt/gian).".format(n,E,G))





