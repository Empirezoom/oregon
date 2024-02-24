from django.db import models

# Create your models here.

class CompanyProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='logo')
    home_img = models.ImageField(upload_to='home_img')
    confirm = models.ImageField(upload_to='confirm')
    thanks = models.ImageField(upload_to='thanks')
    video = models.FileField(upload_to='video')
    p1 = models.TextField()
    p2 = models.TextField()
    p3 = models.TextField()
    p4 = models.TextField()
    copyright = models.CharField(max_length=50)
    banner_h1 = models.CharField( max_length=50,default ='higher/top_text')
    banner_h3 = models.CharField( max_length=50, default = 'lower_text')
    favicon = models.ImageField(upload_to='logo',default='favicon.jpg')
    notification = models.ImageField(upload_to='logo',default='notification.jpg')
    

        
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'CompanyProfile'
        managed = True
        verbose_name = 'CompanyProfile'
        verbose_name_plural = 'CompanyProfile'


class ApplicationChoice(models.Model):
    type = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    item_img = models.ImageField(upload_to='item_img')
    p1 = models.TextField(blank=True,null=True)
    p2 = models.TextField(blank=True,null=True)
    p3 = models.TextField(blank=True,null=True)
    p4 = models.TextField(blank=True,null=True)
    p5 = models.TextField(blank=True,null=True)
 
    

        
    def __str__(self):
        return self.type
    class Meta:
        db_table = 'application'
        managed = True
        verbose_name = 'application'
        verbose_name_plural = 'applications'



class Application(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=500)

    sent = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'application form'
        managed = True
        verbose_name = 'application form'
        verbose_name_plural = 'application form'


class Upload(models.Model):
    screenshot = models.ImageField(upload_to='payment screenshot' )
    uploaded = models.CharField( max_length=50,default='screenshot')
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.uploaded
    
    class Meta:
        db_table = 'upload'
        managed = True
        verbose_name = 'upload'
        verbose_name_plural = 'uploads'


class ThanksEdit(models.Model):
    
    text = models.CharField( max_length=5000)
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text
    
    class Meta:
        db_table = 'thanks edit'
        managed = True
        verbose_name = 'thanks edit'
        verbose_name_plural = 'thanks edits'


class BtcInfo(models.Model):
   
    wallet_address = models.CharField( max_length=5000)
    scan = models.ImageField(upload_to='crypto')
    cryptologo = models.ImageField(upload_to='crypto')
    
    def __str__(self):
        return self.wallet_address
    
    class Meta:
        db_table = 'btc '
        managed = True
        verbose_name = 'btc '
        verbose_name_plural = 'btc '

class BnbInfo(models.Model):
   
    wallet_address = models.CharField( max_length=5000)
    scan = models.ImageField(upload_to='crypto')
    cryptologo = models.ImageField(upload_to='crypto')
    
    def __str__(self):
        return self.wallet_address
    
    class Meta:
        db_table = 'bnb'
        managed = True
        verbose_name = 'bnb'
        verbose_name_plural = 'bnb'

class DogeInfo(models.Model):
   
    wallet_address = models.CharField( max_length=5000)
    scan = models.ImageField(upload_to='crypto')
    cryptologo = models.ImageField(upload_to='crypto')
    
    def __str__(self):
        return self.wallet_address
    
    class Meta:
        db_table = 'doge'
        managed = True
        verbose_name = 'doge'
        verbose_name_plural = 'doge'


    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'