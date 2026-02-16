"""
Marketing Content Database - Simple Version
Uses JSON files instead of ChromaDB (no big downloads!)
"""

import json
import os
from datetime import datetime

class MarketingDatabase:
    """
    Simple file-based database that works immediately!
    No downloads, no waiting, no problems.
    """
    
    def __init__(self):
        print("📦 Opening the memory box...")
        self.data_file = "marketing_data.json"
        self.examples = self._load_examples()
        print("✅ Memory box ready!")
    
    def _load_examples(self):
        """Load examples from file or create default ones"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        
        # Default examples - these are our "memory"
        examples = {
            "ad_copy": [
                {
                    "topic": "running shoes",
                    "content": "🏃‍♂️ Run Faster, Feel Lighter. Our cloud-foam technology makes every step feel like flying. 30-day comfort guarantee or your money back!",
                    "tone": "energetic",
                    "target_audience": "athletes"
                },
                {
                    "topic": "coffee subscription",
                    "content": "☕ Fresh beans delivered before you wake up. Ethically sourced from local farmers. Roasted to order. Your perfect morning starts here. First bag free!",
                    "tone": "warm",
                    "target_audience": "coffee lovers"
                },
                {
                    "topic": "accounting software",
                    "content": "Cut your bookkeeping time by 70%. Automated invoicing, expense tracking, and tax reports. Trusted by 50,000+ small businesses. Start free trial today.",
                    "tone": "professional",
                    "target_audience": "small business owners"
                }
            ],
            "email_campaigns": [
                {
                    "topic": "product launch",
                    "content": """Subject: It's here (and selling out fast!)

Hey [Name],

Remember when you said you wished [problem]?

After 18 months of development, the ProX is finally here. It does exactly what you asked for—and more.

Early access members get 20% off for the next 48 hours only.

[Claim Your Discount]

Cheers,
The Team

P.S. Only 100 units available at this price.""",
                    "tone": "excited",
                    "target_audience": "existing customers"
                }
            ],
            "social_media": [
                {
                    "topic": "fitness app",
                    "content": """Transform your commute into a workout 🚴‍♀️

5-minute exercises you can do anywhere:
• On the bus
• In your office
• While watching TV

No equipment needed. No excuses.

What's your biggest barrier to working out? 👇

#Fitness #QuickWorkout #HealthyLife #NoExcuses""",
                    "tone": "motivational",
                    "target_audience": "busy professionals"
                }
            ],
            "blog_posts": [
                {
                    "topic": "productivity tips",
                    "content": """# 5 Productivity Hacks That Actually Work

## Introduction
We all have the same 24 hours. Why do some people get 10x more done? It's not about working harder—it's about working smarter.

## 1. The 2-Minute Rule
If something takes less than 2 minutes, do it now. Don't add it to a list.

## 2. Time Blocking
Schedule every minute of your day. Yes, including breaks.

## 3. Eliminate Decision Fatigue
Steve Jobs wore the same outfit daily. Reduce trivial choices.

## Conclusion
Pick ONE hack to implement this week. Master it before adding others.

What's your favorite productivity tip? Share below!""",
                    "tone": "helpful",
                    "target_audience": "professionals"
                }
            ],
            "product_descriptions": [
                {
                    "topic": "wireless headphones",
                    "content": """Experience silence like never before. 

Active noise cancellation blocks 95% of ambient sound—perfect for focus at work or peace on your commute.

40-hour battery life means you charge once a week, not daily.

Memory foam ear cups mold to your ears for all-day comfort.

⭐⭐⭐⭐⭐ "Best headphones under $200" - TechReview

Perfect for: Commuters, remote workers, audiophiles who value comfort.""",
                    "tone": "luxurious",
                    "target_audience": "tech enthusiasts"
                }
            ]
        }
        
        self._save_examples(examples)
        return examples
    
    def _save_examples(self, examples):
        """Save examples to file"""
        with open(self.data_file, 'w') as f:
            json.dump(examples, f, indent=2)
    
    def find_similar_examples(self, content_type, topic, tone=None, target_audience=None, n_results=3):
        """Find examples by type - returns matching content"""
        type_examples = self.examples.get(content_type, [])
        if not type_examples:
            return []
        
        # Return first n examples of this type
        return [ex["content"] for ex in type_examples[:n_results]]
    
    def add_example(self, content_type, content, metadata):
        """Add new example to our memory"""
        if content_type not in self.examples:
            self.examples[content_type] = []
        
        self.examples[content_type].append({
            "content": content,
            **metadata
        })
        self._save_examples(self.examples)
        print(f"✅ Added new example to {content_type}")
        return True
    
    def get_stats(self):
        """Show how many examples in each category"""
        return {k: len(v) for k, v in self.examples.items()}


# Test the database
if __name__ == "__main__":
    print("🧪 Testing the database...")
    db = MarketingDatabase()
    
    print("\n📊 Database Stats:")
    stats = db.get_stats()
    for name, count in stats.items():
        print(f"  {name}: {count} examples")
    
    print("\n🔍 Testing search for 'sports shoes':")
    results = db.find_similar_examples("ad_copy", "sports shoes", n_results=2)
    for i, result in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(result[:200] + "..." if len(result) > 200 else result)
    
    print("\n✅ Database test complete!")