#!/usr/bin/env python

import sys

title = 'Hatem Nassrat - Resume'

def myprint(s):
    ''' Print the string s to stdout '''
    sys.stdout.write(s)

state = 0
tecli = []
words = []
for line in sys.stdin:
    if '<title>' in line:
        myprint('''
        <style type="text/css">
        body {width: 700px; margin: 0 auto;}
        div.textsection { margin-left: 2em; }
        td.tech { vertical-align: top; }
        td.techval { padding-left: 1em; }
        nobr { white-space: nowrap; margin-left: 0.5em; }
        </style>
        ''')
        myprint('<title>%s</title>\n' %title)
    else:
        if state == 2 and ('tth_sEc' in line or 'File translated from' in line):
            myprint('<!-- END of SECTION --> </div>\n')
        if 'Technologies:' in line:
            tecli.append(
                '<table><tr><td class="tech"><b>Technologies:</b></td>' \
                '<td class=techval>'
            )
        elif tecli:
            if '</li>' in line:
                tecli.append('</td>')
                myprint('\n'.join(tecli))
                tecli = []
            else:
                if line[:4] != '<div':
                    if words:
                        words[-1] = ''.join([words[-1][:-1], line.strip()])
                    else:
                        words = filter( lambda x: x != ',', [
                            '%s,' % w.strip() if '.' not in w else w.strip()
                            for w in line.replace('&nbsp;',' ').split(',')
                        ])
                    if not line.endswith('</font\n'):
                        tecli.append('<nobr>%s</nobr>' %('</nobr><nobr>'.join(
                            words
                        )))
                        words = []

        elif not tecli:
            myprint(line) #.replace('<br />',''))
        if 'tth_sEc' in line:
            state=1
        elif state == 1 and '</h2>' in line:
            myprint('<div class="textsection">\n')
            state = 2
