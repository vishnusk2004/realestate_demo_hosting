from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import MortgageCalculation

def mortgage_calculator(request):
    """Mortgage calculator page"""
    return render(request, 'mortgage_calc/mortgage_calculator.html')

@csrf_exempt
def calculate_mortgage(request):
    """API endpoint for mortgage calculation"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            property_price = float(data.get('property_price', 0))
            down_payment = float(data.get('down_payment', 0))
            interest_rate = float(data.get('interest_rate', 0))
            loan_term = int(data.get('loan_term', 30))
            loan_type = data.get('loan_type', 'conventional')
            
            # Calculate loan amount
            loan_amount = property_price - down_payment
            down_payment_percentage = (down_payment / property_price * 100) if property_price > 0 else 0
            
            # Calculate monthly payment
            monthly_rate = interest_rate / 100 / 12
            number_of_payments = loan_term * 12
            
            monthly_payment = 0
            if monthly_rate > 0 and loan_amount > 0:
                monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** number_of_payments) / ((1 + monthly_rate) ** number_of_payments - 1)
            
            # Calculate totals
            total_interest = (monthly_payment * number_of_payments) - loan_amount
            total_payment = monthly_payment * number_of_payments
            
            # Estimate additional costs (simplified)
            monthly_property_tax = property_price * 0.012 / 12  # 1.2% annual property tax
            monthly_insurance = property_price * 0.005 / 12   # 0.5% annual insurance
            monthly_pmi = 0  # PMI if down payment < 20%
            
            if down_payment_percentage < 20:
                monthly_pmi = loan_amount * 0.005 / 12  # 0.5% annual PMI
            
            total_monthly_payment = monthly_payment + monthly_property_tax + monthly_insurance + monthly_pmi
            
            # Save calculation if user provided contact info
            contact_name = data.get('contact_name', '')
            contact_email = data.get('contact_email', '')
            contact_phone = data.get('contact_phone', '')
            
            if contact_name and contact_email:
                MortgageCalculation.objects.create(
                    property_price=property_price,
                    down_payment=down_payment,
                    down_payment_percentage=down_payment_percentage,
                    loan_amount=loan_amount,
                    interest_rate=interest_rate,
                    loan_term_years=loan_term,
                    loan_type=loan_type,
                    monthly_principal_interest=monthly_payment,
                    monthly_property_tax=monthly_property_tax,
                    monthly_insurance=monthly_insurance,
                    monthly_pmi=monthly_pmi,
                    total_monthly_payment=total_monthly_payment,
                    total_interest_paid=total_interest,
                    total_payment=total_payment,
                    contact_name=contact_name,
                    contact_email=contact_email,
                    contact_phone=contact_phone
                )
            
            return JsonResponse({
                'success': True,
                'results': {
                    'monthly_payment': round(monthly_payment, 2),
                    'total_monthly_payment': round(total_monthly_payment, 2),
                    'total_interest': round(total_interest, 2),
                    'total_payment': round(total_payment, 2),
                    'loan_amount': round(loan_amount, 2),
                    'down_payment_percentage': round(down_payment_percentage, 2),
                    'monthly_property_tax': round(monthly_property_tax, 2),
                    'monthly_insurance': round(monthly_insurance, 2),
                    'monthly_pmi': round(monthly_pmi, 2),
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
                'error': 'An error occurred during calculation'
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'error': 'Only POST requests are allowed'
    }, status=405)
