from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)
from rest_framework import generics, permissions

from .forms import ProduceForm
from .models import Category, Produce
from .serializers import CategorySerializer, ProduceSerializer

# Create your views here.




class ProduceListCreateView(generics.ListCreateAPIView):
    serializer_class = ProduceSerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = ['category', 'unit']
    search_fields = ['name', 'category__name']
    ordering_fields = ['name', 'quantity', 'date_recorded']

    def get_queryset(self):
        return Produce.objects.filter(
            owner=self.request.user
        ).select_related('category')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProduceDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProduceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Produce.objects.filter(owner=self.request.user)


class CategoryListView(generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]





class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = 'records/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_records = Produce.objects.filter(owner=self.request.user)

        context['total_records'] = user_records.count()

        context['category_count'] = Category.objects.count()

        context['unique_produce'] = (
            user_records.values('name').distinct().count()
        )

        context['recent_records'] = (
            user_records.select_related('category')
            .order_by('-date_recorded')[:5]
        )

        return context



class ProduceListView(LoginRequiredMixin, ListView):

    model = Produce
    template_name = 'records/produce_list.html'
    context_object_name = 'produces'

    def get_queryset(self):
        queryset = Produce.objects.filter(
            owner=self.request.user
        ).select_related('category')

        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(category__name__icontains=search)
            )

        return queryset.order_by('-date_recorded')


class ProduceCreateView(LoginRequiredMixin, CreateView):

    model = Produce
    form_class = ProduceForm
    template_name = 'records/produce_form.html'
    success_url = reverse_lazy('produce-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProduceUpdateView(LoginRequiredMixin, UpdateView):

    model = Produce
    form_class = ProduceForm
    template_name = 'records/produce_form.html'
    success_url = reverse_lazy('produce-list')

    def get_queryset(self):
        return Produce.objects.filter(owner=self.request.user)


class ProduceDeleteView(LoginRequiredMixin, DeleteView):

    model = Produce
    template_name = 'records/produce_confirm_delete.html'
    success_url = reverse_lazy('produce-list')

    def get_queryset(self):
        return Produce.objects.filter(owner=self.request.user)
