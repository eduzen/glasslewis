from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.company_list),
    url(r'^index$', views.company_list),
    url(r'^home$', views.company_list),
    url(r'^companies$', views.company_list),
    url(r'^contact$', views.contacts),
    url(r'^contacts$', views.contacts),
    url(r'^contact/(?P<pk>[0-9]+)/$', views.contact_detail),
    url(r'^about$', views.About.as_view()),
]
