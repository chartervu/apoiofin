from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from models import Club, Detail, Organ
from forms import DetailForm, OrganForm

def ident(request, club_id):
    club = Club.objects.get(usuario=request.user.id)
    detail = Detail.objects.get(club=club_id)
    if detail.id != request.user.id:
        return HttpResponseRedirect('/accounts/logout/')
    else:
        if request.method == 'POST':
            form = DetailForm(request.POST, instance=detail)
            if form.is_valid():
                dtl = form.save(commit=False)
                dtl.club_id = request.user.id
                dtl.save()
                return HttpResponseRedirect('/ident/%d' %detail.id)
            else:
                form = DetailForm(instance=detail)
        else:
            form = DetailForm(instance=detail)
    return render_to_response('ident/ident.html', locals(),
        context_instance=RequestContext(request),)

def board(request, club_id):
    club = Club.objects.get(usuario=request.user.id)
    board = Organ.objects.get(club=club_id)
    if board.id != request.user.id:
        return HttpResponseRedirect('/accounts/logout/')       
    else:
        if request.method == 'POST':
            form = OrganForm(request.POST, instance=board)
            if form.is_valid():
                brd = form.save(commit=False)
                brd.club_id = request.user.id
                brd.save()
                return HttpResponseRedirect('/board/')
            else:
                form = OrganForm(instance=board)
        else:
            form = OrganForm(instance=board)
    return render_to_response('ident/board.html', locals(),
        context_instance=RequestContext(request),)