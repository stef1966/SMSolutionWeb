import re
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Company, Language, RealEstate
from .forms import CompanyForm
import folium

from datetime import datetime


language ={}
companys = Company.objects.all()

def setLanguage():
    global language
    languageChoosed = Company.objects.get(pk='2485b285a29546e5bfbde27b38d75a79').language
    lObject = Language.objects.all().values()
    language = {i['reference']:i['sentence_'+languageChoosed] for i in lObject}

setLanguage()

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('plan')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username OR password is incorrect")

    return render(request, 'renting/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, "User has been loged out")
    return redirect('login')


@login_required(login_url="login")
def company_view(request):
    global companys
    setLanguage()
    company = Company.objects.filter(pk='2485b285a29546e5bfbde27b38d75a79').values().first()
    return render(request, 'renting/company.html', {'company': company, 'companys': companys, 'language': language})

@login_required(login_url="login")
def map_all_view(request):
    global companys
    batiments = [{'lat': 45.53405077985435, 'lon': -73.2769563306875, 'name': "Mini entrepot Saint Basile"}]
    batiments =[]
    for i in companys:
        batimentDict = {'lat': i.latitude, 'lon': i.longitude, 'name': i.name}
        batiments.append(batimentDict)

    map = folium.Map(location=[45.53405077985435, -73.2769563306875], zoom_start=14, tiles="OpenStreetMap")

    fgv = folium.FeatureGroup(name="Real Estate")
    for batiment in batiments:
        print("Batiment:", batiment)
        nom = batiment['name']
        fgv.add_child(
            folium.Marker(
                location=[batiment['lat'], 
                        batiment['lon']
                        ], 
                popup=("<a target='_parent' href='http://127.0.0.1:8000/renting/company/'>Voir</a>"), 
                icon=folium.Icon(
                    color="green", icon="info-sign"
                ),
                tooltip=nom
            )
        )
    
    map.add_child(fgv)
    map.add_child(folium.LayerControl())
    map.save("templates/renting/map_alone.html")
    # map_html = map.get_root().render().replace('<!DOCTYPE html>', '')
    # print("MAP:", map_html)

    company = Company.objects.filter(pk='2485b285a29546e5bfbde27b38d75a79').values().first()
    companys = Company.objects.all()
    return render(request, 'renting/map_all.html', {'company': company, 'companys': companys, 'language': language})

@login_required(login_url="login")
def map_alone_view(request):
    return render(request, 'renting/map_alone.html')

@login_required(login_url="login")
def createCompany(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        company = Company.objects.filter(pk='2485b285a29546e5bfbde27b38d75a79').values().first()
        print("ALLL:", company)
        print("Company 1:", company['name'])
        return HttpResponseRedirect('/renting/company')

@login_required(login_url="login")
def updateCompany(request):
    company = Company.objects.get(pk='2485b285a29546e5bfbde27b38d75a79')
    form = CompanyForm(instance=company)

    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.instance.payment_method = request.POST.getlist('payment_method')
            add_year = request.POST.getlist('inv_add_year')
            form.instance.inv_add_year = True if add_year else False
            form.save()
            return redirect('company')
        else:
            print("NOT VALID:", form.errors)

    return HttpResponseRedirect('/renting/company')

@login_required(login_url="login")
def updateCompanyOLD(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        company = Company.objects.filter(name='PRemiere').values().first()
        print("ALLL:", company)
        print("FAVORITE:", request.POST)
        for key, value in company.items():
            # print("Key:", key, "Value:", value, " FROM POST:", request.POST.get(key))
            fromPost = request.POST.get(key)
           
            if value is None: value = ""
            if fromPost is None: fromPost = ""
            if str(value) != fromPost:
                print("Voici la différence:", "Key:", key, ":Value:", value, "Type:", type(value), ": FROM POST:", fromPost, ":Type:", type(fromPost), ":")
            # print("Key:", key, "Value:", value, " FROM POST:", )
        # updatedCie = Company()
        return HttpResponseRedirect('/renting/company')

@login_required(login_url="login")
def deleteCompany(request, pk):
    company = Company.objects.get(id=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('companies')
    context = {'object': company}
    return render(request, 'renting/delete_template.html', context)

# def createCompany(request):
#     form = CompanyForm()
#     if request.method == 'POST':
#         form = CompanyForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('companies')
#     context = {'form': form}
#     return render(request, 'renting/company_form.html', context)

# def updateCompany(request, pk):
#     company = Company.objects.get(id=pk)
#     form = CompanyForm(instance=company)
#     if request.method == 'POST':
#         form = CompanyForm(request.POST, request.FILES, instance=company)
#         if form.is_valid():
#             form.save()
#             return redirect('companies')
#     context = {'form': form}
#     return render(request, 'renting/company_form.html', context)

# def deleteCompany(request, pk):
#     company = Company.objects.get(id=pk)
#     if request.method == 'POST':
#         company.delete()
#         return redirect('companies')
#     context = {'object': company}
#     return render(request, 'renting/delete_template.html', context)

@login_required(login_url="login")
def test(request, pk):
    companys = Company.objects.get(id=pk)
    return render(request, 'renting/rentings.html', {'companys': companys})

@login_required(login_url="login")
def main(request):
    return render(request, 'renting/main.html')

@login_required(login_url="login")
def dashboard(request):
    return render(request, 'renting/dashboard.html')

@login_required(login_url="login")
def navbar(request):
    return render(request, 'renting/navbar3.html')

@login_required(login_url="login")
def testTemp(request):
    return render(request, 'renting/plan_alone.html')

@login_required(login_url="login")
def listClients(request):
    return render(request, 'renting/listClients.html')

@login_required(login_url="login")
def plan(request):
    company = Company.objects.filter(pk='2485b285a29546e5bfbde27b38d75a79').values().first()
    companys = Company.objects.all()
    return render(request, 'renting/plan.html', {'company': company, 'companys': companys, 'language': language})

@login_required(login_url="login")
def plan_alone_view(request):
    lineMonth = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    moisActual = datetime.now().month
    legendMois = {'m1': lineMonth[moisActual-1]}
    vMonth = moisActual 
    for i in range(1, 7):
        if vMonth >11: vMonth = vMonth -12
        legendMois["m"+str(i)] = lineMonth[vMonth-1]
        vMonth += 1
    
    realEstate = RealEstate.objects.all()
    print(realEstate)
    realEstateActualHtml = ""
    realEstate6MonthlHtml = ""
    vPixel = 0.237
    for local in realEstate:
        print(local)
        shapeList = list(str(local.draw_shape).split(","))
        print("shapeList", shapeList)
        if shapeList[0] == "None":
            vPositionX = 0
            vPositionY = 0
        else:
            # vPositionX = int(shapeList[0])
            # vPositionY = int(shapeList[1])
            vPositionX = (int(shapeList[0])-87)*0.9935 + 98
            vPositionY = (int(shapeList[1])-87)*0.994 + 102
            # vPositionX = 16 + int(shapeList[0])
            # vPositionY = 70 + int(shapeList[1])
            if shapeList[2] != "r":
                vProfondeur = local.length * vPixel
                vLargeur = local.width * vPixel
            else:
                vProfondeur = local.width * vPixel
                vLargeur = local.length * vPixel

        print("Local:", local.number, "positionX:", vPositionX, "positionY:", vPositionY)
        realEstateActualHtml += '<div class="rectangle tooltip layer1" style="height: ' + str(vProfondeur) + 'px;width: ' + str(vLargeur) + \
            'px;top: ' + str(vPositionY) + 'px;left: ' + str(vPositionX) + 'px">' + local.number + '<span class="tooltiptext">Tooltip text</span></div>'
    company = Company.objects.filter(pk='2485b285a29546e5bfbde27b38d75a79').values().first()
    return render(request, 'renting/plan_alone.html', {'company': company, 'legendMois': legendMois, 'actualHtml': realEstateActualHtml})

