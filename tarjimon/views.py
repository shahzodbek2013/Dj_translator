from django.shortcuts import render
from googletrans import Translator


def home_page(request):
    tr = Translator()
    context = {}

    if request.method == 'POST':
        in_lang = request.POST.get('in_lang')
        to_lang = request.POST.get('to_lang')
        text = request.POST.get('text')
        
        context['result_text'] = tr.translate(text=text, src=in_lang, dest=to_lang).text
        context['old_text'] = text
        context['in_lang'] = in_lang
        context['to_lang'] = to_lang
    return render(request, 'home.html', context=context)
