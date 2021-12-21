from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required

def filmy(request):
    #return HttpResponse ("First test")
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': wszystkie})
@login_required
def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(filmy)
    return render(request, 'film_form.html', {'form': form})
@login_required
def edit(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect(filmy)
    return render(request, 'film_form.html', {'form': form})
@login_required
def delete(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == "POST":
        film.delete()
        return redirect(filmy)

    return render(request, 'confirm.html', {'film': film})

