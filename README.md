# pokemonautomation.github.io

This is the repo to build a Github Pages website for the Pokémon Automation project.
The website hosts introduction to the project, user guide, wiki pages on various automation programs we wrote and so on.

To see the website, go to pokemonautomation.github.io.

The website is made by converting markdown files (.md) to HTML using MkDocs Material. For the md file entry point, check [docs/index.md](docs/index.md).

# How to Develop and Update the Website

## Website Update

If you are part of the developer team and want to push changes to pokemonautomation.github.io, just push your commit to the main branch. A Github Action on this repo runs at every main branch push to build and publish the website.

## Local Website Development

To develop the website locally on your PC, you need to install MkDocs Material
```
pip install mkdocs-material
```

After making changes on the main branch, to view the generated website locally, at the root folder of this repo, run
```
mkdocs serve
```
Then visit http://127.0.0.1:8000 in your browser to see the website.


# How the Website Works

The MkDocs configuration is at [mkdocs.yml](mkdocs.yml).

When the Github Action defined at [.github/workflows/deploy-mkdocs.yml](.github/workflows/deploy-mkdocs.yml) is triggered after a main branch push, it installs mkdocs-material and calls
```
mkdocs gh-deploy --force
```
This MkDocs command builds the website from md files and pushes the generated HTML files to a Git branch called gh-deploy.

This repo is setup on Github to load its gh-deploy branch as the Github Pages.

This repo must be named as `<organization_name>.github.io` in order for its Github Pages to be hosted at link `<organization_name>.github.io`. Since this project's organization name on Github is "PokemonAutomation", we have the repo name and Github Pages link as we know them.
