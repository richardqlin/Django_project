from django.shortcuts import render, redirect

import random

from .forms import WordForm

from .models import Word
# Create your views here.

def frontpage(request):
    return render (request,'jumbleword/frontpage.html')

def clear(request):
    Word.objects.all().delete()
    print('hello')
    return redirect('/jumbleword')


def jumble(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/jumbleword/jumble')
    else:
        form = WordForm()
    return render(request,'jumbleword/jumble.html',{'form':form})


def findout(request):
    forms = list(Word.objects.all())
    total_words = len(forms)
    if total_words==0:
        return redirect('/jumbleword')
    shuffle = []
    score = 0
    if request.method == 'POST':
        form = dict(request.POST)['word']
        answers = [x for x in form]
        total_forms=[x.word for x in forms ]
        total_answer=len(answers)
        for i in range(total_answer):
            if total_forms[i] == answers[i]:
                score += 1
        return render(request,'jumbleword/result.html',{'score':score,'total':total_words})
    form = WordForm()
    for doc in forms:
        jumble_letter = list(doc.word)
        random.shuffle(jumble_letter)
        jumble_word = ''.join(jumble_letter)
        shuffle.append(jumble_word)
    return render(request,'jumbleword/findout.html',{'form':form,'shuffle':shuffle})


