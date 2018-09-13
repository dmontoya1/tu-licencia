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
