from django.shortcuts import render, redirect
from .models import CompletedTask, Task, Master, TypeRepair
from .forms import FromTask, FormCompletedTask
from django.contrib.auth.decorators import login_required

from .send_email import send_for_email
 
def index(request):
    return render(request, "index.html")


def post_detail(request, pk):
    try:
        users = CompletedTask.objects.get(id=pk)
        return render(request, "index.html", {'name': users.name, 'video': users.video.name, 'comment': users.comment})
    except:
        return render(request, "not_found.html", {'pk': pk})


def new_task(request):
    new_task = Task()
    if request.method == 'POST':
        form_new_task = FromTask(request.POST)
        if form_new_task.is_valid():
            new_task.name = form_new_task.cleaned_data.get('name')
            new_task.home = form_new_task.cleaned_data.get('home')
            new_task.problem = form_new_task.cleaned_data.get('problem')
            new_task.comment = form_new_task.cleaned_data.get('comment')
            new_task.phone = form_new_task.cleaned_data.get('phone')
            new_task.email = form_new_task.cleaned_data.get('email')
            new_task.save()
            master_info = Master.objects.get(type_reair=new_task.problem)

            send_for_email(master_info.user.email, f'Новая заявка №{new_task.id}! Ознакомьтесь в личном кабинете', new_task.date,  new_task.home)
            return redirect('index')
    else:
        form_new_task = FromTask()
    return render(request, "newtask.html", {"form_new_task": form_new_task})


@login_required
def profile(request):
    if request.user.is_authenticated and request.user.username != "admin":
        master = Master.objects.get(user=request.user.id).type_reair
        tasks = Task.objects.filter(problem=master)[::-1]

        completed_task = CompletedTask()

        if request.method == 'POST':
            form_completed_task = FormCompletedTask(request.POST, request.FILES)
            if form_completed_task.is_valid():
                Task.objects.filter(id=request.POST.get('this_id')).update(is_complete = True)
                task = Task.objects.get(id=int(request.POST.get('this_id')))

                completed_task.name = Master.objects.get(user=request.user.id).user.first_name
                completed_task.organization = task.home
                completed_task.video = form_completed_task.cleaned_data.get('video')
                completed_task.comment = form_completed_task.cleaned_data.get('comment')
                completed_task.phone = task.phone
                completed_task.email = task.email
                completed_task.save()

                this_id = completed_task.id
                finally_completed_task = CompletedTask.objects.get(id=this_id)
                send_for_email(task.email, f'Ваша заявка выполнена!\nМожно ознакомиться по ссылке: http://127.0.0.1:8000/post/{str(this_id)}', finally_completed_task.date, task.home)
                return redirect('profile')

        else:
            form_completed_task = FormCompletedTask()
        return render(request, 'profile.html', {"master": master, "tasks": tasks, "form_completed_task": form_completed_task})

    elif request.user.is_authenticated and request.user.username == "admin":
        masters = Master.objects.all()
        masters_and_tasks = []
        for master in Master.objects.all():
            TEMP_2_masters_and_tasks = []
            for task in Task.objects.filter(problem=master.type_reair):
                TEMP_2_masters_and_tasks.append(task)
            TEMP_3_masters_and_tasks = []
            TEMP_3_masters_and_tasks.append(master)
            how_complete_task = 0
            for i in TEMP_2_masters_and_tasks:
                if i.is_complete == True:
                    how_complete_task += 1
            TEMP_3_masters_and_tasks.append(how_complete_task/len(TEMP_2_masters_and_tasks)*100)
            TEMP_3_masters_and_tasks.append(TEMP_2_masters_and_tasks)
            masters_and_tasks.append(TEMP_3_masters_and_tasks)
            
        return render(request, 'profile_Admin.html', {"masters_and_tasks": masters_and_tasks, "masters": masters})

    else:
        return redirect("login")