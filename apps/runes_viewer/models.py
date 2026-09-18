from django.contrib.gis.db import models
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext_lazy as _
from gridh_abstract.models import (
    AbstractBaseModel,
    AbstractPlaceModel,
    AbstractTagModel,
    get_iiif_path,
)

from runes.storages import IIIFFileStorage


class TimePeriod(AbstractTagModel):

    class Meta:
        verbose_name = _("Time Period")
        verbose_name_plural = _("Time Periods")


class Position(AbstractTagModel):

    class Meta:
        verbose_name = _("Position")
        verbose_name_plural = _("Positions")


class Area(AbstractTagModel):

    class Meta:
        verbose_name = _("Area")
        verbose_name_plural = _("Areas")


class Place(AbstractPlaceModel):
    parish = models.CharField(max_length=256, blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = _("Place")
        verbose_name_plural = _("Places")
    
    def __str__(self) -> str:
        return f"{self.name}"


class Runestone(AbstractBaseModel):
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True,
                                   help_text=("Descriptive text about the runestone surroundings"))
    position = models.ManyToManyField(Position, through="RunestonePosition",
                                      related_name="runestones",
                                      blank=True, help_text=_("Position"))
    coordinates = models.PointField(blank=True, null=True, help_text="Coordinates of current location")
    time_period = models.ForeignKey(TimePeriod, on_delete=models.SET_NULL, blank=True, null=True, help_text=_("Dating of runestone"))    
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, blank=True, null=True, related_name="runestones")
    date_visit = models.DateField(blank=True, null=True)
    
    fornsoek_url = models.URLField(blank=True, null=True)
    lantmaeteriet_url = models.URLField(blank=True, null=True)

    image = models.ImageField(blank=True, null=True,
                              storage=IIIFFileStorage, upload_to=get_iiif_path, verbose_name=_("iiif image"), validators=[validate_image_file_extension])

    class Meta:
        verbose_name = _("Runestone")
        verbose_name_plural = _("Runestones")

    def __str__(self) -> str:
        return f"{self.name}"


class RunestonePosition(models.Model):
    class Status(models.TextChoices):
        YES = "ja", "Ja"
        UNCLEAR = "oklart", "Oklart"
        MAYBE = "möjligen", "Möjligen"
        NO = "nej", "Nej"

    runestone = models.ForeignKey(
        Runestone,
        on_delete=models.CASCADE,
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.YES,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["runestone", "position"],
                name="unique_runestone_position",
            )
        ]