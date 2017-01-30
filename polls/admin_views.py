from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from .utils import summarize_survey_results


@staff_member_required
def results(request):
    return render(request, "admin/results.html",
                  {'survey_results': summarize_survey_results()})
