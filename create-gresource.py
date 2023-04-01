import os, glob

with open("theme.gresource.xml", "w") as gres:
    gres.write('<?xml version="1.0" encoding="UTF-8"?>')
    gres.write('<gresources>')
    gres.write('<gresource prefix="/me/workingrobot/l4/themes/sweet-dark/">')
    for file in glob.glob('assets/*'):
        file = file.replace('\\','/')
        if file.endswith('.svg'):
            gres.write(f'<file compressed="true" preprocess="xml-stripblanks">{file}</file>')
        elif file.endswith('.png'):
            gres.write(f'<file>{file}</file>')
        else:
            gres.write(f'<file compressed="true">{file}</file>')
    for file in glob.glob('gtk-4.0/*.css'):
        file = file.replace('\\','/')
        gres.write(f'<file compressed="true">{file}</file>')
    gres.write('</gresource>')
    gres.write('</gresources>')

os.system(f"glib-compile-resources --sourcedir . --target Sweet-Dark.gresource theme.gresource.xml")