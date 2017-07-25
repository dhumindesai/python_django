from django.shortcuts import render
from . import views
import csv
from io import StringIO


def index(request):
    return render(request,"csvreader/home.html")
    #return HttpResponse("Welcome to %s" % request.path)
# Create your views here.

def csv_post(request):
    if request.FILES:
        csvfile = request.FILES['csvfile']
        csvf = StringIO(csvfile.read().decode())
        csvfilereader = csv.reader(csvf,delimiter=',')

    return render(request, 'csvreader/csv_table.html',{'csvfilereader':csvfilereader})

