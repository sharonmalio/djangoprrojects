from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
#from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
# Create your views here.
from django.views import  generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# class VoteView( generic.DetailView):
#     model = Question
#     template_name = 'polls/vote.html'