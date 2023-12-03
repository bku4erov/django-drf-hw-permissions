from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement, AdvertisementStatusChoices
from advertisements.serializers import AdvertisementSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.filters import AdvertisementFilter
from rest_framework import permissions
from django.db.models import Q

class AdvertisementPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create', 'update', 'partial_update', 'destroy']:
            return permissions.IsAuthenticated()
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update', 'destroy']:
            return (obj.creator == request.user)
        return super().has_object_permission(request, view, obj)

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # filter_backends = [DjangoFilterBackend, AdvertisementFilter]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created_at', 'creator']
    permission_classes = [AdvertisementPermissions]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Advertisement.objects.all().exclude(
                ~Q(creator=self.request.user),
                status=AdvertisementStatusChoices.DRAFT
            )
        else:
            return Advertisement.objects.all().exclude(
                status=AdvertisementStatusChoices.DRAFT
            )

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ['create', 'update', 'partial_update']:
    #         return [IsAuthenticated()]
    #     return []
