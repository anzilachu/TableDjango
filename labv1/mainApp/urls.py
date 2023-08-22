from django.urls import path
from . import views

urlpatterns = [
    path('',views.Login),
    path('homepage/',views.homePage),
    path('chain_of_custody/', views.chain_of_custody,),
    path('chain_of_custody_form/', views.chain_of_custody_form, name ="Chain of Custody"),
    path('SampleIntakelog/', views.SampleIntakelog),
    path('SampleIntakeForm/', views.SampleIntakeForm),
    path('SampleTrackingLog/', views.SampleTrackingLog),
    path('SampleTrackingForm/', views.SampleTrackingForm),
    path('SampleRetainLog/', views.SampleRetainLog),
    path('SampleRetainForm/', views.SampleRetainForm),
    path('Cannibanoidssamplepreplogsheet/',views.Cannibanoidssamplepreplogsheet,name='Cannibanoidssamplepreplogsheet'),
    path('Cannibanoidsdatasheet100xdryweight/', views.Cannibanoidsdatasheet100xdryweight),
    path('Cannibanoidsdatasheet100xmgperg/', views.Cannibanoidsdatasheet100xmgperg),
    path('Cannibanoidsdatasheet100xwetweight/', views.Cannibanoidsdatasheet100xwetweight),
    path('Cannibanoidsdatasheet100x/', views.Cannibanoidsdatasheet100x),
    path('Cannibanoidsdatasheet2000xdryweight/', views.Cannibanoidsdatasheet2000xdryweight),
    path('Cannibanoidsdatasheet2000xmgperg/', views.Cannibanoidsdatasheet2000xmgperg),
    path('Cannibanoidsdatasheet2000xwetweight/', views.Cannibanoidsdatasheet2000xwetweight),
    path('Cannibanoidsdatasheet2000x/', views.Cannibanoidsdatasheet2000x),
    
]


app_name = 'labs'