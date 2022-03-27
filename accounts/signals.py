from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TeacherPorfile, User, StudentPorfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.type=="student":
        StudentPorfile.objects.create(user=instance)
    if created and instance.type=="teacher":
        TeacherPorfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    print(instance.type)
    
    if instance.type=="student":
        if TeacherPorfile.objects.filter(user=instance):
            TeacherPorfile.objects.get(user=instance).delete()
        else:
            pass
        StudentPorfile.objects.update_or_create(user=instance)
    
    elif instance.type=="teacher":
        if StudentPorfile.objects.filter(user=instance):
            StudentPorfile.objects.get(user=instance).delete()
        else:
            pass
        TeacherPorfile.objects.update_or_create(user=instance)