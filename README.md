# 📚 MalikBooks

**MalikBooks** is an open, lightweight self-publishing and online e-book reading platform built with **Python (Django)** and **Tailwind CSS**. It is designed for Hindi, Hinglish, and coding authors to publish, share, and monetize their books easily.

## ✨ Key Features

- **Author Publishing Dashboard:** Authors can register, upload book covers, set pricing (Free or Paid), and track their **70% royalty earnings**.
- **Automatic `.docx` Reader:** Upload any Microsoft Word (`.docx`) manuscript and the platform automatically extracts and formats the book for web reading.
- **Distraction-Free Dark Mode Reader:** Mobile-friendly reading interface with Dark Mode toggle and right-click/copy protection.
- **Category & Search Filters:** Browse books across *Coding & Tech*, *Hindi Stories*, *Motivation*, and *Spirituality*.
- **Admin Moderation Panel:** Built-in Django admin panel to review and publish submitted books with a single click.

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, Tailwind CSS
- **Document Parsing:** `python-docx`
- **Database:** SQLite3

## 🚀 Quick Setup

```bash
git clone https://github.com
cd MalikBooks
pip install -r requirements.txt
python manage.py makemigrations books
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 👨‍💻 Author

Developed by **Shailendra Kumar Singh**
 
