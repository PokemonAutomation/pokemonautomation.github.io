# pokemonautomation.github.io

This is the repo to build a Github Pages website for the Pokémon Automation project.
The website hosts introduction to the project, user guide, wiki pages on various automation programs we wrote and so on.

To see the website, go to pokemonautomation.github.io.

The website is made by converting markdown files (.md) to HTML using MkDocs Material. For the md file entry point, check [docs/index.md](docs/index.md).

# How to Develop and Update the Website

## Website Update

If you are part of the developer team and want to push changes to pokemonautomation.github.io, just push your commit to the main branch. A Github Action on this repo runs at every main branch push to build and publish the website.

## Local Website Development

### Required Installation

To develop the website locally on your PC, you need to install MkDocs Material. Also, install the plugin `mkdocs-include-dir-to-nav` to add folders to `nav`.

```
pip install mkdocs-material "mkdocs-material[imaging]"
pip install mkdocs-include-dir-to-nav
pip install mkdocs-static-i18n
```

See this page for more information/troubleshooting tips:

https://squidfunk.github.io/mkdocs-material/plugins/requirements/image-processing/

**Windows**
- Install Cairo Graphics library. install this via MSYS2
    - within MSYS2 terminal:
```
pacman -S mingw-w64-ucrt-x86_64-cairo
```
- add `C:\msys64\ucrt64\bin` to PATH, within "Environmental Variables".

**macOS**
You also need to install some system-wide libraries (we install them via Homebrew):
```
brew install cairo pango gdk-pixbuf libffi
```

and to ensure those libraries can be found by your Python environment (e.g. Anaconda), run following:

```
export DYLD_FALLBACK_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_FALLBACK_LIBRARY_PATH"
```

### Hosting Local Website

After making changes on the main branch, to view the generated website locally, at the root folder of this repo, run

```
mkdocs serve
```

Then visit http://127.0.0.1:8000 in your browser to see the website.

If you are making multiple changes to the md files, you can add --livereload to the command to automatically refresh the website in your browser when you save changes to md files.

```
mkdocs serve --livereload
```


### Building Local Website

You can also run

```
mkdocs build
```

to build the website into a folder `site/`, which is already ignored by .gitignore. The folder includes all the generated webpages, the 404 page `site/404.html` and social preview cards `site/assets/images/social/index.png`.


# How the Website Works

The MkDocs configuration is at [mkdocs.yml](mkdocs.yml).

When the Github Action defined at [.github/workflows/deploy-mkdocs.yml](.github/workflows/deploy-mkdocs.yml) is triggered after a main branch push, it installs mkdocs-material and calls
```
mkdocs gh-deploy --force
```
This MkDocs command builds the website from md files and pushes the generated HTML files to a Git branch called gh-deploy.

This repo is setup on Github to load its gh-deploy branch as the Github Pages.

This repo must be named as `<organization_name>.github.io` in order for its Github Pages to be hosted at link `<organization_name>.github.io`. Since this project's organization name on Github is "PokemonAutomation", we have the repo name and Github Pages link as we know them.

# CAVEATS on Writing MkDocs Compatible Markdown Files

MkDocs parses markdown files (.md files) slightly differently than how Github renders them.

- For non-numbered lists (starting with "-"), numbered lists ("1. ..."), tables ("|...|") and image tags (`<img src=...>`), you need to add an empty line before them for MkDocs to place them at a new line.

- MkDocs won't create a clickable link (e.g. `https://example.link`) on a raw https link. You have to create it by yourself: `[https://example.link](https://example.link)`.

- If you have nested lists inside a list, the nested lists need to have at least four whitespaces of indent for MkDocs to register them as nested lists.

- If you have nested lists or image tags between two lines of a numbered list, add empty lines surrounding the nested items and indent them with four whitespaces. Otherwise the numbers on the outer list will be broken. e.g.:
```
1. Numbered line 1.

    - Nested line 1

    - Nested line 2

    <img src=...>

2. Numbered line 2.
```

- If you have nested coding block (surrounded by three "`"), add empty lines surrounding them and have eight whitespaces to indent them.

- MkDocs defaults all images' max-width to be 100% and height to be "auto" so we shouldn't use image tab attribute "height" in md files to control image sizes. Use width control like `width="500"` or `width="50%"` instead.

### Contributing

Have you written a program and want to share it with the community? Or do you want to improve an existing guide? Please follow the instructions below to add your program to the website!

1. Fork the repository and create a new branch for your program.
2. Create a new markdown file for your program in the appropriate folder under `docs/Programs/`. 
    - You can use [docs/Templates/ProgramTemplate.md](docs/Templates/ProgramTemplate.md) as a template for your program's markdown file.
    - If your program is complex you may want to refer to some of the other complex program guides. [docs/Programs/PokemonLZA/DonutMaker.md](docs/Programs/PokemonLZA/DonutMaker.md) [docs/Programs/PokemonFRLG/RngManipulationGuide.md](docs/Programs/PokemonFRLG/RngManipulationGuide.md)
3. Most guides include images to illustrate the program. These can be added to the `images/` folder under the program's folder.
    - In an attempt to improve load times, we recommend converting the images to jpg format and compressing them before uploading.
    - If you want a detailed photo you can include a large version to be loaded separately `[<img src="images/SmallImage.jpg" width="300">](images/LargeImage.jpg)`
4. If you are adding a new program guide, make sure to add the program to the correct table in [docs/Programs/index.md](docs/Programs/index.md).
5. Once you have added your program's markdown file and any associated images, create a pull request to merge your changes into the main branch.

## Some FAQs
**Q: I added a new doc but it doesn't show up on the nav bar.**

A: If you added a new folder with your doc (e.g. `docs/Programs/PokemonNewGame/MyProgram.md`), make sure to add the folder to `nav` in [mkdocs.yml](mkdocs.yml). mkdocs doesn't automatically add new folders to nav, but it will automatically add new md files within existing folders.
