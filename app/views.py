from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SinginForm, LoginForm, AgendamentoForm
from .models import User, Atendimento
from django.contrib.auth import login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


def cadastro(request):
    if request.method == 'POST':
        form = SinginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            senha = data['password']

            user = User.objects.create_user(username, email, senha)
            user.user_type = 1
            user.endereco = data['endereco']
            user.telefone = data['telefone']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            
            group = Group.objects.get(name='Clientes')
            group.user_set.add(user)

            user.save()
            
            login_django(request, user)

            return HttpResponseRedirect('agendamento')
    else:
        form = SinginForm()

    return render(request, 'cadastro.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user

            login_django(request, user)

            return HttpResponseRedirect('agendamento')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login')
def agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user = request.user
            serv = data["servico"]
            pag = data["forma_de_pag"]
            date = data["data_servico"]

            agend = Atendimento.objects.create(servico=serv, forma_de_pag=pag, data_servico=date)
            agend.cliente = user
            agend.save()
    else:
        form = AgendamentoForm()

    return render(request, 'agendamento.html', {'form': form})

@login_required(login_url='/login')
def logout(request):
    logout_django(request)
    return HttpResponseRedirect('/login')