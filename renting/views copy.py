from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Company
from .forms import CompanyForm


def company_view(request):
    # print("SALUR")
    # msg = "Salut tu es sur la page de la compagny"

    # number = 10
    # vDic = {'number': number, 'message': msg, 'companys': companys}
    return render(request, 'renting/company.html')
    # return render(request, 'renting/renting.html', vDic)

def createCompany(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        company = Company.objects.filter(name='PRemiere').values().first()
        print("ALLL:", company)
        print("Company 1:", company['name'])
        return HttpResponseRedirect('/renting/company')

def updateCompany(request, pk):
    company = Company.objects.get(id=pk)
    form = CompanyForm(instance=company)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('companies')
    context = {'form': form}
    return render(request, 'renting/company_form.html', context)

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

def test(request, pk):
    companys = Company.objects.get(id=pk)
    return render(request, 'renting/rentings.html', {'companys': companys})

def main(request):
    return render(request, 'renting/main.html')

def dashboard(request):
    return render(request, 'renting/dashboard.html')

def navbar(request):
    return render(request, 'renting/navbar3.html')



