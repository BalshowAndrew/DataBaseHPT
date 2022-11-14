from django.db import models


# модель "Клиническая группа"
class Groups(models.Model):
    group = models.CharField(max_length=20, verbose_name='Группа')

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = 'Клиническая группа'
        verbose_name_plural = 'Клинические группы'
        ordering = ['group']


# модель "Первичная операция"
class Prim_procedure(models.Model):
    prim_proc = models.CharField(max_length=100, verbose_name='Операция')

    def __str__(self):
        return self.prim_proc

    class Meta:
        verbose_name = 'Первичная операция'
        verbose_name_plural = 'Первичные операции'
        ordering = ['prim_proc']


# модель "Первичный диагноз"
class Prim_diagnosis(models.Model):
    prim_diagn = models.CharField(max_length=100, verbose_name='Диагноз')

    def __str__(self):
        return self.prim_diagn

    class Meta:
        verbose_name = 'Первичный диагноз'
        verbose_name_plural = 'Первичные диагнозы'
        ordering = ['prim_diagn']


# модель "Пациенты"
class Patients(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.PROTECT, verbose_name='Клиническая группа')
    p_age = models.IntegerField(verbose_name='Возраст')
    GENDER_CHOICES = [('m', 'мужской'), ('f', 'женский'), ]
    p_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='f', verbose_name='Пол')
    AB0_CHOICES = [(1, 'I(0)'), (2, 'II(A)'), (3, 'III(B)'), (4, 'IV(AB)')]
    p_ab0 = models.IntegerField(choices=AB0_CHOICES, null=True, verbose_name='Группа крови')
    RH_CHOICES = [(1, 'положительный'), (2, 'отрицательный'), ]
    p_rh = models.IntegerField(choices=RH_CHOICES, null=True, verbose_name='Резус фактор')
    prim_proc = models.ForeignKey(Prim_procedure, on_delete=models.PROTECT, verbose_name='Первичная операция')
    prim_proc_date = models.DateField(verbose_name='Дата первичной операции')
    prim_diagn = models.ForeignKey(Prim_diagnosis, on_delete=models.PROTECT, verbose_name='Первичный диагноз')
    anamnesis = models.IntegerField(verbose_name='Продолжительность ГПТ (лет)')

    def __int__(self):
        return self.pk

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['pk']


# модель "Группы доноров"
class DGroups(models.Model):
    d_group = models.CharField(max_length=10, verbose_name='Группа')

    def __str__(self):
        return self.d_group

    class Meta:
        verbose_name = 'Группа донора'
        verbose_name_plural = 'Группы доноров'
        ordering = ['d_group']


# модель "Диагноз донора"
class DDiagnosis(models.Model):
    d_diagnosis = models.CharField(max_length=100, verbose_name='Диагноз')

    def __str__(self):
        return self.d_diagnosis

    class Meta:
        verbose_name = 'Диагноз донора'
        verbose_name_plural = 'Диагнозы доноров'
        ordering = ['d_diagnosis']


# модель "Гистологическое заключение"
class Morphology(models.Model):
    morphology = models.CharField(max_length=255, verbose_name='Заключение')

    def __str__(self):
        return self.morphology

    class Meta:
        verbose_name = 'Гистологическое заключение'
        verbose_name_plural = 'Гистологические заключения'
        ordering = ['morphology']


# модель "Биоматериал"
class Biomaterias(models.Model):
    d_group = models.ForeignKey(DGroups, on_delete=models.PROTECT, verbose_name='Группа донора')
    d_age = models.IntegerField(verbose_name='Возраст')
    GENDER_CHOICES = [('m', 'мужской'), ('f', 'женский'), ]
    d_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='f', verbose_name='Пол')
    AB0_CHOICES = [(1, 'I(0)'), (2, 'II(A)'), (3, 'III(B)'), (4, 'IV(AB)')]
    d_ab0 = models.IntegerField(choices=AB0_CHOICES, null=True, verbose_name='Группа крови')
    RH_CHOICES = [(1, 'положительный'), (2, 'отрицательный'), ]
    d_rh = models.IntegerField(choices=RH_CHOICES, null=True, verbose_name='Резус фактор')
    d_diagnosis = models.ForeignKey(DDiagnosis, on_delete=models.PROTECT, verbose_name='Диагноз')
    d_anamnesis = models.IntegerField(verbose_name='Длительность заболевания (лет)')
    d_pth = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='ПТГ', blank=True)
    d_calcium = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Ca', blank=True)
    d_phosph = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='P', blank=True)
    expl_date = models.DateField(verbose_name='Дата забора биоматериала')
    transfer_time = models.IntegerField(verbose_name='Время транспортировки (мин)')
    morphology = models.ForeignKey(Morphology, on_delete=models.PROTECT, verbose_name='Гистология')

    def __int__(self):
        return self.pk


# модель "Номер трансплантации"
class IndexProcedure(models.Model):
    index_procedure = models.CharField(max_length=1, verbose_name='Номер трансплантации')

    def __str__(self):
        return self.index_procedure

    class Meta:
        verbose_name = 'Номер трансплантации'
        verbose_name_plural = 'Номера трансплантации'
        ordering = ['index_procedure']


# модель "Метод трансалантации"
class Method(models.Model):
    method_proc = models.CharField(max_length=100, verbose_name='Метод трансплантации БМКП')

    def __str__(self):
        return self.method_proc

    class Meta:
        verbose_name = 'Метод трансплантации'
        verbose_name_plural = 'Методы трансплантации'
        ordering = ['method_proc']


# модель "Трансплантация"
class Procedure(models.Model):
    id_patient = models.ForeignKey(Patients, on_delete=models.PROTECT, verbose_name='id_пациента')
    id_biomaterial = models.ForeignKey(Biomaterias, on_delete=models.PROTECT, verbose_name='id_биоматериала')
    index_proc = models.ForeignKey(IndexProcedure, on_delete=models.PROTECT, verbose_name='Номер трансплантации')
    method_proc = models.ForeignKey(Method, on_delete=models.PROTECT, verbose_name='Метод трансалантации')
    date_proc = models.DateField(verbose_name='Дата трансплантации')
    numb_cell = models.IntegerField(verbose_name='Количество клеток')
    complecations = models.CharField(max_length=255, verbose_name='Осложнения')

    class Meta:
        verbose_name = 'Пересадка БМКП'
        verbose_name_plural = 'Пересадки БМКП'



# модель "Виды лабораторных тестов"
class TypeTests(models.Model):
    type_test = models.CharField(max_length=10, verbose_name='Тест')

    def __str__(self):
        return self.type_test

    class Meta:
        verbose_name = 'Лабораторный тест'
        verbose_name_plural = 'Лабораторные тесты'
        ordering = ['type_test']


# модель "Временные интервалы"
class Intervals(models.Model):
    interval = models.CharField(max_length=2, verbose_name='Интервал (мес.)')

    def __str__(self):
        return self.interval

    class Meta:
        verbose_name = 'Временной интервал'
        verbose_name_plural = 'Временные интервалы'
        ordering = ['interval']


# модель "SF-36"
class SF_36(models.Model):
    id_patient = models.ForeignKey(Patients, on_delete=models.PROTECT, verbose_name='id_пациента')
    interval_sf36 = models.ForeignKey(Intervals, on_delete=models.PROTECT, verbose_name='Временной инртервал')
    INDEX_CHOICES = [
        ('PF', 'Физич. функциониров.'),
        ('RF', 'Ролев. функциониров., обусл. физ. сост.'),
        ('BP', 'Интенсивн. боли'),
        ('GH', 'Общ. сост. здоровья'),
        ('VT', 'Жизн. активность'),
        ('SF', 'Социальн. функционир.'),
        ('RE', 'Ролев. функциониров., обусл. эмоц. сост.'),
        ('MH', 'Психич. здоровье'),
        ('ИП_PH', 'Физический компонент здоровья'),
        ('ИП_MH', 'Психологический компонент здоровья'),
    ]
    type_index_sf36 = models.CharField(max_length=5, choices=INDEX_CHOICES, verbose_name='Индексы SF-36')
    date_sf36 = models.DateField(verbose_name='Дата анкетирования')
    result_sf36 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Значение индекса', blank=True)

    def __int__(self):
        return self.pk

    class Meta:
        verbose_name = 'Анкета SF-36'
        verbose_name_plural = 'Анкеты SF-36'
        ordering = ['pk']


# модель "Лабораторные тесты"
class LabTests(models.Model):
    id_patient = models.ForeignKey(Patients, on_delete=models.PROTECT, verbose_name='id_пациента')
    interval_test = models.ForeignKey(Intervals, on_delete=models.PROTECT, verbose_name='Временной инртервал')
    type_test = models.ForeignKey(TypeTests, on_delete=models.PROTECT, verbose_name='Вид лабораторного исследования')
    date_test = models.DateField(verbose_name='Дата проведения исследования')
    result_test = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Результат исследования')

    def __int__(self):
        return self.pk

    class Meta:
        verbose_name = 'Лабораторный тест'
        verbose_name_plural = 'Лабораторные тесты'
        ordering = ['pk']


#   модель "Препараты"
class Drugs(models.Model):
    drug = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.drug

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'
        ordering = ['drug']


# модель "Лечение"
class Treatment(models.Model):
    id_patient = models.ForeignKey(Patients, on_delete=models.PROTECT, verbose_name='id_пациента')
    interval = models.ForeignKey(Intervals, on_delete=models.PROTECT, verbose_name='Временной инртервал')
    drug = models.ForeignKey(Drugs, on_delete=models.PROTECT, blank=True, verbose_name='Препарат')
    dose = models.DecimalField(max_digits=6, decimal_places=3, blank=True, verbose_name='Суточная доза')

    def __int__(self):
        return self.pk

    class Meta:
        verbose_name = 'Лечение'
        verbose_name_plural = 'Лечение'