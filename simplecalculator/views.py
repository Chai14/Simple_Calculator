from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import calculator

def calculate(request):

    data = { 'form': calculator(), 'output': None}

    if request.method == 'POST':

        n1 = float(request.POST.get('num1'))
        n2 = float(request.POST.get('num2'))
        oper = request.POST.get('opr')

        if oper == '+':
            result = n1 + n2
        elif oper == '-':
            result = n1 - n2
        elif oper == '*':
            result = n1 * n2
        elif oper == '/':
            if n2 != 0:
                result = n1 / n2
            else:
                data['output'] = 'Cannot divide by zero'
        else:
            data['output'] = 'Invalid Operator'

        data['output'] = result

    return render(request, "index.html", data)











