from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""

        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text


class Pizzeras(models.Model):
    """pizzera项目"""

    name = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizzera = models.ForeignKey(Pizzeras, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = "Topping"

    def __str__(self):
        return self.name
