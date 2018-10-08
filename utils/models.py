from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from .managers import SoftDeletionManager


class SoftDeletionModelMixin(models.Model):
    """Modelo abstracto para brindar borrado lógico a los modelos.

    Campos del modelo:
        deleted_at: Indica la fecha de borrado lógico del objecto. La nulabilidad de éste
        campo indica si el objeto está 'vivo' o no.
        objects: Manager personalizado
        all_objects: Manager personalizado para obtener todos los objetos, incluyendo 'vivos' y
        lógicamente borrados.
    """

    deleted_at = models.DateTimeField(blank=True, null=True)
    objects = SoftDeletionManager()

    class Meta:
        abstract = True

    def soft_delete(self):
        """Ejecuta un borrado lógico desde la instancia
        """

        self.deleted_at = timezone.now()
        self.save()

    def revive(self):
        """Habilita un objeto que esté lógicamente borrado
        """

        self.deleted_at = None
        self.save()
    

    