from django.shortcuts import render
from Jedi.models import Candidate, Jedi, TestQuestion, TestAnswer, Planet, CandidateAnswers
from Jedi.forms import CandidateForm
from django.views import generic
from django.db.models import Count

# Create your views here.
def index(request):
    """View function for home page of site."""
    num_candidates = Candidate.objects.all().count()
    num_jedi = Jedi.objects.all().count()

    context = {
        'num_candidates': num_candidates,
        'num_jedi': num_jedi,
    }

    return render(request, 'index.html', context=context)


def candidate_resume(request):
    form = CandidateForm
    if request.method == "POST":
        candidate = Candidate.objects.create(
            planet_id=request.POST.get("planet"),
            email=request.POST.get("email"),
            name=request.POST.get("name"),
            age=request.POST.get("age"),
        )
        test_question = TestQuestion.objects.all()
        test_answer = TestAnswer.objects.all()
        return render(request, "challenge.html",
                      {"candidate_id": candidate.id, "Questions": test_question,
                       "Answers": test_answer, 'request': request.method})
    return render(request, "new_member.html", {"form": form})


# def send_message(request):
#     if request.method == "POST":
#         candidate_answer = CandidateAnswers.objects.create(
#             test_question = request.POST.get("question"),
#             test_answer = request.POST.get("answer"),
#             candidate = request.POST.get("candidate"),
#         )
#         return render(request, "gratitude.html", {"candidate":candidate_answer.id})
    

def test_save(request):
    id_candidate = request.POST.get("candidate_id")
    for test_question in TestQuestion.objects.all():
        selected_option = request.POST.get(str(test_question.id))
        test_answer = TestAnswer.objects.get(id=int(selected_option))
        CandidateAnswers.objects.create(test_question=test_question,
                                        test_answer=test_answer,
                                        candidate_id=id_candidate)
    return render(request, "index.html")


def jedis_list(request):
    min_students = request.POST.get('min_number_of_students', 0)
    all_jedi = Jedi.objects.all()
    list_jedi = Jedi.objects.annotate(Count('candidate')).filter(
        candidate__count__gte=min_students
    )
    return render(request, 'list_jedi.html', {'list_jedi': list_jedi,
                                                 'all_jedi': all_jedi,
                                                 'min_number_of_students':
                                                     min_students})


def jedi_from(request):
    jedi = request.POST.get('selected_jedi')
    context = {'list_candidates': Candidate.objects.all().filter(
                    planet=Jedi.objects.get(id=jedi).planet,
                    jedi__isnull=True)}

    return render(request, "djedai_detail.html", context)

def see_test(request):
    test_list = CandidateAnswers.objects.all().filter(candidate=candidate_id)
    context = ({"test_list": test_list,
                "candidate_name": Candidate.objects.get(
                    id__exact=candidate_id).name,
                "number_of_answer": test_list.filter(
                    test_answer__is_correct_answer__exact=True).count(),
                "number_of_questions": test_list.count()})
    return render(request, "check_answer.html", context)