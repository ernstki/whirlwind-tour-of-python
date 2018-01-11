# A Whirlwind Tour of Python

The main repository for this project is:

    https://github.com/ernstki/whirlwind-tour-of-python

## Slides

Slides from the "Python: a quick introduction" presentation (created using
[reveal.js][revealjs]) may be found in the `slides` subdirectory of this
repository, and may also be viewed online [here][slides].

A "Python 101"-level tour of the language syntax is available in
[`tour_of_python_syntax.py`][tour].

## Sequencing Core downloader

A small-but-complete Python application is included which downloads
sequencing results from the [CCHMC Sequencing Core web site][seqcore].

You might like to view the source [here on GitHub][seqsrc].

It has a `--help` option; if you provide the `--with-curl` command line
option, the results include an authentication cookie which allows you to pipe
the results directly into `bash` or [`parallel`][gnupar].

![Sample invocation of `seq_core_downloader.py`](slides/img/core_seq_downloader.gif)

## What you'll need to run the example script

* some small bit of command line experience (_e.g._, where to find the
  Terminal / Command Prompt application for your OS)
* an installation of [Git][] on your computer
  * probably already available on macOS / OS X
  * `sudo apt-get install git` on Debian/Ubuntu or `sudo yum install git` on
    CentOS/Fedora/RHEL
  * optionally, maybe also a GUI like [GitHub's][ghgui] or
    [Syntevo SmartGit][smartgit]
* a code editor like [Atom][] or [Sublime Text][st]; _Windows' Notepad or OS
  X's TextEdit.app are_ not _suitable for this activity_

Decide on a nice home for your copy of the project. (Git calls this
a "clone"). I like putting projects in a folder called "devel" in my home
directory (`$HOME/devel` on Unix or OS X, `C:\Users\YourName\devel` on
Windows).

Then:

```bash
# on Windows, this might look like 'cd /d "C:\Users\YOURUSERNAME\dev\stuff"
cd /to/the/place/where/you/do/dev/stuff

git clone https://github.com/ernstki/whirlwind-tour-of-python

# install dependencies; use a virtualenv if that's your choice
cd whirlwind*
python3 -m venv venv
# on Windows, I think it's just '.\venv\Scripts\activate'
source venv/bin/activate

# skip the above two 'venv'-related commands and add '--user' if you're OK
# with installing to your "personal" Python 'site-packages' directory
pip install -r requirements.txt

# test to see if the 'seq_core_downloader.py' script works
# on Windows, leave off the './'
./seq_core_downloader.py --help
```

## Reporting bugs

Please report bugs on the Weirauch Lab internal issue tracker [here][bugs].

The output of `seq_core_downloader.py --help` also has a shortlink that takes
you to the same place.

## Getting help

Please see the ["Getting started" slide][pystart] (#5) from the included
presentation.

You may also find these slides useful:

* [Why learn Python 3 (or 2.7.x)?][py2or3]
* [Python compared to...][pyvs]

## Author

Kevin Ernst (`kevin.ernst -at- cchmc.org`)

## License

Reveal.js is provided under the MIT license, as are the example Python
scripts.

[atom]: https://atom.io/
[bugs]: https://tfwebdev.research.cchmc.org/gitlab/ern6xv/whirlwind-tour-of-python/issues
[ghgui]: https://desktop.github.com/
[git]: https://git-scm.com/downloads
[gnupar]: https://www.gnu.org/software/parallel/
[revealjs]: https://github.com/hakimel/reveal.js/
[py2or3]: https://ernstki.github.io/whirlwind-tour-of-python/slides/index.html#/3/2
[pystart]: https://ernstki.github.io/whirlwind-tour-of-python/slides/index.html#/5
[pyvs]: https://ernstki.github.io/whirlwind-tour-of-python/slides/index.html#/4
[seqcore]: https://dna.cchmc.org/www/main.php
[seqsrc]: ./seq_core_downloader.py
[slides]: https://ernstki.github.io/whirlwind-tour-of-python/
[smartgit]: https://www.syntevo.com/smartgit/
[st]: https://www.sublimetext.com/
[submodule]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[tour]: ./tour_of_python_syntax.py
[venv]: https://docs.python.org/3.5/library/venv.html
