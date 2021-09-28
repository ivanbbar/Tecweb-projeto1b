from django.shortcuts import render, redirect
from .models import Note

def deleteNote(meuid):
    note = Note.objects.get(id=meuid)
    note.delete()

def updateNote(meuid, title, content, tag):
    note_item = (Note.objects.get(id=meuid))
    note_item.title, note_item.content = title, content
    note_item.tag = tag
    note_item.save()

def createNote(title, content, tag):
    note_item = Note(title=title, content=content, tag=tag)
    note_item.save()


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        meuid = request.POST.get('id-hidden')
        deleteId = request.POST.get('deleteNote')

        if deleteId != None:
            deleteNote(deleteId)

        elif meuid != 'None':
            updateNote(meuid, title, content, tag)

        else:
            createNote(title, content, tag)

        return redirect('index')
    else:
        allNotes = Note.objects.all()

        return render(request, 'notes/index.html', {'notes': allNotes})


def tagsList(request):
    tags = Note.objects.values('tag').distinct()
    tagsList = [i['tag'] for i in tags]
    return render(request, 'notes/tagsList.html', {'allTags': tagsList})


def tag(request, myTag):
    notesTag = Note.objects.filter(tag=myTag)
    return render(request, 'notes/tag.html', {'notes': notesTag})

