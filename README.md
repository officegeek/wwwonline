# Theme

## Config
The following global setting are located in `config.toml`:
- Site setting: URL, descriptions, logos
- Footer copyright

## Menus
Set menus in `data/menus.yml`:
- Navbar menu
- Footer menu
- Social networks

## Markdown

Upload images to `/static/images/` folder and use `![Company](/images/company.svg)` syntax to add it in content.

Markdown [syntax guide](https://commonmark.org/help/). 

## Installation and Development
**Install**  
`npm install`

**To start developing:**  
`npm run dev`

**To generate the site HTML:**  
`npm run build`

**npm run dev** will run two commands parallel:  
`npx tailwindcss -i ./assets/css/main.css -o ./assets/css/style.css --watch`

and
`hugo server`

Note: When you start first time **npm run dev** a style.css must exist - or you get an error! Just do a **Ctrl+c** and run **npm run dev** - even though you got an error but a style was written anyway and 2nd time round it should start fine.

To get out of developing mode you need to do **Ctrl+c** twice.

### Blocks
New site blocks can be added in `layouts/partials/blocks/` directory.
