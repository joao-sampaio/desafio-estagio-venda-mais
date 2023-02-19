from django.contrib import admin
from .models import Atendimento, Pagamento, Servico, User, Situacao
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("username", 'user_type')
    list_filter = ("username", 'user_type')
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email", "endereco", "telefone")}),
        ("Permissions", {"fields": ("is_active","groups",)}),
        ("Tipo", {"fields": ("user_type",)}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2",
                "is_active",
            )}
        ),
    )
    search_fields = ("username", 'email')
    ordering = ("username",)
    def get_readonly_fields(self, request, obj=None):
        if request.user.user_type < 5:
            return self.readonly_fields + ('user_type', 'groups')
        return self.readonly_fields
    def save_model(self, request, obj, form, change) -> None:
        super().save_model(request, obj, form, change)
        if request.user.user_type == 4:
            group = Group.objects.get(name='Atendentes') 
            group.user_set.add(obj)
            obj.user_type = 3
            obj.is_staff = True
            obj.save()
        elif request.user.user_type == 5:
            group = Group.objects.get(name='Gerentes')
            group.user_set.add(obj)
            obj.user_type
            obj.save()
    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        if request.user.user_type == 4:
            qs = qs.filter(user_type=3)
        elif request.user.user_type == 3:
            qs = qs.filter(user_type=2)
        return qs

admin.site.register(Situacao)
admin.site.register(Pagamento)

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'disp',)
    list_editable= ('preco', 'disp')
    def get_queryset(self, request):
        qs = super(ServicoAdmin, self).get_queryset(request)
        print(qs)
        if request.user.user_type < 3:
            qs = []
        elif request.user.user_type == 3:
            qs = qs.filter(disp=True)
        return qs
    def save_model(self, request, obj, form, change) -> None:

        if request.user.user_type < 4:
            obj.desconto = 0
        super().save_model(request, obj, form, change)


red = '<p style="color:red;">'
green = '<p style="color:green;">'
yellow = '<p style="color:yellow;">'
colors = {'Cancelado': red, 'Pendente': yellow, 'Realizado': green}
@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'atendente', 'color_status')
    list_display_links = ('__str__',)
    readonly_fields = ('valor_pago', 'cliente')
    list_filter = ('data_servico', 'situacao')
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "atendente":
            kwargs["queryset"] = User.objects.filter(user_type=3)
        elif db_field.name == "helper":
            kwargs["queryset"] = User.objects.filter(user_type=2)
        elif db_field.name == "servico":
            if request.user.user_type < 4:
                kwargs["queryset"] = Servico.objects.filter(disp=True)
        return super(AtendimentoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    def color_status(self, obj): 
        color = colors[str(obj.situacao)]
        return mark_safe(f'{color}{obj.situacao}</p>')