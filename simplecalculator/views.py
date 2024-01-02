from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import calculator

# def homepage(request):
#     c=''
#     try:
#         if request.method=="POST":
#             n1 = eval(request.POST.get('num1'))
#             n2 = eval(request.POST.get('num2'))
#             opr = request.POST.get('opr')
#             if opr=="+":
#                 c = n1+n2
#             elif opr=="-":
#                 c = n1-n2
#             elif opr=="*":
#                 c = n1*n2
#             elif opr=="/":
#                 c = n1/n2
#     except:
#         c = "Invalid operation"
#     print(c)
#     return render(request, "index.html",{'c':c})


# def calculate(request):
#     result = None
#     error = None

#     if request.method == "POST":
#         try:
#             form = calculator(request.POST)
#             if form.is_valid():
#                 n1 = form.cleaned_data['num1']
#                 n2 = form.cleaned_data['num2']
#                 oper = form.cleaned_data['opr']

#                 if oper == "+":
#                     result = n1 + n2
#                 elif oper == "-":
#                     result = n1 - n2
#                 elif oper == "*":
#                     result = n1 * n2
#                 elif oper == "/":
#                     if n2 != 0:
#                         result = n1 / n2
#                     else:
#                         error = 'Cannot divide by zero'

#         except ValueError:
#             error = 'Invalid input. Please enter valid numbers.'
#         except Exception as e:
#             error = f"An error occurred: {str(e)}"

#     form = calculator()
#     data = {'form': form, 'output': result, 'error': error}

#     return render(request, "index.html", data)

# def homepage(request):
#     c=''
#     try:
#         if request.method=="POST":
#             n1 = eval(request.POST.get('num1'))
#             n2 = eval(request.POST.get('num2'))
#             opr = request.POST.get('opr')
#             if opr=="+":
#                 c = n1+n2
#             elif opr=="-":
#                 c = n1-n2
#             elif opr=="*":
#                 c = n1*n2
#             elif opr=="/":
#                 c = n1/n2
#     except:
#         c = "Invalid operation"
#     print(c)
#     return render(request, "index.html",{'c':c})


def calculate(request):
    data = {'form': calculator(), 'output': None}

    if request.method == 'POST':
        form = calculator(request.POST)
        
        if form.is_valid():
            n1 = float(form.cleaned_data['num1'])
            n2 = float(form.cleaned_data['num2'])
            oper = form.cleaned_data['opr']

            try:
                if oper == "+":
                    result = n1 + n2
                elif oper == "-":
                    result = n1 - n2
                elif oper == "*":
                    result = n1 * n2
                elif oper == "/":
                    if n2 != 0:
                        result = n1 / n2
                    else:
                        data['output'] = 'Cannot divide by zero'
                        return render(request, "index.html", data)
                else:
                    result = None

                data['output'] = result
            except ValueError:
                data['output'] = 'Invalid input. Please enter valid numbers.'

    return render(request, "index.html", data)





