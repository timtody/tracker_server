from django.db import models


class TaskStatus(models.Model):
    status = models.CharField("Status", max_length=32)

    def __str__(self):
        return self.status


class TaskPriority(models.Model):
    priority = models.CharField("Priority", max_length=32)

    def __str__(self):
        return self.priority


class User(models.Model):
    first_name = models.CharField("First name", max_length=32)
    last_name = models.CharField("Last name", max_length=32)
    email = models.EmailField("email")
    phone = models.CharField("Phone", max_length=32)
    description = models.CharField("Description", max_length=128)
    date_created = models.DateField("Member since", auto_now=True)

    def __str__(self):
        return self.first_name


class Project(models.Model):
    summary = models.CharField("Summary", max_length=64)
    description = models.CharField("Description", max_length=1024)
    author = models.ForeignKey("User", on_delete=models.DO_NOTHING)
    date_created = models.DateField(auto_now=True)
    start = models.DateField("Start")
    end = models.DateField("End")

    def __str__(self):
        return self.summary


class Task(models.Model):
    summary = models.CharField("Summary", max_length=64)
    description = models.CharField("Description", max_length=1024)
    author = models.ForeignKey(
        "User", on_delete=models.DO_NOTHING, related_name="Author"
    )
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    assignee = models.ForeignKey(
        "User", on_delete=models.DO_NOTHING, related_name="Assignee"
    )
    status = models.ForeignKey("TaskStatus", on_delete=models.DO_NOTHING)
    priority = models.ForeignKey("TaskPriority", on_delete=models.DO_NOTHING)
    target_resolution_date = models.DateField("Target resolution date")
    actual_resolution_date = models.DateField("Actual resolution date")
    progress = models.CharField("Progress", max_length=255)
    resolution_summary = models.CharField("Resolution summary", max_length=1024)

    def __str__(self):
        return self.summary
