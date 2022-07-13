from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------

class Language(models.Model):
    reference = models.CharField(max_length=200, unique=True)
    sentence_en = models.TextField()
    sentence_fr = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.AutoField(primary_key=True)

    # Display titel in admin page instead of id, so more clean
    def __str__(self):
        return self.reference

class Company(models.Model):
    language_choice = (('en', 'English'),('fr', 'French'),)
    units_choice = (('met', 'Metric'),('imp', 'Imperial'),)
    # payment_method = (('credit', 'Carte de crédit'),('int', 'Interac'),('trans', 'Transfert bancaire'),('compt', 'Comptant'),('other', 'Autre'))
    
    name = models.CharField(max_length=200)
    logo = models.ImageField(null=True, blank=True, default="default.jpg")
    language = models.CharField(max_length=100, default="fr", choices=language_choice)
    units = models.CharField(max_length=20, default="metric", choices=units_choice)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address_street_num = models.CharField(max_length=20, null=True, blank=True)
    address_street_name = models.CharField(max_length=100, null=True, blank=True)
    address_city = models.CharField(max_length=100, null=True, blank=True)
    address_province = models.CharField(max_length=30, null=True, blank=True)
    address_postal_code = models.CharField(max_length=10, null=True, blank=True)
    address_country = models.CharField(max_length=50, null=True, blank=True)
    page_web = models.CharField(max_length=100, null=True, blank=True)
    telephone1_name = models.CharField(max_length=50, null=True, blank=True)
    telephone1_num = models.CharField(max_length=20, null=True, blank=True)
    telephone2_name = models.CharField(max_length=50, null=True, blank=True)
    telephone2_num = models.CharField(max_length=20, null=True, blank=True)
    contact1_firstname = models.CharField(max_length=50, null=True, blank=True)
    contact1_lastname = models.CharField(max_length=50, null=True, blank=True)
    contact1_email = models.CharField(max_length=100, null=True, blank=True)
    contact1_tel = models.CharField(max_length=20, null=True, blank=True)
    contact1_cell = models.CharField(max_length=20, null=True, blank=True)
    contact2_firstname = models.CharField(max_length=50, null=True, blank=True)
    contact2_lastname = models.CharField(max_length=50, null=True, blank=True)
    contact2_email = models.CharField(max_length=100, null=True, blank=True)
    contact2_tel = models.CharField(max_length=20, null=True, blank=True)
    contact2_cell = models.CharField(max_length=20, null=True, blank=True)
    # payment_method = models.CharField(max_length=255, null=True, blank=True, choices=units_choice)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    inv_letters_before = models.CharField(max_length=10, null=True, blank=True)
    inv_add_year = models.BooleanField(default=False, null=True, blank=True)
    inv_length = models.IntegerField(default=0, null=True, blank=True)
    inv_advise_days_bf = models.IntegerField(default=0, null=True, blank=True)
    taxes1_name = models.CharField(max_length=20, null=True, blank=True)
    taxes1_num = models.CharField(max_length=50, null=True, blank=True)
    taxes1_pourc = models.IntegerField(default=0, null=True, blank=True)
    taxes2_name = models.CharField(max_length=20, null=True, blank=True)
    taxes2_num = models.CharField(max_length=50, null=True, blank=True)
    taxes2_pourc = models.IntegerField(default=0, null=True, blank=True)
    taxes3_name = models.CharField(max_length=20, null=True, blank=True)
    taxes3_num = models.CharField(max_length=50, null=True, blank=True)
    taxes3_pourc = models.IntegerField(default=0, null=True, blank=True)

    couleurstatuslibre = models.CharField(max_length=10, blank=True, null=True) 
    couleurstatuslouer = models.CharField(max_length=10, blank=True, null=True)  
    couleurstatusindispo = models.CharField(max_length=10, blank=True, null=True) 
    couleurstatusreserver = models.CharField(max_length=10, blank=True, null=True)
    couleurstatustlibre = models.CharField(max_length=10, blank=True, null=True)
    couleurstatustlouer = models.CharField(max_length=10, blank=True, null=True)
    couleurstatustindispo = models.CharField(max_length=10, blank=True, null=True)
    couleurstatustreserver = models.CharField(max_length=10, blank=True, null=True)
    couleur1mois = models.CharField(max_length=10, blank=True, null=True)
    couleur2mois = models.CharField(max_length=10, blank=True, null=True)
    couleur3mois = models.CharField(max_length=10, blank=True, null=True)
    couleur4mois = models.CharField(max_length=10, blank=True, null=True)
    couleur5mois = models.CharField(max_length=10, blank=True, null=True)
    couleur6mois = models.CharField(max_length=10, blank=True, null=True)
    couleur1tmois = models.CharField(max_length=10, blank=True, null=True)
    couleur2tmois = models.CharField(max_length=10, blank=True, null=True)
    couleur3tmois = models.CharField(max_length=10, blank=True, null=True)
    couleur4tmois = models.CharField(max_length=10, blank=True, null=True)
    couleur5tmois = models.CharField(max_length=10, blank=True, null=True)
    couleur6tmois = models.CharField(max_length=10, blank=True, null=True)

    latitude = models.CharField(max_length=70, blank=True, null=True, default="")
    longitude = models.CharField(max_length=70, blank=True, null=True, default="")

    realestate_id = models.ManyToManyField('RealEstate', through='RealEstate_Company', blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Display titel in admin page instead of id, so more clean
    def __str__(self):
        return self.name
   
class RealEstate(models.Model):
    building_choice = (('room', 'Room'),('whareouse', 'Wharehouse'),('building', 'Building'),
        ('house', 'House'),('self_storage', 'Self storage'),('local', 'Local'),)

    type = models.CharField(max_length=40, choices=building_choice)
    commercial = models.BooleanField(default=False, null=True, blank=True)
    number = models.CharField(max_length=100, null=True, blank=True)
    address_street_num = models.CharField(max_length=20, null=True, blank=True)
    address_street_name = models.CharField(max_length=100, null=True, blank=True)
    address_city = models.CharField(max_length=100, null=True, blank=True)
    address_province = models.CharField(max_length=30, null=True, blank=True)
    address_postal_code = models.CharField(max_length=10, null=True, blank=True)
    address_country = models.CharField(max_length=50, null=True, blank=True)
    page_web = models.CharField(max_length=100, null=True, blank=True)
    telephone1_name = models.CharField(max_length=50, null=True, blank=True)
    telephone1_num = models.CharField(max_length=20, null=True, blank=True)
    telephone2_name = models.CharField(max_length=50, null=True, blank=True)
    telephone2_num = models.CharField(max_length=20, null=True, blank=True)
    contact1_firstname = models.CharField(max_length=50, null=True, blank=True)
    contact1_lastname = models.CharField(max_length=50, null=True, blank=True)
    contact1_email = models.CharField(max_length=100, null=True, blank=True)
    contact1_tel = models.CharField(max_length=20, null=True, blank=True)
    contact1_cell = models.CharField(max_length=20, null=True, blank=True)
    contact2_firstname = models.CharField(max_length=50, null=True, blank=True)
    contact2_lastname = models.CharField(max_length=50, null=True, blank=True)
    contact2_email = models.CharField(max_length=100, null=True, blank=True)
    contact2_tel = models.CharField(max_length=20, null=True, blank=True)
    contact2_cell = models.CharField(max_length=20, null=True, blank=True)

    length = models.IntegerField(default=0, null=True, blank=True)
    width = models.IntegerField(default=0, null=True, blank=True)
    length_letters = models.CharField(max_length=10, null=True, blank=True)
    width_letters = models.CharField(max_length=10, null=True, blank=True)

    area = models.IntegerField(default=0, null=True, blank=True)
    price_month = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    price_year = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    number_floor = models.IntegerField(default=0, null=True, blank=True)
    floor_number = models.IntegerField(default=0, null=True, blank=True)
    door_entrence = models.CharField(max_length=10, null=True, blank=True)
    door_width = models.IntegerField(default=0, null=True, blank=True)
    electricity = models.BooleanField(default=False, null=True, blank=True)
    parking = models.IntegerField(default=0, null=True, blank=True)
    doorcode = models.IntegerField(default=0, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    date_available = models.DateField(null=True, blank=True)
    SMSW_Date = models.DateField(null=True, blank=True)
    app_size = models.CharField(max_length=20, null=True, blank=True)
    bedroom = models.IntegerField(default=0, null=True, blank=True)
    washroom = models.IntegerField(default=0, null=True, blank=True)
    bathroom = models.IntegerField(default=0, null=True, blank=True)
    balcony = models.IntegerField(default=0, null=True, blank=True)
    included = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    draw_shape = models.CharField(max_length=200, null=True, blank=True)
    p = models.IntegerField(default=0, null=True, blank=True)
    

    company_id = models.ManyToManyField(Company, through='RealEstate_Company')
    created = models.DateField(auto_now_add=True, null=True, blank=True)
    updated = models.DateField(auto_now=True, null=True, blank=True)
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    id=models.AutoField(primary_key=True)

    # Display titel in admin page instead of id, so more clean
    def __str__(self):
        return self.type

class RealEstate_Company(models.Model):
    related_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    related_RealEstate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
   
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Display titel in admin page instead of id, so more clean
    def __str__(self):
        return str(self.related_RealEstate)

class Clients(models.Model):
    client_id=models.AutoField(primary_key=True)
    salutation = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    compagnie = models.CharField(max_length=150, blank=True, null=True)

    my_string = [salutation, name, lastname, compagnie]
    # my_string2 = [str(salutation), str(name), str(lastname), str(compagnie)]

    defaultFullname = " ".join(filter(None, str(my_string)))
    fullname = models.CharField(max_length=255, blank=True, null=True, default="salut")

    telephone = models.CharField(max_length=20, blank=True, null=True)
    telephone2 = models.CharField(max_length=20, blank=True, null=True)
    telephonedetails = models.CharField(max_length=40, blank=True, null=True)
    telephone2details = models.CharField(max_length=40, blank=True, null=True)
    website = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    email2 = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    typecontact = models.CharField(max_length=50, blank=True, null=True)
    address_full = models.CharField(max_length=255, blank=True, null=True)
    address_street = models.CharField(max_length=100, blank=True, null=True)
    address_city = models.CharField(max_length=50, blank=True, null=True)
    address_province = models.CharField(max_length=50, blank=True, null=True)
    address_country = models.CharField(max_length=100, blank=True, null=True)
    address_postalcode = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    pucenum = models.CharField(max_length=50, blank=True, null=True)
    facturesuivi = models.BooleanField(default=False, null=True, blank=True)
    facturesuivi2 = models.BooleanField(default=False, null=True, blank=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # rContrats=models.ManyToManyField('Contrats', through='Client_Contrat')
    # rAttentes=models.ManyToManyField('EntrepotsbAppContrats', through='EntrepotsbAppContratclient')

    # Display titel in admin page instead of id, so more clean
    def __str__(self):
        return str(self.fullname)

# class Client_Contrat(models.Model):
#     related_client = models.ForeignKey(Clients, on_delete=models.CASCADE)
#     related_contrat = models.ForeignKey(Contrats, on_delete=models.CASCADE)
   
#     created = models.DateField(auto_now_add=True)
#     updated = models.DateField(auto_now=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

#     # Display titel in admin page instead of id, so more clean
#     def __str__(self):
#         return str(self.related_client)