import os
from django.shortcuts import render, get_object_or_404
from django.conf import settings

def home(request):
    """
    Default home view
    """
    return render(request, 'base.html', {
        
    })
