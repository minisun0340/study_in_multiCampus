from django.shortcuts import render

# Create your views here.
from django.views import View
from django_request_mapping import request_mapping


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        return render(request,'home.html');

    @request_mapping("/login", method="get")
    def login(self, request):
        context = {
            'center': 'login.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/logout", method="get")
    def logout(self, request):
        if request.session['sessionid'] != None:
            del request.session['sessionid'];
        return render(request, 'home.html');

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        print(id, pwd);
        context = {};
        if (id == 'qq') & (pwd == '11'):
            request.session['sessionid'] = id;
            context['center'] = 'loginok.html';
        else:
            context['center'] = 'loginfail.html';

        return render(request, 'home.html', context);

    @request_mapping("/register", method="get")
    def register(self, request):
        context = {
            'center': 'register.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self, request):
        # ID,PWD,NAME
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        name = request.POST['name'];
        print(id, pwd, name);
        context = {
            'center': 'registerok.html',
            'rname': name
        };
        return render(request, 'home.html', context);

    @request_mapping("/html5", method="get")
    def html5(self,request):
        context = {
            'center': 'html5.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/css3", method="get")
    def css3(self,request):
        context = {
            'center': 'css3.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/ajax", method="get")
    def ajax(self,request):
        context = {
            'center': 'ajax.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/json", method="get")
    def json(self,request):
        context = {
            'center': 'json.html'
        };
        return render(request, 'home.html', context);
