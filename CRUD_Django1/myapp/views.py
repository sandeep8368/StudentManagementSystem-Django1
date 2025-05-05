from django.shortcuts import render, redirect
from myapp.models import StudentModel
# Create your views here.
def display_view(request):
    all_data = StudentModel.objects.all()
    return render(request, 'html/display.html', {'data': all_data})



def add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        
        StudentModel.objects.create(
            name = name,
            email = email,
            password = password
        )
        
    return render(request, 'html/add.html')
        
        
        
def delete_view(request,id):
    all_student = StudentModel.objects.get(id=id)
    all_student.delete()
    return render(request, 'html/display.html')



def update_view(request,id):
    student = StudentModel.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.password = request.POST.get('pass')
        student.save()
        
        return redirect('dis')
    return render(request, 'html/update.html', {"data": student})