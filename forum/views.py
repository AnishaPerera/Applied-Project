from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Thread, Comment, Reply
from .forms import ThreadForm, CommentForm, ReplyForm

# Create your views here.

@login_required
def thread_create(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)

        if form.is_valid():
            thread = form.save(commit=False)
            thread.author = request.user
            thread.save()

            return redirect('forumidspage', thread_id=thread.pk)
    else:
        form = ThreadForm()

    return render(request, 'forum/thread_create.html', {'form':form})


@login_required
def thread_edit(request, thread_id):
    thread = get_object_or_404(Thread, thread_id=thread_id)
    if request.user == thread.author:
        if request.method == 'POST':
            form = ThreadForm(request.POST, instance=thread)
            if form.is_valid():
                form.save()
                return redirect('forumidspage', thread_id=thread.pk)
        else:
            form = ThreadForm(instance=thread)

        
        return render(request, 'forum/thread_edit.html', {'form':form, 'thread':thread})
    else:
        return redirect('forumidspage', thread_id=thread.pk)


@login_required
def thread_delete(request, thread_id):
    thread = get_object_or_404(Thread, thread_id=thread_id)
    if request.user == thread.author:
        if request.method == 'POST':
            thread.delete()
            return redirect('forumpage')
        else:
            return render(request, 'forum/thread_delete.html', {'thread': thread})
    else:
        return redirect('forumpage')


@login_required
def add_comments(request, thread_id):
    thread = get_object_or_404(Thread, thread_id=thread_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.thread_id = thread
            comment.author = request.user
            comment.save()

            return redirect('forumidspage', thread_id=thread.pk)
    else:
        form = CommentForm()
    
    return render(request, 'forum/add_comments.html', {'thread': thread, 'commentForm':form})


@login_required
def edit_comments(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('forumidspage', thread_id=comment.thread_id.pk)
        else:
            form = CommentForm(instance=comment)
        
        return render(request, 'forum/comment_edit.html', {'form':form, 'comment':comment})
    else:
        return redirect('forumidspage', thread_id=comment.thread_id.pk)

@login_required    
def delete_comments(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        if request.method == 'POST':
            thread_id = comment.thread_id.pk
            comment.delete()

            return redirect('forumidspage', thread_id=thread_id)
        else:
            return render(request, 'forum/comment_delete.html', {'comment': comment})
    else:
        return redirect('forumpage')

@login_required
def add_reply(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.author = request.user
            reply.save()

            comment.save()
            return redirect('forumidspage', thread_id=comment.thread_id.pk)
    else:
        form = ReplyForm()
    
    return render(request, 'forum/add_reply.html', {'form':form, 'comment':comment})

@login_required
def edit_reply(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST,  instance=reply)
        if form.is_valid():
            form.save()
            return redirect('forumidspage', thread_id=reply.comment.thread_id.pk)
    else:
        form = ReplyForm(instance=reply)
    
    return render(request, 'forum/edit_reply.html',{'form':form, 'reply':reply})

@login_required
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    comment = reply.comment
    if request.method == 'POST':
        reply.delete()

        comment.save()

        return redirect('forumidspage', thread_id=reply.comment.thread_id.pk)
    
    return render(request, 'forum/delete_reply.html',{'reply':reply})

@login_required
def forum(request):
    threads = Thread.objects.all()
    return render(request, 'forum/forum.html', {'threads': threads})

@login_required
def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, thread_id=thread_id)
    return render(request, 'forum/thread.html', {'thread': thread})
