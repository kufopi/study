from django.db import models

# Create your models here.

DEPARTMENT = (
    ('Accounting','Accounting'),
    ('Banking','Banking'),
    ('Business Admin','Business Admin'),
    ('Economics','Economics'),
    ('History','History'),
    ('Inter- Relations','Inter- Relations'),
    ('Political Science','Political Science'),
    ('Psychology','Psychology'),
    ('Mass Comm','Mass Comm'),
    ('Criminology','Criminology')
    
)

GENDER = (
    ('Male','Male'),
    ('Female','Female')
)


DEPARTMENT2 = (
    ('Computer Science','Computer Science'),
    ('Software Eng','Software Eng'),
    ('Cyber Security','Cyber Security'),
    ('Microbiology','Microbiology'),
    ('History','History'),
    ('Chemistry','Chemistry'),
    ('BioChemistry','BioChemistry'),
    ('Mathematics','Mathematics'),
    ('Statistics','Statistics'),
    ('Physics','Physics')
    
)

LEVEL = (
    ('100','100'),
    ('200','200'),
    ('300','300'),
    ('400','400')
)

class CourseReg(models.Model):
    """Model definition for CourseReg."""

    first_name = models.CharField( max_length=50)
    middle_name = models.CharField(blank=True, max_length=50, null=True)
    surname = models.CharField( max_length=50)
    gender = models.CharField(choices = GENDER, max_length=10)
    level = models.CharField(choices = LEVEL, max_length=50)
    department  = models.CharField(choices= DEPARTMENT, max_length=50)
    created  = models.DateTimeField( auto_now_add=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for CourseReg."""

        verbose_name = 'CourseReg'
        verbose_name_plural = 'CourseRegs'
        ordering = ['department','level']

    def __str__(self):
        """Unicode representation of CourseReg."""
        return f'{self.first_name} {self.surname}'



class ConasReg(models.Model):
    """Model definition for ConasReg."""

    first_name = models.CharField( max_length=50)
    middle_name = models.CharField(blank=True, max_length=50, null=True)
    surname = models.CharField( max_length=50)
    gender = models.CharField(choices = GENDER, max_length=10)
    level = models.CharField(choices = LEVEL, max_length=50)
    department  = models.CharField(choices= DEPARTMENT2, max_length=50)
    created  = models.DateTimeField( auto_now_add=True)



    # TODO: Define fields here

    class Meta:
        """Meta definition for ConasReg."""

        verbose_name = 'ConasReg'
        verbose_name_plural = 'ConasRegs'
        ordering = ['department','level']

    def __str__(self):
        """Unicode representation of ConasReg."""
        return f'{self.first_name} {self.surname}'

