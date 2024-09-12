from rest_framework import serializers
from .models import *


class SocietyFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocietyFormSubmission
        fields = '__all__'  # Include all fields, including 'image'




class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = '__all__'  # Include all fields, including 'image'

class HerosliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroslider
        fields = '__all__'  # Include all fields, including 'image'        




class AbouttwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abouttwo
        fields = '__all__'  # Include all fields, including 'image'


class AboutoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutone
        fields = '__all__'  # Include all fields, including 'image'  


class WhyustwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whyustwo
        fields = '__all__'  # Include all fields, including 'image'


class WhyusoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whyusone
        fields = '__all__'            



class HealthvaluesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Healthvalues
        fields = '__all__'  # Include all fields, including 'image'              


class FaqsTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqsTable
        fields = '__all__'  # Include all fields, including 'image'



class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'  # Include all fields, including 'image'


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'  # Include all fields, including 'image'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Include all fields, including 'image'



class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'  # Include all fields, including 'image'        


class PrivacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Privacy
        fields = '__all__'  # Include all fields, including 'image'        

class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = '__all__'  # Include all fields, including 'image'        

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'  # Include all fields, including 'image'
        


class StrategiconeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategicone
        fields = '__all__'  # Include all fields, including 'image'                


class StrategictwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategictwo
        fields = '__all__'  # Include all fields, including 'image'        


class WeeklyMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyMessage
        fields = '__all__'  # Include all fields, including 'image'    




class CompanyVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyVideo
        fields = '__all__'  # Include all fields, including 'image'
