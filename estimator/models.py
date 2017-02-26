from django.db import models

# Create your models here.

#############################################################################
#                                                                           #
#                            Materials data                                 #
#                                                                           #
#############################################################################
class Materials(models.Model):
	material       = models.CharField(max_length=220, )
	materialType   = models.CharField(max_length=50, )
	footagePerUnit = models.DecimalField(max_digits=8, decimal_places=2, )
	costPerUnit    = models.DecimalField(max_digits=8, decimal_places=2, )
	manufacturer   = models.CharField(max_length=50, )
	dataSheetURL   = models.CharField(max_length=200, )
	sdsURL         = models.CharField(max_length=200, )
	distributor    = models.CharField(max_length=220, )
	updated        = models.DateTimeField(auto_now=True, )

	def __str__(self):
		return str(self.material)

#############################################################################
#                                                                           #
#                           Manufacturers' data                             #
#                                                                           #
#############################################################################

class Manufacturer(models.Model):
	name       = models.CharField(max_length=50, )
	address    = models.CharField(max_length=50, )
	address2   = models.CharField(max_length=50, )
	phone      = models.CharField(max_length=20, )
	website    = models.CharField(max_length=220, )
	productRep = models.CharField(max_length=25, )

	def __str__(self):
		return str(self.name)

#############################################################################
#                                                                           #
#                             People data                                   #
#                                                                           #
#############################################################################

class ProductRep(models.Model):
	firstname = models.CharField(max_length=25, )
	lastname = models.CharField(max_length=35, )
	officenumber = models.CharField(max_length=30, )
	mobile = models.CharField(max_length=30, )
	email = models.CharField(max_length=55, )

	def __str__(self):
		return str(self.firstname + ' ' + self.lastname)

class SalesRep(models.Model):
	firstname = models.CharField(max_length=25, )
	lastname = models.CharField(max_length=35, )
	officenumber = models.CharField(max_length=30, )
	mobile = models.CharField(max_length=30, )
	email = models.CharField(max_length=55, )

	def __str__(self):
		return str(self.firstname + ' ' + self.lastname)

class ContractorRep(models.Model):
	firstname = models.CharField(max_length=25, )
	lastname = models.CharField(max_length=35, )
	officenumber = models.CharField(max_length=30, )
	mobile = models.CharField(max_length=30, )
	email = models.CharField(max_length=55, )

	def __str__(self):
		return str(self.firstname + ' ' + self.lastname)

#############################################################################
#                                                                           #
#                           Distributor data                                #
#                                                                           #
#############################################################################

class Distributor(models.Model):
	name       = models.CharField(max_length=50, )
	address    = models.CharField(max_length=50, )
	address2   = models.CharField(max_length=50, )
	phone      = models.CharField(max_length=20, )
	website    = models.CharField(max_length=220, )
	salesRep   = models.CharField(max_length=25, )

	def __str__(self):
		return str(self.name)

#############################################################################
#                                                                           #
#                           Contractor data                                 #
#                                                                           #
#############################################################################

class Contractor(models.Model):
	name       = models.CharField(max_length=50, )
	address    = models.CharField(max_length=50, )
	address2   = models.CharField(max_length=50, )
	phone      = models.CharField(max_length=20, )
	website    = models.CharField(max_length=220, )

	def __str__(self):
		return str(self.name)

#############################################################################
#                                                                           #
#                           Architect data                                  #
#                                                                           #
#############################################################################

class Architect(models.Model):
	name       = models.CharField(max_length=50, )
	address    = models.CharField(max_length=50, )
	address2   = models.CharField(max_length=50, )
	phone      = models.CharField(max_length=20, )
	website    = models.CharField(max_length=220, )

	def __str__(self):
		return str(self.name)


#############################################################################
#                                                                           #
#                            Production data                                #
#                                                                           #
#############################################################################

class ProductionRate(models.Model):
	SQUARE_FOOTAGE    = 'SF'
	LINEAL_FOOTAGE    = 'LF'
	COUNT             = 'CT'
	MAN_DAY           = 'MD'
	MAN_HOUR          = 'MH'
	TWO_MAN_CREW_DAY  = '2D'
	FOUR_MAN_CREW_DAY = '4D'

	FOOTAGE_TYPE_CHOICES = (
		(SQUARE_FOOTAGE, 'Square Footage'),
		(LINEAL_FOOTAGE, 'Lineal Footage'),
		(COUNT, 'Count')
	)
	PRODUCTION_TIME_CHOICES = (
		(MAN_DAY, 'Man Day'),
		(MAN_HOUR, 'Man Hour'),
		(TWO_MAN_CREW_DAY, 'Two Man Crew - 1 Day'),
		(FOUR_MAN_CREW_DAY, 'Four Man Crew - 1 Day'),
	)

	task = models.CharField(max_length=50, )
	footageType = models.CharField(
		max_length=2,
		choices=FOOTAGE_TYPE_CHOICES, 
		default=SQUARE_FOOTAGE,
	)
	productionTime = models.CharField(
		max_length=2,
		choices=PRODUCTION_TIME_CHOICES,
		default=MAN_HOUR,
	)
	production = models.IntegerField()

	def __str__(self):
		return str(self.task)
