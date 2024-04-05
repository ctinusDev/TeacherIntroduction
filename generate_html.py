import os
import shutil
import subprocess

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
                    generate_html(file)
    if generated_files:
        print("Moving generated HTML files to the repository...")
        for file in generated_files:
            shutil.move(file, os.path.join(os.path.dirname(__file__), file))
            print(f"HTML file moved: {file}")
        print("Adding and committing generated HTML files to the repository...")
        subprocess.run(["git", "add", "*.html"])
        subprocess.run(["git", "commit", "-m", "Add generated HTML files"])
        print("HTML files added and committed.")

if __name__ == "__main__":
    main()
