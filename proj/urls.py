from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

# open api documentation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# jwt authentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
   openapi.Info(
      title="generic ecom CRUD API",
      default_version='v0.1',
      description='''generic ecommerce api with: products, reviews and user accounts
                     most Get views (categories, products) are cached with redis
                     authentication via JWT token (simple jwt)
                     swagger api documentation localhost:8000/swagger''',
      terms_of_service="none",
      contact=openapi.Contact(email="none"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)






router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('products/category/<str:cat>', views.ProductByCategory.as_view()),
    path('products/reviews/<int:id>', views.ReviewsByProduct.as_view()),
    path('categories/', views.AllCategories.as_view()),
    path('user/', views.UserList.as_view()),
    
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
