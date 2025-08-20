import global_ai_credential
from vertexai.generative_models import GenerativeModel, Part

import markdown
import webbrowser
import base64

# ---------- 1. Call the model ----------
model = GenerativeModel("gemini-2.5-flash")

# gcs image used as input for the model
image_file = Part.from_uri("gs://vertexai2025/images/fruits.png", "image/png")
res = model.generate_content([image_file, "List all fruits inside image"])
result_text = res.text

# ---------- 2. Read local image and convert to base64 ----------
# NOTE: change the path below to the actual location in your environment
local_image_path = "fruits.png"

with open(local_image_path, "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

# Build the <img> tag with data URI
img_html_tag = f'<img src="data:image/png;base64,{encoded_image}" style="max-width:100%;height:auto;margin-bottom:20px;">'

# ---------- 3. Render HTML ----------
custom_css = """
<style>
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        line-height: 1.6;
        padding: 20px;
        background-color: #f9f9f9;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    p {
        margin: 0 0 1em;
    }
    a {
        color: #2980b9;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    ul {
        list-style-type: disc;
        margin-left: 20px;
    }
    hr {
        border: 0;
        border-top: 1px solid #ecf0f1;
        margin: 20px 0;
    }
</style>
"""

def display_with_embedded_image(markdown_text, image_tag_html):
    html_output = markdown.markdown(markdown_text)
    full_html = f"""<!DOCTYPE html>
<html>
<head>
{custom_css}
</head>
<body>
{image_tag_html}
{html_output}
</body>
</html>"""

    file_path = "output.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    webbrowser.open(file_path)

markdown_text = f"# Fruits Detected\n\n{result_text}"
display_with_embedded_image(markdown_text, img_html_tag)

