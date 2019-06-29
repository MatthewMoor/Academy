from django.shortcuts import render
from Jedi.models import Candidate, Jedi, TestQuestion, TestAnswer, Planet, CandidateAnswers
from Jedi.forms import CandidateForm

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


def send_message(request):
    if request.method == "POST":
        candidate_answer = CandidateAnswers.objects.create(
            test_question = request.POST.get("question"),
            test_answer = request.POST.get("answer"),
            candidate = request.POST.get("candidate"),
        )
        return render(request, "gratitude.html", {"candidate":candidate_answer.id})
    

def test_main(request):
    id_candidate = request.POST.get("candidate_id")
    for test_question in TestQuestion.objects.all():
        selected_option = request.POST.get(str(test_question.id))
        test_answer = TestAnswer.objects.get(id=int(selected_option))
        CandidateAnswers.objects.create(test_question=test_question,
                                        test_answer=test_answer,
                                        candidate_id=id_candidate)
    return render(request, "index.html")



