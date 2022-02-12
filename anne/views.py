from django.shortcuts import render
from anne import models

def searchUser(request):
    obj = models.Item.objects.all()
    site_d = models.SiteDesc.objects.all()
    return render(request,'anne/index.html', {'obj':obj, 'site_des':set(site_d)})

