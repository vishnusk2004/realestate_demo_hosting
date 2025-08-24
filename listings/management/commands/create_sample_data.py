from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Property
from blog_posts.models import Category, BlogPost
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Create sample data for the real estate website'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create a superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Created superuser: admin/admin123')
        
        # Get or create categories
        categories = []
        category_names = ['Market Trends', 'Buying Tips', 'Selling Tips', 'Investment', 'Home Improvement']
        for name in category_names:
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={'slug': name.lower().replace(' ', '-')}
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {name}')
        
        # Create sample properties
        property_data = [
            {
                'title': 'Modern Luxury Home in Downtown',
                'description': 'Discover this architectural masterpiece nestled in downtown Springfield\'s most coveted neighborhood. This stunning 4-bedroom, 3-bathroom contemporary home seamlessly blends modern luxury with timeless elegance. The open-concept main level features soaring 12-foot ceilings, oversized windows, and rich hardwood floors throughout. The chef\'s kitchen is a culinary enthusiast\'s dream, featuring a massive waterfall island, top-of-the-line Wolf appliances, custom Italian cabinetry, and a walk-in pantry. The spacious great room flows effortlessly to a covered outdoor entertaining area with a built-in BBQ and fire pit, perfect for year-round gatherings. Upstairs, the luxurious master suite boasts a private balcony, walk-in closet, and spa-like bathroom with a freestanding soaking tub and glass-enclosed rain shower. Three additional bedrooms offer ample space and comfort. The professionally landscaped yard features mature trees, a three-car garage, and smart home technology throughout. Located minutes from premier shopping, dining, and cultural attractions.',
                'address': '123 Luxury Lane',
                'city': 'Springfield',
                'state': 'IL',
                'zip_code': '62701',
                'price': 750000,
                'property_type': 'house',
                'bedrooms': 4,
                'bathrooms': 3,
                'square_feet': 3200,
                'is_featured': True,
                'is_new_listing': True,
                'main_image_url': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop',
            },
            {
                'title': 'Cozy Family Home with Large Yard',
                'description': 'Perfect family home with 3 bedrooms, 2 bathrooms, and a large backyard for kids and pets.',
                'address': '456 Family Street',
                'city': 'Springfield',
                'state': 'IL',
                'zip_code': '62702',
                'price': 425000,
                'property_type': 'house',
                'bedrooms': 3,
                'bathrooms': 2,
                'square_feet': 2100,
                'is_featured': True,
                'is_new_listing': False,
            },
            {
                'title': 'Downtown Apartment with City Views',
                'description': 'Modern 2-bedroom apartment in the heart of downtown with amazing city views and amenities.',
                'address': '789 Downtown Ave',
                'city': 'Springfield',
                'state': 'IL',
                'zip_code': '62701',
                'price': 285000,
                'property_type': 'apartment',
                'bedrooms': 2,
                'bathrooms': 2,
                'square_feet': 1200,
                'is_featured': True,
                'is_new_listing': True,
            },
            {
                'title': 'Investment Property - Multi-Family',
                'description': 'Excellent investment opportunity with 4 units, great rental income potential.',
                'address': '321 Investment Blvd',
                'city': 'Springfield',
                'state': 'IL',
                'zip_code': '62703',
                'price': 650000,
                'property_type': 'commercial',
                'bedrooms': 8,
                'bathrooms': 4,
                'square_feet': 4800,
                'is_featured': False,
                'is_new_listing': True,
            },
            {
                'title': 'Beautiful Townhouse with Garage',
                'description': 'Spacious 3-bedroom townhouse with attached garage and private patio.',
                'address': '654 Townhouse Way',
                'city': 'Springfield',
                'state': 'IL',
                'zip_code': '62704',
                'price': 380000,
                'property_type': 'townhouse',
                'bedrooms': 3,
                'bathrooms': 2,
                'square_feet': 1800,
                'is_featured': False,
                'is_new_listing': False,
            },
            {
                'title': 'Luxury Condo with Pool Access',
                'description': 'Experience sophisticated urban living in this stunning 2-bedroom, 2-bathroom luxury condominium located in the prestigious Luxury Circle. This meticulously designed unit features an open-concept floor plan with floor-to-ceiling windows that flood the space with natural light and offer breathtaking city views. The gourmet kitchen boasts premium stainless steel appliances, quartz countertops, custom cabinetry, and a spacious island perfect for entertaining. The master suite includes a walk-in closet and spa-like ensuite bathroom with dual vanities and a glass-enclosed shower. Residents enjoy exclusive access to world-class amenities including a resort-style swimming pool, state-of-the-art fitness center, rooftop terrace, concierge services, and secure parking. The building also features 24/7 security, a business center, and guest suites. Located in the heart of downtown Springfield, you\'ll be steps away from fine dining, shopping, entertainment, and major business districts. This is luxury living at its finest.',
                'address': '987 Luxury Circle',
                'city': 'Springfield',
                'state': 'IL',
                'zip_code': '62705',
                'price': 520000,
                'property_type': 'condo',
                'bedrooms': 2,
                'bathrooms': 2,
                'square_feet': 1400,
                'is_featured': True,
                'is_new_listing': False,
            },
        ]
        
        for data in property_data:
            property_obj, created = Property.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created property: {data["title"]}')
        
        # Create sample blog posts
        blog_data = [
            {
                'title': 'Spring 2024 Real Estate Market Trends',
                'content': '''The real estate market is experiencing significant shifts this spring, presenting both opportunities and challenges for buyers and sellers alike. After a period of uncertainty, we're witnessing increased buyer confidence driven by stabilizing interest rates and improving economic indicators.

**Key Market Indicators:**
- Average home prices have stabilized with a modest 3.2% year-over-year increase
- Inventory levels are up 15% compared to last spring, giving buyers more options
- Days on market have decreased to an average of 28 days, indicating strong demand
- First-time buyer activity has increased by 22% quarter-over-quarter

**Regional Highlights:**
The Springfield metropolitan area continues to outperform national averages, with luxury properties seeing particularly strong demand. Neighborhoods like Downtown Springfield and Luxury Circle are experiencing premium pricing due to their proximity to business districts and amenities.

**What This Means for Buyers:**
While competition remains fierce, the increased inventory provides more negotiating power. Buyers should act quickly when they find the right property, but they now have more leverage in negotiations than they did last year.

**Seller Opportunities:**
Sellers in desirable neighborhoods can expect multiple offers, but proper pricing and staging remain crucial. Properties that are priced correctly and well-presented are selling within the first two weeks on the market.

**Looking Ahead:**
Economists predict continued stability through the summer months, with potential for modest price appreciation in premium markets. We recommend both buyers and sellers work with experienced professionals to navigate this dynamic market successfully.''',
                'excerpt': 'Discover the latest trends shaping the real estate market this spring and what they mean for buyers and sellers.',
                'category': categories[0],  # Market Trends
                'author': User.objects.first(),
                'status': 'published',
            },
            {
                'title': '10 Essential Tips for First-Time Home Buyers',
                'content': '''Purchasing your first home is one of life's most significant milestones, but it doesn't have to be overwhelming. With proper preparation and the right guidance, you can navigate the process with confidence. Here are our top 10 essential tips to ensure your home buying journey is successful.

**1. Check Your Credit Score Early**
Your credit score directly impacts your mortgage rate and terms. Aim for a score of 740+ for the best rates. If your score needs improvement, start working on it at least 6 months before house hunting.

**2. Get Pre-Approved, Not Just Pre-Qualified**
Pre-approval shows sellers you're a serious buyer with verified financing. This gives you a significant advantage in competitive markets and helps you understand your true budget.

**3. Save for More Than Just the Down Payment**
Beyond your down payment (typically 3-20%), budget for closing costs (2-5% of purchase price), moving expenses, immediate repairs, and a cash reserve for unexpected issues.

**4. Research Neighborhoods Thoroughly**
Visit potential neighborhoods at different times of day and days of the week. Consider commute times, school districts, future development plans, and resale values.

**5. Don't Forget About Property Taxes and Insurance**
These ongoing costs can significantly impact your monthly budget. Research local tax rates and get insurance quotes before making an offer.

**6. Hire a Qualified Home Inspector**
Never skip the inspection, even in a seller's market. A thorough inspection can reveal costly issues and provide negotiating leverage.

**7. Understand Different Loan Types**
Explore FHA, VA, conventional, and local first-time buyer programs. Each has different requirements and benefits that might work better for your situation.

**8. Keep Your Finances Stable During the Process**
Avoid making major purchases, changing jobs, or opening new credit accounts between pre-approval and closing.

**9. Plan for the Long Term**
Consider how long you plan to stay in the home. If it's less than 5 years, renting might be more cost-effective.

**10. Work with Experienced Professionals**
A knowledgeable real estate agent, mortgage lender, and attorney can guide you through the process and help you avoid costly mistakes.

Remember, buying a home is a marathon, not a sprint. Take your time to make informed decisions, and don't let emotions drive your choices. With proper preparation and the right team, you'll be holding your keys in no time!''',
                'excerpt': 'Navigate the home buying process with confidence using these essential tips for first-time buyers.',
                'category': categories[1],  # Buying Tips
                'author': User.objects.first(),
                'status': 'published',
            },
            {
                'title': 'How to Stage Your Home for Maximum Appeal',
                'content': '''Professional staging can be the difference between a home that sells quickly at full asking price and one that lingers on the market. In today's competitive real estate environment, first impressions are everything. Here's your comprehensive guide to staging your home for maximum appeal.

**The Psychology of Staging**
Staging helps potential buyers envision themselves living in your home. It creates an emotional connection while highlighting your property's best features and minimizing any shortcomings. Staged homes typically sell 73% faster and for 10% more than non-staged homes.

**Start with Deep Cleaning and Decluttering**
Before any staging can begin, your home must be immaculately clean and decluttered. Remove personal items, excess furniture, and anything that makes spaces feel cramped. Consider renting a storage unit for items you'll need after the move.

**Key Staging Principles:**

**1. Neutralize Your Color Palette**
Paint walls in neutral colors like warm whites, soft grays, or beiges. This creates a blank canvas that appeals to the widest range of buyers and makes spaces feel larger and brighter.

**2. Maximize Natural Light**
Open all curtains and blinds during showings. Clean windows inside and out. Replace heavy drapes with light, airy window treatments. Add mirrors strategically to reflect light and create the illusion of space.

**3. Create Focal Points**
In each room, establish a clear focal point like a fireplace, large window, or piece of artwork. Arrange furniture to highlight these features.

**4. The Two-Thirds Rule**
Remove about one-third of your furniture and belongings. This makes rooms appear larger and allows buyers to focus on the space rather than your possessions.

**Room-by-Room Staging Tips:**

**Living Room:**
- Arrange furniture to create conversation areas
- Add fresh flowers or plants for life and color
- Use throw pillows and blankets in current colors
- Ensure adequate lighting with lamps and overhead fixtures

**Kitchen:**
- Clear all countertops except for a few decorative items
- Update cabinet hardware if dated
- Add a bowl of fresh fruit or flowers
- Ensure all appliances are spotless

**Master Bedroom:**
- Invest in luxurious bedding in neutral colors
- Remove all personal photos and items
- Create symmetry with matching nightstands and lamps
- Keep surfaces clear and uncluttered

**Bathrooms:**
- Replace old towels with new, fluffy white ones
- Add spa-like touches with candles or plants
- Ensure all fixtures are spotless and updated
- Remove all personal care items

**Outdoor Spaces:**
- Enhance curb appeal with fresh landscaping
- Power wash driveways and walkways
- Add potted plants for color and life
- Ensure outdoor furniture is clean and arranged invitingly

**Professional vs. DIY Staging**
While you can stage many elements yourself, consider hiring a professional for vacant homes or if you lack design experience. Professional stagers understand current market preferences and have access to rental furniture and accessories.

**Common Staging Mistakes to Avoid:**
- Over-personalizing with family photos and collections
- Using outdated or worn furniture
- Blocking natural light sources
- Neglecting odors from pets, cooking, or smoking
- Leaving rooms unfurnished (they appear smaller)

**Final Thoughts**
Remember, staging is about creating a lifestyle that buyers want to purchase. Every element should work together to create a cohesive, appealing environment that allows potential buyers to imagine themselves calling your house their home.

Invest in staging early in the process – the return on investment typically far exceeds the cost, and you'll likely sell faster with less stress.''',
                'excerpt': 'Learn professional staging techniques to make your home more attractive to potential buyers.',
                'category': categories[2],  # Selling Tips
                'author': User.objects.first(),
                'status': 'published',
            },
            {
                'title': 'Understanding Mortgage Types: A Complete Guide',
                'content': '''Navigating the world of mortgages can feel overwhelming, especially for first-time buyers. Understanding the different types of loans available can help you make an informed decision that aligns with your financial situation and long-term goals.

**Conventional Loans**
These are the most common type of mortgage, not backed by government agencies. They typically require a 20% down payment for the best terms, though some programs allow as little as 3% down. Conventional loans are ideal for borrowers with good credit (740+) and stable income.

**FHA Loans**
Backed by the Federal Housing Administration, these loans are designed for borrowers who may not qualify for conventional financing. Benefits include down payments as low as 3.5% and more flexible credit requirements. However, they require mortgage insurance premiums.

**VA Loans**
Available to qualifying veterans, active-duty military, and eligible spouses. These loans offer 100% financing (no down payment required), competitive interest rates, and no private mortgage insurance.

**Adjustable vs. Fixed Rate**
Fixed-rate mortgages maintain the same interest rate throughout the loan term, providing payment stability. Adjustable-rate mortgages (ARMs) start with lower rates that adjust periodically based on market conditions.

**Choosing the Right Loan**
Consider your down payment capability, credit score, debt-to-income ratio, and how long you plan to stay in the home. Consult with multiple lenders to compare terms and find the best fit for your situation.''',
                'excerpt': 'Explore different mortgage types and find the financing option that best fits your needs.',
                'category': categories[1],  # Buying Tips
                'author': User.objects.first(),
                'status': 'published',
            },
            {
                'title': 'Real Estate Investment Strategies for 2024',
                'content': '''Real estate remains one of the most reliable long-term investment strategies, offering both passive income potential and appreciation opportunities. Here's what investors should know about the current market landscape.

**Market Conditions**
Despite economic uncertainties, real estate continues to provide stability compared to volatile stock markets. Rental demand remains strong, particularly in growing metropolitan areas like Springfield.

**Investment Property Types**
Single-family rentals offer easier management and financing, while multi-family properties provide higher cash flow potential. Commercial properties require more capital but can yield significant returns.

**Financing Strategies**
Investment property loans typically require 20-25% down payments and higher interest rates than primary residences. Consider portfolio lenders for multiple properties or alternative financing for fix-and-flip projects.

**Key Metrics to Track**
Focus on cash flow, cap rates, and cash-on-cash returns rather than just appreciation potential. A good investment property should generate positive cash flow from day one.

**Market Analysis**
Research local job growth, population trends, and development plans. Properties near transportation hubs, schools, and amenities typically appreciate faster and attract quality tenants.''',
                'excerpt': 'Discover proven real estate investment strategies and market insights for building wealth.',
                'category': categories[3],  # Investment
                'author': User.objects.first(),
                'status': 'published',
            },
            {
                'title': 'Home Renovation ROI: Projects That Add Value',
                'content': '''Not all home improvements are created equal when it comes to return on investment. Understanding which renovations add the most value can help you make smart decisions whether you're planning to sell soon or improve your home's long-term value.

**High-ROI Projects**

**Kitchen Updates (70-80% ROI)**
Minor kitchen remodels consistently rank among the top value-adding projects. Focus on updating cabinets, countertops, and appliances rather than complete overhauls.

**Bathroom Renovations (60-70% ROI)**
Adding a bathroom or updating existing ones significantly increases home value. Focus on modern fixtures, improved lighting, and quality materials.

**Exterior Improvements (75-85% ROI)**
New siding, roofing, and front door replacement offer excellent returns. These projects improve curb appeal and energy efficiency.

**Flooring Updates (60-70% ROI)**
Hardwood floors are highly desirable. Refinishing existing floors or installing luxury vinyl plank provides excellent returns.

**Projects to Approach Carefully**
Swimming pools, high-end luxury finishes, and over-improving for your neighborhood typically don't provide strong returns.

**Timing Your Projects**
Complete major renovations at least six months before listing to ensure everything is settled and any issues are resolved.''',
                'excerpt': 'Learn which home improvement projects provide the best return on investment.',
                'category': categories[4],  # Home Improvement
                'author': User.objects.first(),
                'status': 'published',
            },
        ]
        
        for i, data in enumerate(blog_data):
            slug = f"{data['title'].lower().replace(' ', '-').replace(':', '')}-{i+1}"
            blog_post, created = BlogPost.objects.get_or_create(
                title=data['title'],
                defaults={
                    **data,
                    'slug': slug,
                    'published_at': timezone.now(),
                }
            )
            if created:
                self.stdout.write(f'Created blog post: {data["title"]}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
        self.stdout.write('You can now view the website with sample properties and blog posts.')
        self.stdout.write('Admin login: admin/admin123')
