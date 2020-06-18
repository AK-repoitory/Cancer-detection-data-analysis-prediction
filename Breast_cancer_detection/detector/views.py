import pickle
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import sys


from subprocess import run,PIPE
# Create your views here.
def home(request):
    return render(request,'temp/home.html')

def parent(request):
    return render(request,'temp/home.html')


def doc(request):
    return render(request,'doc.html')

def redirect_view(request):
    # return render(request,'form.html')
    return render(request,'temp/test.html') 


def About(request):
    return render(request,'temp/contact_us.html')
    # return render(request,'contact_us.html')

def submit(request):
    firstname = request.POST['firstname']
    age = int(request.POST['age'])
    lastname = request.POST['lastname']
    radius_mean = float(request.POST['radius_mean'])
    concavity_se = float(request.POST['concavity_se'])
    concave_points_se = float(request.POST['concave_points_se'])
    radius_worst = float(request.POST['radius_worst'])
    texture_worst = float(request.POST['texture_worst'])
    perimeter_worst = float(request.POST['perimeter_worst'])
    area_worst = float(request.POST['area_worst'])
    texture_mean = float(request.POST['texture_mean'])
    perimeter_mean = float(request.POST['perimeter_mean'])
    area_mean = float(request.POST['area_mean'])
    smoothness_mean = float(request.POST['smoothness_mean'])
    compactness_mean = float(request.POST['compactness_mean'])
    concavity_mean = float(request.POST['concavity_mean'])
    concave_points_mean = float(request.POST['concave_points_mean'])
    radius_se = float(request.POST['radius_se'])
    perimeter_se = float(request.POST['perimeter_se'])
    area_se = float(request.POST['area_se'])
    compactness_se = float(request.POST['compactness_se'])
    smoothness_worst = float(request.POST['smoothness_worst'])
    compactness_worst = float(request.POST['compactness_worst'])
    concavity_worst = float(request.POST['concavity_worst'])

    concave_points_worst = float(request.POST['concave_points_worst'])
    symmetry_worst = float(request.POST['symmetry_worst'])
    # lastname=lastname+'atul'
    # out = run([sys.executable,'//Users//DELL//Desktop//pyhon.py',lastname],shell=False,stout=PIPE)
    # print(out)

    loadm = pickle.load(open('a.sav','rb'))

    d=pd.DataFrame(dict(radius_mean_log=[],concavity_se_log=[],concave_points_se_log=[],radius_worst_log=[],texture_worst_log=[],perimeter_worst_log=[],area_worst_log=[],texture_mean_log=[],perimeter_mean_log=[],area_mean_log=[],smoothness_mean_log=[],compactness_mean_log=[],concavity_mean_log=[],concave_points_mean_log=[],radius_se_log=[],perimeter_se_log=[],area_se_log=[],compactness_se_log=[],smoothness_worst_log=[],compactness_worst_log=[],concavity_worst_log=[],concave_points_worst_log=[],symmetry_worst_log=[]))
    # new={'radius_mean_log':2.482545,'concavity_se_log':0.329457,'concave_points_se_log':0.104067,'radius_worst_log':3.009142,'texture_worst_log':3.323493,'perimeter_worst_log':5.305015,'area_worst_log':10.826478,'texture_mean_log':2.934507,'perimeter_mean_log':4.678428,'area_mean_log':9.01397,'smoothness_mean_log':0.476514,'compactness_mean_log':0.55364,'concavity_mean_log':0.552113,'concave_points_mean_log':0.443969,'radius_se_log':-0.823256,'perimeter_se_log':1.252191,'area_se_log':3.772761,'compactness_se_log':0.312679,'smoothness_worst_log':0.547482,'compactness_worst_log':0.848556,'concavity_worst_log':0.795927,'concave_points_worst_log':0.449889,'symmetry_worst_log':0.73846}
    n={'radius_mean_log':radius_mean,'concavity_se_log':concavity_se,'concave_points_se_log':concave_points_se,'radius_worst_log':radius_worst,'texture_worst_log':texture_worst,'perimeter_worst_log':perimeter_worst,'area_worst_log':area_worst,'texture_mean_log':texture_mean,'perimeter_mean_log':perimeter_mean,'area_mean_log':area_mean,'smoothness_mean_log':smoothness_mean,'compactness_mean_log':compactness_mean,'concavity_mean_log':concavity_mean,'concave_points_mean_log':concave_points_mean,'radius_se_log':radius_se,'perimeter_se_log':perimeter_se,'area_se_log':area_se,'compactness_se_log':compactness_se,'smoothness_worst_log':smoothness_worst,'compactness_worst_log':compactness_worst,'concavity_worst_log':concavity_worst,'concave_points_worst_log':concave_points_worst,'symmetry_worst_log':symmetry_worst}

    d=d.append(n,ignore_index=True)

    pecentage_matrix=loadm.predict_proba(d)
    print(pecentage_matrix)
    max_percentage=pecentage_matrix[0][1]*100
    min_percentage=pecentage_matrix[0][0]*100
    # e=fname*age*lastname
    return render(request,'result.html',{'max_percentage':max_percentage,'min_percentage':min_percentage,'fname':firstname,'lastname':lastname,'age':age})

def back(request):
    return render(request,'home.html')

def b(request):
    return render(request,'contact_us.html')