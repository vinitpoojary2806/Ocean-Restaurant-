from django.contrib import admin
from django.urls import path, include
from Homes import views
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.Homepage, name="homepage"),
    path('about', views.about, name="aboutpage"),
    path('bookings', views.bookings, name="Booking"),
    path('service', views.service, name="service"),
    path('contacts', views.contacts, name="contact"),
    path('menus', views.menus, name="menu"),
    path('teams', views.teams, name="team"),
    path('testimonials', views.testimonials, name="testimonial"),
    path('category', views.category, name="category"),
    path('startersmenu', views.startersmenus, name="startersmenu"),
    path('maincoursemenu', views.maincoursemenus, name="maincoursemenu"),
    path('chinesemenu', views.chinesemenus, name="chinesemenu"),
    path('sizzlersmenu', views.sizzlersmenus, name="sizzlersmenu"),
    path('mocktailsmenu', views.mocktailsmenus, name="mocktailsmenu"),
    path('desertsmenu', views.desertsmenus, name="desertsmenu"),
    path('chatbot', views.chatbots, name="chatbot"),
    path('icecreamfloat', views.icecreamfloats, name="icecreamfloat"),
    path('drumsofheaven', views.drumsofheavens, name="drumsofheaven"),
    path('frenchpotato', views.frenchpotatos, name="frenchpotato"),
    path('manchuriandry', views.manchuriandrys, name="manchuriandry"),
    path('viewdish/<id>', views.viewDishes, name="dishesviewurl"),

    path('displaydish/<id>', views.displayDishes, name="getdishes"),

    path('printReport/<id>', views.printReport, name="getReport"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

