from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Background(models.Model):
    image = models.ImageField(upload_to='back_images/')  # You need to define the 'upload_to' path


class Heroslider(models.Model):
  
    image = models.ImageField(upload_to='hero_sliderimages/')  # You need to define the 'upload_to' path
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.description

class Abouttwo(models.Model):
    icon = models.FileField(upload_to='about_images/')  # You need to define the 'upload_to' path.
    heading = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
   
    def __str__(self):
        return self.heading

class Aboutone(models.Model):
    description = models.TextField()
    story = models.TextField()

    def __str__(self):
        return self.description


class Whyusone(models.Model):
    heading = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    readmore = models.TextField(default="yes")
   
    def __str__(self):
        return self.heading        


class Whyustwo(models.Model):
    icon = models.FileField(upload_to='whyus_images/')  # You need to define the 'upload_to' path.
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
   
    def __str__(self):
        return self.title        



class Healthvalues(models.Model):
    item = models.CharField(max_length=500)  

    def __str__(self):
        return self.item              


class FaqsTable(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.question



class Gallery(models.Model):
    images = models.ImageField(upload_to='gallery/')  # You need to define the 'upload_to' path.  

    
    def __str__(self):
        return self.images      



class Testimonials(models.Model):
    image = models.ImageField(upload_to='testimonials/')  # You need to define the 'upload_to' path.
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)  
    words = models.CharField(max_length=700)  

    
    def __str__(self):
        return self.image              






class Product(models.Model):
    image = models.ImageField(upload_to='product_images/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    diseases = models.TextField()  # Store diseases as a comma-separated string

    def __str__(self):
        return self.title



class Hero(models.Model):
    image = models.ImageField(upload_to='hero_images/')
    mainheading = models.CharField(max_length=255)
    subheading = models.TextField()


    def __str__(self):
        return self.mainheading



class Privacy(models.Model):
   privacies = models.TextField()

   def __str__(self):
        return self.privacies



class Security(models.Model):
   securities = models.TextField()



   def __str__(self):
        return self.securities        


class Service(models.Model):
   image = models.FileField(upload_to='service_images/')
   service = models.TextField()
   description = models.TextField(default="description")



   def __str__(self):
        return self.service        


class Strategicone(models.Model):
   image = models.FileField(upload_to='strategic_images/')
   heading = models.TextField()
   description = models.TextField()



   def __str__(self):
        return self.heading               


class Strategictwo(models.Model):
   image = models.FileField(upload_to='strategic_images/')
   heading = models.TextField()
   description = models.TextField()



   def __str__(self):
        return self.heading



class WeeklyMessage(models.Model):
    week = models.CharField(max_length=200)
    message = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # Added for message state
    has_badge = models.BooleanField(default=False)  # Added for badge


    def __str__(self):
        return self.week  



class SocietyFormSubmission(models.Model):


    

    date_of_birth = models.DateField()
    gender = models.CharField(max_length=255, choices=[('Me', 'Me'), ('ke', 'Ke')])
    occupation = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    health_status_description = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    has_disease = models.BooleanField()
    disease_name = models.CharField(max_length=255, blank=True, null=True)
    medication_used = models.CharField(max_length=255, blank=True, null=True)
    treatment_facility = models.CharField(max_length=255, choices=[
        ('Kliniki ya tiba mbadala', 'Kliniki ya tiba mbadala'),
        ('Zahanati', 'Zahanati'),
        ('Kituo cha Afya', 'Kituo cha Afya'),
        ('Hospitali', 'Hospitali'),
        ('Duka la dawa', 'Duka la dawa'),
    ], blank=True, null=True)
    
    has_allergy = models.BooleanField()
    allergy_description = models.TextField(blank=True, null=True)
    
    family_health_conditions = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Society Form Submission - {self.date_of_birth}"



class CompanyVideo(models.Model):
    Video = models.FileField(upload_to='companyvideo/')  # You need to define the 'upload_to' path        
    


# class SocietyFormSubmission(models.Model):
#     date_of_birth = models.DateField()
#     gender = models.CharField(max_length=255, choices=[('Me', 'Me'), ('ke', 'Ke')])
#     occupation = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)
#     region = models.CharField(max_length=255)
#     district = models.CharField(max_length=255)
#     ward = models.CharField(max_length=255)
#     neighborhood = models.CharField(max_length=255)
#     health_status_description = models.TextField()
    
#     has_disease = models.BooleanField()
#     disease_name = models.CharField(max_length=255, blank=True, null=True)
#     medication_used = models.CharField(max_length=255, blank=True, null=True)
#     treatment_facility = models.CharField(max_length=255, choices=[
#         ('Kliniki ya tiba mbadala', 'Kliniki ya tiba mbadala'),
#         ('Zahanati', 'Zahanati'),
#         ('Kituo cha Afya', 'Kituo cha Afya'),
#         ('Hospitali', 'Hospitali'),
#         ('Duka la dawa', 'Duka la dawa'),
#     ], blank=True, null=True)
    
#     has_allergy = models.BooleanField()
#     allergy_description = models.TextField(blank=True, null=True)
    
#     family_health_conditions = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"Society Form Submission - {self.date_of_birth}"




        




