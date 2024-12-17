import os

title = "The-Beginning-After-The-End"

md_files = [f for f in os.listdir("chapters") if f.endswith(".md")]

md_files.sort(key=lambda x: int(x.split(".")[0]))

pandoc_command = (
    f"cd chapters && pandoc -o ../epubs/{title}.epub ./info/metadata.txt "
    + " ".join(md_files)
)

with open("create_epub.bat", "w") as bat_file:
    bat_file.write(pandoc_command)


print("O arquivo 'create_epub.bat' foi criado.")
