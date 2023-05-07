from django.views.generic import ListView
from .models import *


class SubMenuListView(ListView):
    model = Menu
    template_name = 'tree_menu/category.html'


class MenuListView(ListView):
    context_object_name = 'sub_menu'
    template_name = 'tree_menu/post.html'

    def get_queryset(self):
        self.menu = Menu.objects.get(slug=self.kwargs['slug'])
        queryset = SubMenu.objects.filter(menu=self.menu)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.menu
        return context
