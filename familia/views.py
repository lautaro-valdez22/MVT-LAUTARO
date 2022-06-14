from django.shortcuts import render
from Familiares.models import Familiar

# Create your views here.

def familiares(request):
        familiar_nuevo = Familiar.objects.create(
                name='Claudia',
                last_name='Degregorio', 
                age= 60, 
                dni= '14958687', 
                birth_date= '05/08/1962')
        familiar_nuevo2 = Familiar.objects.create(
                name = 'Roberto',
                last_name = 'Nowicki',
                age= 62,
                dni= '14090856',
                birth_date = '16/10/1960')
        familiar_nuevo3 = Familiar.objects.create(
                name='Christian',
                last_name = 'Nowicki',
                age = 18,
                dni= '',
                birth_date = '15/06/2002'
        )
        

        context = { 'familiar_nuevo': familiar_nuevo, 'familiar_nuevo2': familiar_nuevo2, 'familiar_nuevo3':familiar_nuevo3}
        return render(request,'familiares1.html',context=context)

def probando_template(request):
    context = {
        'nombre':'Luca',
        'apellido':'Citta Giordano',
        'fecha':datetime.now(),
        'edades':[18,20,5,10,12,17,22,40]
    }
    return render(request, 'template_1.html', context = context)
