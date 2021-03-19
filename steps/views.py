import json

from django.shortcuts import render
from django.http.response import JsonResponse

from .models import JobTitle, OpportunityAvailable, WorkExperience, InputSession

from .forms import WorkExperienceForm, OpportunityAvailableForm


# Create your views here.
def home(request):
    template_name = "steps.html"
    if request.method == 'GET':
        context = {
            "experience_form": WorkExperienceForm(),
            "opportunity_form": OpportunityAvailableForm(),
        }
        return render(request, template_name, context=context)


def save_work_title(request):
    if request.method == 'POST':
        try:
            title = request.POST['job_title']
            if not title:
                raise ValueError("Field cannot be empty")
        except Exception as e:
            return JsonResponse({"status": "error", "message": "Saving error. {}".format(str(e))})

        job_title = JobTitle.objects.create(title=title)
        session = InputSession.objects.create(job_title=job_title)

        return JsonResponse({"status": "ok", "session_id": session.id})


def save_work_experience(request):
    if request.method == "POST":
        try:
            session_id = request.POST['session_id']
            data = json.loads(request.POST['data'])
            session = InputSession.objects.get(id=session_id)
        except Exception as e:
            return JsonResponse({"status": "error", "message": "Saving error {}".format(str(e))})

        form = WorkExperienceForm(data=data)
        if form.is_valid():
            instance = form.save()
            InputSession.objects.filter(id=session.id).update(work_experience=instance)

            work_experience_json = {
                "title": instance.title,
                "company_name": instance.company_name,
                "working_here": instance.working_here,
                "date_started": instance.date_started,
                "date_ended": instance.date_ended,
                "skills_used": instance.skills_used,
                "describe_accomplishment": instance.describe_accomplishment
            }
            return JsonResponse({"status": "ok",
                                 "session_id": session.id,
                                 "experience": work_experience_json})
        return JsonResponse({"status": "error", "message": "Form invalid"})


def save_opportunity_available(request):
    if request.method == "POST":
        try:
            session_id = request.POST['session_id']
            data = json.loads(request.POST['data'])
            session = InputSession.objects.get(id=session_id)
        except Exception as e:
            return JsonResponse({"status": "error", "message": "Saving error {}".format(str(e))})

        form = OpportunityAvailableForm(data=data)
        if form.is_valid():
            instance = form.save()
            InputSession.objects.filter(id=session.id).update(opportunity=instance)
            return JsonResponse({"status": "ok", "session_id": session.id})
        return JsonResponse({"status": "error", "message": "Form invalid"})


