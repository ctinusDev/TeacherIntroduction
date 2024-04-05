import os
import shutil

def generate_html(filename):
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Full Screen Video</title>
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
        }}

        video {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}
    </style>
</head>
<body>
    <video controls autoplay>
        <source src="{filename}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</body>
</html>"""
    html_filename = f"{filename[:-4]}.html"
    with open(html_filename, "w") as html_file:
        html_file.write(html_content)
    return html_filename

def main():
    generated_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".mp4"):
                html_filename = f"{file[:-4]}.html"
                if not os.path.exists(html_filename):
                    generated_files.append(html_filename)
                    print(f"Generating HTML file for {file}...")
                    generated_html = generate_html(file)
                    print(f"HTML file generated: {generated_html}")
    if generated_files:
        print("Moving generated HTML files to the repository...")
        for file in generated_files:
            shutil.move(file, os.path.join(os.path.dirname(__file__), file))
            print(f"HTML file moved: {file}")

if __name__ == "__main__":
    main()
