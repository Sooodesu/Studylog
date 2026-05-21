from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import StudyLog, Tag
from .forms import StudyLogForm, TagForm

@login_required
def log_list(request):
    logs = StudyLog.objects.filter(user=request.user).order_by('-study_date')
    tags = Tag.objects.all()

    keyword = request.GET.get('q')
    
    if keyword:
        logs = logs.filter(title__icontains=keyword)
    
    tag_id = request.GET.get('tag')
    if tag_id:
        logs = logs.filter(tags=tag_id)

    tags = Tag.objects.all()

    return render(request, 'logs/list.html', {
        'logs': logs,
        'tags': tags
    })

def tag_list(request):
    tags = Tag.objects.all()
    
    return render(request, 'logs/tag_list.html',{
        'tags': tags
    })

@login_required    
def log_create(request):
    
    if request.method == 'POST':
        form = StudyLogForm(request.POST)
        
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            
            return redirect('log_list')
        
    else:
        form = StudyLogForm()
        
    return render(request,'logs/create.html',{
        'form': form
    })

def tag_create(request):
    
    if request.method == 'POST':

        form = TagForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('tag_list')

    else:

        form = TagForm()

    return render(request, 'logs/tag_create.html', {
        'form': form
    })
    
@login_required
def log_update(request,pk):
    log = get_object_or_404(StudyLog, pk=pk,user=request.user)
    
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
    
def tag_update(request, pk):
    
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == 'POST':

        form = TagForm(
            request.POST,
            instance=tag
        )

        if form.is_valid():

            form.save()

            return redirect('tag_list')

    else:

        form = TagForm(instance=tag)

    return render(request, 'logs/tag_update.html', {
        'form': form
    })

@login_required
def log_delete(request,pk):
    log = get_object_or_404(StudyLog, pk=pk,user=request.user)
    
    if request.method == 'POST':
        log.delete()
        
        return redirect('log_list')
    
    return render(request, 'logs/delete.html',{
        'log': log
    })
    
def tag_delete(request, pk):
    
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == 'POST':

        tag.delete()

        return redirect('tag_list')

    return render(request, 'logs/tag_delete.html', {
        'tag': tag
    })