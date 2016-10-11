from django.http import Http404
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album



def index(request):
    all_Album = Album.objects.all()
    context = {'all_Album' : all_Album}
    return render(request,'music/index.html',context)

    #template = loader.get_template('music/index.html')
    #context = {
    #    'all_Album' : all_Album,
    #}
    #return HttpResponse(template.render(context,request))


    #html = ''
    #for album in all_Album:
    #    url = '/music/'+ str(album.id)+ '/'
    #    html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    #return HttpResponse(html)


def detail(request, album_id):
    album = get_object_or_404(Album,id=album_id)


    #try:
    #   album = Album.objects.get(id=album_id)
    #except Album.DoesNotExist:
    #    raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album':album})


        #return HttpResponse('<h1>detail Album ID is '+str(album_id)+'</h2>')