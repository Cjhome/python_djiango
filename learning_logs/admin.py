from django.contrib import admin

from learning_logs.models import Topic, Entry, Pizzeras, Topping

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Pizzeras)
admin.site.register(Topping)
