from django.contrib import admin
from .models import CompletedTask, Task, Master, TypeRepair, AllObjects


admin.site.register(CompletedTask)
admin.site.register(Task)
admin.site.register(Master)
admin.site.register(TypeRepair)
admin.site.register(AllObjects)
