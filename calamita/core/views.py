from os import mkdir
from os.path import join, exists

from django.shortcuts import render
from django.contrib import messages
from django.views.generic import FormView

from .models import Location, Url
from .forms import LocationForm
from calamita.settings import MEDIA_ROOT


def index(request):
    context = {
        'title': 'Сервис обмена любимыми локациями',
        'locations': Location.objects.all()
    }
    return render(request, 'core/index.html', context=context)


def location(request):
    title = request.GET.get('title')
    context = {
        'title': title,
        'l': Location.objects.get(title=title),
        'list_for_dss': [1, 4, 2, 4],
        'js_scroll': True
    }
    return render(request, 'core/location.html', context=context)


class LocationFormView(FormView):

    form_class = LocationForm
    template_name = 'core/create.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        images = request.FILES.getlist('images')
        if form.is_valid():
            l = save_location_meta(request, form)
            save_images_url(l, images)
            messages.success(request, 'Локация была успешна добавлена!')
            return self.form_valid(form)
        else:
            messages.warning(request, 'Проверьте, верно ли указан адрес, и попробуйте снова.')
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать локацию'
        return context


def save_location_meta(request, form):
    data = form.cleaned_data
    l = Location(
        title=data.get('title'),
        category=data.get('category'),
        description=data.get('description'),
        longitude=data.get('longitude'),
        latitude=data.get('latitude'),
        user=request.user
    )
    l.save()
    return l


def save_images_url(location, images):
    for img in images:
        location_url = join(location.title, img.name).replace('\\', '/')
        url = Url(location=location, location_url=location_url)
        url.save()
        pathdir = join(MEDIA_ROOT, location.title)
        if not exists(pathdir):
            mkdir(pathdir)
        with open(join(pathdir, img.name), 'wb') as f:
            for chunk in img.chunks():
                f.write(chunk)
