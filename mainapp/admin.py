from django.contrib import admin

#Personalización del panel de control
title = "Blog Personal"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
