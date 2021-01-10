from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone

from bonus.models import LoyaltyModel
from bonus.forms import LoyaltyStatusForm, LoyaltyGeneratorForm,DateForm

import datetime



class LoyaltyListView(FormMixin, ListView):
    model=LoyaltyModel
    template_name = "loyalty.html"
    form_class = DateForm
    queryset = LoyaltyModel.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(LoyaltyListView, self).get_context_data(*args, **kwargs)
        context["object"] = LoyaltyModel.objects.all()
        query = self.request.GET.get("q")
        if query:
            try:
                context["object"] = self.model.objects.filter(
                    Q(start_time__icontains=query) |
                    Q(expiried_time__icontains=query) |
                    Q(last_usage__icontains=query) |
                    Q(card_number__icontains=query) |
                    Q(serial__icontains=query)

                )

            except:
                context["object"] = self.model.objects.filter(
                Q(card_number__icontains=query) |
                Q(serial__icontains=query)
                      )

        return context


    def create_cards(self, request):
        return


class LoyaltyDetailView(DetailView):
    model=LoyaltyModel
    template_name = "card_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LoyaltyDetailView, self).get_context_data(*args, **kwargs)
        obj=self.get_object()
        context["object"] = obj
        context['form'] = LoyaltyStatusForm()
        return context


class LoyaltyDeleteView(DeleteView):
    model=LoyaltyModel
    success_url = reverse_lazy("select")


class LoyaltyUpdateView(UpdateView):
    model = LoyaltyModel
    fields = ['status']
    template_name = "update_status.html"


class LoyalityCreateView(CreateView):
    model = LoyaltyModel
    template_name = "update_status.html"
    fields = ["serial",
               "card_number",
               "expiried_time"]


def generator(request):
    form = LoyaltyGeneratorForm(request.POST)
    template = "card_generator.html"
    context={'form':LoyaltyGeneratorForm()}
    submitted=False
    if form.is_valid():
        cleaned=form.cleaned_data
        context["test"] = cleaned
        date_range = int(cleaned['expiried_time'])
        obj_gen=[]
        expiried = timezone.localdate() + datetime.timedelta(days=(date_range))
        card_number_checkup=int(cleaned["number_of_generated_cards"])
        serial_checkup=cleaned["serial"]
        model_check= (LoyaltyModel.objects.filter(serial=serial_checkup))
        test = len(model_check)
        if  test > 0:

            new_range = card_number_checkup+model_check.last().card_number
            for i in range(model_check.last().card_number, new_range):
                obj_gen.append(LoyaltyModel(serial=serial_checkup, card_number=i+1, expiried_time=expiried))
        else:
            for i in range(card_number_checkup):
                obj_gen.append(LoyaltyModel(serial=serial_checkup, card_number=i+1, expiried_time=expiried))
        LoyaltyModel.objects.bulk_create(obj_gen)

        return_string = "/bonus/?q="+cleaned["serial"]
        return HttpResponseRedirect (return_string)
    else:
        form = LoyaltyGeneratorForm()
        if 'submitted' in request.GET:
            submitted = True
        return render(request, template, {'form': form, 'submitted': submitted})

