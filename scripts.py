import os
import csv

# 1. SETTINGS - Change these to match your GitHub
GITHUB_USERNAME = "your-github-username"
REPO_NAME = "your-repo-name"
BASE_URL = f"https://{GITHUB_USERNAME}.github.io/{REPO_NAME}"
AMAZON_ID = "your-tag-20" # Replace with your Amazon Associate ID

# Ensure output folder exists
if not os.path.exists("output"):
    os.makedirs("output")

# 2. LOAD DATA
with open("keywords.txt") as f:
    keywords = [k.strip() for k in f.readlines()]

with open("templates/article_template.html") as f:
    template = f.read()

# 3. SETUP PINTEREST CSV
csv_file = open("pinterest_bulk.csv", mode="w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Media URL", "Title", "Description", "Destination Link"])

def create_article(keyword):
    title = keyword.title()
    slug = keyword.replace(" ", "-")
    
    # Links for the CSV
    page_url = f"{BASE_URL}/output/{slug}.html"
    # Pinterest needs a direct link to the image you uploaded to GitHub
    main_image_url = f"{BASE_URL}/images/{slug}-1.jpg"

    # Generate the Content Blocks (with Amazon Links)
    intro = f"{title} inspiration for modern homes. Discover simple, beautiful ideas designed for minimalist spaces."
    content = ""
    amazon_search = keyword.replace(" ", "+")
    
    for i in range(1, 11):
        content += f"""
        <div class="item-block">
            <h2>Idea {i}</h2>
            <img src="../images/{slug}-{i}.jpg" alt="{title} inspiration {i}">
            <p>This minimalist {keyword} setup focuses on clean lines and functional beauty.</p>
            <a href="https://www.amazon.com/s?k={amazon_search}&tag={AMAZON_ID}" 
               style="display:inline-block; background:#222; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">
               Shop Similar Styles on Amazon →
            </a>
        </div>
        """

    # Fill the Template
    html = template.replace("{{TITLE}}", title)
    html = html.replace("{{INTRO}}", intro)
    html = html.replace("{{CONTENT}}", content)
    html = html.replace("{{DESCRIPTION}}", f"{title} ideas for modern minimalist homes.")

    # Save the HTML file
    filename = f"{slug}.html"
    with open(f"output/{filename}", "w") as f:
        f.write(html)

    # 4. ADD TO PINTEREST CSV
    # This creates one Pin per Keyword.
    csv_writer.writerow([
        main_image_url, 
        f"10 Genius {title} Ideas", 
        f"Transform your space with these {keyword} tips. See the full gallery of minimalist designs.", 
        page_url
    ])

# RUN THE PROCESS
for keyword in keywords:
    create_article(keyword)

csv_file.close()
print(f"Success! {len(keywords)} articles and pinterest_bulk.csv generated.")
