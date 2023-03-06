from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Comment
from .forms import InsertNewComment


@login_required(login_url='/register/login_user')
def comment_list(request):
    cmnt_list = list(Comment.objects.all())
    return render(request, "commentstoreapp/comment_list.html", {'cmnt_list': cmnt_list})


@login_required(login_url='/register/login_user')
def add_comment(request):
    if request.method == 'POST':
        form = InsertNewComment(request.POST)
        if form.is_valid():
            t = Comment(name=form.cleaned_data['name'], visit_date=form.cleaned_data['visit_date'],
                        comment_str=form.cleaned_data['comment_str'])
            t.save()
            return redirect('comment_list')
        else:
            return render(request, 'commentstoreapp/add_comment.html', {'insert_new_comment': form})
    else:
        form = InsertNewComment()
    return render(request, 'commentstoreapp/add_comment.html', {'insert_new_comment': form})
