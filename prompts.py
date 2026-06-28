def build_prompt(content_type, audience, tone, product, keywords):

    prompt = f"""
You are an expert marketing strategist and professional business content writer.

Generate a high-quality {content_type}.

Target Audience:
{audience}

Writing Tone:
{tone}

Product or Service:
{product}

SEO Keywords:
{keywords}

Instructions:
1. Create an attractive and professional title.
2. Write a detailed introduction.
3. Explain the industry background.
4. Describe the customer's problem.
5. Explain how the product or service solves the problem.
6. Mention at least 5 key features.
7. Mention at least 5 business benefits.
8. Include real-world business applications.
9. Mention future trends related to the product.
10. Write a strong conclusion.
11. Add a compelling Call-to-Action.
12. Use clear and professional English.
13. Generate approximately 700–900 words.

Return only the final content without any explanations.
"""

    return prompt