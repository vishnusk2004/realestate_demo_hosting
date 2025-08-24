from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PropertyValue

def home_value(request):
    """Home value estimation page"""
    return render(request, 'property_value/home_value.html')

@csrf_exempt
def estimate_value(request):
    """API endpoint for home value estimation"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            address = data.get('address', '').strip()
            city = data.get('city', '').strip()
            state = data.get('state', '').strip()
            zip_code = data.get('zip_code', '').strip()
            bedrooms = data.get('bedrooms')
            bathrooms = data.get('bathrooms')
            square_feet = data.get('square_feet')
            year_built = data.get('year_built')
            
            # Contact information
            contact_name = data.get('contact_name', '').strip()
            contact_email = data.get('contact_email', '').strip()
            contact_phone = data.get('contact_phone', '').strip()
            
            if not all([address, city, state, zip_code]):
                return JsonResponse({
                    'success': False,
                    'error': 'Please provide complete address information'
                }, status=400)
            
            # Mock estimation algorithm (in real app, this would call a real estate API)
            # This is a simplified estimation based on location and property details
            
            # Base price per square foot (varies by location)
            base_price_per_sqft = 150  # This would be determined by market data
            
            # Adjustments based on property details
            if bedrooms:
                base_price_per_sqft += (bedrooms - 2) * 10  # More bedrooms = higher value
            if bathrooms:
                base_price_per_sqft += (bathrooms - 1) * 15  # More bathrooms = higher value
            if year_built:
                age = 2024 - year_built
                if age < 10:
                    base_price_per_sqft += 20  # Newer homes worth more
                elif age > 50:
                    base_price_per_sqft -= 30  # Older homes worth less
            
            # Location adjustments (mock data)
            location_multiplier = 1.0
            if state.lower() in ['california', 'new york', 'massachusetts']:
                location_multiplier = 1.5
            elif state.lower() in ['texas', 'florida', 'georgia']:
                location_multiplier = 1.2
            elif state.lower() in ['ohio', 'michigan', 'indiana']:
                location_multiplier = 0.8
            
            # Calculate estimated value
            if square_feet:
                estimated_value = square_feet * base_price_per_sqft * location_multiplier
            else:
                # Fallback estimation without square footage
                estimated_value = 250000 * location_multiplier
                if bedrooms:
                    estimated_value += (bedrooms - 2) * 25000
                if bathrooms:
                    estimated_value += (bathrooms - 1) * 15000
            
            # Add some randomness to make it more realistic
            import random
            variation = random.uniform(0.9, 1.1)
            estimated_value *= variation
            
            # Calculate value range
            value_range_low = estimated_value * 0.9
            value_range_high = estimated_value * 1.1
            
            # Save the estimation
            property_value = PropertyValue.objects.create(
                address=address,
                city=city,
                state=state,
                zip_code=zip_code,
                estimated_value=estimated_value,
                value_range_low=value_range_low,
                value_range_high=value_range_high,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                square_feet=square_feet,
                year_built=year_built,
                contact_name=contact_name,
                contact_email=contact_email,
                contact_phone=contact_phone
            )
            
            return JsonResponse({
                'success': True,
                'results': {
                    'estimated_value': round(estimated_value, 2),
                    'value_range_low': round(value_range_low, 2),
                    'value_range_high': round(value_range_high, 2),
                    'full_address': f"{address}, {city}, {state} {zip_code}",
                    'estimation_id': property_value.id
                }
            })
            
        except (json.JSONDecodeError, ValueError, KeyError) as e:
            return JsonResponse({
                'success': False,
                'error': 'Invalid data provided'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': 'An error occurred during estimation'
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'error': 'Only POST requests are allowed'
    }, status=405)
