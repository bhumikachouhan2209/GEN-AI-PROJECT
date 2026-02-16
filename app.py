"""
Streamlit Web Application
This creates a beautiful, interactive website for our tool.
"""

import streamlit as st
from content_generator import MarketingContentGenerator
import time

# Page configuration (makes it look professional)
st.set_page_config(
    page_title="✨ Marketing Magic Generator",
    page_icon="✨",
    layout="wide",  # Wide layout for more space
    initial_sidebar_state="expanded"
)

# Custom CSS to make it look amazing
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        background-color: #d4edda;
        border-left: 6px solid #28a745;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .info-box {
        background-color: #d1ecf1;
        border-left: 6px solid #17a2b8;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        height: 3rem;
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 0.5rem;
    }
    .variation-box {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state (remembers things between clicks)
if 'generator' not in st.session_state:
    st.session_state.generator = None
if 'last_result' not in st.session_state:
    st.session_state.last_result = None
if 'history' not in st.session_state:
    st.session_state.history = []

# Header
st.markdown('<p class="main-header">✨ Marketing Magic Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Transform your ideas into professional marketing copy with AI</p>', unsafe_allow_html=True)

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Content type selection with icons
    content_types = {
        "ad_copy": "📢 Ad Copy",
        "email_campaigns": "📧 Email Campaign",
        "social_media": "📱 Social Media Post",
        "blog_posts": "📝 Blog Post",
        "product_descriptions": "🛍️ Product Description"
    }
    
    selected_type = st.selectbox(
        "What do you want to create?",
        options=list(content_types.keys()),
        format_func=lambda x: content_types[x]
    )
    
    # Tone selection
    tone_options = [
        "professional", "friendly", "luxurious", "urgent", 
        "playful", "inspirational", "authoritative", "empathetic"
    ]
    tone = st.select_slider("Tone of Voice", options=tone_options, value="professional")
    
    # Target audience
    target_audience = st.text_input(
        "Target Audience",
        placeholder="e.g., busy moms, tech startups, fitness enthusiasts",
        help="Be specific! Instead of 'everyone', try '25-35 year old yoga enthusiasts'"
    )
    
    # Advanced options
    with st.expander("🔧 Advanced Options"):
        brand_voice = st.text_area(
            "Brand Voice Guidelines (Optional)",
            placeholder="e.g., We never use exclamation marks. We prefer short sentences.",
            help="Specific rules for your brand"
        )
        
        creativity = st.slider(
            "Creativity Level",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            help="0 = strict and predictable, 1 = wild and creative"
        )

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🎯 Your Project")
    
    # Topic input
    topic = st.text_area(
        "What is this content about?",
        placeholder="Describe your product, service, or idea in detail...\n\nExample: A sustainable water bottle made from recycled ocean plastic. Keeps drinks cold for 24 hours. Comes in 5 colors. $35 price point.",
        height=120
    )
    
    # Key points
    key_points_str = st.text_input(
        "Key Points to Include (comma separated)",
        placeholder="sustainability, durability, keeps cold 24hrs, ocean plastic",
        help="What are the main benefits or features?"
    )

with col2:
    st.subheader("💡 Pro Tips")
    
    tips = {
        "ad_copy": """
        **Ad Copy Best Practices:**
        • Lead with the benefit
        • Use power words: Discover, Proven, Exclusive
        • Include numbers when possible
        • End with clear CTA
        """,
        "email_campaigns": """
        **Email Best Practices:**
        • Subject under 50 characters
        • One message per email
        • Personalize the greeting
        • Mobile-friendly formatting
        """,
        "social_media": """
        **Social Media Tips:**
        • Hook in first 3 words
        • Use 2-3 emojis max
        • Ask questions to engage
        • 3-5 relevant hashtags
        """,
        "blog_posts": """
        **Blog Post Structure:**
        • Catchy headline with number
        • Problem in introduction
        • Scannable with headers
        • Actionable conclusion
        """,
        "product_descriptions": """
        **Product Description Formula:**
        • Benefit first, feature second
        • Use sensory words
        • Include social proof
        • Specify who it's for
        """
    }
    
    st.info(tips[selected_type])

# Generate button
st.markdown("---")

if st.button("✨ GENERATE MAGIC CONTENT", type="primary", use_container_width=True):
    
    # Validation
    if not topic or not target_audience:
        st.error("⚠️ Please fill in both the topic and target audience!")
    else:
        # Show progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Step 1: Initialize generator
            status_text.text("🚀 Initializing...")
            progress_bar.progress(10)
            
            if st.session_state.generator is None:
                st.session_state.generator = MarketingContentGenerator()
            
            # Step 2: Parse key points
            status_text.text("📝 Analyzing your requirements...")
            progress_bar.progress(30)
            
            key_points = [p.strip() for p in key_points_str.split(',') if p.strip()]
            if not key_points:
                key_points = ["quality", "value"]
            
            # Step 3: Generate
            status_text.text("🤖 AI is crafting your content...")
            progress_bar.progress(50)
            
            result = st.session_state.generator.generate(
                content_type=selected_type,
                topic=topic,
                tone=tone,
                target_audience=target_audience,
                key_points=key_points,
                brand_voice=brand_voice if brand_voice else None
            )
            
            progress_bar.progress(90)
            status_text.text("✨ Finalizing...")
            
            if result["success"]:
                # Save to history
                st.session_state.last_result = result
                st.session_state.history.append({
                    "type": selected_type,
                    "topic": topic,
                    "preview": result["content"][:100] + "..."
                })
                
                progress_bar.progress(100)
                status_text.empty()
                progress_bar.empty()
                
                # Display success
                st.success("✅ Content generated successfully!")
                
                # Display the content in a nice box
                st.markdown("---")
                st.subheader("📝 Your Generated Content")
                
                # Copy button
                st.code(result["content"], language="markdown")
                
                # Action buttons
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    if st.button("📋 Copy to Clipboard", use_container_width=True):
                        st.write("Copied! (Use Ctrl+C on the text above)")
                
                with col_b:
                    if st.download_button(
                        label="💾 Download as TXT",
                        data=result["content"],
                        file_name=f"{selected_type}_{topic[:20]}.txt",
                        mime="text/plain",
                        use_container_width=True
                    ):
                        pass
                
                with col_c:
                    if st.button("🔄 Generate Again", use_container_width=True):
                        st.experimental_rerun()
                
                # Stats
                st.caption(f"Tokens used: {result['tokens_used']} | Cost: ${result['estimated_cost']:.4f} | Model: GPT-4")
                
                # Show the prompt (for learning)
                with st.expander("🔍 See the Prompt Engineering Magic (Advanced)"):
                    st.text_area("Full Prompt Sent to AI", result["prompt_used"], height=400)
            else:
                progress_bar.empty()
                status_text.empty()
                st.error(f"❌ Generation failed: {result['error']}")
                
        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.error(f"❌ An error occurred: {str(e)}")
            st.exception(e)

# History section
if st.session_state.history:
    st.markdown("---")
    st.subheader("📚 Recent Generations")
    
    for idx, item in enumerate(reversed(st.session_state.history[-5:]), 1):
        with st.expander(f"{idx}. {content_types[item['type']]} - {item['topic'][:30]}..."):
            st.write(item["preview"])

# Footer
st.markdown("---")
st.caption("""
Built with ❤️ using Python, ChromaDB, OpenAI, and Streamlit | 
Memory: Vector Database | Brain: GPT-4 | Heart: Prompt Engineering
""")