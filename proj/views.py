from django.shortcuts import render, redirect, reverse
from .models import DataModel
from .forms import InputName
from django.forms import formset_factory
import logging
logging.basicConfig(level=logging.INFO)


def process_data(list):
    result_dict = {}
    for i, elem in enumerate(list, start=0):
        result_dict[i] = elem.get('inp_name')
    return result_dict


def index(request):
    form = InputName(request.POST or None)
    input_formset = formset_factory(InputName, extra=1)
    formset = input_formset(request.POST or None)
    context = {'formset': formset}
    if request.method == "POST":
        if input_formset.is_valid(formset):
            print("valid!")
            data = formset.cleaned_data
            DataModel(data=process_data(data)).save()
            print(f"data: {data}")
            print(request.POST)
            context["data"] = data
    return render(request, 'index.html', context)


def data_view(request):
    data = DataModel.objects.all().order_by()
    print(data)
    return render(request, 'data.html', {'all_data': data})

# class Index:
#
#
#     def get_request(self, request):
#         pass
#     def post_request(self):
