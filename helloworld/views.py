from django.db.models import F,Q
from django.http import HttpResponseForbidden,JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from helloworld.models import Helloworld
from helloworld.forms import SnippetForm


def top(request):
    snippets = Helloworld.objects.order_by('code')
    trend_snippets = Helloworld.objects.order_by('-click_count',"code")[:10]
    context = {
        'snippets': snippets,
        "trend_snippets":trend_snippets,
    }
    return render(request, 'snippets/top.html', context)


@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk)
    else:
        form = SnippetForm()
    return render(request, 'snippets/snippet_new.html', {'form': form})


@login_required
def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Helloworld, pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden('このスニペットの編集は許可されていません．')
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('snippet_detail', snippet_id=snippet_id)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_edit.html', {'form': form})


def snippet_detail(request, snippet_id):
    ##指定されたIDの単語探して
    Helloworld.objects.filter(pk=snippet_id).update(
        click_count = F('click_count') + 1,
    )
    snippet = get_object_or_404(Helloworld, pk=snippet_id)
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})

def search_suggest(request):
   query = request.GET.get('q',"").strip()

   if not query :
       return JsonResponse({"results:[]"})

   snippets = Helloworld.objects.filter(
       Q(title__icontains=query) |
       Q(code__icontains=query) |
       Q(description__icontains=query)
   ).order_by("code")


   result = [
       {
           "title": snippet.title,
           "code": snippet.code,
           "url":reverse("snippet_detail",args = [snippet.id])
       }
       for snippet in snippets
   ]
   return JsonResponse({"results":result})