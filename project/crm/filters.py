import django_filters
from .models import TaskBoard

class TaskBoardFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')
    assigned_to = django_filters.NumberFilter(field_name='assigned_to__id')

    class Meta:
        model = TaskBoard
        fields = ['status', 'assigned_to']