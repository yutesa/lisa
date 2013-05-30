#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductsStatus(models.Model):
	ProductStatusId = models.AutoField(primary_key=True)
	ProductStatusName = models.CharField(max_length=20, help_text='Nombre del Status del Producto', verbose_name=u'Status')

	def __unicode__(self):
		return self.ProductStatusName

class ProductCategories(models.Model):
	ProductCategoryId = models.AutoField(primary_key=True)
	ProductCategoryName = models.CharField(max_length=50, help_text='Nombre de la Categoria de Producto', verbose_name=u'Nombre')
	ProductCategoryDescription = models.TextField(max_length=100, help_text='Descripción de la Categoría', verbose_name=u'Descripción')

	def __unicode__(self):
		return self.ProductCategoryName

class UsersActions(models.Model):
	UserActionId = models.AutoField(primary_key=True)
	UserActionUserId = models.ForeignKey(User)
	UserActionDescription = models.TextField(max_length=100, help_text='Descripción de la Acción', verbose_name=u'Descripción')
	UserActionDate = models.DateTimeField(auto_now=True, auto_now_add=True, help_text='Fecha de Realización', verbose_name=u'Fecha')

	def __unicode__(self):
		return self.UserActionDescription

class Products(models.Model):
	ProductId = models.AutoField(primary_key=True)
	ProductProductCategoryId = models.ForeignKey(ProductCategories)
	ProductProductsStatusId = models.ForeignKey(ProductsStatus)
	ProductName = models.CharField(max_length=100, help_text='Nombre del Producto', verbose_name=u'Nombre')
	ProductDescription = models.TextField(max_length=500, help_text='Drescripción del Producto', verbose_name=u'Descripción')
	ProductPrice = models.DecimalField(max_digits=3, decimal_places=2, help_text='Precio del Producto', verbose_name=u'Precio')
	ProductOfferPrice = models.DecimalField(max_digits=3, decimal_places=2, help_text='Precio en Oferta', verbose_name=u'Precio Oferta')
	ProductQuantity = models.IntegerField()
	ProductLikes = models.IntegerField(null=True)
	ProductUnlike = models.IntegerField(null=True)

	def __unicode__(self):
		return self.ProductName

class UsersLikesUnlikes(models.Model):
	UserLikeUnlikeId = models.AutoField(primary_key=True)
	UserLikeUnlikeUserId = models.ForeignKey(User)
	UserLikeUnlikeProductId = models.ForeignKey(Products)
	UserLikeUnlikeType = models.IntegerField()
	UserLikeUnlikeValue = models.BooleanField()

	def __unicode__(self):
		return self.UserLikeUnlikeId

class Cities(models.Model):
	CityId = models.AutoField(primary_key=True)
	CityName = models.CharField(max_length=80, help_text='Nombre de la Ciudad', verbose_name=u'Ciudad')

	def __unicode__(self):
		return self.CityName

class Information(models.Model):
	InformationId = models.AutoField(primary_key=True)
	InformationUserName = models.CharField(max_length=100, help_text='Nombre de Usuario', verbose_name=u'Usuario')
	InformationUserEmail = models.EmailField(max_length=75, help_text='Correo Electrónico', verbose_name=u'Email')
	InformationCityId = models.ForeignKey(Cities)
	InformationDescription = models.TextField(max_length=500, help_text='Descripción', verbose_name=u'Descripción')

	def __unicode__(self):
		return self.InformationId

class Comments(models.Model):
	CommentId = models.AutoField(primary_key=True)
	CommentProductId = models.ForeignKey(Products)
	CommentUserId = models.ForeignKey(User)
	CommentDescription = models.TextField(max_length=1000, help_text='Descripción del Comentario', verbose_name=u'Comentario')

	def __unicode__(self):
		return self.CommentDescription