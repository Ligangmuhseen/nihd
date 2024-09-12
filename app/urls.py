from django.urls import path
from .views import AbouttwoView, AbouttwoDetailView
from .views import FaqsTableView, FaqsTableDetailView
from .views import GalleryView, GalleryDetailView
from .views import TestimonialsView, TestimonialsDetailView
from .views import ProductView, ProductDetailView
from .views import HeroView, HeroDetailView
from .views import PrivacyView, PrivacyDetailView
from .views import SecurityView, SecurityDetailView
from .views import ServiceView, ServiceDetailView
from .views import AboutoneView, AboutoneDetailView
from .views import HealthvaluesView, HealthvaluesDetailView
from .views import BackgroundView, BackgroundDetailView
from .views import WhyusoneView,WhyusoneDetailView
from .views import WhyustwoView,WhyustwoDetailView
from .views import StrategiconeView,StrategiconeDetailView
from .views import StrategictwoView,StrategictwoDetailView
from .views import WeeklyMessageView,WeeklyMessageDetailView
from .views import HerosliderView,HerosliderDetailView
from .views import CompanyVideoView,CompanyVideoDetailView
from .views import SocietyFormSubmissionView,SocietyFormSubmissionDetailView,SocietyFormSubmissionCountView

from django.contrib.sitemaps.views import sitemap
from .sitemaps import (
    AboutoneSitemap, BackgroundSitemap, AbouttwoSitemap, FaqsTableSitemap,
    GallerySitemap, TestimonialsSitemap, ProductSitemap, HeroSitemap,
    PrivacySitemap, SecuritySitemap, ServiceSitemap, HealthvaluesSitemap,
    WhyusoneSitemap, WhyustwoSitemap, StrategiconeSitemap, StrategictwoSitemap,
    WeeklyMessageSitemap, HerosliderSitemap, SocietyFormSubmissionSitemap
)


from . import views
from django.urls import path, re_path
from django.views.generic import TemplateView


app_name = "app"

sitemaps = {
    'societyformsubmission': SocietyFormSubmissionSitemap,
    'aboutone': AboutoneSitemap,
    'background': BackgroundSitemap,
    'abouttwo': AbouttwoSitemap,
    'faqstable': FaqsTableSitemap,
    'gallery': GallerySitemap,
    'testimonials': TestimonialsSitemap,
    'product': ProductSitemap,
    'hero': HeroSitemap,
    'privacy': PrivacySitemap,
    'security': SecuritySitemap,
    'service': ServiceSitemap,
    'healthvalues': HealthvaluesSitemap,
    'whyusone': WhyusoneSitemap,
    'whyustwo': WhyustwoSitemap,
    'strategicone': StrategiconeSitemap,
    'strategictwo': StrategictwoSitemap,
    'weeklymessage': WeeklyMessageSitemap,
    'heroslider': HerosliderSitemap,
   
}


urlpatterns = [

   
    
    
    # path('login', views.index, name='index'),

    
    

    

     # aboutone
    path('aboutone/upload/', AboutoneView.as_view(), name='aboutone-list'),
    path('aboutone/upload/<int:pk>/', AboutoneDetailView.as_view(), name='aboutone-detail'),

      # background
    path('background/upload/', BackgroundView.as_view(), name='background-list'),
    path('background/upload/<int:pk>/', BackgroundDetailView.as_view(), name='background-detail'),

    # about2

    path('abouttwo/upload/', AbouttwoView.as_view(), name='abouttwo-list'),
    path('abouttwo/upload/<int:pk>/', AbouttwoDetailView.as_view(), name='abouttwo-detail'),

    # faqs
    path('faqs/upload/', FaqsTableView.as_view(), name='faq-list'),
    path('faqs/upload/<int:pk>/', FaqsTableDetailView.as_view(), name='faq-detail'),

    #  gallery
    path('gallery/upload/', GalleryView.as_view(), name='gallery-list'),
    path('gallery/upload/<int:pk>/', GalleryDetailView.as_view(), name='gallery-detail'),

    # testimonials
    path('testimonials/upload/', TestimonialsView.as_view(), name='testimonials-list'),
    path('testimonials/upload/<int:pk>/', TestimonialsDetailView.as_view(), name='testimonials-detail'),

    # product
    path('product/upload/', ProductView.as_view(), name='product-list'),
    path('product/upload/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    
    # hero
    path('hero/upload/', HeroView.as_view(), name='hero-list'),
    path('hero/upload/<int:pk>/', HeroDetailView.as_view(), name='hero-detail'),


    # privacy
    path('privacy/upload/', PrivacyView.as_view(), name='privacy-list'),
    path('privacy/upload/<int:pk>/', PrivacyDetailView.as_view(), name='privacy-detail'),
     

     # security
    path('security/upload/', SecurityView.as_view(), name='security-list'),
    path('security/upload/<int:pk>/', SecurityDetailView.as_view(), name='security-detail'),


    # service

    path('service/upload/', ServiceView.as_view(), name='service-list'),
    path('service/upload/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),

   

    # healthvalues

    path('health/upload/', HealthvaluesView.as_view(), name='health-list'),
    path('health/upload/<int:pk>/', HealthvaluesDetailView.as_view(), name='health-detail'),

    #whyusone

    path('whyusone/upload/', WhyusoneView.as_view(), name='whyus1-list'),
    path('whyusone/upload/<int:pk>/', WhyusoneDetailView.as_view(), name='whyus1-detail'),


    #whyustwo

    path('whyustwo/upload/', WhyustwoView.as_view(), name='whyus2-list'),
    path('whyustwo/upload/<int:pk>/', WhyustwoDetailView.as_view(), name='whyus2-detail'),


    #strategicone

    path('strategicone/upload/', StrategiconeView.as_view(), name='strategic1-list'),
    path('strategicone/upload/<int:pk>/', StrategiconeDetailView.as_view(), name='strategic1-detail'),


    #strategictwo

    path('strategictwo/upload/', StrategictwoView.as_view(), name='strategic2-list'),
    path('strategictwo/upload/<int:pk>/', StrategictwoDetailView.as_view(), name='strategic2-detail'),

    #weeklymessage

    path('message/upload/', WeeklyMessageView.as_view(), name='message-list'),
    path('message/upload/<int:pk>/', WeeklyMessageDetailView.as_view(), name='message-detail'),


     #heroslider

    path('heroslider/upload/', HerosliderView.as_view(), name='heroslider-list'),
    path('heroslider/upload/<int:pk>/', HerosliderDetailView.as_view(), name='heroslider-detail'),

    path('video/upload/', CompanyVideoView.as_view(), name='CompanyVideo-list'),
    path('video/upload/<int:pk>/', CompanyVideoDetailView.as_view(), name='CompanyVideo-detail'),



    path('societyform3/upload/', SocietyFormSubmissionView.as_view(), name='societyform3-list'),
    path('societyform3/upload/<int:pk>/', SocietyFormSubmissionDetailView.as_view(), name='societyform3-detail'),
    path('societyform3/count/', SocietyFormSubmissionCountView.as_view(), name='form-submission-count'),


    # re_path(r'', views.catchall),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    

    

]


