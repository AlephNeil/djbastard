from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Enquiry

# Create your views here.

def shebang(request, who_spec, which_spec):
    all_enquiries = Enquiry.objects.order_by('-created')
    template = loader.get_template('enqs/shebang.html')
    context = {
        'enquiries': all_enquiries,
    }
    return HttpResponse(template.render(context, request))