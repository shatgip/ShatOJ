from django.shortcuts import render

from django.shortcuts import render
from.models import Problem

def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'problems/problem_list.html', {'problems': problems})

def problem_detail(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    return render(request, 'problems/problem_detail.html', {'problem': problem})