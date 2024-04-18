from django.shortcuts import render
from .models import PortfolioItem  # Import the PortfolioItem model

def index(request):
    """ A view to return the index page with portfolio items """

    # Retrieve all portfolio items from the database
    portfolios = PortfolioItem.objects.all()

    # Pass the portfolio items to the template
    context = {
        'portfolios': portfolios,
    }

    # Render the index template with the portfolio items
    return render(request, 'home/index.html', context)
