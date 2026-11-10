import os
import html

SITES_DIR = "sites"
INDEX_PATH = "index.html"

def main():
    sites = []
    if os.path.exists(SITES_DIR):
        for entry in sorted(os.listdir(SITES_DIR)):
            full_path = os.path.join(SITES_DIR, entry)
            if os.path.isdir(full_path):
                sites.append(entry)

    items_html = ""
    if not sites:
        items_html = "<p>No site previews available yet.</p>"
    else:
        items_html = '<ul class="site-list">\n'
        for site in sites:
            display_name = site.replace('-', ' ').replace('_', ' ').title()
            items_html += f'''        <li class="site-item">
            <span>{html.escape(display_name)}</span>
            <a href="./sites/{html.escape(site)}/">View Preview &rarr;</a>
        </li>\n'''
        items_html += '    </ul>'

    page_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Preview Static - Site Directory</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            background-color: #f4f5f7;
            color: #333;
        }}
        h1 {{ color: #0066cc; }}
        .site-list {{
            list-style: none;
            padding: 0;
        }}
        .site-item {{
            background: white;
            margin-bottom: 10px;
            padding: 15px 20px;
            border-radius: 6px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        a {{
            color: #0066cc;
            text-decoration: none;
            font-weight: 600;
        }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Preview Static Directory</h1>
    <p>Available static site previews:</p>
    {items_html}
</body>
</html>
"""

    with open(INDEX_PATH, "w") as f:
        f.write(page_content)
    print(f"Generated {INDEX_PATH} with {len(sites)} sites.")

if __name__ == "__main__":
    main()
