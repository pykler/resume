#!/usr/bin/env python

import sys
from optparse import OptionParser

usage = "usage: %prog [options] <infile.html >outfile.html"

parser = OptionParser(usage=usage)
parser.add_option(
    "-B", "--big", action="store_true", dest="big", default=False,
    help="Write out big legible html"
)
parser.add_option(
    "-p", "--public", action="store_true", dest="public", default=False,
    help="Remove address and phone, add email as link"
)
(options, args) = parser.parse_args()


title = 'Hatem Nassrat - Resume'
body_css = '''
        body {
            margin: 0 auto; %s
        } '''
if options.big:
    body_css = body_css % '''
            width: 768px;
            font-family:sans-serif;'''
else:
    body_css = body_css % '''
            width: 90%;
            font-family:sans-serif;
            font-size:60%;'''

main_css = '''
    <style type="text/css"> 
        %s
        div.textsection { margin-left: 2em; }
        td.tech { vertical-align: top; }
        td.techval { padding-left: 1em; }
        span.nowrap { white-space: nowrap; margin-left: 0.5em; }
        .flr { float: right; }
        li.nobul { list-style: none; margin-left: -1.3em; }
        ul { text-indent: -1.1em; list-style-position: inside; }
        .w3clinks { border:0;height:25px; }
        a { color: #336699; text-decoration: none; }
        a:hover { text-decoration: underline; }

        /* Menu CSS */
        .vert_menu { 
            list-style: none;
            text-indent: 0; 
            position: fixed; top: 1em; right: 1em;
            opacity:.40;filter:alpha(opacity=40);-moz-opacity:0.4;
        }
        .vert_menu li a {
            font-size: 10pt;
            display: block;
            border: 1px dotted #336699;
            padding: 5px 0px 2px 4px;
            text-decoration: none;
            text-align:center;
            color: #666666;
            width:178px;
        }
        .vert_menu li a:hover, .vert_menu li a:focus {
            color: #000000;
            font-weight:bold;
            letter-spacing:1px;
        }
    </style> ''' % body_css

valid_links = '''<div class="flr">
    <a href="http://jigsaw.w3.org/css-validator/check">
        <img class="w3clinks"
            src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
    <a href="http://validator.w3.org/check?uri=referer">
        <img class="w3clinks"
            src="http://www.w3.org/Icons/valid-xhtml10-blue"
            alt="Valid XHTML 1.0 Transitional" />
    </a>
</div>'''

def myprint(*args):
    ''' Print the string s to stdout '''
    for s in args:
        sys.stdout.write(s)

state = 0
tecli = []
words = []
cwords = []
cskills = [[]]
sections = [('', 'Back to the Top')]
dtd = False
section_id = section_title = None
for line in sys.stdin:
    if not dtd and line.strip().startswith('"DTD/'):
        dtd = True
        myprint('   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')
    elif '<body>' in line:
        myprint('<body>', '<h1 align="center">')
        if options.public:
            myprint('''<script type="text/javascript">
                <!--
                var s="=b!isfg>#nbjmup;iobttsbuAhnbjm/dpn#?Ibufn!Obttsbu=0b?";
                m=""; for (i=0; i<s.length; i++) m+=String.fromCharCode(s.charCodeAt(i)-1); document.write(m);
                //-->
                </script>
                <ins><noscript>
                <a href="#Enable JS for contact info" title="Enable JavaScript to see my email">Hatem Nassrat</a>
                </noscript></ins>''')
        else:
            myprint('<a href="mailto:hnassrat@gmail.com">Hatem Nassrat</a>')
        myprint('</h1>')
    elif options.public and line.strip().startswith('<h3') and (
        'B3K' in line or '(902)' in line or 'hnassrat@' in line):
        pass
    elif '<title>' in line:
        myprint(main_css)
        myprint('<title>%s</title>\n' %title)
        myprint('<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />\n')
    else:
        if state == 2 and ('tth_sEc' in line or 'File translated from' in line):
            myprint('<!-- END of SECTION --> </div>\n')
        if 'Technologies:' in line:
            tecli.append(
                '<li class="nobul"><table><tr><td class="tech"><b>Technologies:</b></td>' \
                '<td class="techval">'
            )
        elif tecli:
            if '</li>' in line:
                tecli.append('</td></tr></table></li>')
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
                            '<span class="nowrap">%s</span>' %('</span><span class="nowrap">'.join(words))
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
                    '<span class="nowrap">%s</span>' %('</span><span class="nowrap">'.join(cwords))
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
        # Work and Education Dates
        elif '<i>' in line and '200' in line: #200X watch out in 2010+ (bugs)
            ind = line.index('</i>')+4
            l1, l2 = '%s <br />' %(line[:ind]), line[ind:].replace('<br />', '')
            myprint('<span class="flr">%s</span>\n' %(l2), l1)
        elif '</h2>' in line:
            myprint(line[1:].replace('<br />', ''))
            # Get section title
            section_title = \
                line.split(';')[2].split('</h2')[0].replace('<br />','').strip()
            print >>sys.stderr, section_title, line
            sections.append((section_id, section_title))
        elif not tecli:
            if '</body>' in line:
                myprint(valid_links)
                myprint('<ul class="vert_menu">\n%s\n</ul>' %'\n'.join([
                        '<li><a href="#%s">%s</a></li>' %x for x in sections]))
            myprint(line)
        if 'tth_sEc' in line:
            state=1
            # Get section id
            section_id = line.split('"')[1].strip()
        elif state == 1 and '</h2>' in line:
            myprint('<div class="textsection">\n')
            state = 2
