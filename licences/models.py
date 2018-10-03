from django.db import models


class Licence(models.Model):
    """Crea las licencias disponibles para los CEA
    """

    CATEGORIES = (
        ("A1", 'A1'),
        ("A2", 'A2'),
        ("B1", 'B1'),
        ("C1", 'C1'),
        ("C2", 'C2'),
        ("C3", 'C3'),
    )

    category = models.CharField(
        "Categoría",
        choices=CATEGORIES,
        max_length=2,
        unique=True
    )
    description = models.TextField("Descripción de la categoría")

    def __str__(self):
        return "Categoría %s" % (self.category)

    
    class Meta:
        verbose_name = "Licencia"


class AgeRange(models.Model):
    """Creación de los rangos de edades para los ansv
    Se creó un modelo aparte ya que hay que validar en que rango de edad
    se encuentra una persona, y asi determinar el precio que debe cancelar
    """

    start_age = models.CharField(
        "Edad inicial",
        max_length=3
    )
    end_age = models.CharField(
        "Edad final",
        max_length=3
    )

    def __str__(self):
        return "Rango entre %s y %s años" % (self.start_age, self.end_age)
    

    class Meta:
        verbose_name = "Rango de edad"
        verbose_name_plural = "Rangos de edades"


class AnsvRanges(models.Model):
    """Crear los valores ansv por género y rango de edades
    para cada una de las categorías
    """

    MALE = 'M'
    FEMALE = 'F'

    GENDER = (
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino' )
    )

    licence = models.ForeignKey(
        Licence,
        verbose_name="Licencia",
        on_delete=models.CASCADE,
    )
    gender = models.CharField(
        "Género",
        max_length=1,
        choices=GENDER,
    )
    age_range = models.ForeignKey(
        AgeRange,
        verbose_name="Rango de edades",
        on_delete=models.CASCADE
    )
    price = models.CharField(
        "Precio",
        max_length=10,
    )

    def __str__(self):
        return "Valor de ansv para género %s y rango %s" %(self.gender, self.age_range)

    class Meta:
        verbose_name = 'Valor de ANSV'
        verbose_name_plural = 'Valores de ANSV'
        unique_together = ("licence", "gender", "age_range")
