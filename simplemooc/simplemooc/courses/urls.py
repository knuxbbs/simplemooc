from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    #Aceita um número inteiro como parâmetro e o associa ao nome 'pk'
    url(r'^(?P<pk>\d+)/$', views.get_by_id, name='details'),
    
    #Aceita uma cadeia de caracteres alfanuméricos 
    # (com underline e hífen) e os associa ao nome 'slug'
    url(r'^(?P<slug>[\w_-]+)/$', views.get_by_slug, name='details')
]