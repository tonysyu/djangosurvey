from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from .models import UserResponse


@staff_member_required
def results(request):
    return render(request, "admin/results.html",
                  {'survey_results': UserResponse.objects.all()})
