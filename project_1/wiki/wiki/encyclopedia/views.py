from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_info(request, title):
    entry = util.get_entry(title)
    context = {
        'entry': entry,
        'entry_name': title
    }
    return render(request, "encyclopedia/entry_info.html", context=context)


def edit_entry(request, title):
    entry = util.get_entry(title)
    context = {
        'entry': entry,
        'entry_name': title
    }
    return render(request, "encyclopedia/edit_entry.html", context=context)


def save_entry(request, title):
    entry_dict = request.GET
    content = entry_dict.get('entry_content')

    util.save_entry(title, content)

    return redirect('entry_info', title=title)
    
