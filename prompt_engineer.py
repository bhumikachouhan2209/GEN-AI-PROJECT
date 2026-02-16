"""
Prompt Engineering Engine
This creates perfect instructions for the AI using advanced techniques.
"""

from datetime import datetime

class PromptEngineer:
    """
    This class is like a master chef writing recipes.
    It knows exactly how to instruct the AI to get the best results.
    """
    
    def __init__(self, database):
        """
        Connect to our memory box so we can include examples.
        """
        self.db = database
        
        # Define style rules for each content type
        # These are industry best practices for marketing
        self.style_guides = {
            "ad_copy": {
                "name": "Advertisement Copy",
                "rules": [
                    "Maximum 50 words for the main message",
                    "Use power words: Discover, Exclusive, Proven, Instant, Guaranteed",
                    "Include emotional trigger (fear, joy, FOMO, aspiration)",
                    "End with clear call-to-action (CTA)",
                    "Benefit-focused, not feature-focused",
                    "Use numbers when possible (increases trust)"
                ],
                "format": """HEADLINE (7 words max):
[Attention-grabbing hook]

BODY (2-3 sentences):
[Benefit statement with power words]

CTA BUTTON TEXT:
[Action verb] [Benefit]""",
                "examples_needed": 2
            },
            
            "email_campaigns": {
                "name": "Email Marketing Campaign",
                "rules": [
                    "Subject line under 50 characters (mobile-friendly)",
                    "Personalized greeting with [Name] placeholder",
                    "One clear message per email (don't confuse)",
                    "Single, prominent call-to-action button",
                    "Scannable with short paragraphs and bullet points",
                    "P.S. line for urgency or bonus"
                ],
                "format": """SUBJECT LINE:
[Curiosity or benefit driven]

PREVIEW TEXT:
[Supporting subject line]

BODY:
Hi [Name],

[Opening hook - relate to their problem]

[Solution presentation]

[Social proof or benefit]

[CTA Button]

Best,
[Your Name]

P.S. [Urgency or bonus]""",
                "examples_needed": 2
            },
            
            "social_media": {
                "name": "Social Media Post",
                "rules": [
                    "Hook in first 3 words (stop the scroll)",
                    "Use 2-3 emojis strategically (not randomly)",
                    "Include 3-5 relevant hashtags",
                    "Ask a question to drive engagement",
                    "Keep under 150 words for optimal engagement",
                    "Include visual description if needed"
                ],
                "format": """[HOOK - stop the scroll]

[Body text with emoji]

[Engagement question]

[Hashtags]""",
                "examples_needed": 2
            },
            
            "blog_posts": {
                "name": "Blog Article",
                "rules": [
                    "Catchy H1 headline with number or power word",
                    "Introduction with problem statement (relatable)",
                    "3-5 H2 subheadings for scannability",
                    "Include actionable tips, not just theory",
                    "Conclusion with key takeaways",
                    "End with engagement question"
                ],
                "format": """# [Number] [Power Word] Ways to [Benefit]

## Introduction
[Hook with problem statement]
[Why this matters]
[What they'll learn]

## 1. [First Tip]
[Explanation with example]

## 2. [Second Tip]
[Explanation with example]

## Conclusion
[Summary of key points]
[Call to action]

[Engagement question]""",
                "examples_needed": 2
            },
            
            "product_descriptions": {
                "name": "Product Description",
                "rules": [
                    "Lead with benefit, not feature (so what?)",
                    "Use sensory words (imagine, feel, experience)",
                    "Include social proof if possible",
                    "Specify exactly who it's for",
                    "Address objections subtly",
                    "Make the CTA low-risk"
                ],
                "format": """[Benefit statement - the dream]

[Feature] → [Benefit]
[Feature] → [Benefit]
[Feature] → [Benefit]

[Social proof]

Perfect for: [Specific persona]

[Low-risk CTA]""",
                "examples_needed": 2
            }
        }
    
    def create_prompt(self, content_type, topic, tone, target_audience, key_points, brand_voice=None):
        """
        Create the perfect prompt using Few-Shot technique.
        
        Few-Shot Prompting means showing examples so the AI learns the pattern.
        Like showing a child 2-3 examples of a cat before asking them to draw one.
        """
        
        # Step 1: Get the style guide for this content type
        style = self.style_guides.get(content_type, {})
        if not style:
            return f"Write {content_type} about {topic}"  # Fallback
        
        # Step 2: Fetch similar examples from our database
        similar_examples = self.db.find_similar_examples(
            content_type=content_type,
            topic=topic,
            tone=tone,
            target_audience=target_audience,
            n_results=style.get("examples_needed", 2)
        )
        
        # Step 3: Build the prompt piece by piece
        
        # === IDENTITY SECTION ===
        prompt = f"""You are an elite marketing copywriter with 20 years of experience.
You've written for Fortune 500 companies and won multiple advertising awards.
Your copy converts readers into customers. You write in a {tone} tone.

TASK: Create {style['name']} about {topic}

TARGET AUDIENCE: {target_audience}
TONE: {tone}
KEY POINTS TO EMPHASIZE: {', '.join(key_points)}
"""
        
        # Add brand voice if provided
        if brand_voice:
            prompt += f"\nBRAND VOICE GUIDELINES: {brand_voice}\n"
        
        # === STYLE RULES SECTION ===
        prompt += f"\nSTRICT RULES YOU MUST FOLLOW:\n"
        for i, rule in enumerate(style['rules'], 1):
            prompt += f"{i}. {rule}\n"
        
        # === FEW-SHOT EXAMPLES SECTION ===
        if similar_examples:
            prompt += f"\n{'='*60}\n"
            prompt += "EXAMPLES OF EXCELLENT WORK (Study these patterns):\n"
            prompt += f"{'='*60}\n"
            
            for idx, example in enumerate(similar_examples, 1):
                prompt += f"\n--- EXAMPLE {idx} ---\n"
                prompt += f"{example}\n"
            
            prompt += f"\n{'='*60}\n"
            prompt += "NOTICE THE PATTERNS ABOVE. NOW CREATE SOMETHING ORIGINAL.\n"
            prompt += f"{'='*60}\n"
        
        # === OUTPUT FORMAT SECTION ===
        prompt += f"\nOUTPUT FORMAT (Follow this exactly):\n"
        prompt += style['format']
        
        # === FINAL INSTRUCTIONS ===
        prompt += f"""

ADDITIONAL INSTRUCTIONS:
• Be original - do not copy the examples word for word
• Focus on benefits, not just features
• Make it sound human, not robotic
• Ensure every word earns its place
• The content should feel {tone}

Now create the {style['name']} for: {topic}

YOUR RESPONSE:"""
        
        return prompt


# Test the prompt engineer
if __name__ == "__main__":
    print("🧪 Testing Prompt Engineer...")
    
    # Import database
    from database import MarketingDatabase
    
    # Create database
    db = MarketingDatabase()
    
    # Create engineer
    engineer = PromptEngineer(db)
    
    # Test prompt creation
    test_prompt = engineer.create_prompt(
        content_type="ad_copy",
        topic="vegan protein powder",
        tone="energetic",
        target_audience="fitness enthusiasts",
        key_points=["plant-based", "20g protein", "tastes great"]
    )
    
    print("\n" + "="*60)
    print("GENERATED PROMPT:")
    print("="*60)
    print(test_prompt[:500] + "...")  # Show first 500 characters
    print("="*60)
    print(f"\nPrompt length: {len(test_prompt)} characters")
    print("✅ Prompt Engineer test complete!")