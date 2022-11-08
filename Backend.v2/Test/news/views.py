from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    r=requests.get('http://api.mediastack.com/v1/news?access_key=1b6cebc1da12d2e0981ddc8a46ff4e58&categories=sports&countries=in')
    res=r.json()
    data=res['data']
    title=[]
    description=[]
    image=[]
    url=[]
    for i in range(0,len(data)):
        title.append(data[i]['title'])
        description.append(data[i]['description'])
        image.append(data[i]['image'])
        url.append(data[i]['url'])
    
    news=zip(title,description,image,url)
    return render(request,'news/index.html',{'news':news})