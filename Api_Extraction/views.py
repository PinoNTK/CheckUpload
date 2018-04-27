from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from Api_Extraction.extraction import Extraction
import os

from recruitment_recommender_system.settings import BASE_DIR
import json
dir_path = os.path.join(BASE_DIR,'Api_Extraction/cv')

extraction = Extraction(BASE_DIR)
@api_view(['GET'])
def extract_cv(request,pathfile):
    return Response(extraction.parse_cv(os.path.join(dir_path,pathfile)))


@api_view(['GET','POST'])
def Upload_CV(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        fs = FileSystemStorage()

        filename = fs.save('cv/'+myfile.name, myfile)

        result_json = (extraction.parse_cv(fs.path(filename)))
        url = fs.url(filename)
        return render(request,'templates/Info.html' ,context={'msg':json.dumps(result_json, ensure_ascii=False)})

    return render(request, 'templates/index.html',context={'msg':json.dumps({})})