from babel.messages import mofile
import os
path = os.path.join('D:/Gestion-temps-paramedical/translations', 'ar_DZ', 'LC_MESSAGES', 'messages.mo')
with open(path, 'rb') as f:
    catalog = mofile.read_mo(f)
    print(catalog)
    for msg in catalog:
        print(msg.id, msg.string)