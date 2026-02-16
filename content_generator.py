"""
Content Generator - DEMO VERSION
Works without OpenAI API - uses sample content instead!
"""

import os
from dotenv import load_dotenv
from database import MarketingDatabase
from prompt_engineer import PromptEngineer
import random

# Load secret API key from .env file (not used in demo, but kept for compatibility)
load_dotenv()

class MarketingContentGenerator:
    """
    DEMO VERSION: Shows how the system works without calling OpenAI
    Uses pre-written sample content instead.
    """
    
    # Sample generated content for demo purposes
    DEMO_CONTENT = {
        "ad_copy": {
            "warm": """☕ Your Perfect Morning Starts Here

Freshly roasted organic beans delivered to your door every week. Ethically sourced from sustainable farms, roasted to order for maximum flavor.

Wake up to the aroma of premium coffee without leaving home. First delivery includes a free ceramic mug!

👉 Start Your Subscription - 20% Off First Month""",
            
            "professional": """Organic Coffee Subscription Service

Premium arabica beans delivered weekly. Certified organic and fair trade. Customizable roast preferences.

Join 50,000+ professionals who start their day with quality coffee. Corporate plans available.

📦 Schedule Your First Delivery""",
            
            "energetic": """🔥 Fuel Your Hustle!

Tired of weak gas station coffee? Our organic beans pack 40% more caffeine punch. Delivered fresh every Monday morning.

⚡ Boost your productivity
⚡ 100% organic & sustainable  
⚡ Cancel anytime

👉 Get Fueled Today - First Bag FREE!"""
        },
        
        "email_campaigns": {
            "warm": """Subject: Your coffee is waiting ☕

Hi [Name],

I noticed you checked out our organic coffee subscription but didn't complete your order.

Here's what you're missing:
✓ Fresh beans roasted 24 hours before shipping
✓ Free delivery to your door
✓ Skip or cancel anytime

As a welcome gift, use code WELCOME20 for 20% off your first 3 months.

[Complete My Order]

Questions? Just reply to this email - I read every one.

Cheers,
Sarah from BeanBox

P.S. This offer expires in 48 hours ⏰""",
            
            "professional": """Subject: Exclusive offer for [Company Name]

Dear [Name],

Thank you for your interest in our corporate coffee solutions.

Based on your team size of [X] employees, I recommend our Business Premium plan:

• Weekly delivery of 5lb fresh roast
• 3 blend varieties included
• Complimentary brewing equipment
• Dedicated account manager

Special pricing: $299/month (regular $399)

[Schedule Consultation]

Best regards,
Michael Chen
Enterprise Sales Director""",
            
            "excited": """Subject: 🎉 We're launching (and you're invited!)

Hey [Name]!

Remember when you said you wished you could get coffee shop quality at home?

After 2 years of testing 200+ beans, we cracked the code. BeanBox launches next week!

VIP early access includes:
🎁 50% off for life
🎁 Free $200 grinder
🎁 Exclusive "Founding Member" status

Only 100 spots available.

[Claim My VIP Access]

See you on the inside!
The BeanBox Team

P.S. Current members are already sharing their referral links. Don't wait! 🚀"""
        },
        
        "social_media": {
            "motivational": """POV: You finally found coffee that matches your ambition ☕✨

No more mid-afternoon crashes. No more bitter aftertaste. Just pure, organic fuel for your goals.

What's your biggest productivity hack? Share below! 👇

#OrganicCoffee #Productivity #MorningRoutine #EntrepreneurLife #FuelYourHustle""",
            
            "professional": """Monday morning meeting fuel: sorted ✅

Our corporate clients report 23% increase in morning meeting engagement after switching to fresh-roasted organic coffee.

DM us for office samples.

#OfficeCulture #CorporateWellness #CoffeeAtWork #B2B""",
            
            "playful": """Me: I'll just have one cup
Also me: *finishes entire pot* ☕😅

Who else is "one cup" person? Comment with your coffee meme!

👇 Shop our best sellers (link in bio)

#CoffeeAddict #Relatable #CoffeeMemes #OrganicLife #ButFirstCoffee"""
        },
        
        "blog_posts": {
            "helpful": """# 7 Ways to Upgrade Your Morning Coffee Routine

## Introduction
That $6 latte habit? It's costing you $1,500+ per year. Here's how to get cafe-quality coffee at home for under $1 per cup.

## 1. Buy Fresh, Not Fancy
Grocery store coffee sits for months. Buy from roasters who ship within 48 hours of roasting.

## 2. Grind Your Own
Pre-ground coffee loses flavor in 20 minutes. A $20 burr grinder changes everything.

## 3. Water Temperature Matters
195-205°F is the sweet spot. Too hot = bitter. Too cool = weak.

## 4. The 1:16 Golden Ratio
1 gram coffee to 16 grams water. Use a kitchen scale. Seriously.

## 5. Bloom Your Grounds
Pour a little water first, wait 30 seconds. Releases CO2 for better extraction.

## 6. Clean Your Equipment
Oily residue ruins flavor. Clean weekly with vinegar solution.

## 7. Store Beans Properly
Airtight container, cool dark place. Never in the fridge (causes condensation).

## Conclusion
Start with #1 and #4 this week. Master those before adding others.

What's your current coffee setup? Pour-over, French press, or machine? 👇""",
            
            "professional": """# The Business Case for Premium Office Coffee

## Executive Summary
Companies investing in quality coffee see measurable ROI through increased productivity and employee satisfaction.

## The Data
• 67% of employees drink coffee daily (National Coffee Association)
• 46% say coffee improves their work performance
• Average worker spends $1,100/year on coffee runs

## Cost Analysis

**Option A: Coffee Runs**
- 20 employees × $5/day × 250 work days = $25,000/year
- Lost productivity: 15 min/day × 20 staff = 125 hours/day wasted

**Option B: Office Subscription**
- Premium service: $6,000/year
- Time saved: 3,125 hours annually
- Effective hourly rate: $1.92/hour of productivity

## Implementation Guide

**Month 1:** Pilot with 5-person team
**Month 2:** Survey satisfaction and productivity
**Month 3:** Roll out company-wide

## Key Takeaway
Premium coffee isn't an expense—it's a $19,000 net savings with productivity gains.

Ready to calculate your office's potential savings? [Download our ROI calculator]""",
            
            "inspirational": """# From Bean to Cup: The Journey of Ethical Coffee

## The Problem You Didn't Know About
80% of coffee farmers live below the poverty line. Your morning habit could change that.

## Meet Maria

Maria tends 500 coffee trees in Colombia's Huila region. For 20 years, she sold to middlemen for $0.50/lb—barely covering costs.

## The Direct Trade Difference

Through our partner network:
• Maria now earns $2.50/lb (500% increase)
• Her children attend school full-time
• She's invested in sustainable farming practices

## What "Ethical" Really Means

**Fair Trade:** Minimum price guarantee
**Direct Trade:** Relationship-based, premium pricing
**Organic:** No synthetic chemicals

## Your Impact

One subscription = 2lb/month from farmers like Maria
Annual impact: $48 additional income per farmer

## Beyond the Cup

Maria's cooperative now runs:
• Community health clinic
• Women's business microloan program
• Sustainable agriculture training

## Conclusion

Every sip matters. Choose coffee that creates change.

What's your non-negotiable when choosing coffee brands? Share below! 👇"""
        },
        
        "product_descriptions": {
            "luxurious": """Experience the perfect cup, every single morning.

Our Organic Reserve Subscription delivers rare, single-origin beans from the world's finest growing regions. Each 12oz bag is roasted to order within 24 hours of shipping, ensuring peak freshness and complex flavor profiles that mass-market coffee simply cannot match.

✓ Limited micro-lot selections (500 bags max per harvest)
✓ Tasting notes card with each delivery
✓ Complimentary glass storage canister
✓ Personal coffee concierge service

⭐⭐⭐⭐⭐ "Finally understand what 'third wave coffee' means. Game changer." - James R., subscriber since 2022

Perfect for: Discerning coffee enthusiasts, home baristas, anyone who's outgrown grocery store blends.

Elevate your morning ritual. Limited memberships available.

[Begin Your Coffee Journey]""",
            
            "professional": """Enterprise Coffee Solution for Modern Workplaces

BeanBox Corporate delivers premium organic coffee to offices of 10-10,000 employees. Our flexible subscription model eliminates procurement headaches while ensuring consistent quality.

Features:
• Scheduled delivery (weekly, bi-weekly, or monthly)
• Multiple roast profiles per order
• Equipment leasing options (grinders, brewers)
• Usage analytics and reporting
• Dedicated account management

Compliance:
• USDA Organic certified
• Fair Trade certified
• B-Corp pending
• Carbon neutral shipping

Pricing: Starting at $4.50/employee/month

Implementation: 48-hour setup, no long-term contracts

[Request Corporate Sample Box]""",
            
            "friendly": """Hey Coffee Lover! ☕

Tired of sad, stale grocery store coffee? We were too.

That's why we started BeanBox—fresh, organic beans delivered before they even think about going stale.

What you get:
🚚 Free shipping (always)
🔄 Skip or cancel anytime (seriously, no guilt)
🎁 Free mug with first order
😊 Happiness guarantee (don't love it? full refund)

Real talk: Our founder still personally tastes every batch. That's how much we care.

Join 50,000+ happy coffee drinkers. First bag is on us!

[Claim My Free Coffee]"""
        }
    }
    
    def __init__(self):
        """
        Setup everything when we create this object.
        DEMO VERSION: Doesn't need OpenAI API key!
        """
        print("🚀 Initializing Marketing Content Generator [DEMO MODE]...")
        
        # Step 1: Connect to our memory box (database)
        print("📦 Loading database...")
        self.db = MarketingDatabase()
        
        # Step 2: Connect to our recipe creator (prompt engineer)
        print("📝 Loading prompt engineer...")
        self.prompt_engineer = PromptEngineer(self.db)
        
        # DEMO: No OpenAI connection needed!
        print("🎭 DEMO MODE: Using sample content (no API calls)")
        print("✅ All systems ready!")
        print("-" * 50)
    
    def generate(self, content_type, topic, tone="professional", 
                 target_audience="general", key_points=None, brand_voice=None):
        """
        Main function to generate content.
        DEMO VERSION: Returns pre-written sample content.
        """
        
        # Default key points if none provided
        if key_points is None:
            key_points = ["quality", "value"]
        
        print(f"🎯 Generating {content_type} about: {topic}")
        print(f"   Tone: {tone} | Audience: {target_audience}")
        
        try:
            # Step 1: Create the prompt (for display purposes)
            prompt = self.prompt_engineer.create_prompt(
                content_type=content_type,
                topic=topic,
                tone=tone,
                target_audience=target_audience,
                key_points=key_points,
                brand_voice=brand_voice
            )
            
            # DEMO: Simulate API call delay
            print("   Sending to OpenAI... [DEMO: Using sample content]")
            
            # Get demo content based on type and tone
            content_by_type = self.DEMO_CONTENT.get(content_type, {})
            
            # Try to match tone, fallback to random if not found
            if tone in content_by_type:
                generated_content = content_by_type[tone]
            else:
                # Get any available tone for this content type
                available_tones = list(content_by_type.keys())
                if available_tones:
                    generated_content = content_by_type[random.choice(available_tones)]
                else:
                    generated_content = f"[Demo content for {content_type} with {tone} tone]\n\nThis is sample marketing content. In the real version, OpenAI would generate this based on your topic: {topic}"
            
            # Simulate token count (for demo purposes)
            tokens_used = len(generated_content.split()) * 1.3  # Rough estimate
            cost = tokens_used * 0.000002  # GPT-3.5-turbo rate
            
            # Step 2: Save to database for future learning
            self.db.add_example(
                content_type=content_type,
                content=generated_content,
                metadata={
                    "topic": topic,
                    "tone": tone,
                    "target_audience": target_audience,
                    "generated": "true",
                    "model": "gpt-3.5-turbo-demo"
                }
            )
            
            print(f"   ✅ Generated! [DEMO] (Tokens: {int(tokens_used)}, Cost: ${cost:.4f})")
            
            return {
                "success": True,
                "content": generated_content,
                "content_type": content_type,
                "topic": topic,
                "tone": tone,
                "prompt_used": prompt,
                "tokens_used": int(tokens_used),
                "estimated_cost": cost,
                "saved_to_db": True,
                "demo_mode": True
            }
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "content_type": content_type,
                "topic": topic
            }


# Test the generator
if __name__ == "__main__":
    print("🧪 Testing Content Generator [DEMO MODE]...")
    print("=" * 60)
    
    # Initialize (no API key needed!)
    generator = MarketingContentGenerator()
    
    print("\n" + "=" * 60)
    print("TEST: Generate Ad Copy")
    print("=" * 60)
    
    # Test single generation
    result = generator.generate(
        content_type="ad_copy",
        topic="organic coffee subscription",
        tone="warm",
        target_audience="busy professionals",
        key_points=["fresh roasted", "delivered weekly", "sustainable sourcing"]
    )
    
    if result["success"]:
        print("\n📝 GENERATED CONTENT:")
        print("-" * 40)
        print(result["content"])
        print("-" * 40)
        print(f"Tokens used: {result['tokens_used']}")
        print(f"Estimated cost: ${result['estimated_cost']:.4f}")
        print("[DEMO MODE: No actual API call made]")
    else:
        print(f"❌ Error: {result['error']}")
    
    print("\n✅ Test complete! [DEMO MODE]")
    print("\n💡 To use real OpenAI: Add payment method at platform.openai.com")