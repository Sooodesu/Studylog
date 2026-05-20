from django.shortcuts import render, redirect,get_object_or_404
from .models import StudyLog
from .forms import StudyLogForm

def log_list(request):
    logs = StudyLog.objects.order_by('-study_date')

    return render(request, 'logs/list.html', {
        'logs': logs
    })
    
def log_create(request):
    
    if request.method == 'POST':
        form = StudyLogForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('log_list')
        
    else:
        form = StudyLogForm()
        
    return render(request,'logs/create.html',{
        'form': form
    })

def log_update(request,pk):
    log = get_object_or_404(StudyLog, pk=pk)
    
    if request.method == 'POST':
        
        form = StudyLogForm(request.POST, instance=log)
        
        if form.is_valid():
            form.save()
            
            return redirect('log_list')
        
    else:
        form = StudyLogForm(instance=log)
        
    return render(request, 'logs/update.html',{
        'form': form
    })
    
def log_delete(request,pk):
    log = get_object_or_404(StudyLog, pk=pk)
    
    if request.method == 'POST':
        log.delete()
        
        return redirect('log_list')
    
    return render(request, 'logs/delete.html',{
        'log': log
    })