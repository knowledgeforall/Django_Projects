# myapi/urls.py
from django.urls import include, path
from myapi import views
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
      path('', views.index, name='index'),
	  path('about_us.html', views.about_us, name='about_us'),
	  path('contact_us.html', views.contact_us, name='contact_us'),
	  path('current_work.html', views.current_work, name='current_work'),
	  path('donate.html', views.donate, name='donate'),
	  path('future_work.html', views.future_work, name='future_work'),
	  path('Gallery.html', views.Gallery, name='Gallery'),
	  path('Join_Us.html', views.Join_Us, name='Join_Us'),
	  path('members.html', views.members, name='members'),
	  path('our_vision.html', views.our_vision, name='our_vision'),
	  path('our_work.html', views.our_work, name='our_work'),
	  path('past_work.html', views.past_work, name='past_work'),
	  path('privacy_policy.html', views.privacy_policy, name='privacy_policy'),
	  path('Resources.html', views.Resources, name='Resources'),
	  path('terms_conditions.html', views.terms_conditions, name='terms_conditions'),
	  path('register', views.register_request, name='register'),
	  
	  
]