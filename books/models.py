from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('coding', 'Coding & Tech'),
        ('story', 'Hindi Stories'),
        ('motivation', 'Motivation'),
        ('spirituality', 'Spirituality'),
    ]
    STATUS_CHOICES = [
        ('review', 'In Review'),
        ('live', 'Live'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='story')
    language = models.CharField(max_length=50, default='Hindi')
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    chapter_number = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        ordering = ['chapter_number']

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    author_royalty = models.DecimalField(max_digits=6, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)
 
