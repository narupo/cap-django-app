{@ 
    n = opts.get("n") or opts.get("app-name")
    if n == nil:
        puts("n is nil in views.py")
        exit(0)
    end
@}from django.shortcuts import render


def home_view(request):
    return render(request, '{: n :}/home.html')



