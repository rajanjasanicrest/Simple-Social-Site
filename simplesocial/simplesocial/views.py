from django.views.generic import CreateView, TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = 'posts/post_list.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'