from django.shortcuts import render
from .models import media
from .forms import MediaForm , UserRegistrationForms
from django.shortcuts import get_list_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request, 'index.html')


def media_list(request):
    medi = media.objects.all().order_by('-created_at')
    return render(request, 'media_list.html', {'media': medi})


@login_required
def media_create(request):
     if request.method == 'POST':
         form = MediaForm(request.POST, request.FILES)
         if form.is_valid():
             media = form.save(commit=False)
             media.user = request.user
             media.save()
             return redirect('media_list')
     else:
         form = MediaForm()
         return render(request, 'media_form.html', {'form': form})
     
     
@login_required    
def media_edit(request, media_id):
         media = get_list_or_404(media, pk=media_id, user=request.user)
         if request.method == 'POST':
             form = MediaForm(request.POST, request.FILES, instance=media)
             if form.is_valid():
                 media = form.save(commit=False)
                 media.user = request.user
                 media.save()
                 login(request, user)
                 return redirect('media_list')
         else:
             form = MediaForm(instance=media)
             return render(request, 'media_form.html', {'form': form})
         
@login_required         
def media_delete(request, media_id):
             medi = get_list_or_404(media, pk=media_id, user=request.user)
             if request.method == 'POST':
               medi.delete()
             return render(request, 'media_confirm_delete.html', {'media': medi})
         
         
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('/media_list')
    else:
        form = UserRegistrationForms()
        return render(request, 'registration/register.html', {'form': form})