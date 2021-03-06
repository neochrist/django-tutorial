from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    
    path('', views.IndexView(), name='index'),
    
    path('<int:pk>/', views.DetailView(), name='detail'),
    
    path('<int:question_id>/results/', views.ResultsView(), name='results'),
    
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

###exp
'''

Take a look in your browser, at “/polls/34/”. 
It’ll run the detail() method and display whatever ID you provide in the URL. 
Try “/polls/34/results/” and “/polls/34/vote/” too – these will display the placeholder results and voting pages.






When somebody requests a page from your website – say, “/polls/34/”,
Django will load the mysite.urls Python module because it’s pointed to by the ROOT_URLCONF setting. 
It finds the variable named urlpatterns and traverses the patterns in order. After finding the match at 'polls/', 
it strips off the matching text ("polls/") and sends the remaining text – "34/" – to the ‘polls.urls’ URLconf for further processing. 
There it matches '<int:question_id>/', resulting in a call to the detail() view like so:





detail(request=<HttpRequest object>, question_id=34)
The question_id=34 part comes from <int:question_id>. U
sing angle brackets “captures” part of the URL and sends it as a keyword argument to the view function. 
The question_id part of the string defines the name that will be used to identify the matched pattern, 
and the int part is a converter that determines what patterns should match this part of the URL path. 
The colon (:) separates the converter and pattern name.
'''