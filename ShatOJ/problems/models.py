from django.db import models

class Problem(models):
    title = models.CharField(max_length=255)
    description = models.TextField()
    input_requirement = models.TextField()
    output_requirement = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    difficulty_level = models.CharField(max_length=10, choices=[
        ('easy', '简单'),
        ('medium', '中等'),
        ('hard', '困难')
    ])
    def __str__(self):
        return self.title