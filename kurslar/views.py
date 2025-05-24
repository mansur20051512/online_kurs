from django.shortcuts import render, get_object_or_404
from .models import Kurs, Dars


def home(request):
    kurslar = Kurs.objects.all()
    return render(request, 'kurslar/index.html', {'kurslar': kurslar})

def kurslar_royxati(request):
    kurslar = Kurs.objects.all()
    return render(request, 'kurslar/kurslar.html', {'kurslar': kurslar})

def kurs_detail(request, slug):
    kurs = get_object_or_404(Kurs, slug=slug)
    darslar = Dars.objects.filter(kurs=kurs)

    # URL orqali video id olamiz (agar kerak bo‘lsa)
    video_id = request.GET.get('video', None)

    if video_id:
        try:
            tanlangan_video = darslar.get(id=video_id)
        except Dars.DoesNotExist:
            tanlangan_video = None
    else:
        tanlangan_video = None

    return render(request, 'kurslar/kurs_detail.html', {
        'kurs': kurs,
        'darslar': darslar,
        'tanlangan_video': tanlangan_video,
    })