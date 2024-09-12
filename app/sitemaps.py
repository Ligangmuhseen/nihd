from django.contrib import sitemaps
from django.urls import reverse
from .models import Aboutone, Background, Abouttwo, FaqsTable, Gallery, Testimonials, Product, Hero, Privacy, Security, Service, Healthvalues, Whyusone, Whyustwo, Strategicone, Strategictwo, WeeklyMessage, Heroslider, SocietyFormSubmission
 
 

# dynamic pages
 
class SocietyFormSubmissionSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'http'

   
    def items(self):
        return SocietyFormSubmission.objects.all()

    def location(self, item):
        return reverse('app:societyform3-detail', kwargs={'pk': item.pk})
    

class AboutoneSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Aboutone.objects.all()

    def location(self, item):
        return reverse('app:aboutone-detail', kwargs={'pk': item.pk})


class AbouttwoSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Abouttwo.objects.all()

    def location(self, item):
        return reverse('app:abouttwo-detail', kwargs={'pk': item.pk})

class BackgroundSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Background.objects.all()

    def location(self, item):
        return reverse('app:background-detail', kwargs={'pk': item.pk})
    


class FaqsTableSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return FaqsTable.objects.all()

    def location(self, item):
        return reverse('app:faq-detail', kwargs={'pk': item.pk})

class GallerySitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Gallery.objects.all()

    def location(self, item):
        return reverse('app:gallery-detail', kwargs={'pk': item.pk})
    


class TestimonialsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Testimonials.objects.all()

    def location(self, item):
        return reverse('app:testimonials-detail', kwargs={'pk': item.pk})

class ProductSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Product.objects.all()

    def location(self, item):
        return reverse('app:product-detail', kwargs={'pk': item.pk})

class HeroSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Hero.objects.all()

    def location(self, item):
        return reverse('app:hero-detail', kwargs={'pk': item.pk})

class PrivacySitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Privacy.objects.all()

    def location(self, item):
        return reverse('app:privacy-detail', kwargs={'pk': item.pk})  



class SecuritySitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Security.objects.all()

    def location(self, item):
        return reverse('app:security-detail', kwargs={'pk': item.pk})

class ServiceSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Service.objects.all()

    def location(self, item):
        return reverse('app:service-detail', kwargs={'pk': item.pk})

class HealthvaluesSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Healthvalues.objects.all()

    def location(self, item):
        return reverse('app:health-detail', kwargs={'pk': item.pk})

class WhyusoneSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Whyusone.objects.all()

    def location(self, item):
        return reverse('app:whyus1-detail', kwargs={'pk': item.pk})

class WhyustwoSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Whyustwo.objects.all()

    def location(self, item):
        return reverse('app:whyus2-detail', kwargs={'pk': item.pk})

class StrategiconeSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Strategicone.objects.all()

    def location(self, item):
        return reverse('app:strategic1-detail', kwargs={'pk': item.pk})

class StrategictwoSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Strategictwo.objects.all()

    def location(self, item):
        return reverse('app:strategic2-detail', kwargs={'pk': item.pk})

class WeeklyMessageSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return WeeklyMessage.objects.all()

    def location(self, item):
        return reverse('app:message-detail', kwargs={'pk': item.pk})

class HerosliderSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Heroslider.objects.all()

    def location(self, item):
        return reverse('app:heroslider-detail', kwargs={'pk': item.pk})      


    































































  # static pages

# class StaticSitemap(Sitemap):
#     changefreq = "yearly"
#     priority = 0.8
#     protocol = 'http'

#     def items(self):
#        return ['main:homepage_view', 'main:contact_view']

#     def location(self, item):
#        return reverse(item)  