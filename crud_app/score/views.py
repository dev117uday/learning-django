# Create your views here.
from django.shortcuts import render
from score.models import Score
from score.forms import ScoreForm


def scorepage(http_request):
    context = {}
    scores = Score.objects.all()
    form = ScoreForm()
    context["scores"] = scores
    context["title"] = "Home Page"

    print(http_request)
    print(http_request.method)
    print(http_request.POST)

    if http_request.method == "POST":
        if "save" in http_request.POST:
            pk = http_request.POST.get("save")
            if not pk:
                form = ScoreForm(http_request.POST)
            else:
                score = Score.objects.get(id=pk)
                form = ScoreForm(http_request.POST, instance=score)
            form.save()
            form = ScoreForm()

        elif "delete" in http_request.POST:
            pk = http_request.POST.get("delete")
            score = Score.objects.get(id=pk)
            score.delete()
        elif "edit" in http_request.POST:
            pk = http_request.POST.get("edit")
            score = Score.objects.get(id=pk)
            form = ScoreForm(instance=score)

    context["form"] = form
    return render(http_request, "index.html", context)


def aboutpage(http_request):
    context = {}
    context["title"] = "About Page"
    return render(request=http_request, template_name="about.html", context=context)
