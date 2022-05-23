
from django.http import render


def Movie_Name(request):
page = request.GET.get("page")
    return render(request,"base.html",{'page':page})

