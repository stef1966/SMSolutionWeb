from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        # exclude = ['payment_method']
        # print("TYPE:", fields)
        # fields.__add__('ALLO')
        # widgets = {
        #     'payment_method': forms.Textarea      
        # }
        # fields = ['name', 'logo', 'language', 'units']

class RawCompanyForm(forms.Form):
    name = forms.CharField()
    logo = forms.ImageField()
    language = forms.CharField()
    units = forms.CharField()
    telephone = forms.CharField()
    email = forms.CharField()
    address_street_num = forms.CharField()
    address_street_name = forms.CharField()
    address_city = forms.CharField()
    address_province = forms.CharField()
    address_postal_code = forms.CharField()
    address_country = forms.CharField()
    page_web = forms.CharField()
    telephoone1_name = forms.CharField()
    telephoone1_num = forms.CharField()
    telephoone2_name = forms.CharField()
    telephoone2_num = forms.CharField()
    contact1_firstname = forms.CharField()
    contact1_lastname = forms.CharField()
    contact1_email = forms.CharField()
    contact1_tel = forms.CharField()
    contact1_cell = forms.CharField()
    contact2_firstname = forms.CharField()
    contact2_lastname = forms.CharField()
    contact2_email = forms.CharField()
    contact2_tel = forms.CharField()
    contact2_cell = forms.CharField()
    payment_method = forms.CharField()
    inv_letters_before = forms.CharField()
    inv_add_year = forms.BooleanField()
    inv_length = forms.IntegerField()
    inv_advise_days_bf = forms.IntegerField()
    taxes1_name = forms.CharField()
    taxes1_num = forms.CharField()
    taxes1_pourc = forms.IntegerField()
    taxes2_name = forms.CharField()
    taxes2_num = forms.CharField()
    taxes2_pourc = forms.IntegerField()
    taxes3_name = forms.CharField()
    taxes3_num = forms.CharField()
    taxes3_pourc = forms.IntegerField()

    couleurstatuslibre = forms.CharField() 
    couleurstatuslouer = forms.CharField()  
    couleurstatusindispo = forms.CharField() 
    couleurstatusreserver = forms.CharField()
    couleurstatustlibre = forms.CharField()
    couleurstatustlouer = forms.CharField()
    couleurstatustindispo = forms.CharField()
    couleurstatustreserver = forms.CharField()
    couleur1mois = forms.CharField()
    couleur2mois = forms.CharField()
    couleur3mois = forms.CharField()
    couleur4mois = forms.CharField()
    couleur5mois = forms.CharField()
    couleur6mois = forms.CharField()
    couleur1tmois = forms.CharField()
    couleur2tmois = forms.CharField()
    couleur3tmois = forms.CharField()
    couleur4tmois = forms.CharField()
    couleur5tmois = forms.CharField()
    couleur6tmois = forms.CharField()

