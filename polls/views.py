from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser

def index(request):
    x = [{
            'id':1,
            'userName':'motiour',
        },
        {
           'id':2,
            'userName':'sayam',
        }
    ]

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    request.session[0] = 'bar'
    request.session['fev_color'] = '1'
    request.session['has_commented'] = True
    # request.session.set_expiry(180)
    # request.session[1] = x
    # request.session[1].append({
    #     'id':3,
    #     'userName':'manaun',
    # })
    # print( request.session['1'])
    # print(request.session.keys())
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        print('work')
    response = HttpResponse()

    response.set_cookie("favorite_color",
                            "black")
    print(request.session.items())

    if "favorite_color" in request.COOKIES:
        print("your favorite color is %s" / request.COOKIES['favorite_color'])
    else:
        print("You don't have a favorite color.")



    return render(request, 'index.html', context)


def detail(request, question_id):
    fev_color = ''


    fev_color = request.session.items() 

    print(fev_color, 'color')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    # del request.session['fav_color']
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
