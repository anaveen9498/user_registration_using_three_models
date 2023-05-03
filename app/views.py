from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.



def registration(request):
    TopicObject=TopicForm()
    WebObject=WebpageForm()
    AccessObject=AccessRecordsForm()
    A={'TFO':TopicObject, 'WFO':WebObject, 'AFO':AccessObject}
    

    if request.method=='POST':
        TopicData=TopicForm(request.POST)
        WebData=WebpageForm(request.POST)
        AccessData=AccessRecordsForm(request.POST)

        if TopicData.is_valid() and WebData.is_valid() and AccessData.is_valid():
            Not_Saved_Topic_Dta=TopicData.save(commit=False)
            Not_Saved_Topic_Dta.save()

            Not_Saved_Web_Data=WebData.save(commit=False)
            Not_Saved_Web_Data.topic_name=Not_Saved_Topic_Dta
            Not_Saved_Web_Data.save()

            Not_Saved_Access_Dta=AccessData.save(commit=False)
            Not_Saved_Access_Dta.player_name=Not_Saved_Web_Data
            Not_Saved_Access_Dta.save()
            

            return HttpResponse('Yours Players Data Is Successfully Registered ! ! !')
        return HttpResponse('Your Entered Invalid Data....')
    
    return render(request,'registration.html',A)