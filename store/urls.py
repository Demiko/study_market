from django.conf.urls import url
from . import views

app_name = 'store'
urlpatterns = [
    url(r'^details/(?P<pk>[0-9]+)/(?P<slug>[a-z0-9]+)',views.ProductView.as_view(),name='details'),
    url(r'^details/(?P<pk>[0-9]+)',views.ProductView.as_view(),name='details_wo_slug'),
    url(r'^list/(?P<page>[0-9]+)',views.ProductList.as_view(),name='product_list'),
    url(r'^list',views.ProductList.as_view(),name='product_list_wo_page'),
]
