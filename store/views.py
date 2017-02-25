from django.shortcuts import render,redirect,reverse
from django.core.paginator import Paginator

# Create your views here.
from django.views import generic
from .models import Product


class ProductView(generic.DetailView):
    model = Product
    template_name = 'store/details.html'
    context_object_name = 'product'

class ProductList(generic.ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product_list'
    url_name = 'store:product_list'
    page_kwarg = 'page'
    paginate_by = 10

    # def get(self, request, *args, **kwargs):
    #     paginator = Paginator(self.model.objects.all(),2)
    #     try:
    #         page = int(kwargs['page'])
    #     except:
    #         page = 1
    #     print('\n', page, '\n')
    #     if page < 1:
    #         result = redirect(reverse(self.url_name,kwargs={'page':1}))
    #     elif page > paginator.num_pages:
    #         result = redirect(reverse(self.url_name,kwargs={'page':2}))
    #     else:
    #         result = render(request,
    #                         self.template_name,
    #                         {'product_list':paginator.page(page)})
    #     return result
