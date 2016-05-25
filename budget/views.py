from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from models import Budget, BudgetForm
from ident.models import Club

def budget(request, club_id):
    club = Club.objects.get(usuario=request.user.id)
    budget = Budget.objects.get(club=club_id)
    if budget.id != request.user.id:
        return HttpResponseRedirect('/accounts/logout/')
    else:
        if request.method == 'POST':
            form = BudgetForm(request.POST, instance=budget)
            if form.is_valid():
                bdg = form.save(commit=False)
                bdg.club = request.user.id
                bdg.save()
                return HttpResponseRedirect('/budget/%d' %budget.id)
            else:
                form = BudgetForm(instance=budget)
        else:
            form = BudgetForm(instance=budget)
    return render_to_response('budget/budget.html', locals(),
        context_instance=RequestContext(request),)
