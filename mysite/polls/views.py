from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    myname = "Thế Việt"
    cuacai = ["500k", "điện thoại A8S clone", "laptop HP Elitebook 8560w"]
    return render(request, "polls/index.html", {"name":myname, "tien":cuacai})

def viewlist(request):
    #get_object_or_404(Question, pk=3)
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs":q})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
    except:
        return HttpResponse("lỗi không có sự lựa chọn nào")
        c.vote = c.vote + 1
        c.save()
        return HttpResponse(c.vote)

