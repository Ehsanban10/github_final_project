from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Course(models.Model):
    # ... existing fields ...

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    grade_point = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class Enrollment(models.Model):
    # ... existing fields ...

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
    # ... other fields ...

    def calculate_score(self):
        correct_choices = self.choices.filter(is_correct=True)
        total_correct = correct_choices.count()
        total_selected = self.choices.count()

        if total_correct > 0 and total_selected == total_correct:
            return 100.0  # All correct choices were selected
        elif total_selected > 0:
            return (correct_choices.count() / total_selected) * 100.0
        else:
            return 0.0
