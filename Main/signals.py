# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from .send_email import send_for_email
# # from .send_tel import send_for_sms
# from .models import User
# from django.template.defaultfilters import slugify

# # @receiver(pre_save, sender=User)
# # def pre_smy_callbackave(sender, instance, *args, **kwargs):
# #     instance.comment = slugify(instance.name)
# #     instance.save(phone=instance.name)
# #     super(User, instance).pre_save(sender, instance, *args, **kwargs)
# #     # instance.Model.save(instance)
# #     print("Request finished!")


# @receiver(post_save, sender=User)
# def my_save(sender, instance, *args, **kwargs):
#     if instance.organization is None:
#         organization = instance.organization_other
#     else:
#         organization = instance.organization
#     number = instance.id
#     send_for_email(instance.email, number, instance.date, organization, instance.file)
#     # send_for_sms(instance.email, instance.phone.split(), number, instance.date, organization)
#     # models.Model.save(instance)