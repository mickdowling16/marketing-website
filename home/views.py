from django.shortcuts import render
from .models import PortfolioItem, Partner  # Import the Partner model

def index(request):
    """ A view to return the index page with portfolio items and partner images """

    # Retrieve all portfolio items from the database
    portfolios = PortfolioItem.objects.all()

    # Retrieve all partner images from the database
    partners = Partner.objects.all()

    # Pass the portfolio items and partner images to the template
    context = {
        'portfolios': portfolios,
        'partners': partners,  # Add partners queryset to the context
    }

    # Render the index template with the portfolio items and partner images
    return render(request, 'home/index.html', context)
