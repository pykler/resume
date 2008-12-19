#!/usr/bin/env python

import sys

title = 'Hatem Nassrat - Resume'

def myprint(*args):
    ''' Print the string s to stdout '''
    for s in args:
        sys.stdout.write(s)

state = 0
tecli = []
words = []
cwords = []
cskills = [[]]
for line in sys.stdin:
    if '<body>' in line:
        myprint('<body>\n', '<h1 align="center">Hatem Nassrat</h1>\n')
    elif '<title>' in line:
        myprint('''
        <style type="text/css">
        body {width: 700px; margin: 0 auto; font-family:sans-serif;}
        div.textsection { margin-left: 2em; }
        td.tech { vertical-align: top; }
        td.techval { padding-left: 1em; }
        nobr { white-space: nowrap; margin-left: 0.5em; }
        span.flr { float: right; }
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
                        tecli.append(
                            '<nobr>%s</nobr>' %('</nobr><nobr>'.join(words))
                        )
                        words = []

        elif '<i>' in line and ':' in line:
            ind1, ind2 = line.index('<i>')+3, line.index('</i>')
            cskills[-1].append(line[ind1:ind2].replace('&nbsp;','').strip())
        elif len(cskills[-1]) == 1:
            if cwords:
                cwords[-1] = ' '.join([
                    cwords[-1][:-1], line.replace('&nbsp;', '').strip()
                ])
            else:
                cwords = [':'] + filter( lambda x: x != ',', [
                    '%s,' % w.strip() if '.' not in w else w.strip()
                    for w in line.replace('<br />',' ').split(',')
                ])
            # Too specific watch this line for bugs
            if not (
                'Worked on' in cwords[-1] and 'Dalhousie' not in cwords[-1]
            ):
                cskills[-1].append(
                    '<nobr>%s</nobr>' %('</nobr><nobr>'.join(cwords))
                )
                cwords = []
                if len(cskills) == 3:
                    myprint('<table>\n')
                    for s in cskills:
                        myprint('<tr><td class="tech">%s</td>' \
                                '<td class="techval">%s</td></tr>\n' %tuple(s))
                    myprint('</table>\n')
                else:
                    cskills.append([])
        elif '<i>' in line and '200' in line: #200X watch out in 2010+ (bugs)
            ind = line.index('</i>')+4
            l1, l2 = '%s <br />' %(line[:ind]), line[ind:].replace('<br />', '')
            myprint('<span class="flr">%s</span>\n' %(l2), l1)
        elif '</h2>' in line:
            myprint(line[1:].replace('<br />', ''))
        elif not tecli:
            myprint(line) #.replace('<br />',''))
        if 'tth_sEc' in line:
            state=1
        elif state == 1 and '</h2>' in line:
            myprint('<div class="textsection">\n')
            state = 2
