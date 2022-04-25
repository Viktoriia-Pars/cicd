from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 254, null=False)
    image = models.ImageField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(max_length = 200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("slug-slug", kwargs={"slug": self.slug})