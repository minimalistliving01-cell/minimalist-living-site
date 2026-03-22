import os
from datetime import date

# load keywords
with open("keywords.txt") as f:
    keywords = [k.strip() for k in f.readlines()]

# load template
with open("templates/article_template.html") as f:
    template = f.read()

def create_article(keyword):

    title = keyword.title()

    intro = f"{title} inspiration for modern homes. Discover simple, beautiful ideas designed for minimalist spaces."

    content = ""

    for i in range(1,11):

        content += f"""
        <h2>Idea {i}</h2>

        <img src="../images/{keyword.replace(' ','-')}-{i}.jpg">

        <p>Modern {keyword} inspiration designed for functionality and comfort. Focus on clean layouts, neutral colors and timeless decor.</p>
        """

    html = template.replace("{{TITLE}}", title)
    html = html.replace("{{INTRO}}", intro)
    html = html.replace("{{CONTENT}}", content)
    html = html.replace("{{DESCRIPTION}}", f"{title} ideas for modern minimalist homes.")

    filename = keyword.replace(" ","-") + ".html"

    with open(f"output/{filename}","w") as f:
        f.write(html)

for keyword in keywords:
    create_article(keyword)

print("articles generated")
