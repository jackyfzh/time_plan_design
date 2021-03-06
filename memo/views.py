# 引入redirect重定向模块
from django.shortcuts import render, redirect
# 引入HttpResponse
from django.http import HttpResponse
# 引入刚才定义的ArticlePostForm表单类
from .forms import MemoForm
# 引入User模型
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# 导入数据模型ArticlePost
from .models import Memo

@login_required(login_url='/userprofile/login/')
def memo_list(request):
    # 取出所有博客文章
    memos = Memo.objects.filter(author=request.user)
    # 需要传递给模板（templates）的对象
    context = { 'memos': memos }
    # render函数：载入模板，并返回context对象
    return render(request, 'memo/list.html', context)

def memo_detail(request, id):
    # 取出相应的文章
    memo = Memo.objects.get(id=id)
    # 需要传递给模板的对象
    context = { 'memo': memo }
    # 载入模板，并返回context对象
    return render(request, 'memo/detail.html', context)

# 删文章
def memo_delete(request, id):
    # 根据 id 获取需要删除的文章
    memo = Memo.objects.get(id=id)
    # 调用.delete()方法删除文章
    memo.delete()
    # 完成删除后返回文章列表
    return redirect("memo:list")

@login_required(login_url='/userprofile/login/')
def memo_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        memo_post_form = MemoForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if memo_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_memo = memo_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_memo.author = User.objects.get(id=request.user.id)
            # 将新文章保存到数据库中
            new_memo.save()
            # 完成后返回到文章列表
            return redirect("memo:list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        memo_post_form = MemoForm()
        # 赋值上下文
        context = { 'memo_post_form': memo_post_form }
        # 返回模板
        return render(request, 'memo/create.html', context)