from django.conf.urls import url
from SEProject import settings
from . import views
from django.conf.urls.static import static


app_name = 'onlinetest' 

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^studentlogin$', views.studentlogin, name='studentlogin'),
    url(r'^clientlogin$', views.clientlogin, name='clientlogin'),
    url(r'^clientloginVal$', views.clientloginVal, name='clientloginVal'),
    url(r'^clientregister$', views.clientregister, name='clientregister'),
    url(r'^adminhome$', views.adminhome, name='adminhome'),
    url(r'^home$', views.home, name='home'),
    url(r'^studentReg$', views.studentReg, name='studentReg'),
    url(r'^addtest$', views.addtest, name='addtest'),
    url(r'^(?P<test_id>[0-9]+)/deletetest/$', views.deletetest, name='deletetest'),
    url(r'^studentLogincheck$', views.studentLogincheck, name='studentLogincheck'),
    url(r'^studenthome$', views.studenthome, name='studenthome'),
    url(r'^yourtest$', views.yourtest, name='yourtest'),
    url(r'^studentRegSave', views.studentRegSave, name='studentRegSave'),
    url(r'^studentInfo', views.studentInfo, name='studentInfo'),
    url(r'^clientlogout', views.clientlogout, name='clientlogout'),
    url(r'^studentmarksAnalysis', views.studentmarksAnalysis, name='studentmarksAnalysis'),
    url(r'^studentmarksGraphAnalysis', views.studentmarksGraphAnalysis, name='studentmarksGraphAnalysis'),
    url(r'^testMarksGraph', views.testMarksGraph, name='testMarksGraph'),
    url(r'^studentlogout', views.studentlogout, name='studentlogout'),
    url(r'^simple_upload', views.simple_upload, name='simple_upload'),
    url(r'^paper_submit$',views.paper_submit, name='paper_submit'),
    url(r'^studentreview$',views.studentreview, name='studentreview'),
    url(r'^add_review',views.add_review, name='add_review'),
    url(r'^client_review',views.client_review, name='client_review'),
    url(r'^studentseeanswers', views.studentseeanswers, name='studentseeanswers'),
    url(r'^update_scores',views.update_scores, name='update_scores'),


    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
