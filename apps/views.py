
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView, ListView

from apps.forms import RegisterForm, ProfileForm
from apps.models import User, Product, Category


class RegisterFormView(FormView):
    template_name = 'Auth/reg.html'
    form_class = RegisterForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')


class CustomLoginView(TemplateView):
    template_name = 'Auth/login.html'

    def post(self, request, *args, **kwargs):
        email = self.request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            user = authenticate(request, username=user.email, password=request.POST['password'])

            if user:
                login(request, user)
                return redirect('product')
            else:
                context = {
                    "messages_error": ["Invalid password or email"]
                }
                return render(request, template_name='', context=context)
        else:
            return redirect('login')


class CategoryListView(ListView):
    queryset = Product.objects.all()
    template_name = 'Product/product.html'
    context_object_name = 'products'
    # paginate_by = 2

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['categories'] = Category.objects.all()
        return data


def Prod(request,slug):
    context = {
        "products": Product.objects.filter(category_id=slug),
        "categories": Category.objects.all()
    }

    return TemplateResponse(request,'Product/product.html',context=context)


class ProductList(ListView):
    queryset = Product.objects.all()
    template_name = 'product_delete/del_up_product.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        return data


class ProductDelete(View):
    def get(self,request,pk,*args,**kwargs):
        Product.objects.filter(id=pk).delete()
        return redirect('my-orders')

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['categories'] = Category.objects.all()
        return data


class ProfileFormView(FormView):
    template_name = 'Profilim/profil.html'
    form_class = ProfileForm

    def form_valid(self, form):
        if form.is_valid():
            # form.cleaned_data['password'] = make_password(form.cleaned_data['password'])
            User.objects.filter(pk=self.request.user.pk).update(**form.cleaned_data)
        return redirect('profile')

    def form_invalid(self, form):
        print(10)