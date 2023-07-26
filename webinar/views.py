from django.shortcuts import render
from .forms import SearchForm
from django.views.generic import View, TemplateView
from .forms import SearchForm
# Create your views here.

#Vue basée sur les fonctions
def home(request):
    if request.method == "GET":
        form = SearchForm(request.POST or None)
        if form.is_valid():
            """Traitement du formulaire valide"""
            #rediriger
        else:
            """Traitement du formulaire invalide"""
    else:
        print("La méthode home a été bien appelée après un autre verbe")
    context = {"form": form}

    return render(request, "webinar/home.html", context)



class HomzView(TemplateView):
    template_name = "webinar/home.html"
    def get_template_name(self):
        if self.template_name is None:
            """Error"""
        else:
            return self.template_name
    def get(request, self, *args, **kwargs):
        context = {"message": "A la muerte"}
        return render(request, self.get_template_name, context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(self, **kwargs)
        context['message'] = "Hello world"
        return context
