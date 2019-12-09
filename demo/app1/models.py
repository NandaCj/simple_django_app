from django.db import models


class EmpDetails(models.Model):

    emp_name = models.CharField(db_column="emp_name", max_length=255, blank=False, null=False, primary_key=True)
    emp_id = models.CharField(db_column="emp_id", max_length=255, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'emp_details'
        ordering = ['emp_name']
