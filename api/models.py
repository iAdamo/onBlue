from email.mime import image
from django.db import models
from django.core.validators import RegexValidator


class Geo(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.latitude}, {self.longitude}"


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{5}(-\d{4})?$', message='Invalid zipcode format')]
    )
    geo = models.ForeignKey(
        Geo,
        on_delete=models.CASCADE,
        related_name='addresses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.zipcode}"


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures", blank=True, null=True)
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='residents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, editable=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="post_images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, editable=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments')
    content = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')
    image = models.ImageField(upload_to="comment_images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, editable=False)

    class Meta:
        ordering = ['-created_at']


class Reaction(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='reactions')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reactions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} reacted to {self.post}"

    class Meta:
        ordering = ['-created_at']


class Follow(models.Model):
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following")
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.follower} follows {self.following}"

    class Meta:
        ordering = ['-created_at']
