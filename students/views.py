from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate, logout
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import FormView,CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import  Course
from .forms import CourseEnrollForm
from account.forms import RegistrationForm


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        account = authenticate(email=email,password=raw_password)
        login(self.request,account)
        return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail',args=[self.course.id])


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        if 'module_id' in self.kwargs:
            context['module'] = course.modules.get(
                                    id=self.kwargs['module_id'])
        else:
            context['module'] = course.modules.all()[0]
        return context