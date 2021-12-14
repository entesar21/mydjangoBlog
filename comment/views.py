from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Comment
from .form import NewComment

def comments(request):
    comments = models.Comment.objects.all()
    print(comments)
    return render(request, 'comments.html',{'comments' : comments})


def new_comment(request):
    form = NewComment(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        site_name = form.cleaned_data.get("site_name")
        host = form.cleaned_data.get("host")
        your_post = form.cleaned_data.get("your_post")
        web_design = form.cleaned_data.get("web_design")
        work_field = form.cleaned_data.get("work_field")
        budget = form.cleaned_data.get("budget")
        support = form.cleaned_data.get("support")

        cooperation = form.cleaned_data.get("cooperation")
        details = form.cleaned_data.get("details")
        contacts = form.cleaned_data.get("contacts")

        site_system = form.cleaned_data.get("site_system")
        budget_amount = form.cleaned_data.get("budget_amount")
        who_support = form.cleaned_data.get("who_support")
        content_technical = form.cleaned_data.get("content_technical")

        new_comment = Comment.objects.create(site_name=site_name, host=host, your_post=your_post,web_design=web_design,
                                             work_field=work_field,budget=budget,
                                             support=support,cooperation=cooperation,
                                             details=details,contacts=contacts,
                                             site_system=site_system,budget_amount=budget_amount,
                                             who_support=who_support,content_technical=content_technical)
        print(new_comment)

    return render(request,'new_comment.html',context)