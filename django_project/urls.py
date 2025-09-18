from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from app.controllers.user_controller import router as user_router

# 建立 API
api = NinjaAPI(
    title="My Project API",     
    description="API",  
    version="1.0.0",            
)

# 加入 router
api.add_router("/users/", user_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),  
]
