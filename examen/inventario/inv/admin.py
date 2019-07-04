from django.contrib import admin
from .models import Inventario, Carga
from pyxlsb import open_workbook
# Register your models here.


class Test(admin.ModelAdmin):
     def save_model(self, request, obj, form, change):
         js = []
         with open_workbook(request.FILES['archivo']) as wb:
              with wb.get_sheet(1) as sheet:
                   for row in sheet.rows(sparse=True):
                       if row[0].r >0:
                          p = Inventario(serie=row[0].v, cantidad=row[1].v, precio=row[2].v)
                          p.save()
                          js.append({"serie": row[0].v, "cantidad":row[1].v, "precio":row[2].v})
                   obj.my_json_field = js
         super(Test, self).save_model(request, obj, form, change)


admin.site.register(Inventario)
admin.site.register(Carga, Test)
