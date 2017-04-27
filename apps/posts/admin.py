from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from apps.posts.models import Category, Article


class ArticleAdminForm(forms.ModelForm):
    short_post = forms.CharField(label='Краткое описание',
                                 widget=CKEditorWidget())
    full_post = forms.CharField(label='Полное описание',
                                widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ('category',
                  'name',
                  'short_post',
                  'full_post',
                  'slug',
                  'thumb',
                  'date',
                  'tags')


class CategoryAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Category
        fields = ('name',
                  'description',
                  'slug',
                  'title_meta',
                  'description_meta',
                  'icon'
                  )


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Общие', {'fields': ['category', 'name', ]}),
        ('Статья', {'fields': ['short_post', 'full_post']}),
        ('SEO', {'fields': ['slug', 'title_meta', 'description_meta'],
                 'classes': ('collapse',)}),
        ('Тэги', {'fields': ('tags',), 'classes': ('collapse',)}),
        (None, {'fields': ('thumb',)}),
    ]
    filter_horizontal = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    form = ArticleAdminForm

    def save_model(self, request, instance, form, change):
        if 'category' in request.POST:
            category_id = request.POST.getlist('category')[0]
            category = Category.objects.get(pk=category_id)
            instance.slug_cat_unique = category.slug

        instance.save()


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name',
              'description',
              'slug',
              'title_meta',
              'description_meta',
              'icon')
    form = CategoryAdminForm


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
