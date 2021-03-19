from django.db import models


# Create your models here.
class JobTitle(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.title}"


class WorkExperience(models.Model):
    title = models.CharField(max_length=120)
    company_name = models.CharField(max_length=120)
    working_here = models.BooleanField(default=False)
    date_started = models.DateField(null=True)
    date_ended = models.DateField(null=True)
    skills_used = models.CharField(null=True, blank=True, max_length=300)
    describe_accomplishment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class OpportunityAvailable(models.Model):
    full_time = models.BooleanField(default=False)
    part_time = models.BooleanField(default=False)
    temporary = models.BooleanField(default=False)
    contract = models.BooleanField(default=False)
    internship = models.BooleanField(default=False)
    seasonal = models.BooleanField(default=False)
    co_founder = models.BooleanField(default=False)
    freelance = models.BooleanField(default=False)
    per_diem = models.BooleanField(default=False)
    reserve = models.BooleanField(default=False)


class InputSession(models.Model):
    job_title = models.OneToOneField(JobTitle, related_name="+", null=True, on_delete=models.CASCADE)
    work_experience = models.OneToOneField(WorkExperience, related_name="+", null=True, on_delete=models.CASCADE)
    opportunity = models.OneToOneField(OpportunityAvailable, related_name="+", null=True, on_delete=models.CASCADE)
