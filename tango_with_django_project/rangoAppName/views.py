from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect

from django.contrib.auth.models import User
import regex as re
import pandas as pd
from .forms import FeedbackForm
from .forms import MyForm
from .models import DataTable
User="User1"
user_id=6
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rangoAppName\index.html', context=context_dict)


def box_data_view(request):
    # Implement code to read data from the box file and prepare the data to be passed to the template
    boxes = r"C:\Users\reeba\Downloads\RK_himnae\valid.box"
    box = open(boxes, "r").read().strip().split('\n')
    summary_box= r"C:\Users\reeba\Downloads\RK_himnae\valid.summary"
    all_article_data=[]
    sum_box = open(summary_box, "r").read().strip().split('\n')
    sum_for_all_data=[]
    for summary in sum_box:
        sum_for_all_data.append(summary)
    index=0
    for article in box:
            data = []
            item = article.split('\t')
            for it in item:
                if len(it.split(':')) > 2:
                    continue
                # print it
                label, word = it.split(':')
                if(word!='<none>'):
                    data.append({'label': label, 'word': word})
                    
            all_article_data.append({'table':data,'Summary':sum_for_all_data[index]})
            index=index+1
                
            


    
    return render(request, 'rangoAppName/box_tables.html', {'data': all_article_data})

    

def landing_page_view(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    #context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rangoAppName\landing_page.html')


def summary_view(request):
    data_file_path = r"C:\Users\reeba\Downloads\summary.csv"
    df = pd.read_csv(data_file_path)
    data = df[['NewsArticleId','PegasusCnn', 'PegasusAdam', 'PegasusXsum','Golden']].iloc[0].to_dict()
    #return JsonResponse(json_data)
    return render(request, 'rangoAppName\Summary.html',{'data': data})


def na1_submit_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            User='User1'
            if User=='User1':
                s1m1_value = form.cleaned_data['s1m1']
                user_id_value=1
                news_article_id_value=1
                s1_cnn_original_value=s1m1_value
                

                DataTable.objects.create(s1_cnn_original=s1m1_value,user_id=user_id_value,news_article_id=1)
            return redirect('rangoAppName\success_page.html')
    data_file_path = r"C:\Users\reeba\Downloads\sample.csv"
    df = pd.read_csv(data_file_path)
    data = df[['NewsArticleId','PegasusCnn', 'PegasusAdam', 'PegasusXsum']].iloc[0].to_dict()
    return render(request, 'rangoAppName\landing_page.html',{'data': data})

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=1
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form2_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form1.html', {'form': form})
def summary_view(request):
    data_file_path = r"C:\Users\reeba\Downloads\sample.csv"
    df = pd.read_csv(data_file_path)
    data = df[['NewsArticleId','PegasusCnn', 'PegasusAdam', 'PegasusXsum']].iloc[0].to_dict()
    #return JsonResponse(json_data)
    return render(request, 'rangoAppName\Summary.html',{'data': data})


def na1_submit_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            User='User1'
            if User=='User1':
                s1m1_value = form.cleaned_data['s1m1']
                user_id_value=1
                news_article_id_value=1
                s1_cnn_original_value=s1m1_value
                

                DataTable.objects.create(s1_cnn_original=s1m1_value,user_id=user_id_value,news_article_id=1)
            return redirect('rangoAppName\success_page.html')
    data_file_path = r"C:\Users\reeba\Downloads\sample.csv"
    df = pd.read_csv(data_file_path)
    data = df[['NewsArticleId','PegasusCnn', 'PegasusAdam', 'PegasusXsum']].iloc[0].to_dict()
    return render(request, 'rangoAppName\landing_page.html',{'data': data})

def form2_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=2
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form3_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form2.html',{'form': form})
def form3_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=3
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form4_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form3.html',{'form': form})
def form4_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=4
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form5_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form4.html',{'form': form})
def form5_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=5
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form6_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form5.html',{'form': form})
def form6_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=6
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form7_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form6.html',{'form': form})
def form7_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=7
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form8_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form7.html',{'form': form})
def form8_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=8
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form9_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form8.html',{'form': form})
def form9_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=9
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form10_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form9.html',{'form': form})
def form10_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=10
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form11_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form10.html',{'form': form})

def form11_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=11
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form12_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form11.html',{'form': form})

def form12_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=12
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form13_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form12.html',{'form': form})
def form13_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=13
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form14_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form13.html',{'form': form})

def form14_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=14
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return redirect('rangoAppName:form15_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form14.html',{'form': form})

def form15_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        
        news_article_id=15
        if form.is_valid():
            # Handle the validated data
            if User=="User1":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User2":
                s1_cnn = form.cleaned_data['S1M1']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M1']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M1']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M1']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M1Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User3":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M3']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M3']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M3']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M3']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M3Rank']
            elif User=="User4":
                s1_cnn = form.cleaned_data['S1M2']
                s1_adam = form.cleaned_data['S1M3']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M2']
                s2_adam = form.cleaned_data['S2M3']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M2']
                s3_adam = form.cleaned_data['S3M3']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M2']
                s4_adam = form.cleaned_data['S4M3']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M2Rank']
                adam_rank=form.cleaned_data['M3Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            elif User=="User5":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M1']
                s1_xsum=form.cleaned_data['S1M2']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M1']
                s2_xsum=form.cleaned_data['S2M2']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M1']
                s3_xsum=form.cleaned_data['S4M2']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M1']
                s4_xsum=form.cleaned_data['S4M2']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M1Rank']
                Xsum_rank=form.cleaned_data['M2Rank']
            elif User=="User6":
                s1_cnn = form.cleaned_data['S1M3']
                s1_adam = form.cleaned_data['S1M2']
                s1_xsum=form.cleaned_data['S1M1']
                s2_cnn = form.cleaned_data['S2M3']
                s2_adam = form.cleaned_data['S2M2']
                s2_xsum=form.cleaned_data['S2M1']
                s3_cnn = form.cleaned_data['S3M3']
                s3_adam = form.cleaned_data['S3M2']
                s3_xsum=form.cleaned_data['S4M1']
                s4_cnn = form.cleaned_data['S4M3']
                s4_adam = form.cleaned_data['S4M2']
                s4_xsum=form.cleaned_data['S4M1']
                cnn_rank=form.cleaned_data['M3Rank']
                adam_rank=form.cleaned_data['M2Rank']
                Xsum_rank=form.cleaned_data['M1Rank']
            DataTable.objects.create(user_id=user_id,news_article_id=news_article_id,s1_cnn_original=s1_cnn,s1_adam=s1_adam,s1_xsum=s1_xsum,s2_cnn_original=s2_cnn,s2_adam=s2_adam,s2_xsum=s2_xsum,s3_cnn_original=s3_cnn,s3_adam=s3_adam,s3_xsum=s3_xsum,s4_cnn_original=s4_cnn,s4_adam=s4_adam,s4_xsum=s4_xsum,cnn_original_rank=cnn_rank,xsum_rank=Xsum_rank,adam_rank=adam_rank)
            return render(request, 'rangoAppName/Summary.html',{'form': form})
            return redirect('rangoAppName:form15_view')

    else:
        form = MyForm()
    return render(request, 'rangoAppName/form15.html',{'form': form})



