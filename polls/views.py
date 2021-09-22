from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic

from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

from django.urls import reverse



'''
Note that once we’ve done this in all these views, 
we no longer need to import loader and HttpResponse 
(you’ll want to keep HttpResponse if you still have 
the stub methods for detail, results, and vote).

The render() function takes the request object 
as its first argument, a template name as its 
second argument and a dictionary as its optional t
hird argument. It returns an HttpResponse object of
 the given template rendered with the given context.
'''

"""

Each generic view needs to know what model 
it will be acting upon. This is provided using 
the model attribute.

The DetailView generic view expects 
the primary key value captured from the 
URL to be called "pk", so we’ve changed 
question_id to pk for the generic views.

By default, the DetailView generic view uses a 
template called <app name>/<model name>_detail.html. 


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    contect_obbject_name = 'latest_question_list'

    def get_queryset(self):
        """Return the list five published questions """
        return Question.object.order_by("-pub_date")[:5]



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form

        return render(request, 'polls/detail.html', {
            'question' : question,
            "error_message" : "You did not select a choice",
        })

    else:
        selected_choice.votes +=1
        selected_choice.save()

        #Always return an HttpRedirect after successfuly dealing
        #with POST data. This prevents data from being posted twice if a 
        #user hits the Back button

        return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))