from django.contrib import admin
from .models import *


class GroupsAdmin(admin.ModelAdmin):
    list_display = ('group',)


class Prim_procedureAdmin(admin.ModelAdmin):
    list_display = ('prim_proc',)


class Prim_diagnosisAdmin(admin.ModelAdmin):
    list_display = ('prim_diagn',)


class PatientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'p_age',
                    'p_gender', 'p_ab0', 'p_rh',
                    'prim_proc', 'prim_proc_date',
                    'prim_diagn', 'anamnesis',
                    )
    list_display_links = ('id',)
    list_filter = ('group',)


class DGroupsAdmin(admin.ModelAdmin):
    list_display = ('d_group',)


class DDiagnosisAdmin(admin.ModelAdmin):
    list_display = ('d_diagnosis',)


class MorphologyAdmin(admin.ModelAdmin):
    list_display = ('morphology',)

class BiomaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'd_group', 'd_age', 'd_gender',
                    'd_ab0', 'd_rh', 'd_diagnosis', 'd_anamnesis',
                    'd_pth', 'd_calcium', 'd_phosph', 'expl_date',
                    'transfer_time', 'morphology',
                    )
    list_display_links = ('id',)
    list_filter = ('d_group',)


class IndexProcedureAdmin(admin.ModelAdmin):
    list_display = ('index_procedure',)


class MethodAdmin(admin.ModelAdmin):
    list_display = ('method_proc',)


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_patient', 'id_biomaterial',
                    'index_proc', 'method_proc', 'date_proc',
                    'numb_cell', 'complecations',)
    list_display_links = ('id', 'id_patient', 'id_biomaterial')
    list_filter = ('index_proc', 'method_proc',)


class TypeTestsAdmin(admin.ModelAdmin):
    list_display = ('type_test',)


class IntervalsAdmin(admin.ModelAdmin):
    list_display = ('interval',)


class SF_36Admin(admin.ModelAdmin):
    list_display = ('id', 'id_patient', 'interval_sf36',
                    'type_index_sf36', 'date_sf36', 'result_sf36',)
    list_display_links = ('id', 'id_patient',)
    list_filter = ('interval_sf36', 'type_index_sf36',)


class LabTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_patient', 'interval_test',
                    'type_test', 'date_test', 'result_test',)
    list_display_links = ('id', 'id_patient',)
    list_filter = ('interval_test', 'type_test',)


class DrugsAdmin(admin.ModelAdmin):
    list_display = ('drug',)


class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_patient', 'interval',
                    'drug', 'dose',)
    list_display_links = ('id', 'id_patient')
    list_filter = ('interval',)




admin.site.register(Groups, GroupsAdmin)
admin.site.register(Prim_procedure, Prim_procedureAdmin)
admin.site.register(Prim_diagnosis, Prim_diagnosisAdmin)
admin.site.register(Patients, PatientsAdmin)
admin.site.register(DGroups, DGroupsAdmin)
admin.site.register(DDiagnosis, DDiagnosisAdmin)
admin.site.register(Morphology, MorphologyAdmin)
admin.site.register(Biomaterias, BiomaterialsAdmin)
admin.site.register(IndexProcedure, IndexProcedureAdmin)
admin.site.register(Method, MethodAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(TypeTests, TypeTestsAdmin)
admin.site.register(Intervals, IntervalsAdmin)
admin.site.register(SF_36, SF_36Admin)
admin.site.register(LabTests, LabTestAdmin)
admin.site.register(Drugs, DrugsAdmin)
admin.site.register(Treatment, TreatmentAdmin)



