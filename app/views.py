from django.shortcuts import render

from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def registration(request):
    ETMFO=TopicMF()
    EWMFO=WebpageMF()
    EARMFO=AccessRecordMF()
    d={'ETMFO':ETMFO,'EWMFO':EWMFO,'EARMFO':EARMFO}

    if request.method=='POST':
        NMTMFO=TopicMF(request.POST)
        NMWMFO=WebpageMF(request.POST)
        NMARMFO=AccessRecordMF(request.POST)

        if NMTMFO.is_valid() and NMWMFO.is_valid() and NMARMFO.is_valid():
            MTMFO=NMTMFO.save(commit=False)
            MTMFO.save()

            #---------------------------------

            MWMFO=NMWMFO.save(commit=False)
            MWMFO.topic_name=MTMFO
            MWMFO.save()

           # ----------------------------------

            MARMFO=NMARMFO.save(commit=False)
            MARMFO.name=MWMFO
            MARMFO.save()

            return HttpResponse('REGISTRATION SUCCESSFULL........')
        else:
            return HttpResponse('INVALID!!!!')

    return render(request,'registration.html',d)