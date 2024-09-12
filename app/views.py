from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from rest_framework.response import Response
from rest_framework import generics
from django.views.generic import TemplateView
from rest_framework.views import APIView
from .models import *
from .serializers import *



# def index(request):
#     context = {}
#     return render(request, 'index.html',context)



class SocietyFormSubmissionView(generics.ListCreateAPIView):
    queryset = SocietyFormSubmission.objects.all()
    serializer_class = SocietyFormSubmissionSerializer
    parser_classes = (MultiPartParser, FormParser,JSONParser)

    def perform_create(self, serializer):
        serializer.save()

class SocietyFormSubmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocietyFormSubmission.objects.all()
    serializer_class = SocietyFormSubmissionSerializer

    def perform_update(self, serializer):
        serializer.save(is_read=True)     


class SocietyFormSubmissionCountView(APIView):
    def get(self, request, format=None):
        count = SocietyFormSubmission.objects.filter(is_read=False).count()
        return Response({'count': count}) 




class BackgroundView(generics.ListCreateAPIView):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class BackgroundDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer


class HerosliderView(generics.ListCreateAPIView):
    queryset = Heroslider.objects.all()
    serializer_class = HerosliderSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class HerosliderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Heroslider.objects.all()
    serializer_class = HerosliderSerializer










# aboutfaqs xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class AbouttwoView(generics.ListCreateAPIView):
    queryset = Abouttwo.objects.all()
    serializer_class = AbouttwoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class AbouttwoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Abouttwo.objects.all()
    serializer_class = AbouttwoSerializer

# faqs views xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


class FaqsTableView(generics.ListCreateAPIView):
    queryset = FaqsTable.objects.all()
    serializer_class = FaqsTableSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class FaqsTableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FaqsTable.objects.all()
    serializer_class = FaqsTableSerializer



# gallery

class GalleryView(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class GalleryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer    





# testimonials


class TestimonialsView(generics.ListCreateAPIView):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class TestimonialsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer    




class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer        





# hero section


class HeroView(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class HeroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer    




class PrivacyView(generics.ListCreateAPIView):
    queryset = Privacy.objects.all()
    serializer_class = PrivacySerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class PrivacyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Privacy.objects.all()
    serializer_class = PrivacySerializer        



class SecurityView(generics.ListCreateAPIView):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class SecurityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer                


class ServiceView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer                


class AboutoneView(generics.ListCreateAPIView):
    queryset = Aboutone.objects.all()
    serializer_class = AboutoneSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class AboutoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aboutone.objects.all()
    serializer_class = AboutoneSerializer  






class HealthvaluesView(generics.ListCreateAPIView):
    queryset = Healthvalues.objects.all()
    serializer_class = HealthvaluesSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class HealthvaluesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Healthvalues.objects.all()
    serializer_class = HealthvaluesSerializer                


class WhyusoneView(generics.ListCreateAPIView):
    queryset = Whyusone.objects.all()
    serializer_class = WhyusoneSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class WhyusoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Whyusone.objects.all()
    serializer_class = WhyusoneSerializer     



class WhyustwoView(generics.ListCreateAPIView):
    queryset = Whyustwo.objects.all()
    serializer_class = WhyustwoSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class WhyustwoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Whyustwo.objects.all()
    serializer_class = WhyustwoSerializer                    




class StrategiconeView(generics.ListCreateAPIView):
    queryset = Strategicone.objects.all()
    serializer_class = StrategiconeSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class StrategiconeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Strategicone.objects.all()
    serializer_class = StrategiconeSerializer                    



class StrategictwoView(generics.ListCreateAPIView):
    queryset = Strategictwo.objects.all()
    serializer_class = StrategictwoSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class StrategictwoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Strategictwo.objects.all()
    serializer_class = StrategictwoSerializer     


class WeeklyMessageView(generics.ListCreateAPIView):
    queryset = WeeklyMessage.objects.all()
    serializer_class = WeeklyMessageSerializer
    parser_classes = (JSONParser,MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class WeeklyMessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeeklyMessage.objects.all()
    serializer_class = WeeklyMessageSerializer         

# catchall = TemplateView.as_view(template_name='index.html')




class CompanyVideoView(generics.ListCreateAPIView):
    queryset = CompanyVideo.objects.all()
    serializer_class = CompanyVideoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class CompanyVideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyVideo.objects.all()
    serializer_class = CompanyVideoSerializer