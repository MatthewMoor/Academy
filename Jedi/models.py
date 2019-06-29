from django.db import models

# Create your models here.
from django.db import models


class TestQuestion(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Planet(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Jedi(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    max_number_pupils = models.IntegerField()

    def __str__(self):
        return self.name


class Candidate(models.Model):
    jedi = models.ForeignKey(Jedi, blank=True, null=True,
                             on_delete=models.SET_NULL)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class TestAnswer(models.Model):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct_answer = models.BooleanField()

    def __str__(self):
        return self.text


class CandidateAnswers(models.Model):
    test_question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    test_answer = models.ForeignKey(TestAnswer, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}, {1}, {2}".format(self.candidate, self.test_question, self.test_answer)