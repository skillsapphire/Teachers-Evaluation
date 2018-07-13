# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InstitutionalStudents(models.Model):
    # Field name made lowercase.
    idperson = models.AutoField(db_column='idPerson', primary_key=True)
    enrollment = models.CharField(max_length=30)
    # Field name made lowercase.
    idcareer = models.CharField(
        db_column='idCareer', max_length=20, blank=True, null=True)
    type = models.CharField(max_length=14, blank=True, null=True)
    name = models.CharField(max_length=60)
    # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=60)
    # Field name made lowercase.
    lastname2 = models.CharField(
        db_column='lastName2', max_length=60, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    # Field name made lowercase.
    instemail = models.CharField(
        db_column='instEmail', max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    celphone = models.CharField(max_length=20, blank=True, null=True)
    cycle = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    municipality = models.CharField(max_length=50, blank=True, null=True)
    colony = models.CharField(max_length=60, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    # Field name made lowercase.
    numberext = models.CharField(
        db_column='numberExt', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    numberint = models.CharField(
        db_column='numberInt', max_length=10, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    turn = models.CharField(max_length=10, blank=True, null=True)
    # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)
    wifi_status = models.CharField(max_length=8)
    # Field name made lowercase.
    createdon = models.DateTimeField(db_column='createdOn')
    # Field name made lowercase.
    updateon = models.DateTimeField(db_column='updateOn')

    def __str__(self):
        return '%s' % (self.enrollment)

    class Meta:
        managed = False
        db_table = 'institutional_students'
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'


class InstitutionalTeachers(models.Model):
    # Field name made lowercase.
    idperson = models.AutoField(db_column='idPerson', primary_key=True)
    enrollment = models.CharField(max_length=30)
    # Field name made lowercase.
    idcareer = models.CharField(
        db_column='idCareer', max_length=20, blank=True, null=True)
    type = models.CharField(max_length=14, blank=True, null=True)
    name = models.CharField(max_length=60)
    # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=60)
    # Field name made lowercase.
    lastname2 = models.CharField(
        db_column='lastName2', max_length=60, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    # Field name made lowercase.
    instemail = models.CharField(
        db_column='instEmail', max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    celphone = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    municipality = models.CharField(max_length=50, blank=True, null=True)
    colony = models.CharField(max_length=60, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    # Field name made lowercase.
    numberext = models.CharField(
        db_column='numberExt', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    numberint = models.CharField(
        db_column='numberInt', max_length=10, blank=True, null=True)
    status = models.CharField(max_length=50)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    turn = models.CharField(max_length=10, blank=True, null=True)
    # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)
    wifi_status = models.CharField(max_length=8)
    # Field name made lowercase.
    createdon = models.DateTimeField(db_column='createdOn')
    # Field name made lowercase.
    updateon = models.DateTimeField(db_column='updateOn')

    def __str__(self):
        return '%s' % (self.enrollment)

    class Meta:
        managed = False
        db_table = 'institutional_teachers'
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'


class EvaluationsAnswers(models.Model):
    # Field name made lowercase.
    idstudent = models.ForeignKey(
        'InstitutionalStudents', on_delete=models.PROTECT, db_column='idStudent')
    # Field name made lowercase.
    idgroup = models.ForeignKey(
        'EvaluationsGroups', on_delete=models.PROTECT, db_column='idGroup')
    # Field name made lowercase.
    idquestion = models.ForeignKey(
        'EvaluationsQuestions', on_delete=models.PROTECT, db_column='idQuestion')
    answer = models.CharField(max_length=255, blank=True, null=True)

    STATUS_CHOICES = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return '%s' % (self.answer)

    class Meta:
        managed = False
        db_table = 'evaluations_answers'
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'


class EvaluationsDetailExamQuestion(models.Model):
    # Field name made lowercase.
    idexam = models.ForeignKey(
        'EvaluationsExams', on_delete=models.PROTECT, db_column='idExam')
    # Field name made lowercase.
    idquestion = models.ForeignKey(
        'EvaluationsQuestions', on_delete=models.PROTECT, db_column='idQuestion')
    # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='updatedOn')
    # Field name made lowercase.
    createdon = models.DateTimeField(db_column='createdOn')

    STATUS_CHOICES = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return '%s' % (self.idexam)

    class Meta:
        managed = False
        db_table = 'evaluations_detail_exam_question'
        verbose_name = 'Examen - Respuesta'
        verbose_name_plural = 'Examenes - Respuestas'


class EvaluationsDetailStudentGroup(models.Model):
    # Field name made lowercase.
    idgroup = models.ForeignKey(
        'EvaluationsGroups', on_delete=models.PROTECT, db_column='idGroup')
    # Field name made lowercase.
    idstudent = models.ForeignKey(
        'InstitutionalStudents', on_delete=models.PROTECT, db_column='idStudent')
    # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='updatedOn')
    # Field name made lowercase.
    createdon = models.DateTimeField(db_column='createdOn')

    STATUS_CHOICES = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    EVALUATED_CHOICES = (
        ('YES', 'Si'),
        ('NO', 'No'),
    )
    evaluated = models.CharField(
        max_length=8, choices=EVALUATED_CHOICES, default='NO')

    class Meta:
        managed = False
        db_table = 'evaluations_detail_student_group'
        verbose_name = 'Alumno - Grupo'
        verbose_name_plural = 'Alumnos - Grupos'


class EvaluationsExams(models.Model):
    description = models.CharField(max_length=255)
    # Field name made lowercase.
    idcareer = models.ForeignKey(
        'ParkingCareer', on_delete=models.PROTECT, db_column='idCareer', blank=True, null=True)
    # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='updatedOn')
    # Field name made lowercase.
    createdon = models.DateTimeField(db_column='createdOn')

    STATUS_CHOICES = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return '%s' % (self.description)

    class Meta:
        managed = False
        db_table = 'evaluations_exams'
        verbose_name = 'Examen'
        verbose_name_plural = 'Examenes'


class EvaluationsGroups(models.Model):
    # Field name made lowercase.
    idsignature = models.ForeignKey(
        'EvaluationsSignatures', on_delete=models.PROTECT, db_column='idSignature')
    # Field name made lowercase.
    idteacher = models.ForeignKey(
        'InstitutionalTeachers', on_delete=models.PROTECT, db_column='idTeacher')
    # Field name made lowercase.
    idperiod = models.ForeignKey(
        'InstitutionalPeriod', on_delete=models.PROTECT, db_column='idPeriod')
    # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='updatedOn')
    # Field name made lowercase.
    createdon = models.DateTimeField(db_column='createdOn')

    def __str__(self):
        return '%s' % (self.id)

    STATUS_CHOICES = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    class Meta:
        managed = False
        db_table = 'evaluations_groups'
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'


class EvaluationsQuestions(models.Model):
    TYPE_CHOICES = (
        ('DATEPICKER', 'Seleccion de fecha'),
        ('RADIO', 'Si y No'),
        ('RANGE', 'Medicion'),
        ('SELECT', 'Multiple'),
        ('TEXT', 'Abierta'),
    )

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.CharField('Question', max_length=255)
    # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='updatedOn')
    # Field name made lowercase.
    createdon = models.DateTimeField(db_column='createdOn')

    STATUS_CHOICES = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return '%s' % (self.description)

    class Meta:
        managed = False
        db_table = 'evaluations_questions'
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'


class EvaluationsSignatures(models.Model):
    name = models.CharField(max_length=255)
    credits = models.IntegerField()

    TYPE_CHOICES = (
        ('REGULAR', 'Regular'),
        ('OPTATIVA', 'Optativa'),
    )
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)

    # Field name made lowercase.
    idcareer = models.ForeignKey(
        'ParkingCareer', on_delete=models.PROTECT, db_column='idCareer')

    STATUS_CHOICES = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        managed = False
        db_table = 'evaluations_signatures'
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'


class InstitutionalPeriod(models.Model):
    # Field name made lowercase.
    idperiodo = models.AutoField(db_column='IDPeriodo', primary_key=True)
    period = models.CharField(max_length=15, blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    # Field name made lowercase.
    idgroup = models.IntegerField(db_column='IDgroup', blank=True, null=True)

    def __str__(self):
        return '%s' % (self.period)

    class Meta:
        managed = False
        db_table = 'institutional_period'
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'


class InstitutionalPeriodDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    id_grupo = models.IntegerField(blank=True, null=True)
    carrera = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.id)

    class Meta:
        managed = False
        db_table = 'institutional_period_detail'
        verbose_name = 'Detalle de Perodo'
        verbose_name_plural = 'Detalles de Periodos'


class ParkingCareer(models.Model):
    # Field name made lowercase.
    idcareer = models.AutoField(db_column='idCareer', primary_key=True)
    # Field name made lowercase.
    idcareergissa = models.CharField(db_column='idCareerGissa', max_length=20)
    abbreviation = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=8)
    # Field name made lowercase.
    createdon = models.DateTimeField(db_column='createdOn')
    # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='updatedOn')

    def __str__(self):
        return '%s' % (self.description)

    class Meta:
        managed = False
        db_table = 'parking_career'
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
