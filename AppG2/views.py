from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404

from .forms import FormSoli,FormAtender
from .models import Funcionario,Solicitacao,Atender


    

def inicio(request):    
    fun = Funcionario.objects.get(usuario=request.user)
    sol = Solicitacao.objects.all()
    if fun.cargo.eh_chefe and fun.departamento.eh_transporte:
        return render(request,'listat.html',{'sol':sol})
    else:
        if fun.eh_motorista:
            return redirect('solicitar/')
        soli = Solicitacao.objects.filter(solicitante__usuario=request.user)
        return render(request,'inicio.html',{'soli':soli})


def atender(request):
    fun = Funcionario.objects.get(usuario=request.user)
    if fun.cargo.eh_chefe and fun.departamento.eh_transporte:
        if request.method =='POST':
            form = FormAtender(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                return render(request,'atender.html',{'form':form})
        else:
            form = FormAtender()
            return render(request,'atender.html',{'form':form})
    
    return redirect('/')


def solicitar(request):
    fun = Funcionario.objects.get(usuario=request.user)
    if fun.cargo.eh_chefe:
        if fun.cargo.eh_chefe and not fun.departamento.eh_transporte:
            if request.method =='POST':
                form = FormSoli(request.POST)
                if form.is_valid():
                    solici = form.save(commit=False)
                    solici.solicitante = fun
                    solici.save()
                    return redirect('/')
                else:
                    return render(request,'solicitar.html',{'form':form})
            else:
                form = FormSoli()
                return render(request,'solicitar.html',{'form':form})
        else:
            return redirect('/')    
    
    fun = Atender.objects.filter(motorista__usuario=request.user)
    return render(request,'viagens.html',{'fun':fun})

def atendimentos(request):
    fun = Funcionario.objects.get(usuario=request.user)
    atendimentos = Atender.objects.all()
    if fun.cargo.eh_chefe and fun.departamento.eh_transporte:
        return render(request,'atendimentos.html',{'atendimentos':atendimentos})

    else:
        return redirect('/')

def detalhesat(request,id):
    atendimento = Atender.objects.filter(pk=id)
    print (atendimento)
    return render(request,'detalhes_atendimento.html',{'atendimento':atendimento})
