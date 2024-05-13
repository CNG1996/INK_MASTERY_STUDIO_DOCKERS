from django.db import models

class region (models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'region'

class provincia (models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    region = models.ForeignKey('region', models.DO_NOTHING, blank=True, null = True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'provincia'
    
class comuna (models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    provincia = models.ForeignKey('provincia', models.DO_NOTHING, blank=True, null = True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 'comuna'

class persona(models.Model):
    rut = models.CharField(unique=True, max_length=13, blank=True, null=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    edad = models.IntegerField ( blank=True, null=True)
    genero = models.CharField (max_length= 50, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'persona'

class emails(models.Model):
    mail = models.CharField(max_length=150, blank=True, null=True)
    persona = models.ForeignKey('persona', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.mail

    class Meta:
        managed = False
        db_table = 'emails'

class telefono (models.Model):
    telefono = models.CharField(max_length=12, blank=True, null= True)
    persona = models.ForeignKey('persona', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.telefono

    class Meta:
        managed = False
        db_table = 'telefono'

class direccion (models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    block = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.ForeignKey('comuna', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'direccion'

class cliente (models.Model):
    persona = models.ForeignKey('persona', models.DO_NOTHING, blank=True, null=True)
    direccion = models.ForeignKey('direccion', models.DO_NOTHING, blank=True, null=True)
    emails = models.ForeignKey('emails', models.DO_NOTHING, blank=True, null=True)
    telefono = models.ForeignKey('telefono', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        if self.persona:
            return self.persona.nombre
        else:
            return "Cliente sin persona asociada"

    class Meta:
        managed = False
        db_table = 'cliente'

class estudio (models.Model):
    nombre = models.CharField(max_length= 45, blank=True, null=True)
    descripcion = models.CharField(max_length= 45, blank=True, null=True)
    direccion = models.ForeignKey('direccion', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'estudio'

class tatuador (models.Model):
    persona = models.ForeignKey('persona', models.DO_NOTHING, blank=True, null=True)
    emails = models.ForeignKey('emails', models.DO_NOTHING, blank=True, null=True)
    telefono = models.ForeignKey('telefono', models.DO_NOTHING, blank=True, null=True)
    estudio = models.ForeignKey('estudio', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        if self.persona:
            return self.persona.nombre
        else:
            return "Tatuador sin persona asociada"

    class Meta:
        managed = False
        db_table = 'tatuador'

class reseña (models.Model):
    titulo = models.CharField(max_length= 45, blank=True, null=True)
    cuerpo = models.CharField(max_length= 200, blank=True, null=True)
    calificacion = models.IntegerField( blank=True, null=True)
    cliente = models.ForeignKey('cliente', models.DO_NOTHING, blank=True, null=True)
    tatuador = models.ForeignKey('tatuador', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reseña'

class portafolio (models.Model):
    titulo = models.CharField(max_length= 45, blank=True, null=True)
    descripcion = models.CharField(max_length= 200, blank=True, null=True)
    foto = models.CharField(max_length= 200, blank=True, null=True)
    tatuador = models.ForeignKey('tatuador', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portafolio'

class diseños (models.Model):
    titulo = models.CharField(max_length= 45, blank=True, null=True)
    descripcion = models.CharField(max_length= 200, blank=True, null=True)
    estilo = models.CharField(max_length= 45, blank=True, null=True)
    foto = models.CharField(max_length= 200, blank=True, null=True)
    tatuador = models.ForeignKey('tatuador', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diseños'

class materiales (models.Model):
    nombre = models.CharField(max_length= 45, blank=True, null=True)
    cantidad = models.IntegerField(blank= True, null= True)
    descripcion = models.CharField(max_length= 100, blank=True, null=True)
    tatuador = models.ForeignKey('tatuador', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'materiales'

class cita (models.Model):
    fecha = models.DateTimeField (blank=True, null=True)
    descripcion = models.CharField(max_length= 45, blank=True, null=True)
    tatuador = models.ForeignKey('tatuador', models.DO_NOTHING, blank=True, null=True)
    cliente = models.ForeignKey('cliente', models.DO_NOTHING, blank=True, null=True)
    estudio = models.ForeignKey('estudio', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cita'

class factura (models.Model):
    total= models.IntegerField(blank= True, null= True)
    estado = models.CharField(max_length= 45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura'

class metodo_pago (models.Model):
    nombre = models.CharField(max_length= 50, blank=True, null=True)
    descripcion = models.CharField(max_length= 150, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'metodo_pago'

class transacciones (models.Model):
    monto = models.IntegerField(blank= True, null= True)
    fecha = models.DateTimeField (blank=True, null=True)
    metodo_pago = models.ForeignKey('metodo_pago', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transacciones'

class detalle_factura (models.Model):
    nro_citas_pendientes= models.IntegerField(blank= True, null= True)
    abono= models.IntegerField( blank= True, null= True)
    cita = models.ForeignKey('cita', models.DO_NOTHING, blank=True, null=True)
    factura = models.ForeignKey('factura', models.DO_NOTHING, blank=True, null=True)
    transacciones = models.ForeignKey('transacciones', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_factura'