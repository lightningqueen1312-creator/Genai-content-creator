def build_prompt(content_type, audience, tone, product, keywords):

    return f"""
You are a professional marketing expert and business content writer.

Write a detailed {content_type}.

Target Audience:
{audience}

Writing Tone:
{tone}

Product/Service:
{product}

SEO Keywords:
{keywords}

Requirements:

- Generate approximately 1000-1200 words.
- Create a catchy and professional title.
- Write a detailed introduction.
- Explain the industry background.
- Discuss current business challenges.
- Explain why customers need this product.
- Describe at least 7 major features.
- Explain each feature in detail.
- Describe at least 7 business benefits.
- Include real-world examples.
- Explain future trends.
- Include best practices.
- Add a detailed conclusion.
- Finish with a strong Call-to-Action.

Return only the article.
"""