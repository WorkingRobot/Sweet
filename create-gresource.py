import os, glob

THEMES = {
    "Sweet-Ambar": 'ambar',
    "Sweet-Ambar-Blue": 'ambar-blue',
    "Sweet": 'base',
    "Sweet-Mars": 'mars',
    "Sweet-Dark": 'nova',
}

base_dir = os.getcwd()

for theme_name, theme_path in THEMES.items():
    print(f"Processing {theme_name}")
    os.chdir(f'{base_dir}/{theme_path}')

    with open("theme.gresource.xml", "w") as gres:
        gres.write('<?xml version="1.0" encoding="UTF-8"?>')
        gres.write('<gresources>')
        gres.write(f'<gresource prefix="/org/gtk/libgtk/theme/{theme_name}/">')
        for file in glob.glob('assets/*'):
            file = file.replace('\\','/')
            if file.endswith('.svg'):
                gres.write(f'<file compressed="true" preprocess="xml-stripblanks">{file}</file>')
            elif file.endswith('.png'):
                gres.write(f'<file>{file}</file>')
            else:
                gres.write(f'<file compressed="true">{file}</file>')
        for file in glob.glob('*.css'):
            file = file.replace('\\','/')
            gres.write(f'<file compressed="true">{file}</file>')
        gres.write('</gresource>')
        gres.write('</gresources>')

    print(f"Compiling {theme_name}")
    os.system(f"glib-compile-resources --sourcedir . --target {base_dir}/{theme_name}.gresource theme.gresource.xml")

os.chdir(base_dir)