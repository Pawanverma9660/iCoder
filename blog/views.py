from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return render(request,'blog/blogHome.html')
    # return HttpResponse('this is BlogHome : we will keep all the blog post here')

def blogPost(request,slug):
    return render(request,'blog/blogPost.html')
    # return HttpResponse(f'this is BlogPost : {slug}')
