from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View

from .models import Country


class FlowersView(View):
    def get(self, request):
        flowers = Country.objects.all()
        return render(request, "flower/flower_list.html", {"flower_list": flowers})