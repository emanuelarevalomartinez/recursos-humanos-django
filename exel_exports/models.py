from django.db import models
import datetime
from django.utils.timezone import now


# Create your models here.
def fecha_year():
    return now().date().strftime('%Y')

def fecha_month():
    return now().date().strftime('%m')

def fecha_day():
    return now().date().day

# Create your models here.
class Data(models.Model):
    
    id_empleado = models.CharField(unique=True, max_length=150,primary_key=True)
    nombre = models.CharField(max_length=130)
    apellido_1 = models.CharField(max_length=150)
    apellido_2 = models.CharField(max_length=150)
    tipo_de_contrato = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    subcategoria = models.CharField(max_length=200, null=True)
    cargo = models.CharField(max_length=150)
    categoria_di = models.CharField(max_length=150,null=True)
    grado_cientifico = models.CharField(max_length=150, null=True)
    sexo = models.CharField(max_length=1,choices=[('F','F'),('M','M')],)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.CharField(max_length=50)
    edad =models.IntegerField()
    menor_o_igual_35 = models.BooleanField()
    causa_alta = models.CharField(max_length=2)
    nivel_escolaridad = models.CharField(max_length=100,null=True)
    siglas = models.CharField(max_length=3)
    salario_basico = models.IntegerField()

    def __str__(self):
     return self.id_empleado



class Ae2(models.Model):
   mes_creado = models.CharField(max_length=30)
   fecha_creacion = models.DateField(auto_now_add=True)
   anno = models.IntegerField(default= fecha_year)
   day = models.IntegerField(default= fecha_day)
   month = models.IntegerField(default=fecha_month)
   total_platilla_aprobada = models.IntegerField() 
   total_platilla_cubierta = models.IntegerField()
   total_general_contratos = models.IntegerField()
   total_contrato_P_det = models.IntegerField() #4.- Total de Contratos de Profesores por tiempo determinado 
   total_contratos_P_comp = models.IntegerField() #5.- De ellos: a tiempo completo
   total_contrato_no_d = models.IntegerField() #6.- Total de Contratos No Docentes (7+14)
   contrato_no_doc_resp = models.IntegerField() #7.- Contratos No Docentes con respaldo de plazas (8 a 13)
   contrato_no_doc_resp_s = models.IntegerField() #8.- De ellos: por sustitución
   periodo_prueba = models.IntegerField() #8.- De ellos: por sustitución
   seren_aux = models.IntegerField() #10.- Serenos y Auxiliares de Limpieza
   labores_a = models.IntegerField() #11.- Labores Agrícolas
   jubilados = models.IntegerField() #12.- Jubilados 
   otros = models.IntegerField() #13.- Otros
   contratos_no_d = models.IntegerField() #14.- Contratos No Docentes sin respaldo de plazas (15 a 19)
   contratos_no_d_e = models.IntegerField() #15 contratos_no_d
   eject_obra = models.IntegerField() #18.- Ejecución de Obra
   reserva_cientif = models.IntegerField() #20.- Reserva Científica en Preparación
   recien_graduados = models.IntegerField() #21.- Recién Graduados en Preparación (Nivel Sup.)
   reserva_d_p = models.IntegerField() #22.- Reserva Dirección Provincial de Trabajo
   tecnico_m_prepa = models.IntegerField() #23.- Técnicos Medios en Preparación
   estu_contr_d = models.IntegerField() #24 - Total de estudiantes de la Universidad de CD contratados por tiempo determinado 
   estu_cont_a = models.IntegerField() #25 - Del total de estudiantes de CD contratados, cifras como Auxiliar Técnico de la Docencia
   estu_cont_n = models.IntegerField() #26 - Del total de estudiantes de CD contratados, cifras en cargos No Docentes
   confeccionado = models.CharField(max_length=150)
   c_cargo = models.CharField(max_length=150)
   revisado = models.CharField(max_length=150)
   r_cargo = models.CharField(max_length=150)


   def save(self, *args, **kwargs):
    
        if not self.fecha_creacion:  # Solo si es un nuevo registro
            self.mes_creado = get_mes_actual()
            super().save(*args, **kwargs)


def get_mes_actual():
    return datetime.datetime.now().strftime('%B')


class Ae3(models.Model):
    mes_creado = models.CharField(max_length=30)
    fecha_creacion = models.DateField(auto_now_add=True)
    anno = models.IntegerField(default= fecha_year)
    day = models.IntegerField(default= fecha_day)
    month = models.IntegerField(default=fecha_month)
    total_de_cuadros = models.IntegerField()
    cuadros_docente = models.IntegerField()
    cuadros_admin = models.IntegerField()
    cuadros_invest = models.IntegerField()
    otros_cuadros = models.IntegerField()
    total_tecnicos = models.IntegerField()
    prof_tiempo_compl = models.IntegerField()
    asesores_metodol = models.IntegerField()
    investigadores = models.IntegerField()
    otros_tecnicos = models.IntegerField()
    administrativos = models.IntegerField()
    servicio = models.IntegerField()
    operarios = models.IntegerField()
    total = models.IntegerField()
    profe_tiempo_pars = models.IntegerField()

    total_de_cuadros_fem = models.IntegerField()
    total_jovenes_t = models.IntegerField() #los que estan en true
    total_jovenes_t_fem = models.IntegerField() #los que estan en true y fem
    profe_titular = models.IntegerField()
    profe_aux = models.IntegerField()
    asistente = models.IntegerField()
    instructor = models.IntegerField()

    cuadros_docente_fem = models.IntegerField()
    cuadros_docente_jovenes_t = models.IntegerField()
    cuadros_docente_jovenes_t_fem = models.IntegerField()
    cuadros_docente_profe_titular = models.IntegerField()
    cuadros_docente_profe_aux = models.IntegerField()
    cuadros_docente_asistente = models.IntegerField()
    cuadros_docente_instructor = models.IntegerField()

    total_tecnicos_fem = models.IntegerField()
    total_tecnicos_jovenes_t = models.IntegerField()
    total_tecnicos_jovenes_t_fem = models.IntegerField()
    total_tecnicos_profe_titular = models.IntegerField()
    total_tecnicos_profe_aux = models.IntegerField()
    total_tecnicos_asistente = models.IntegerField()
    total_tecnicos_instructor = models.IntegerField()
    

    confeccionado = models.CharField(max_length=150)
    aprobado = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.id:  # Solo si es un nuevo registro
            self.mes_creado = get_mes_actual()
        super().save(*args, **kwargs)