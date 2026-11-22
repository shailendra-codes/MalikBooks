from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Sum
from decimal import Decimal
from .models import Book, Chapter, Purchase
import docx

def home(request):
    category = request.GET.get('category')
    q = request.GET.get('q')
    books = Book.objects.filter(status='live').order_by('-created_at')
    if category:
        books = books.filter(category=category)
    if q:
        books = books.filter(title__icontains=q)
    return render(request, 'books/home.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id, status='live')
    has_access = book.price == 0 or (request.user.is_authenticated and (
        request.user == book.author or Purchase.objects.filter(user=request.user, book=book).exists()
    ))
    return render(request, 'books/detail.html', {'book': book, 'has_access': has_access})

@login_required
def buy_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, status='live')
    if not Purchase.objects.filter(user=request.user, book=book).exists():
        royalty = (book.price * Decimal('0.70')).quantize(Decimal('0.01'))
        Purchase.objects.create(user=request.user, book=book, amount_paid=book.price, author_royalty=royalty)
    return redirect('read_book', book_id=book.id, chapter_num=1)

def read_book(request, book_id, chapter_num=1):
    book = get_object_or_404(Book, id=book_id, status='live')
    has_access = book.price == 0 or (request.user.is_authenticated and (
        request.user == book.author or Purchase.objects.filter(user=request.user, book=book).exists()
    ))
    if not has_access:
        return redirect('book_detail', book_id=book.id)
    chapter = get_object_or_404(Chapter, book=book, chapter_number=chapter_num)
    total = book.chapters.count()
    return render(request, 'books/reader.html', {
        'book': book, 'chapter': chapter,
        'prev_ch': chapter_num - 1 if chapter_num > 1 else None,
        'next_ch': chapter_num + 1 if chapter_num < total else None,
    })

@login_required
def publish_book(request):
    if request.method == 'POST':
        book = Book.objects.create(
            author=request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            category=request.POST['category'],
            language=request.POST['language'],
            price=request.POST.get('price', 0) or 0,
            cover=request.FILES.get('cover'),
            status='live' if request.user.is_superuser else 'review'
        )
        docx_file = request.FILES.get('docx_file')
        if docx_file:
            doc = docx.Document(docx_file)
            full_text = "\n\n".join([p.text for p in doc.paragraphs if p.text.strip()])
            Chapter.objects.create(book=book, chapter_number=1, title="Full Book", content=full_text)
        return redirect('dashboard')
    return render(request, 'books/publish.html')

@login_required
def author_dashboard(request):
    my_books = Book.objects.filter(author=request.user).order_by('-created_at')
    earnings = Purchase.objects.filter(book__author=request.user).aggregate(total=Sum('author_royalty'))['total'] or 0
    return render(request, 'books/dashboard.html', {'my_books': my_books, 'earnings': earnings})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'books/signup.html', {'form': form})
 
