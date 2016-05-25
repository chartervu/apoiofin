from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from ident.models import Club

from models import Team, Modal, TeamForm

def teams(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
        club = Club.objects.get(usuario=request.user.id)
        teams = Team.objects.filter(club=club.id)
        return render_to_response('team/teams.html', locals(),
            context_instance=RequestContext(request),)

def team(request, team_id):
    club = Club.objects.get(usuario=request.user.id)
    team = Team.objects.get(id=team_id)
    if team.club_id != request.user.id:
        return HttpResponseRedirect('/accounts/logout/')
    else:
        if request.method == 'POST':
            form = TeamForm(request.POST, instance=team)
            if form.is_valid():
                tam = form.save(commit=False)
                tam.club_id = request.user.id
                tam.save()
                return HttpResponseRedirect('/team/%d' %team.id)
            else:
                form = TeamForm(instance=team)
        else:
            form = TeamForm(instance=team)
    return render_to_response('team/team.html', locals(),
        context_instance=RequestContext(request),)

def team_new(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    else:
        team = Team.objects.create(club_id=request.user.id, modal_id="0",age="0")
        team.save()
        return HttpResponseRedirect('/teams/')