import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from .forms import UploadFileForm, dateForm, 
from .forms import *
# from .helper import clean_file, get_sublist, find_average, get_year_list
from .helper import *
from django.urls import reverse
import json


def home(request):
    return HttpResponse("Hello, Django")

def hello_there(request, name):
    
    print(request.build_absolute_uri()) #optional
    temp = {'name' : name, 'date': datetime.now()}
    return render(  

        request,
        'hello/hello_there.html',
        temp
        # {
            # 'name': name,
            # 'date': datetime.now()
        # }
    )

def file_select(request):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/file_upload.html',

    )

    
def upload_file(request):
    # print(request.method)
    params = {}
    if request.method == 'POST':
        
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES['file']
            # Process the file (e.g., read content)
            file_content = uploaded_file.read().decode('utf-8')
            clean_file_content = clean_file(file_content)
            # return render(request, 'hello/file_display.html', {'file_content': clean_file_content})
            
            request.session['list'] = clean_file_content
            return HttpResponseRedirect('file')
    else:
        form = UploadFileForm()

    return render(request, 'hello/upload_form.html', {'form': form})


def present_data(request):
    clean_file_content = request.session['list']
    context = {'file_content': clean_file_content}

    yearList = get_year_list(clean_file_content)
    # print(yearList)

    if request.method == 'POST':
        form = checkForm(yearList, request.POST)
        if form.is_valid():
            selected_items = form.cleaned_data['yearList']
            sublist = get_year_sublist(selected_items, clean_file_content)
            context = {'header': sublist[0], 'list': sublist[1:], 'headerJs': json.dumps(sublist[0]), 'listJs': json.dumps(sublist[1:])}
            return render(request, 'hello/result.html', context)
    else:
        form = checkForm(yearList)

    return render(request, 'hello/year_select.html', {'form': form})

    # if request.method == 'POST':
    #     form = dateForm(request.POST)
    #     if form.is_valid():
    #         selected_value = form.cleaned_data['date_dropdown']
    #         sublist = get_sublist(selected_value, clean_file_content)
    #         avgList = find_average(sublist)
    #         # print(sublist)
    #         context = {'header': sublist[0], 'list': sublist[1:], 'headerJs': json.dumps(sublist[0]), 'listJs': json.dumps(sublist[1:])}
    #         return render(request, 'hello/result.html', context)
    # else:
    #     form = dateForm()

    # return render(request, 'hello/user_date.html', {'form':form} )
    #return render(request, 'hello/file_display.html', context)