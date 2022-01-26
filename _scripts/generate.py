"""resport: Research portfolio site generator."""

__version__ = "0.1.2"

import os
import shutil
import glob
import argparse
import datetime
import markdown

css_style_note = 'font-size: 60%; font-weight: bold; margin-left: 2px;'
start_card = '<div class="card" style="border: 1px solid rgba(0,0,0,.125); border-radius: .25rem; padding: 1.1rem; opacity: 1; font-size: smaller">'

# keywords for fields in entries
#
#    'article' : standard bibtex keywords
#    'experience' : ['position', 'period', 'employer',
#                    'location', 'description', 'activity']


def markdown_no_p(text):
    """Wrap around markdown.markdown function."""
    html = markdown.markdown(text, extensions=['markdown.extensions.tables', 'toc'])
    # don't use the trailing paragraphs
    html = html[3:-4]
    return html


def format_basic(key, value, doctype='latex'):
    """Takes a key and generates output.

    According to the value of the key, a latex formated string value is returned.
    """
    if key in ['entryType', 'key']:
        s = ''
    elif key == 'position':
        s = r'\textsc{' + value + '}'
    elif key == 'employer':
        s = r'\small{\textbf{' + value + '}}'
    elif key == 'location' and doctype == 'latex':
        s = r'\small{\textbf{' + value + '}}'
    else:
        s = value
    return s


def read_file(source):
    """Reads a .bib sourcefile and returns a list of entries.

    Each entry consists of a dictionary with different fields. The key of these
    fields describes the type of the field and may not be unique.
    """
    entries = []
    # iterate over lines in source file
    for line in open(source):
        # if a new entry starts
        if line.startswith('@'):
            fields = {}
            fields['entryType'], fields['key'] = line.strip('@ \n,').split('{')
        elif '=' in line:
            key, value = line.split('= {')
            key = key.strip()
            # strip empty space, comma, newline and then avoid
            # the brace "}" using [:-1]
            value = value.strip(' ,\n')[:-1]
            if key not in fields:
                fields[key] = [value]
            else:
                fields[key].append(value)
        # entry is over, append fields to entries
        elif line.startswith('}'):
            entries.append(fields)
    return entries


def format_latex_experience(entry):
    """Format the output of experience.
    """
    # apply basic latex formating
    for key in entry:
        # iterate over the keys that are of type list
        # these are all but key and entryType
        if type(entry[key]) == list:
            for i, value in enumerate(entry[key]):
                entry[key][i] = format_basic(key, value)
    # new line variables
    n = '\n'
    nl = r'\\' + '\n'
    # start assembling
    s = r'\newpage' if 'newpage' in entry else '' + n
    # indent
    leftskip_indent = 0
    if 'indent' in entry:
        leftskip_indent += 1.285
        s += r'\setlength{\leftskip}{'+str(leftskip_indent) + r'em}\vspace{-.2em}' + n
    # vspace
    s += r'\vspace{0em}\noindent'
    # employer
    if 'employer' in entry:
        s += entry['employer'][0]
        if 'location' in entry:
            s += ', ' + entry['location'][0]
        s += r'\\[0.1em]'
    # employer info
    if 'employer_info' in entry:
        s += entry['employer_info'][0] + r'\\[.3em]' + '\n'
    # position and period, go backwards through position and period entries
    for i in range(len(entry['position'])-1, -1, -1):
        s += entry['position'][i]
        if i != 0:
            s += ' (' + entry['period'][i] + ') / '
    if '-' in entry['period'][0]:
        start, end = entry['period'][0].split('-')
        months = int(end.split('.')[0]) - int(start.split('.')[0])
        years = int(end.split('.')[1]) - int(start.split('.')[1])
        if months < 0:
            years -= 1
            months = 12 + months
        months += 1
        if months == 12:
            years += 1
            months = 0
        # assemble string
        duration = ((str(years) if years > 0 else str(100 + years) if years < 0 else '')
                    + (' year ' if years == 1 else ' years ' if (years > 1 or years < 0) else ''))
        if months > 0:
            duration += str(months) + ' month' + ('s' if months > 1 else '')
        duration += ' $\cdot$ '
    else:
        duration = ''
    s += ' \hfill ' + duration + entry['period'][0].replace('.', '/20').replace('-', '--') + n + n
    # description and activities
    if 'description' in entry or 'activity' in entry:
        s += r'{\footnotesize ' + n
        s += r'\vspace{-.6em}\begin{itemize}'
        s += '[leftmargin=' + ('1.5em' if 'indent' not in entry else
                               '{}em'.format(1.8 + leftskip_indent)) + ']'
        s += r'\setlength\itemsep{-.1em}' + n
        s += r'\setstretch{1.1}' + n
        if 'description' in entry:
            s += r'\item[$\bullet$] ' + entry['description'][0] + n
        if 'activity' in entry:
            for activity in entry['activity']:
                s += '\item ' + activity + n
        s += r'\end{itemize}' + n
        s += r'\setstretch{1.2}' + n
        s += r'}' + n + n
    if 'indent' in entry:
        s += r'\setlength{\leftskip}{0em}' + n + n
    return s


def format_pub(entry, doctype='html', ascard=False):
    """Format publications.

    All for html.
    """
    # apply basic html formating
    newentry = {}
    for key in entry:
        # iterate over the keys that are of type list
        # these are all but key and entryType
        if type(entry[key]) == list:
            if len(entry[key]) == 1:
                newentry[key.lower()] = format_basic(key, entry[key][0],
                                                     doctype=doctype)
            else:
                for i, value in enumerate(entry[key]):
                    newentry[key.lower()][i] = format_basic(key, value,
                                                            doctype=doctype)
        else:
            newentry[key] = entry[key]
    entry = newentry
    if doctype == 'html':
        css_style_note = 'font-size: 10px; font-weight: normal; margin-left: 2px;'
        if ascard:
            s = start_card
            css_style_note = 'font-size: 10px; font-weight: normal; margin-left: 2px;'
        elif 'mark' in entry:
            s = '<p>'
            # if entry['mark'] == 'noncentral':  # ignore for now
            #     s = '<p style="opacity: 0.6;">'
        else:
            s = '<p>'
    else:
        s = ''
    # format id
    if doctype == 'html':
        s += '<span id="' + entry['id'] + '" style="font-size: 10px">' + entry['id'] + '</span> '
    else:
        s += '\paperitemdef{' + entry['id'] + '} & '
    # format title
    if doctype == 'html':
        s += ('<span '
    #            +'" style="font-variant: small-caps; font-size: 90%">'
               + ' style="font-weight: bold">'
               + entry['title'] + '</span> <br> ')
    else:
        s += r'\textit{' + entry['title'] + r'}\\' + ' \n & '
    # format author
    if entry['entryType'] != 'otherpub' or 'and' in entry['author']:
        authors = entry['author'].split(' and ')
        if len(authors) == 2:
            if doctype == 'html':
                sep = ' &'
            else:
                sep = ' \&'
        else:
            sep = ','
        for iauthors, author in enumerate(authors):
            names = author.split(' ')
            lennames = len(names) - 1
            # initials
            if 'Wolf' in names or 'Wolf†' in names:
                if doctype == 'html':
                    s += '<u style="font-size: 100%">'
                else:
                    s += r'\underline{'
            for name in names[:-1]:
                s += name[0]
            s += ' ' + names[-1]
            if 'Wolf' in names or 'Wolf†' in names:
                if doctype == 'html':
                    s += '</u>'
                else:
                    s += '}'
            s += (sep + ' ' if iauthors < len(authors)-1 else ' ')
        if doctype == 'html':
            s += ' <br> '
        else:
            s += r'\\ & ' + '\n'
    # format journal, if present
    if 'journal' in entry:
        if 'doi' in entry:
            if doctype == 'html':
                s += ('<a href="https://doi.org/' + entry['doi'] + '">'
                      + entry['journal'] + ' ')
            else:
                s += ('\href{https://doi.org/' + entry['doi'] + '}{'
                      + entry['journal'] + ' ')
        elif 'url' in entry:
            if doctype == 'html':
                s += ('<a href="' + entry['url'] + '">'
                      + entry['journal'] + ' ')
            else:
                s += ('\href{' + entry['url'] + '}{'
                      + entry['journal'] + ' ')
        else:
            s += entry['journal'] + ' '
        # format year
        if doctype == 'html':
            s += '(' + entry['year'] + ')</a> '
        else:
            s += '(' + entry['year'] + ')'
            if 'doi' in entry or 'url' in entry: s += '}'
    if 'note' in entry:
        # format note
        if doctype == 'html':
            note = markdown_no_p(entry["note"])
            s += f' <span style="{css_style_note}">{note}</span> '
    if doctype == 'html':
        # preprints
        if 'eprint' in entry:
            s += (' <a href="http://arxiv.org/abs/'
                  + entry['eprint'] + '" style="{}">arXiv</a> '.format(css_style_note))
        if 'biorxivdoi' in entry:
            s += (' <a href="http://dx.doi.org/'
                  + entry['biorxivdoi'] + '" style="{}">bioRxiv</a> '.format(css_style_note))
        if 'researchgateurl' in entry:
            s += (' <a href="'
                  + entry['researchgateurl'] + '" style="{}">ResearchGate</a> '.format(css_style_note))
        # pdf
        linktopdf = ''
        if 'pdf' in entry:
            linktopdf = entry['pdf']
        elif 'eprint' in entry:
            linktopdf = 'http://arxiv.org/pdf/' + entry['eprint']
        if linktopdf != '':
            s += ' <a href="' + linktopdf + '" style="{}"> pdf </a>'.format(css_style_note)
        # code
        if 'code' in entry:
            code = entry['code']
            s += f' <a href="{code}" style="{css_style_note}">code</a> '
            # if 'github' in entry:
            #     code = entry['github']
            # user_repo = code.replace('https://github.com/', '')
            # s += f'<img src="https://img.shields.io/github/stars/{user_repo}.svg">'
        # dimenions citations & altmetric
        if 'doi' in entry:
            doi = entry['doi']
            s += f'<span class="__dimensions_badge_embed__" data-doi="{doi}" data-style="small_rectangle" style="display: inline-block; margin-left: 3px; vertical-align: baseline;"></span>'
            # vertical_align = 'baseline' if ascard else 'middle'
            # s += f'<span class="altmetric-embed" data-badge-type="2" data-doi="{doi}" data-condensed="true" data-hide-no-mentions="true" style="display: inline-block; margin-left: 5px; vertical-align: {vertical_align};"></span>'
    # end of publication entry
    if doctype == 'html':
        s += '</div>' if ascard else '</p>\n\n'
    else:
        s += r'\newline' + '\n'
    return s


def format_talks(entry, doctype='html'):
    """Format talks

    All for html.
    """
    # apply basic html formating
    # apply basic html formating
    newentry = {}
    for key in entry:
        # iterate over the keys that are of type list
        # these are all but key and entryType
        if type(entry[key]) == list:
            if len(entry[key]) == 1:
                newentry[key.lower()] = format_basic(key, entry[key][0],
                                                     doctype=doctype)
            else:
                for i, value in enumerate(entry[key]):
                    newentry[key.lower()][i] = format_basic(key, value,
                                                            doctype=doctype)
        else:
            newentry[key] = entry[key]
    entry = newentry
    s = '<p>'
    # format title
    s += '<span id="' + entry['id'] + '" style="font-size: 60%">' + entry['id'] + '</span> '
    s += ('<span '
           # +'" style="font-variant: small-caps; font-size: 90%">'
           + ' style="font-weight: bold">'
           + entry['title'] + '</span> <br> ')
    # format type
    s += markdown_no_p(entry['type']) + '<br>'
    # format data
    s += entry['location']
    s += ' (' + entry['date'] + ')</a> '
    # pdf
    if 'pdf' in entry:
        s += ' <a href="' + entry['pdf'] + '" style="{}">pdf</a>'.format(css_style_note)
    # html
    if 'html' in entry:
        s += ' <a href="' + entry['html'] + '" style="{}">html</a>'.format(css_style_note)
    # end of publication entry
    s += '</p>' + '\n' + '\n'
    return s


talks_header = "<h1>Talks</h1>"


def format_all_publications(f, entries, doctype):
    if doctype == 'html':
        f.write('''\
<h1>Publications</h1>
<ul>
<li> See
    <a href="http://scholar.google.de/citations?user=1FnOtMoAAAAJ&hl=en">google scholar</a> and
    <a href="http://orcid.org/0000-0002-8760-7838">ORCID</a>.</li>
<li> Co-first and co-last authors are indicated by * and †, respectively.</li>
<li> For publications grouped by context, see <a href="/research">research</a>.</li>
</ul>

<script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
''')

        f.write('<h2 id="preprints"> Preprints </h2> \n\n')
    else:
        f.write('\n\subsubsection*{Preprints}' + r'\vspace{-1em}' + '\n')
        f.write(r'\noindent\begin{longtable}[t]{p{.02\textwidth} p{.93\textwidth}}' + '\n')
    journals = True
    patents = True
    otherpub = True
    for entry in entries:
        if 'Article' == entry['entryType'] and journals:
            if doctype == 'html':
                f.write('<h2>Reviewed articles</h2>\n\n')
            else:
                f.write(r'\end{longtable}\vspace*{-2.5em}')
                f.write('\n\subsubsection*{Reviewed articles}' + r'\vspace{-1em}' + '\n')
                f.write(r'\noindent\begin{longtable}[t]{p{.02\textwidth} p{.93\textwidth}}' + '\n')
            journals = False
        if 'patent' == entry['entryType'] and patents:
            if doctype == 'html':
                f.write('<h2>Patents</h2> \n\n')
            else:
                f.write(r'\end{longtable}\vspace*{-2.5em}')
                f.write('\n\subsubsection*{Patents}' + r'\vspace{-1em}' + '\n')
                f.write(r'\noindent\begin{longtable}[t]{p{.02\textwidth} p{.93\textwidth}}' + '\n')
            patents = False
        if 'otherpub' == entry['entryType'] and otherpub:
            if doctype == 'html':
                f.write('<h2>Other publications</h2> \n\n')
            else:
                f.write(r'\end{longtable}\vspace*{-2.5em}')
                f.write('\n\subsubsection*{Other publications}' + r'\vspace{-1em}' + '\n')
                f.write(r'\noindent\begin{longtable}[t]{p{.02\textwidth} p{.93\textwidth}}' + '\n')
            otherpub = False
        f.write(format_pub(entry, doctype=doctype))
    if doctype != 'html':
        f.write(r'\end{longtable}\vspace*{-2.5em}')


def process_source(single_source):
    """Process a source file.
    """
    global posts  # add to global dict that tracks all posts
    source_out = single_source
    source_out_stripped = source_out.split('.')[0]  # base filename without ending
    is_post = source_out.startswith('_posts/')

    if '.bib' in single_source:
        entries = read_file(single_source)

    # this is for the experience section of the cv
    if single_source == '_cv/experience.bib':
        f = open('_cv/source/generated_experience.tex', 'w')
        for entry in entries:
            f.write(format_latex_experience(entry))
        f.close()
    # this is everything else
    else:
        if single_source.endswith('.bib'):
            if doctype == 'html':
                f = open('_build/' + source_out.replace('.bib', '.txt'), 'w')
            else:
                f = open('_cv/source/generated_publications.tex', 'w')
            if 'publications' in single_source:
                format_all_publications(f, entries=entries, doctype=doctype)
            elif 'talks' in single_source:  # these are only the talks, only html
                f.write(talks_header)
                for entry in entries:
                    f.write(format_talks(entry))
            else:
                raise ValueError('Unknown bib file.')
            f.close()

        if doctype == 'html':
            source_isdir = os.path.isdir(single_source)
            # transform notebooks into .md files
            cleanup = False
            if source_isdir:
                for s in glob.glob(single_source + '/*'):
                    if s.endswith(('.ipynb')):
                        os.system('jupyter nbconvert --log-level="WARN" --to markdown ' + s)
            else:
                if single_source.endswith(('.ipynb')):
                    new_source_dir = single_source.split('.')[0]
                    os.system('jupyter nbconvert --log-level="WARN" --to markdown --output-dir {} {}'
                              .format(new_source_dir, single_source))
                    value = os.rename(new_source_dir + '/' + single_source.split('/')[-1].replace('.ipynb', '.md'),
                              new_source_dir + '/index.md')
                    source_isdir = True
                    single_source = new_source_dir
                    cleanup = True
            # now, deal with .md and .rst sources
            if source_out == 'about.md':  # generate the page root (index.html)
                target_dir = '_site'
                child = False
            elif is_post:  # deal with posts
                year = source_out.split('-')[0].lstrip('_posts/')  # get year
                date = '-'.join(source_out.split('-')[:3]).lstrip('_posts/')  # extract ISO-format date
                string = '-'.join(source_out.split('-')[3:])   # strip ISO-format date
                target_link = year + '/' + string.split('.')[0]
                target_dir = '_site/' + target_link
                child = True
                posts[source_out] = [target_link, date]
            else:
                target_dir = '_site/' + source_out.split('.')[0]
                child = True
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            if source_isdir:
                if not single_source.endswith('/'):
                    single_source += '/'
                build_dir = '_build/' + single_source
                if not os.path.exists(build_dir):
                    os.makedirs(build_dir)
            # copy the content of a directory, mostly image files etc
            source_files = []
            if source_isdir:
                for s in glob.glob(single_source + '*'):
                    if not s.endswith(('.rst', '.md')):
                        if os.path.isdir(s):
                            shutil.copytree(s, target_dir)
                        # we do not need to copy the ipynbs to the deploy
                        # directory
                        elif not s.endswith('.ipynb'):
                            shutil.copy(s, target_dir)
                    else:
                        source_files.append(s)
            else:
                source_files.append(single_source)

            # generate and write all source files
            for source_file in source_files:
                if source_isdir:
                    target = target_dir + '/' + os.path.basename(source_file).split('.')[0] + '.html'
                else:
                    target = target_dir + '/index.html'
                raw_html = ('_build/' + source_file).split('.')[0] + '.txt'

                def remove_docutils_header_footer(textfile):
                    read = False
                    lines = []
                    for l in open(textfile):
                        if l.startswith('</body>'): read = False
                        if read: lines.append(l)
                        if l.startswith('<body>'): read = True
                    with open(textfile, 'w') as f:
                        f.write(''.join(lines))

                md = None
                if '.md' in source_file:
                    md = markdown.Markdown(extensions=[
                        'mdx_math', 'markdown.extensions.tables', 'toc', 'meta', 'fenced_code'])
                    md.convertFile(source_file, raw_html)

                if '.rst' in source_file:
                    os.system('rst2html.py --link-stylesheet {} {}'
                              .format(source_file, raw_html))
                    remove_docutils_header_footer(raw_html)

                def adjust_child_dir(line):
                    if (line.startswith('    <link href="_vendor/')
                        or line.startswith('    <link href="_css/')
                        or line.startswith('    <link href="_js/')):
                        return line.replace('href="', 'href="../../')
                    elif (line.startswith('    <script src="_vendor/')
                          or line.startswith('    <script src="_js/')):
                        return line.replace('src="', 'src="../../')
                    else:
                        return line

                out = open(target, 'w')
                publications = read_file('publications.bib')
                for line in open('_includes/blog.html'):
                    if 'INSERT' not in line:
                        out.write(line)
                    elif 'INSERT_HEADER' in line:
                        for l in open('_includes/header.html'):
                            if '{title}' in l:
                                title = source_out_stripped[0].upper() + source_out_stripped[1:]
                                l = l.format(title=title)
                            out.write(adjust_child_dir(l) if child else l)
                    elif 'INSERT_FOOTER' in line:
                        for l in open('_includes/footer.html'):
                            if l.startswith('#BLOG'):
                                if not target.startswith('_site/blog/'):
                                    continue  # ignore these lines for non-blog
                                else:
                                    l = l.replace('#BLOG', '')  # strip this start sequence
                            out.write(adjust_child_dir(l) if child else l)
                    elif 'INSERT_CONTENT' in line:
                        history_link = f'<a href="https://github.com/falexwolf/site/blame/master/{single_source}">History</a>'
                        history = '<div class="card pull-right" style="display: inline-block;">' + start_card + history_link + '</div></div>'
                        # deal with title as delivered by metadata
                        if md is not None and 'title' in md.Meta:
                            title = f'{md.Meta["title"][0]}'
                            l = '<div>' + '<span style="font-size: 38px; font-weight: 800;"<h1>' + title + '</h1></span>' + history + '</div>'
                            out.write(l)
                        for l in open(raw_html):
                            # deal with title if present in doc
                            if l.startswith('<h1'):
                                parsed_result = l.split('<h1')[1].split('</h1>')[0].split('">')
                                title = parsed_result[1] if len(parsed_result) == 2 else parsed_result[0]
                                l = '<div>' + '<span style="font-size: 38px; font-weight: 800;">' + title + '</span>' + history + '</div>'
                            # replace paper macros
                            if l.startswith('<p>{'):
                                key = l.split('{')[1].split('}')[0]  # strip off html stuff
                                for p in publications:
                                    if p['id'][0] == key:
                                        l = format_pub(p, ascard=True)
                                        break
                            out.write(l)
                        if is_post:
                            posts[source_out].append(title)  # also add title to posts dictionary 
                out.close()

            if cleanup:
                os.remove(new_source_dir + '/index.md')
                os.rmdir(new_source_dir)


if __name__ == '__main__':

    p = argparse.ArgumentParser(description='')
    aa = p.add_argument
    aa('-v', '--verbosity',
        type=int, default=0,
        help='specify integer > 0 to get more output')
    aa('-t', '--doctype',
        type=str, default='html',
        help='the doctype, \'latex\' or \'html\'')
    args = p.parse_args()

    global doctype, posts
    doctype = args.doctype
    posts = {}

    if not os.path.exists('_build'):
        os.makedirs('_build')
        os.makedirs('_build/_posts')

    # process posts
    sources = sorted(glob.glob('_posts/*'), reverse=True)   

    for single_source in sources:
        print('processing source: {}'.format(single_source))
        process_source(single_source)

    # process root level files & folders
    sources = [
        single_source for single_source in sorted(glob.glob('*'))
        if single_source.endswith(('.md', '.bib', '.rst')) and single_source != 'README.md'
    ]

    for single_source in sources:
        print('processing source: {}'.format(single_source))
        process_source(single_source)

    with open('blog.md', 'w') as blog:
        blog.write('Title: Blog\n\n')
        for source, post in posts.items():
            target, date, title = post
            blog.write(f'* [{title}](../{target}) <span style="{css_style_note}">| {date}</span>\n')

    process_source('blog.md')

    # update _site directory by copying over from _assets
    from dirsync import sync
    sync('_assets/', '_site', 'sync')