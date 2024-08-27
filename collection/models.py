import datetime
from django.urls import reverse
from PIL import Image
import PIL
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import models
from django.utils.text import slugify
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string



class EmailMsg(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    date = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        mail_subject = f"Hi bob gee you have a new notification "
        message = render_to_string('email-like.html', {
            'user': self.name,
            'sender': self.email,
        })
        to_email = 'bobg@gmail.com'
        email = EmailMultiAlternatives(
            mail_subject, message, to=[to_email]
        )
        email.attach_alternative(message, 'text/html')
        email.send()


class Category(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100, default='provision')

    class Meta:
        indexes = [models.Index(fields=['image', 'name'])]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/category/{self.name}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()


        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)




class Product(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )

    CURRENCY = (
        ('$', '$'),
        ('₦', '₦'),
        ('£', '£'),
        ('€', '€'),
    )

    file_1 = models.FileField(upload_to="product_pic", blank=True, null=True)
    file_2 = models.FileField(upload_to="product_pic", blank=True, null=True)
    file_3 = models.FileField(upload_to="product_pic", blank=True, null=True)
    file_4 = models.FileField(upload_to="product_pic", blank=True, null=True)
    file_5 = models.FileField(upload_to="product_pic", blank=True, null=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=14, blank=True, null=True)
    discount = models.FloatField(max_length=14, blank=True, null=True)
    currency = models.CharField(max_length=11, choices=CURRENCY, default=None, blank=True, null=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="category", default='shirt')
    status = models.CharField(max_length=11, choices=STATUS, default='Published')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        indexes = [models.Index(fields=['name', 'price', 'discount', 'currency', 'category', 'status',
                                        'description'])]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        value = self.name
        na = slugify(value, allow_unicode=True)
        return reverse('post-detail', kwargs={'name': na, 'pk': self.pk})



