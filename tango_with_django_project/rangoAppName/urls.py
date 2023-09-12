from django.urls import path
from rangoAppName import views
#from rangoAppName.views import form_view

app_name = 'rangoAppName'
urlpatterns = [
path('', views.index, name='index'),

path('box_tables/', views.box_data_view, name='box_data_view'),
path('landing_page/', views.landing_page_view, name='landing_page_view'),
path('Summary/', views.summary_view, name='summary_view'),
path('sucess_page/', views.na1_submit_view, name='na1_submit_view'),
path('form1/', views.my_view, name='my_view'),
path('form2/', views.form2_view, name='form2_view'),
path('form3/', views.form3_view, name='form3_view'),
path('form4/', views.form4_view, name='form4_view'),
path('form5/', views.form5_view, name='form5_view'),
path('form6/', views.form6_view, name='form6_view'),
path('form7/', views.form7_view, name='form7_view'),
path('form8/', views.form8_view, name='form8_view'),
path('form9/', views.form9_view, name='form9_view'),
path('form10/', views.form10_view, name='form10_view'),
path('form11/', views.form11_view, name='form11_view'),
path('form12/', views.form12_view, name='form12_view'),
path('form13/', views.form13_view, name='form13_view'),
path('form14/', views.form14_view, name='form14_view'),
path('form15/', views.form15_view, name='form15_view'),
]
