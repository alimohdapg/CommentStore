from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from commentstoreapp.commentstore import CommentStore
from commentstoreapp.forms import InsertNewComment


@login_required(login_url='/register/login_user')
def comment_list(request):
    store = CommentStore()
    cmnt_list = list(store.comment_list.queue)
    return render(request, "commentstoreapp/comment_list.html", {'cmnt_list': cmnt_list})


@login_required(login_url='/register/login_user')
def add_comment(request):
    store = CommentStore()
    if request.method == 'POST':
        form = InsertNewComment(request.POST)
        if form.is_valid():
            store.insert_comment(form.cleaned_data['name'], form.cleaned_data['visit_date'],
                                 form.cleaned_data['comment_str'])
            return redirect('comment_list')
        else:
            return render(request, 'commentstoreapp/add_comment.html', {'insert_new_comment': form})
    else:
        form = InsertNewComment()
    return render(request, 'commentstoreapp/add_comment.html', {'insert_new_comment': form})
