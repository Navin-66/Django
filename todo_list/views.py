from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm

from django.http import JsonResponse
from botbuilder.schema import Activity
import aiohttp

from botbuilder.core import BotFrameworkAdapter

def handle_bot_messages(request):
    if request.method == 'POST':
        activity_data = request.body.decode('utf-8')
        activity = Activity().deserialize(activity_data)
        
        # Create an instance of BotFrameworkAdapter
        adapter = BotFrameworkAdapter(app_id='46f57800-deac-4cb5-8d89-e245b135754c', app_password='b2eb69b3-5cce-45a4-8286-1b73c5d9fa41')
        
        # Implement your bot logic here
        # You can send a response back to the user using adapter.send_activities()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def home(request):
    try:
        if request.method == "POST":
            form = ListForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'The item has been added to the list successfully!')
    except Exception as e:
        return render(request, 'home.html', {'all_items': all_items})

    all_items = List.objects.all()
    return render(request, 'home.html', {'all_items': all_items})

def about(request):
    return render(request, 'about.html', {})

def delete(request, item_id):
    item = List.objects.get(pk=item_id)
    item.delete()
    messages.success(request, ('The item has been deleted successfully!'))
    return redirect('home')

def cross_off(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, item_id):
    if request.method == "POST":
        item = List.objects.get(pk=item_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('The item has been edited successfully!'))
            return redirect('home')   
    else:
        item = List.objects.get(pk=item_id)
        return render(request, 'edit.html', {'item': item})
