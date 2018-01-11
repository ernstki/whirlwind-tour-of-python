# A Whirlwind Tour of Python

The main repository for this project is:

    https://tfwebdev.research.cchmc.org/ern6xv/whirlwind-tour-of-python.git

A "Python 101"-level tour of the language syntax is available in
[`tour_of_python_syntax.py`][tour].

## Slides

Slides from the "Python: a quick introduction" presentation (created using
[reveal.js][revealjs]) may be found in the `slides` subdirectory of this
repository, and may also be viewed online [here][slides].

## What you'll need to get started

* some small bit of command line experience (_e.g._, where to find the
  Terminal / Command Prompt application for your OS)
* [Git]
  * probably already available on macOS / OS X
  * `sudo apt-get install git` on Debian/Ubuntu or 'sudo yum install git' on
    CentOS/Fedora/RHEL
  * optionally, maybe also a GUI like GitHub's or Syntevo SmartGit
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

# replace `usr0xy` with your actual CCHMC username
git clone https://usr0xy@tfwebdev.research.cchmc.org/ern6xv/whirlwind-tour-of-python.git

# install dependencies; use a virtualenv if that's your choice
cd whirlwind*
python3 -m venv venv
# on Windows, I think it's just '.\venv\Scripts\activate'
source venv/bin/activate

# skip the above two commands and add '--user' if you're OK with installing to
# your "personal" Python 'site-packages' directory
pip install -r requirements.txt

# test to see if the 'seq_core_downloader.py' script works
# on Windows, leave off the './'
./seq_core_downloader.py --help
```

## Sequencing Core downloader

A small-but-complete Python application is included which downloads
sequencing results from the [CCHMC Sequencing Core web site][seqcore].

You might like to view the source [here on GitLab/Hub][seqsrc].

It has a `--help` option; if you provide the `--with-curl` command line
option, the results include an authentication cookie which allows you to pipe
the results directly into `bash` or [`parallel`][gnupar].

![Sample invocation of `seq_core_downloader.py`](slides/img/core_seq_downloader.gif)

## Getting help

**TODO**


[atom]:      https://atom.io/
[git]:       https://git-scm.com/downloads
[gnupar]:    https://www.gnu.org/software/parallel/
[revealjs]:  https://github.com/hakimel/reveal.js/
[seqcore]:   https://dna.cchmc.org/www/main.php
[seqsrc]:    ./seq_core_downloader.py
[slides]:    https://ernstki.github.io/whirlwind-tour-of-python/
[st]:        https://www.sublimetext.com/
[submodule]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[tour]:      ./tour_of_python_syntax.py
[venv]:      https://docs.python.org/3.5/library/venv.html
