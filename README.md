# DjangoEcommerce

## Overview
DjangoEcommerce is a full-featured e-commerce platform built with Django. It provides user authentication, product management, order tracking, and a seamless shopping experience with integrated payment gateways.

## Features
- **User Authentication**: Secure login/logout using Django Rest Framework SimpleJWT.
- **Product Management**: Add, edit, and delete products with images and descriptions.
- **Shopping Cart**: Users can add products to the cart and proceed to checkout.
- **Order Management**: Users can track, cancel, and reorder previous purchases.
- **Search & Filtering**: Full-text search and category-based filtering.
- **Payment Integration**: Supports PayPal, Stripe, and Razorpay.
- **Admin Dashboard**: Manage users, orders, and products with Django Admin.
- **Database Support**: Compatible with PostgreSQL and MySQL.
- **Background Tasks**: Uses Celery and RabbitMQ for handling async tasks.

## Tech Stack
- **Backend**: Django 5.0.2, Django Rest Framework 3.15.2
- **Database**: PostgreSQL/MySQL
- **Caching**: Redis
- **Search**: Elasticsearch 8.14.0
- **Task Queue**: Celery 5.4.0, RabbitMQ
- **WebSockets**: Django Channels, Daphne
- **Testing & Monitoring**: Locust for load testing, Django Debug Toolbar
- **Automation**: Cron jobs using Django-Crontab

## Installation
### Prerequisites
- Python 3.10+
- PostgreSQL/MySQL
- Redis
- Elasticsearch
- RabbitMQ

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/django-ecommerce.git
   cd django-ecommerce
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Configure environment variables:
   ```sh
   cp .env.example .env
   ```
4. Run database migrations:
   ```sh
   python manage.py migrate
   ```
5. Start Redis, Celery, and Django server:
   ```sh
   redis-server &
   celery -A django-ecommerce worker --loglevel=info &
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/admin/` for the admin panel.
- API documentation available at `/api/docs/` if configured.
- Use Postman or a frontend client to interact with the API.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.
