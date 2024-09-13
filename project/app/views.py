from django.shortcuts import render

# Create your views here.
def home(request):
    data={'key':'value','name':'deepa'}
    data1={}
    data2={}
    return render(request,'home.html',{'key':data,'key2':data1,'key3':data2})
def collection(request):
   data=[{'name':'deepa','age':25,'quali':'btech'},
   {'name':'disha','age':22,'quali':'btech'},
   {'name':'dia','age':23,'quali':'bsc'},
   {'name':'isha','age':21,'quali':'bca'},
   {'name':'disa','age':24,'quali':'btech'}]
   return render(request,'collection.html',{'data':data})
def myfilter(request):
    #return render(request,'myfilter.html',{'first':[20,3,45,6],'second':[30,10,20,8]},{'value':10})
    return render(request,'myfilter.html',{'name':"welcome to django class....."})