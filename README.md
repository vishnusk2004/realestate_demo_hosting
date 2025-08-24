# Real Estate Website

A comprehensive real estate website built with Django, featuring property listings, mortgage calculator, home value estimation, blog, and admin management system.

## Features

### For Users
- **Property Listings**: Browse properties for sale and rent with detailed information
- **Buy a Home**: Search and filter properties for purchase
- **Sell a Home**: Submit inquiries to sell your property
- **Home Value**: Get estimated property values by entering address details
- **Featured Listings**: View highlighted properties
- **New Listings**: Browse recently added properties
- **Mortgage Calculator**: Calculate monthly payments and total costs
- **Blog**: Read real estate articles and tips
- **Contact Forms**: Submit inquiries for specific properties

### For Administrators
- **Admin Dashboard**: Manage all website content through Django admin
- **Property Management**: Add, edit, and manage property listings with images and videos
- **Blog Management**: Create and manage blog posts with categories
- **Inquiry Management**: Track and manage user inquiries
- **User Management**: Manage user accounts and permissions

## Technology Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Image Processing**: Pillow
- **Icons**: Font Awesome

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd realestate_project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the website**
   - Website: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Project Structure

```
realestate_project/
├── realestate_project/     # Main project settings
├── listings/              # Property listings app
├── blog_posts/           # Blog functionality
├── mortgage_calc/        # Mortgage calculator
├── property_value/       # Home value estimation
├── inquiries/            # Contact forms and inquiries
├── templates/            # HTML templates
├── static/               # CSS, JS, and images
├── media/                # User-uploaded files
└── manage.py
```

## Apps Overview

### Listings App
- Property models with images and videos
- Search and filtering functionality
- Featured and new listings
- Property detail pages

### Blog Posts App
- Blog post management
- Categories and authors
- SEO-friendly URLs

### Mortgage Calculator App
- Real-time mortgage calculations
- Multiple loan types support
- Payment breakdown

### Property Value App
- Home value estimation
- Address-based calculations
- Contact information collection

### Inquiries App
- Contact form handling
- Property-specific inquiries
- Inquiry status tracking

## Admin Features

The Django admin interface provides comprehensive management capabilities:

- **Properties**: Add/edit properties with multiple images and videos
- **Blog Posts**: Create and manage blog content
- **Inquiries**: Track and manage user inquiries
- **Categories**: Manage blog categories
- **Users**: Manage user accounts

## Customization

### Adding New Property Types
Edit `listings/models.py` and add new choices to `PROPERTY_TYPES`.

### Modifying Calculator
Update calculation logic in `mortgage_calc/views.py`.

### Styling
Modify `static/css/style.css` for custom styling.

## Deployment

For production deployment:

1. Set `DEBUG = False` in settings
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure media file storage
5. Set up environment variables for sensitive data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please contact the development team.
