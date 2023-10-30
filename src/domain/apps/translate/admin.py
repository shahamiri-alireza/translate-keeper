from django.contrib import admin

from .models.dictionary import Dictionary


class DictionaryAdmin(admin.ModelAdmin):
    model = Dictionary
    list_display = (
        "id",
        "user",
        "name",
        "get_languages",
        "created_date",
    )
    search_fields = list_display
    list_filter = ("user__username", "name", "language")
    ordering = ("id", "user", "name", "language")

    def get_languages(self, obj):
        return " - ".join([p.name for p in obj.language.all()])


admin.site.register(Dictionary, DictionaryAdmin)
