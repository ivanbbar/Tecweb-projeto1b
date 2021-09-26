from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import NoteSerializer

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

@api_view(['GET', 'POST'])
def api_note(request, noteId):
    try:
        note = Note.objects.get(id=noteId)
    except Note.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        new_note_data = request.data
        note.title = new_note_data['title']
        note.content = new_note_data['content']
        note.tag = new_note_data['tag']
        note.save()

    return Response(NoteSerializer(note).data)

@api_view(['GET', 'POST'])
def api_notes(request):
    if request.method == 'POST':
        newNote = request.data
        newNote = Note(title=newNote['title'], content=newNote['content'], tag=newNote['tag'])
        newNote.save()

    all_notes = Note.objects.all()

    return Response(NoteSerializer(all_notes, many=True).data)