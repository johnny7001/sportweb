from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#login_required=登入要求, 沒有登入的話無法進入頁面
#from django.contrib.auth.forms import UserCreationForm #創建使用者的表格
from .forms import MyUserCreationForm

import requests
from bs4 import BeautifulSoup
import time
from lxml import html
import json
import csv
import pandas as pd
import numpy as np
import plotly.offline as py
import plotly.figure_factory as ff
from sklearn.preprocessing import LabelEncoder #載入標籤功能  #Label Encoding = 標籤編碼
import plotly.graph_objects as go
#from django.http import HttpResponse
#from django.views.decorators.clickjacking import xframe_options_exempt


@login_required 
def dashboard(request):
    url = 'https://tw.sports.yahoo.com/npb/'
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}
        #headers 建立偽裝
    resp = requests.get(url, headers=headers)
    resp.encoding = "UTF-8"
    time.sleep(5)
    soup = BeautifulSoup(resp.text, "lxml")
    title = soup.select('h2')[0]
    news_title = title.text
    news_url = soup.find('a', class_="Fw(b) Td(n) C(#fff) C(#fff):h").get('href')
    news_title1 = soup.find_all('h3')
    news_url1 = soup.find_all('a', class_="ie-7_D(b)")
    url_list = []
    title_list = []
    for url in news_url1:
        url_list.append(url.get('href'))
    for title in news_title1[:3]:
        title_list.append(title.text.replace(u'\u3000', u''))
    
    news_title2 = soup.find_all('h3', class_='Mb(5px)')

    url_list1 = []
    title_list1 = []
    for item in news_title2:
        title_list1.append(item.a.text.replace(u'\u3000', u''))
        url_list1.append(item.a.get('href'))
    return render(
        request,
        'account/dashboard.html',
        {'news_title': news_title, 'news_url': news_url, 'news_title0':title_list[0], 
        'news_title1':title_list[1], 'news_title2':title_list[2],'news_url0': url_list[0], 
        'news_url1': url_list[1], 'news_url2': url_list[2], 'news_url3': url_list1[0],
        'news_url4': url_list1[1], 'news_title3': title_list1[0], 'news_title4': title_list1[1]}
    )


def register(request): #註冊帳號
    if request.method == 'POST':
        user_form = MyUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False) #先創造一個空的user, 不要commit
            new_user.set_password( #將密碼存成hash值
                user_form.cleaned_data['password1'] #用戶輸入的password值(UserCreationForm裡面的password有1跟2, 選一個當作認證)
            )
            new_user.save()
            return render(
                request,
                'account/register_dome.html',
                {'new_user': new_user}
            )
    else:
        user_form = MyUserCreationForm()
    return render(
        request,
        'account/register.html',
        {'user_form': user_form}
    )

def mlbData(request):
    return render(request, 'account/mlbData.html')

def mlbSO_HR(request):
    return render(request, 'account/mlbSO_HR.html')

def mlbBB_HR(request):
    return render(request, 'account/mlbBB_HR.html')
    
def npbData(request):
    return render(request, 'account/npbData.html')




""" @xframe_options_exempt
def register_views(request):
    return render(request,'account/mlbData.html') """

""" def mlbData(request):
    mlbdf = pd.read_csv('mlbTest.csv')
    table = ff.create_table(mlbdf)
    barPlayer = py.plot(table)

    data = [go.Bar(x=mlbdf.playerName, y=mlbdf.babip)]
    barData = py.plot(data)
    return render(
        request,
        'account/mlbData.html',
        {'mlbdf': (py.plot(table))},
        {'data': (py.plot(data))}
    ) """

""" def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'],)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse(
                        'Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form}) """
