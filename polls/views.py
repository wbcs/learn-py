from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import Question, Choice

# def my_render(request, filename, context):
#   template = loader.get_template(filename)
#   res = template.render(context, request)
#   return HttpResponse(res)

# Create your views here.
def index(request):
  question_list = Question.objects.order_by('pub_date')
  choice_list = Choice.objects.all()
  res = ','.join([item.question_text for item in question_list])
  res += '+'.join([item.choice_text for item in choice_list])
  context = {
    'question_list': question_list,
  }
  return render(request, 'index.html', context)


def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
