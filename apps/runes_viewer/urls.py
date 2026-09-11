from .views import MetadataViewSet, VennViewSet


def register_routes(router):
   router.register('metadata', MetadataViewSet, basename='metadata')
   router.register('venn', VennViewSet, basename='venn diagram')
