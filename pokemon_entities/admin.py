from django.contrib import admin
from django.utils.html import format_html

from .models import Pokemon, PokemonEntity, PokemonElementType


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    fields = ['title', 'title_en', 'title_jp', 'image', 'get_image_preview',
              'description', 'element_type', 'previous_evolution']
    readonly_fields = ['get_image_preview']

    def get_image_preview(self, obj):
        if not obj.image or not obj.id:
            return 'нет изображения'
        return format_html(f'<img src={obj.image.url} height="200"/')
    get_image_preview.short_description = 'превью'


@admin.register(PokemonElementType)
class PokemonElementTypeAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'get_image_preview', 'strong_against']
    readonly_fields = ['get_image_preview']

    def get_image_preview(self, obj):
        if not obj.image or not obj.id:
            return 'нет изображения'
        return format_html(f'<img src={obj.image.url} height="20"/')

    get_image_preview.short_description = 'превью'


admin.site.register(PokemonEntity)
