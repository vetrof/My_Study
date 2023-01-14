# File Extensions to media types
# happy.jpg - image/jpeg
# document.pdf - application/pdf
usr_input = input('File name: ').strip().lower()

if '.gif' in usr_input:
    print('image/gif')
elif '.jpg' in usr_input:
    print('image/jpeg')
elif '.jpeg' in usr_input:
    print('image/jpeg')
elif '.png' in usr_input:
    print('image/png')
elif '.pdf' in usr_input:
    print('application/pdf')
elif '.txt' in usr_input:
    print('text/plain')
elif '.zip' in usr_input:
    print('application/zip')
else: print('application/octet-stream')