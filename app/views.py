

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import io
import urllib, base64
import datetime



def index(request):
    URL = 'https://www.worldometers.info/coronavirus/country/india/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    mydiv = soup.findAll("div", {"class": "maincounter-number"})
    #print(mydiv)
    stats = []
    for i in mydiv:
        stats.append(i.contents[1].text)
    #print(stats)
    #print(type(mydiv))
    a=5
    currentinfected=stats[0]
    currentdeaths=stats[1]
    currentrecovered=stats[2]
    print(currentinfected)
    

    URL = 'https://www.mohfw.gov.in/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
    mydiv = soup.findAll("div", {"class": "data-table table-responsive"})
#print(type(mydiv))
    mydiv=mydiv[0]
    myt= mydiv.find_all('td')
    print(myt)

#print(myt)
#print(type(myt))
#myt=myt[0]
#print(myt[0].contents[0])
    statecount=[]
    statename= []
    stateinfected=[]
    statedeath=[]
    staterecovered=[]
    i=0
    while(i<160):
        statecount.append(myt[i].contents[0])
        statename.append(myt[i+1].contents[0])
        stateinfected.append(myt[i+2].contents[0])
        staterecovered.append(myt[i+3].contents[0])
        statedeath.append(myt[i+4].contents[0])
        #print("next")
        i=i+5

   
    
    currentinfected=sum([int(i) for i in stateinfected])
    currentrecovered=sum([int(i) for i in staterecovered])
    currentdeaths=sum([int(i) for i in statedeath])
    
    statedata= zip(statename, stateinfected, staterecovered, statedeath)

    context = {'currentinfected' : currentinfected,'segment' : 'index','currentrecovered' : currentrecovered,'currentdeaths' : currentdeaths, 'statedata':statedata}    
    return render(request, "myhome.html", context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    
    try:

        load_template = request.path.split('/')[-1]

        context['segment'] = load_template

        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))


def importantlinks(request):
    context={}
    return render(request, "importantlinks.html", context)


def statewise(request):
    URL = 'https://www.mohfw.gov.in/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
    mydiv = soup.findAll("div", {"class": "data-table table-responsive"})
#print(type(mydiv))
    mydiv=mydiv[0]
    myt= mydiv.find_all('td')
    print(myt)

#print(myt)
#print(type(myt))
#myt=myt[0]
#print(myt[0].contents[0])
    statecount=[]
    statename= []
    stateinfected=[]
    statedeath=[]
    staterecovered=[]
    i=0
    while(i<160):
        statecount.append(myt[i].contents[0])
        statename.append(myt[i+1].contents[0])
        stateinfected.append(myt[i+2].contents[0])
        staterecovered.append(myt[i+3].contents[0])
        statedeath.append(myt[i+4].contents[0])
        #print("next")
        i=i+5

   
    
    currentinfected=sum([int(i) for i in stateinfected])
    currentrecovered=sum([int(i) for i in staterecovered])
    currentdeaths=sum([int(i) for i in statedeath])
    
    statedata= zip(statename, stateinfected, staterecovered, statedeath)

    context = {'currentinfected' : currentinfected,'segment' : 'index','currentrecovered' : currentrecovered,'currentdeaths' : currentdeaths, 'statedata':statedata, 'statename':statename,'staterecovered':staterecovered,'statedeath':statedeath,'stateinfected':stateinfected}    
    return render(request, "statewise.html", context)





def infectedstate(request):
    URL = 'https://www.mohfw.gov.in/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
    mydiv = soup.findAll("div", {"class": "data-table table-responsive"})
#print(type(mydiv))
    mydiv=mydiv[0]
    myt= mydiv.find_all('td')
    print(myt)

#print(myt)
#print(type(myt))
#myt=myt[0]
#print(myt[0].contents[0])
    statecount=[]
    statename= []
    stateinfected=[]
    statedeath=[]
    staterecovered=[]
    i=0
    while(i<160):
        statecount.append(myt[i].contents[0])
        statename.append(myt[i+1].contents[0])
        stateinfected.append(myt[i+2].contents[0])
        staterecovered.append(myt[i+3].contents[0])
        statedeath.append(myt[i+4].contents[0])
        #print("next")
        i=i+5

   
    
    currentinfected=sum([int(i) for i in stateinfected])
    currentrecovered=sum([int(i) for i in staterecovered])
    currentdeaths=sum([int(i) for i in statedeath])
    
    statedata= zip(statename, stateinfected, staterecovered, statedeath)

    context = {'currentinfected' : currentinfected,'segment' : 'index','currentrecovered' : currentrecovered,'currentdeaths' : currentdeaths, 'statedata':statedata, 'statename':statename,'staterecovered':staterecovered,'statedeath':statedeath,'stateinfected':stateinfected}    
    return render(request, "infectedstate.html", context)





def recoveredstate(request):
    URL = 'https://www.mohfw.gov.in/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
    mydiv = soup.findAll("div", {"class": "data-table table-responsive"})
#print(type(mydiv))
    mydiv=mydiv[0]
    myt= mydiv.find_all('td')
    print(myt)

#print(myt)
#print(type(myt))
#myt=myt[0]
#print(myt[0].contents[0])
    statecount=[]
    statename= []
    stateinfected=[]
    statedeath=[]
    staterecovered=[]
    i=0
    while(i<160):
        statecount.append(myt[i].contents[0])
        statename.append(myt[i+1].contents[0])
        stateinfected.append(myt[i+2].contents[0])
        staterecovered.append(myt[i+3].contents[0])
        statedeath.append(myt[i+4].contents[0])
        #print("next")
        i=i+5

   
    
    currentinfected=sum([int(i) for i in stateinfected])
    currentrecovered=sum([int(i) for i in staterecovered])
    currentdeaths=sum([int(i) for i in statedeath])
    
    statedata= zip(statename, stateinfected, staterecovered, statedeath)

    context = {'currentinfected' : currentinfected,'segment' : 'index','currentrecovered' : currentrecovered,'currentdeaths' : currentdeaths, 'statedata':statedata, 'statename':statename,'staterecovered':staterecovered,'statedeath':statedeath,'stateinfected':stateinfected}    
    return render(request, "recoveredstate.html", context)




def deathstate(request):
    URL = 'https://www.mohfw.gov.in/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
    mydiv = soup.findAll("div", {"class": "data-table table-responsive"})
#print(type(mydiv))
    mydiv=mydiv[0]
    myt= mydiv.find_all('td')
    print(myt)

#print(myt)
#print(type(myt))
#myt=myt[0]
#print(myt[0].contents[0])
    statecount=[]
    statename= []
    stateinfected=[]
    statedeath=[]
    staterecovered=[]
    i=0
    while(i<160):
        statecount.append(myt[i].contents[0])
        statename.append(myt[i+1].contents[0])
        stateinfected.append(myt[i+2].contents[0])
        staterecovered.append(myt[i+3].contents[0])
        statedeath.append(myt[i+4].contents[0])
        #print("next")
        i=i+5

   
    
    currentinfected=sum([int(i) for i in stateinfected])
    currentrecovered=sum([int(i) for i in staterecovered])
    currentdeaths=sum([int(i) for i in statedeath])
    
    statedata= zip(statename, stateinfected, staterecovered, statedeath)

    context = {'currentinfected' : currentinfected,'segment' : 'index','currentrecovered' : currentrecovered,'currentdeaths' : currentdeaths, 'statedata':statedata, 'statename':statename,'staterecovered':staterecovered,'statedeath':statedeath,'stateinfected':stateinfected}    
    return render(request, "deathstate.html", context)








def prediction(request, city_name):
    dataframe = pd.read_csv('complete.csv')
    # dfn = df.groupby('Date').sum()['Total Confirmed cases'].reset_index()
    df = dataframe.loc[dataframe['Name of State / UT'] == city_name, ['Date', 'Cured/Discharged/Migrated', 'Death',
                                                                  'Total Confirmed cases']]

    confirmed = df.groupby('Date').sum()['Total Confirmed cases'].reset_index()
    deaths = df.groupby('Date').sum()['Death'].reset_index()
    recovered = df.groupby('Date').sum()['Cured/Discharged/Migrated'].reset_index()

    k = confirmed.loc[['Name of State / UT'] == city_name:, 'Total Confirmed cases']
    kerala_confirmed = k.values.tolist()

    kerala_confirmed

    growth_diff = []

    for i in range(1, len(kerala_confirmed)):
        growth_diff.append(kerala_confirmed[i] / kerala_confirmed[i - 1])

    growth_factor = sum(growth_diff) / len(growth_diff)
    print('Average growth factor', growth_factor)

    dates = list(confirmed.loc[:, 'Date'])
    dates = list(pd.to_datetime(dates))
    dates_kerala = dates[:]

    prediction_dates = []

    start_date = dates_kerala[len(dates_kerala) - 1]
    for i in range(15):
        date = start_date + datetime.timedelta(days=1)
        prediction_dates.append(date)
        start_date = date

    cities = ['Kerala', 'Delhi', 'Telengana', 'Rajasthan', 'Haryana', 'Uttar Pradesh',
              'Tamil Nadu', 'Union Territory of Ladakh', 'Karnataka', 'Maharashtra',
              'Punjab', 'Union Territory of Jammu and Kashmir', 'Andhra Pradesh',
              'Uttarakhand', 'Odisha', 'Puducherry', 'West Bengal', 'Chhattisgarh',
              'Union Territory of Chandigarh', 'Gujarat', 'Chandigarh', 'Himachal Pradesh',
              'Jammu and Kashmir', 'Ladakh', 'Madhya Pradesh', 'Bihar', 'Manipur', 'Mizoram',
              'Andaman and Nicobar Islands', 'Goa', 'Assam', 'Jharkhand',
              'Arunachal Pradesh', 'Tripura']

    national_confirmed = []

    for city in cities:
        k = df.loc[:, 'Total Confirmed cases']
        national_confirmed.append(k.values.tolist())

    previous_day_cases = national_confirmed[5][len(dates_kerala) - 1]
    predicted_cases = []

    for i in range(15):
        predicted_value = previous_day_cases * growth_factor
        predicted_cases.append(predicted_value)
        previous_day_cases = predicted_value

    plt.figure(figsize=(15, 10))
    plt.xticks(rotation=90, fontsize=11)
    plt.yticks(fontsize=10)
    plt.xlabel("Dates", fontsize=20)
    plt.ylabel('Total cases', fontsize=20)
    plt.title("Predicted Values for the next 15 Days", fontsize=20)
    plt.plot_date(y=predicted_cases, x=prediction_dates, linestyle='-', color='c')

    fig = plt.gcf()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)



    context = {
        'data': uri
    }
    return render(request, 'prediction.html', context)












def predictionall(request):
    URL = 'https://www.worldometers.info/coronavirus/country/india/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    mydiv = soup.findAll("div", {"class": "maincounter-number"})
    # print(mydiv)
    stats = []
    for i in mydiv:
        stats.append(i.contents[1].text)
    # print(stats)
    # print(type(mydiv))
    a = 5
    currentinfected = stats[0]
    currentdeaths = stats[1]
    currentrecovered = stats[2]
    print(currentinfected)

    URL = 'https://www.mohfw.gov.in/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    mydiv = soup.findAll("div", {"class": "data-table table-responsive"})
    # print(type(mydiv))
    mydiv = mydiv[0]
    myt = mydiv.find_all('td')
    print(myt)

    # print(myt)
    # print(type(myt))
    # myt=myt[0]
    # print(myt[0].contents[0])
    statecount = []
    statename = []
    stateinfected = []
    statedeath = []
    staterecovered = []
    i = 0
    while (i < 160):
        statecount.append(myt[i].contents[0])
        statename.append(myt[i + 1].contents[0])
        stateinfected.append(myt[i + 2].contents[0])
        staterecovered.append(myt[i + 3].contents[0])
        statedeath.append(myt[i + 4].contents[0])
        # print("next")
        i = i + 5

    currentinfected = sum([int(i) for i in stateinfected])
    currentrecovered = sum([int(i) for i in staterecovered])
    currentdeaths = sum([int(i) for i in statedeath])

    statedata = zip(statename, stateinfected, staterecovered, statedeath)
    context = {'currentinfected': currentinfected, 'segment': 'index', 'currentrecovered': currentrecovered,
               'currentdeaths': currentdeaths, 'statedata': statedata}


    return render(request, 'predictionall.html', context)