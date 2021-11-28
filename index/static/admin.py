from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from django import forms
from .models import Users, Viloyat, Tuman, Tip_documents, Documents, Sub_tip_documents, \
 Application, Company, Services, Profile, Profile_edit
from adminsortable2.admin import SortableAdminMixin

# Register your models here.

admin.site.site_header = 'ГЕОПОРТАЛ ГГК Республики Узбекистан'
admin.site.site_title = 'ГЕОПОРТАЛ ГГК'
admin.site.index_title = 'ГЕОПОРТАЛ ГГК'

from .models import Services, Profile
from proj.redline_models import adminsRedline

admin.site.register(adminsRedline)

from proj.funk_genplan_models import adminsFunkGenplans

admin.site.register(adminsFunkGenplans)

from proj.funk_apot_models import adminsFunkApots

admin.site.register(adminsFunkApots)

from proj.geologik_rayon_models import adminsGeologRayon

admin.site.register(adminsGeologRayon)

from proj.funk_genplan_models import FunkZones


class FunkZonesAdmin(admin.ModelAdmin):
    list_display = ['disUz', 'disRu']
    ordering = ['type']


admin.site.register(FunkZones, FunkZonesAdmin)

from proj.reestr_add_models import Crontab_data


class Crontab_dataAdmin(admin.ModelAdmin):
    list_display = ['service', 'date']
    ordering = ['date']


admin.site.register(Crontab_data, Crontab_dataAdmin)


# new admin models
class ViloyatAdmin(admin.ModelAdmin):
    list_display = ['vil_id', 'disUz']


from proj.reestr_projects_models import Apz


class ServicesAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Services
    list_display = ("title", "zindex")
    search_fields = ("title",)


admin.site.register(Services, ServicesAdmin)


# admin.site.register(Test)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user')
    filter_horizontal = ('services',)


admin.site.register(Profile, ProfileAdmin)

class Profile_editAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    filter_horizontal = ('services',)

admin.site.register(Profile_edit, Profile_editAdmin)



class ApzAdmin(LeafletGeoAdmin):
    list_display = ['task_id', 'name_building', 'location_building', 'passport_number', 'tin', 'legal_entity_tin',
                    'region', 'district', 'date']
    list_display_links = ['task_id', 'name_building']
    ordering = ['date']
    search_fields = ['task_id', 'date', 'district', 'region', 'name_building', 'location_building', 'passport_number',
                     'tin', 'legal_entity_tin', 'task_id']
    fields = (
        'our_id', 'date', 'task_id', 'name_building', 'location_building', 'passport_number', 'tin', 'legal_entity_tin',
        'region', 'district')
    readonly_fields = ['date', 'task_id', 'name_building', 'location_building', 'passport_number', 'tin',
                       'legal_entity_tin', 'region', 'district', 'date']


admin.site.register(Apz, ApzAdmin)

from proj.reestr_projects_models import Psd


class PsdAdmin(LeafletGeoAdmin):
    list_display = ['task_id', 'name_design_estimates', 'legal_entity_tin', 'tin_project_org', 'passport_number',
                    'individual_tin', 'region_id', 'district_id', 'date']
    ordering = ['date']
    list_display_links = ['task_id', 'name_design_estimates']
    search_fields = ['task_id', 'name_design_estimates', 'tin_project_org', 'legal_entity_tin', 'passport_number',
                     'individual_tin', 'region_id', 'district_id', 'date']
    fields = (
        'our_id', 'date', 'task_id', 'name_design_estimates', 'tin_project_org', 'legal_entity_tin', 'passport_number',
        'individual_tin', 'region_id', 'district_id')
    readonly_fields = ['date', 'task_id', 'name_design_estimates', 'tin_project_org', 'legal_entity_tin',
                       'passport_number', 'individual_tin', 'region_id', 'district_id']


admin.site.register(Psd, PsdAdmin)

from proj.reestr_projects_models import Psd_ind


class Psd_indAdmin(LeafletGeoAdmin):
    list_display = ['task_id', 'object_name', 'object_adress', 'passport_number', 'tin', 'region', 'district', 'date']
    ordering = ['date']
    list_display_links = ['task_id', 'object_name', 'object_adress']
    search_fields = ['our_id', 'task_id', 'object_name', 'object_adress', 'passport_number', 'tin', 'region',
                     'district', 'date']
    fields = (
        'our_id', 'date', 'task_id', 'object_name', 'object_adress', 'passport_number', 'tin', 'region', 'district')
    readonly_fields = ['date', 'task_id', 'object_name', 'object_adress', 'passport_number', 'tin', 'region',
                       'district']


admin.site.register(Psd_ind, Psd_indAdmin)

from proj.reestr_objects_models import Perm_rec


class Perm_recAdmin(LeafletGeoAdmin):
    list_display = ['task_id', 'name_building', 'building_location', 'passport_number', 'tin', 'legal_entity_tin',
                    'district', 'date']
    ordering = ['date']
    list_display_links = ['task_id', 'name_building', 'building_location']
    search_fields = ['task_id', 'name_building', 'building_location', 'passport_number', 'tin', 'legal_entity_tin',
                     'district', 'date']
    fields = (
        'our_id', 'date', 'task_id', 'name_building', 'building_location', 'passport_number', 'tin', 'legal_entity_tin',
        'district')
    readonly_fields = ['date', 'task_id', 'name_building', 'building_location', 'passport_number', 'tin',
                       'legal_entity_tin', 'district']


admin.site.register(Perm_rec, Perm_recAdmin)

from proj.reestr_add_models import Location_obj


class Location_objAdmin(LeafletGeoAdmin):
    list_display = ['our_id', 'adress', 'apz', 'psd', 'psd_ind', 'perm_rec', 'smr', 'pexpl', 'pexpl_ind']
    ordering = ['pk']
    list_display_links = ['adress', 'our_id']
    search_fields = ['adress', 'our_id', 'apz', 'psd', 'psd_ind', 'perm_rec', 'smr', 'pexpl', 'pexpl_ind']
    fields = ('our_id', 'adress', 'geoPoint', 'geoPolygon')
    readonly_fields = ['our_id']

    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions

    # def has_delete_permission(self, request, obj=None):
    # 	return False

    def my_delete_selected(self, request, queryset):
        for i in queryset:
            Location_obj.objects.get(pk=i.pk).delete()

    my_delete_selected.short_description = "Belgilanganlarni o'chirish"

    actions = ['my_delete_selected', ]

    class Media:
        js = (
            '/static/js/jquery/jquery1.12.js',
            '/static/admin_maps.js',
        )


admin.site.register(Location_obj, Location_objAdmin)

from proj.reestr_objects_models import Smr


class SmrAdmin(LeafletGeoAdmin):
    list_display = ['task_id', 'name_building', 'location_building', 'passport_number', 'tin', 'legal_entity_tin',
                    'region_id', 'district_id', 'date']
    ordering = ['date']
    list_display_links = ['task_id', 'name_building', 'location_building']
    search_fields = ['task_id', 'name_building', 'location_building', 'passport_number', 'tin', 'legal_entity_tin',
                     'region_id', 'district_id', 'date']
    fields = (
        'our_id', 'date', 'task_id', 'name_building', 'location_building', 'passport_number', 'tin', 'legal_entity_tin',
        'region_id', 'district_id')
    readonly_fields = ['date', 'task_id', 'name_building', 'location_building', 'passport_number', 'tin',
                       'legal_entity_tin', 'region_id', 'district_id']


admin.site.register(Smr, SmrAdmin)

from proj.reestr_objects_models import Pexpl


class PexplAdmin(LeafletGeoAdmin):
    list_display = ['task_id', 'buildings_name', 'buildings_location', 'tin_project_org', 'tin_contractor_org',
                    'passport_number', 'tin', 'legal_entity_tin', 'region_id', 'district_id', 'date']
    ordering = ['date']
    list_display_links = ['task_id', 'buildings_name', 'buildings_location']
    search_fields = ['task_id', 'buildings_name', 'buildings_location', 'tin_project_org', 'tin_contractor_org',
                     'passport_number', 'tin', 'legal_entity_tin', 'region_id', 'district_id', 'date']
    fields = (
        'our_id', 'date', 'task_id', 'buildings_name', 'buildings_location', 'tin_project_org', 'tin_contractor_org',
        'passport_number', 'tin', 'legal_entity_tin', 'region_id', 'district_id')
    readonly_fields = ['date', 'task_id', 'buildings_name', 'buildings_location', 'tin_project_org',
                       'tin_contractor_org', 'passport_number', 'tin', 'legal_entity_tin', 'region_id', 'district_id']


admin.site.register(Pexpl, PexplAdmin)

from proj.reestr_objects_models import Pexpl_ind


class Pexpl_indAdmin(LeafletGeoAdmin):
    list_display = ['task_id', 'buildings_name', 'buildings_location', 'tin_project_org', 'tin_contractor_org',
                    'passport_number', 'tin', 'legal_entity_tin', 'region_id', 'district_id', 'date']
    ordering = ['date']
    list_display_links = ['task_id', 'buildings_name', 'buildings_location']
    search_fields = ['task_id', 'buildings_name', 'buildings_location', 'tin_project_org', 'tin_contractor_org',
                     'passport_number', 'tin', 'legal_entity_tin', 'region_id', 'district_id', 'date']
    fields = (
        'our_id', 'date', 'task_id', 'buildings_name', 'buildings_location', 'tin_project_org', 'tin_contractor_org',
        'passport_number', 'tin', 'legal_entity_tin', 'region_id', 'district_id')
    readonly_fields = ['date', 'task_id', 'buildings_name', 'buildings_location', 'tin_project_org',
                       'tin_contractor_org', 'passport_number', 'tin', 'legal_entity_tin', 'region_id', 'district_id']


admin.site.register(Pexpl_ind, Pexpl_indAdmin)

from proj.reestr_add_models import Authority


class AuthorityAdmin(admin.ModelAdmin):
    list_display = ['kod', 'title']
    list_display_links = ['title']
    ordering = ['title']
    search_fields = ['title']


admin.site.register(Authority, AuthorityAdmin)

from proj.reestr_subjects_models import Loyihalovchi


class LoyihalovchiAdmin(LeafletGeoAdmin):
    list_display = ['nomi', 'adress', 'inn']
    search_fields = ['nomi', 'inn']
    ordering = ['id']

    class Media:
        js = (
            '/static/js/jquery/jquery1.12.js',
            '/static/admin_maps.js',
        )


admin.site.register(Loyihalovchi, LoyihalovchiAdmin)

from proj.reestr_subjects_models import Quruvchi


class QuruvchiAdmin(LeafletGeoAdmin):
    list_display = ['nomi', 'adress', 'inn']
    search_fields = ['nomi', 'inn']
    ordering = ['id']

    class Media:
        js = (
            '/static/js/jquery/jquery1.12.js',
            '/static/admin_maps.js',
        )


admin.site.register(Quruvchi, QuruvchiAdmin)


class TumanAdmin(admin.ModelAdmin):
    list_display = ['nomi']
    list_display_links = ['nomi']
    list_filter = ['nomi']
    search_fields = ['nomi']


class Tip_documentsAdmin(admin.ModelAdmin):
    list_display = ['tip_dis']
    ordering = ['tip_dis']


class Myform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        print(1)


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['tip_doc', 'sub_tip_doc', 'doc_nomi', 'nomer_doc', 'data']
    list_display_links = ['doc_nomi']

    class Media:
        js = (
            '/static/js/jquery/jquery1.12.js',
            '/static/admin_pod9.js',
        )


class Sub_tip_documentsAdmin(admin.ModelAdmin):
    list_display = ['sub_tip_dis', 'tip_doc']
    ordering = ['tip_doc']
    search_fields = ['sub_tip_doc']


admin.site.register(Users)

admin.site.register(Tuman, TumanAdmin)
admin.site.register(Viloyat, ViloyatAdmin)

admin.site.register(Tip_documents, Tip_documentsAdmin)
admin.site.register(Sub_tip_documents, Sub_tip_documentsAdmin)
admin.site.register(Documents, DocumentsAdmin)

from proj.genplan_models import adminsGenplan, Sub_genplan, Sub_sub_genplan, genplansEvent

from adminsortable2.admin import SortableAdminMixin


class Sub_genplanAdmin(SortableAdminMixin, admin.GeoModelAdmin):
    model = Sub_genplan
    list_display = ("nomi", "zindex")
    search_fields = ("nomi",)


admin.site.register(Sub_genplan, Sub_genplanAdmin)
admin.site.register(Sub_sub_genplan)
admin.site.register(adminsGenplan)
admin.site.register(genplansEvent)

from proj.pdp_models import adminsPdp, Sub_pdp, Sub_sub_pdp

admin.site.register(Sub_pdp)
admin.site.register(Sub_sub_pdp)
admin.site.register(adminsPdp)

from proj.apot_models import adminsApot, Sub_apot

admin.site.register(adminsApot)
admin.site.register(Sub_apot)


admin.site.register(Application)
admin.site.register(Company)
