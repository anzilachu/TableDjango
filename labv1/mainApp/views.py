from django.shortcuts import render,HttpResponseRedirect
from .models import *


def Login(Request):
    return render(Request,"Login.html")

def homePage(Request):
    return render(Request,"home.html")

def chain_of_custody(Request):
   
    return render(Request,"Chain of Custody.html")
 

def chain_of_custody_form(Request):
    return render(Request,"Chain of Custody.html")

def SampleIntakelog(Request):
    return render(Request,"Sample Intake log.html")

def SampleIntakeForm(Request):
    return render(Request,"Sample Intake Form.html")

def SampleTrackingLog(Request):
    return render(Request,"Sample Tracking Log.html")

def SampleTrackingForm(Request):
    return render(Request,"Sample Tracking Form.html")

def SampleRetainLog(Request):
    return render(Request,"Sample Retention Log.html")

def SampleRetainForm(Request):
    return render(Request,"Sample Retention Form.html")

def Cannibanoidssamplepreplogsheet(Request):
    return render(Request,"FO-121 Cannabinoids Sample Prep Log Sheet.html")

def Cannibanoidsdatasheet100xdryweight(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 100x dry weight .html")

def Cannibanoidsdatasheet100xmgperg(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 100x mg per g.html")

def Cannibanoidsdatasheet100xwetweight(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 100x wet weight .html")

def Cannibanoidsdatasheet100x(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 100x.html")

def Cannibanoidsdatasheet2000xdryweight(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 2000x dry weight .html")

def Cannibanoidsdatasheet2000xmgperg(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 2000x mg per g.html")

def Cannibanoidsdatasheet2000xwetweight(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 2000x wet weight .html")

def Cannibanoidsdatasheet2000x(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 2000x.html")