#
# You can't run this file. It only has the '.py' extension so it'll be
# properly syntax-highlighted.
#

>>> # demonstrations of "equality (of value)" with the '==' comparison
>>> # operator vs. "object identity" with the 'is' comparison operator

>>> a = 3

>>> b = 3

>>> a is b
True

>>> a == b
True

>>> # keep in mind that strings and integers are "primitives", which
>>> # means that two "names" pointing at the same primitive value do NOT
>>> # have unique IDs; they point to the same memory location

>>> s1 = 'hi'

>>> s2 = 'hi'

>>> s1 is s2
True

>>> id(s1)
4565235448

>>> id(s2)
4565235448

>>> # what makes a Python object an object is that it has a unique
>>> # id(), as you'll see below; furthermore, objects (usually) have
>>> # methods that can cause them to be manipulated in place (have their
>>> # internal values changed), without returning a copy, as with string
>>> # concatenation and other operations on primitives

>>> d1 = {}

>>> d2 = {}

>>> id(d1)
4584066376

>>> id(d2)
4584059464

>>> d1 is d2
False

>>> # strings have methods on them (kinda like objects), but they always
>>> # return a copy

>>> s1 = 'E.E. CUMMINGS WOULD BE AGHAST'

>>> s1.lower()
'e.e. cummings would be aghast'

>>> s1
'E.E. CUMMINGS WOULD BE AGHAST'

>>> # strings are "immutable": there are no methods that can "mutate" or
>>> # modify a string "in-place"

>>> # so you must make a copy

>>> s2 = s1.lower()

>>> s2
'e.e. cummings would be aghast'

>>> s2.replace('aghast', 'proud')
'e.e. cummings would be proud'

>>> # Python does not have a build-in regular expression (a pattern
>>> # matching language) syntax; you must include the 're' library

>>> # Python is known as a "batteries included" language, so the
>>> # standard library is pretty complete

>>> import re

>>> s2
'e.e. cummings would be aghast'

>>> s2 = s2.replace('aghast', 'proud')

>>> s2
'e.e. cummings would be proud'

>>> re.match('cummings', s2)

>>> s2
'e.e. cummings would be proud'

>>> # hrrmmm, here is the first of the Python "gotchas": re.match acts
>>> # as if the expression given as the first argument is anchored at
>>> # the beginning of the line

>>> # that is, as if the pattern began with the "anchor" metachar '^'

>>> # 're.search()' will act more like what you're used to from Perl,
>>> # Ruby, or JavaScript

>>> re.search('cummings', s2)
<_sre.SRE_Match object; span=(5, 13), match='cummings'>

>>> # in Python "truthy" values include non-empty objects and non-zero
>>> # integers

>>> # "falsy" values include empty objects (lists, dictionaries), the
>>> # integer 0, or the special object(ish) value 'None'

>>> # the '==' operator is used to test for equality (the values are the
>>> # same), 'is' tests for object identity (the exact same object)

>>> {} == {}
True

>>> {} is {}
False

>>> # because variables containing primitive values are really pointing
>>> # at the same memory location...

>>> # (primitives are immutable--they offer no methods that can modify
>>> # them in place, only return modified copies)

>>> # ...two primitives will both be equal and identical (that is the
>>> # return value of '==' AND 'is' will be True)

>>> # Booleans are another built-in type, and the capitalization of
>>> # "True" and "False" is important

>>> type(True)
<class 'bool'>

>>> a = 3

>>> b = 3

>>> a == b
True

>>> a is b
True

>>> s1 = 'hi mom'

>>> s2 = 'hi mom'

>>> s1 == s2
True

>>> s1 is s2
False

>>> # because strings are immutable (any operations that would change
>>> # their values will return a copy), it's sometimes

>>> # it is slightly more efficient to use the 'join' string method to
>>> # concatenate them

>>> # 'join()' is a weird one: it operates on a string, takes a list (or
>>> # really any iterable) as its argument, and

>>> # returns all the elements of the list with the string put in
>>> # between them. It looks like this

>>> delimiter = ' '

>>> delimiter.join(['well,', 'la', 'de', 'frickin', 'da!'])
'well, la de frickin da!'

>>> # note that the delimiter need not be a single character!

>>> delimiter = '... '

>>> delimiter.join(['well,', 'la', 'de', 'frickin', 'da!'])
'well,... la... de... frickin... da!'

>>> # I forgot to mention that Python infers string concatenation when
>>> # two strings are butted up right next to each other, similar to C

>>> a_string = "can consist of " "multiple strings " "cuddled together"

>>> print(a_string)
can consist of multiple strings cuddled together

>>> # This can make passing long strings into functions look a bit nicer

>>> # There is a community standard for Python coding "style" called
>>> # PEP8 (for Python Enhancement Proposal) which recommends you limit
>>> # code to less than ~80 characers.

>>> # Python has multi-line strings, but leading whitespace would be
>>> # significant if you used those

>>> # Python also allows the backslash (the one below the backSPACE key,
>>> # '\') to be used as a line continuation character

>>> # so, for example...

>>> print("quite a bit " \
...       "much longer " \
...       "string")
quite a bit much longer string

>>> # works the same as...

>>> print("quite a bit "
...       "much longer "
...       "string")
quite a bit much longer string

>>> # ...in this case, but may be useful elsewhere, like long 'import'
>>> # statements

>>> # Nota Bene: the Python parser doesn't require line continuation
>>> # characters if there is an open brace, bracket, or paren

>>> from os.path import dirname, \
...                     basename, \
...                     isdir

>>> # (without those backslashes, that would be a syntax error)

>>> # Here's what a multi-line string looks like. They're often used for
>>> # "docstrings," a Python convention for documenting functions and
>>> # modules

>>> a_multi_line_string = """This string consists of multiple lines.
... Any whitespace within the multi-line string becomes a literal part of the string.
...       See
...            What
...                    I
...                          Mean?
... """

>>> print(a_multi_line_string)
This string consists of multiple lines.
Any whitespace within the multi-line string becomes a literal part of the string.
      See
           What
                   I
                         Mean?


>>> # including the newline after "Mean?"

>>> # let's learn about Python's lists and dictionaries, through
>>> # a "fun" example for some reason, the MACS2 project page
>>> # requires you (or used to) to have a password to download
>>> # the latest release, but they include an "encrypted"
>>> # version of the username and password on the project page:
>>> # http://liulab.dfci.harvard.edu/MACS/Download.html

>>> macs_supersecret_password = """
... hfreanzr: znpf
...
... cnffjbeq: puvcfrd
... """

>>> # this looks like a "substitution" cypher (spoiler alert: it's a
>>> # "rot13" substitution)

>>> # I'll bet that "hfreanzr" means "username" -- call it a hunch ;)

>>> # notice that the second letter is 'f' and if "cnffjbeq" is
>>> # "password", the double 'f' as the third and fourth characters
>>> # makes sense, too

>>> # so let's store all these letters in a dictionary, along with the
>>> # letters that they translate into when they're "decoded"

>>> # one thing to note first, strings are sort of like lists, in that
>>> # they can be iterated over:

>>> for character in "mana-mana!":
...     print(character)
m
a
n
a
-
m
a
n
a
!

>>> # but when you really want them to behave like real list objects,
>>> # you have to convert them with the 'list()' function dictionaries
>>> # are sets of key-value pairs, called "hashes" in Perl, "associative
>>> # arrays" in PHP, and "objects" in JavaScript

>>> # they are very fast to access (big-Oh of 1), but you can't rely on
>>> # the elements being in any kind of order (unlike lists)

>>> # there are several ways to initialize dictionaries

>>> d1 = { 'a': 1, 'b': 2 }

>>> d1 = dict(a=1, b=2)  # only if dict's keys are valid identifiers

>>> print(d1)
{'b': 2, 'a': 1}

>>> # oh, and most Python objects have a built-in "to string" method
>>> # that produces a sensible text version of the object whenever it's
>>> # used in a string context, like the 'print()' statement; this is a
>>> # big improvement over lower-level languages like C/C++ where you'd
>>> # have to write code /just/ to inspect the insides of your data
>>> # structures. :(

>>> # dictionary keys don't have to be strings, though

>>> d2 = { 1: 'one', 2: 'two' }

>>> print(d2)
{1: 'one', 2: 'two'}

>>> # but they *do* have to be valid Python identifiers (i.e., something
>>> # that could be a variable name), so this wouldn't work

>>> # d1 = dict(1='one', 2='two')

>>> # since dictionaries are objects, they have methods that can
>>> # "mutate" them, or modify them in-place

>>> d1.update({'c': 3, 'd': 4})

>>> d1
{'b': 2, 'a': 1, 'd': 4, 'c': 3}

>>> # unlike JavaScript (where you can use the '.' operator, like an
>>> # object property), you have to use the square brackets to access
>>> # individual elements from the dict, like subscripting an array
>>> # (lists--Python's name for arrays--are discussed farther down)

>>> d1['c']
3

>>> # and there's no .delete() method for dictionary keys; you use the
>>> # del() built-in

>>> del(d1['c'])

>>> d1
{'b': 2, 'a': 1, 'd': 4}

>>> # although the approach makes sense, neither of these actually work

>>> d1['d'].delete()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'delete'
'int' object has no attribute 'delete'

>>> d1.delete('d')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'delete'
'dict' object has no attribute 'delete'

>>> # there is a .clear() method, though:

>>> d2
{1: 'one', 2: 'two'}

>>> d2.clear()

>>> d2
{}

>>> # dictionaries can also be instantiated with a list of tuples, which
>>> # are another Python data type (they're basically immutable lists)

>>> # tl;dr: you can .append() to a list or change individual indices,
>>> # but you can't do those things to a tuple

>>> a = [1,2,3]

>>> a.append(4)

>>> a
[1, 2, 3, 4]

>>> t = (1,2,2)

>>> t.append()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
'tuple' object has no attribute 'append'

>>> # see, it didn't work! the 'append()' method doesn't even exist for
>>> # tuples.

>>> # okay, back to dictionaries... you can ALSO instantiate a new
>>> # dictionary with a list of (key,value) tuples (or with keyword
>>> # arguments, as mentioned above, as long as all the keys are valid
>>> # Python identifiers)

>>> d3 = dict([('one', 1), ('two', 2)])

>>> d3
{'one': 1, 'two': 2}

>>> # why would you ever use this?

>>> # let's go back to the "encoded" username and password for the MACS
>>> # download page, because that's the reason we started talking about
>>> # this

>>> print(macs_supersecret_password)

hfreanzr: znpf

cnffjbeq: puvcfrd


>>> # let's turn the "encrypted" or "encoded" character string into a
>>> # real list

>>> list('hfreanzr')
['h', 'f', 'r', 'e', 'a', 'n', 'z', 'r']

>>> # then let's make another list that represents the "decrypted"
>>> # version of that character string

>>> list('password')
['p', 'a', 's', 's', 'w', 'o', 'r', 'd']

>>> # finally, let's use a function called 'zip' to turn them into a
>>> # list of pairs of tuples, which we'll then use to initialize a
>>> # dictionary

>>> zip(list('hfreanzr'), list('username'))
<zip object at 0x11168f208>

>>> # here's a Python 3 pitfall: many things that would return regular
>>> # ol' lists, now return iterables, or generators (not totally
>>> # positive the difference)

>>> # the long and the short of it is, you can *always* use the 'for i
>>> # in iterable:' syntax, but if you want to SEE the list with your
>>> # eyeballs you have to use the list() function to get the iterable
>>> # to spin out all of its values for you

>>> list(zip(list('hfreanzr'), list('username')))
[('h', 'u'), ('f', 's'), ('r', 'e'), ('e', 'r'), ('a', 'n'), ('n', 'a'), ('z', 'm'), ('r', 'e')]

>>> # OK so far?

>>> # let's make a dictionary out of that, which will act as our "codebook"

>>> codebook = dict(zip(list('hfreanzr'), list('username')))

>>> # note that there was no syntax error there; that's because the
>>> # dict() initializer can act on iterables, as well as "regular"
>>> # lists

>>> # again, both of those things are data structures that you can
>>> # say "give me the next of your things" (e.g., 'for thing in
>>> # list_of_things') and when it has no more things it tells Python "I
>>> # have no more things"

>>> # OK, let's test if what we have works like we expect...

>>> codebook
# FIXME
{'a': 'n', 'e': 'r', 'z': 'm', 'f': 's', 'r': 'e', 'n': 'a', 'h': 'u'}

>>> for c in 'hfreanzr':
...     print(codebook[c])
u
s
e
r
n
a
m
e

>>> # great! let's add the second part that we know, the "encoded"
>>> # version of the string "username"

>>> print(macs_supersecret_password)

hfreanzr: znpf

cnffjbeq: puvcfrd


>>> codebook.update(zip(list('cnffjbeq'), list('password')))

>>> codebook
{'a': 'n', 'j': 'w', 'c': 'p', 'e': 'r', 'z': 'm', 'q': 'd', 'f': 's', 'r': 'e', 'b': 'o', 'n': 'a', 'h': 'u'}

>>> # let's see how far we're getting by trying to decode one of the
>>> # unknown strings

>>> for c in 'puvcfrd':
...     print(codebook[c])
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyError: 'p'
'p'

>>> # OH NOES! the letter 'p' isn't in our codebook yet. let's fix that

>>> # firstly, let's write a function, so we don't have to do all this
>>> # re-typing and let's learn about exception handling now, too

>>> def decode(some_string):
...     for c in some_string:
...         print(codebook[c], end='')  # suppress the newline
...     print()  # add a newline at the end

>>> decode('puvcfrd')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in decode
KeyError: 'p'
'p'

>>> # OK, we have to handle the 'KeyError'; you do exception handling in
>>> # Python by wrapping the code you expect to throw an exception in a
>>> # 'try ... except' construct

>>> def decode(some_string):
...     for c in some_string:
...         try:
...             print(codebook[c], end='')
...         except KeyError:
                # string concat w/ a variable requires the '+' operator
...             print('<' + c + '=?>', end='')
...     print()  # a final newline

>>> # let's see if that worked

>>> decode('puvcfrd')
<p=?><u=?><v=?>pse<d=?>

>>> # OK, looks good. we still don't know how to decode the letters 'p',
>>> # 'u', 'v', and 'd'

>>> # time for an aside about string interpolation and formats

>>> # remember, I said strings can be implicitly concatenated if they're
>>> # nestled right up next to each other

>>> # this isn't true with variable names that /contain/ strings; you
>>> # have to use the '+' (string concatenation) operator, as seen above

>>> # this can be hard to type if you are substituting in a lot of
>>> # variables in a string (plus inefficient, since strings are
>>> # immutable, so each concatenation creates a copy--at least it did
>>> # in older Pythons)

>>> # there are several ways of doing variable interpolation within
>>> # strings in Python; maybe too many ways, I dunno
>>> #
>>> # 1. the old 'printf'-style formatting, using the '%' (mod) operator
>>> #    -> https://docs.python.org/3/library/stdtypes.html#old-string-formatting
>>> #
>>> # 2. format strings (using the .format() method on a string literal)
>>> #    -> https://docs.python.org/3/library/string.html#formatstrings
>>> #
>>> # 3. "formatted string literals" - new in Python 3.6
>>> #    -> https://docs.python.org/3/reference/lexical_analysis.html#f-strings

>>> method1 = 'old skool, using the mod ("%") operator'

>>> # by the by: single and double-quotes are interchangeable in Python;
>>> # I like to use double quotes when some kind of interpolation is
>>> # happening (just a personal preference, consistent with how Perl
>>> # and the Bash/Bourne shell treat double vs. single quotes)

>>> # Also, you can nest one kind of quotes inside the other to prevent
>>> # having to "escape" quotes within quotes (that is, prefix them with
>>> # a '\' in order to prevent Python from mistaking them for the end
>>> # of the string)

>>> print("The first method is: %s" % method1)
The first method is: old skool, using the mod ("%") operator

>>> # the '%' (mod) operator tells Python to interpolate everything that
>>> # comes after it into the placeholders in the string that comes
>>> # /before/ it; if there are multiple values to interpolate, put them
>>> # in a tuple, that is, ('sub1', 'sub2');

>>> # the placeholders are very similar to those of the 'printf'
>>> # function in some other langauges; '%s' means a string
>>> # placeholderk, %d is an integer, '%3.2f' means a two-decimal place
>>> # representation of a float, where the whole-number part is padded
>>> # to three places.

>>> # it's best to experiment with these in the Python REPL while
>>> # looking at the docs;see also 'man 3 printf' in Unix

>>> # the '%' operator version of string interpolation isn't going
>>> # anywhere in Python 3.x, and I personally prefer it because I use
>>> # 'printf' in C, MATLAB, and PHP, so I'm used to the format strings

>>> method2 = 'new-style, using the .format() string method'

>>> print("The second method is: {}".format(method2))
The second method is: new-style, using the .format() string method

>>> # with the "new" style substitution, curly braces

>>> # both methods can "name" the replaceable parts of the string, and
>>> # accept key-value pairs (a dict) for the replacements

>>> replacements = {'a': 'mystery', 'b': 'string'}

>>> print("By using old-style %(b)s replacements you will "
...       "discover the %(a)s word" % replacements)
By using old-style string replacements you will discover the mystery word

>>> print("You can also unravel the {} {} with the .format() "
...       "function".format(replacements))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
tuple index out of range

>>> # oops, the .format() function expects a list of replacements as its
>>> # arguments, not a variable representing a list; time to talk about
>>> # "argument unpacking"

>>> print("You can also unravel the {b} {a} with the .format() "
          "function".format(**replacements))
You can also unravel the string mystery with the .format() function

>>> # OK, that worked. argument unpackers: that's the '**' you saw

>>> # the .format() method on strings (fairly new, only on Python 2.7
>>> # or later) expects a list, in which case you can either omit the
>>> # "name" between the curly braces, or if you want reorder things in
>>> # the output string in a different order than they appear in the
>>> # list, you can put numbers inside the curly braces

>>> # the other option is to give keyword arguments (name=value) to the
>>> # .format() method, in which case the '**' operator "flattens out" a
>>> # dictionary into a list like name1='value1', name2='value2' this is
>>> # the format that .format() expects

>>> # another way of doing it would be like this

>>> print("You can also unravel the {} {} with the .format() "
...       "function".format('string', 'mystery'))
You can also unravel the string mystery with the .format() function

>>> # in that case, order is important! ...or, alternatively

>>> print("You can also unravel the {a} {b} with the .format() "
...       "function".format(b='string', a='mystery'))
You can also unravel the mystery string with the .format() function

>>> # order there was unimportant, because you told the format string
>>> # exactly where you wanted 'a' and 'b' to be placed

>>> # OK, back to our 'decode' function then, finally:

>>> def decode(some_string):
...     for c in some_string:
...         try:
...             print(codebook[c], end='')
...         except KeyError:
...             print("<%s=?>" % c, end='')  
...             # or new-style: print("<{}=?>".format(c), end='')
...     print()  # a final newline

>>> # it still works the same, though, trust me.

>>> print(macs_supersecret_password)

hfreanzr: znpf

cnffjbeq: puvcfrd


>>> # let's work on the missing letters in our "codebook"

>>> # maybe if we sort the keys, we can discover a pattern

>>> # except, remember that dictionaries can't be relied on to return
>>> # the keys in any kind of predictable order, /least/ of all the
>>> # order you inserted them in

>>> codebook.keys()
dict_keys(['e', 'a', 'r', 'h', 'f', 'j', 'b', 'n', 'q', 'c', 'z'])

>>> # key lookups are done with a hash table, which is a kind of data
>>> # structure that is very fast for lookups (big-Oh of 1) but doesn't
>>> # respect the order that you inserted items into it

>>> codebook.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'sort'

>>> # see, there's not even a method for it. you can't just sort a
>>> # hashed data structure; you'd have to operate on the keys or the
>>> # "items", using an intermediate variable

>>> # unfortunately, you can't sort dict_items (the kind of object
>>> # returned by dict.items()), see?

>>> codebook.items().sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict_items' object has no attribute 'sort'
'dict_items' object has no attribute 'sort'

>>> # we can get a list of tuples out, though, with the .items() method
>>> # on dicts, and then sort /that/ list

>>> codebook.items()
dict_items([('e', 'r'), ('a', 'n'), ('r', 'e'), ('h', 'u'), ('f', 's'), ('j', 'w'), ('b', 'o'), ('n', 'a'), ('q', 'd'), ('c', 'p'), ('z', 'm')])

>>> list(codebook.items())
[('e', 'r'), ('a', 'n'), ('r', 'e'), ('h', 'u'), ('f', 's'), ('j', 'w'), ('b', 'o'), ('n', 'a'), ('q', 'd'), ('c', 'p'), ('z', 'm')]

>>> # I'm using Python 3, so the behavior of what you see above might
>>> # be slightly different than what you see if you use 2.7; I need
>>> # to turn that not-quite-list into a real list in order to use the
>>> # .sort() method on lists.

>>> # we can turn a list of dictionary items into a "normal" list, which
>>> # has a .sort() method, but the .sort() method operates in-place; so
>>> # if you tried something like

>>> dictitems = list(codebook.items()).sort()

>>> dictitems

>>> # wait, wha? it's empty!

>>> # surprising, right? that's because list() returned an as-yet
>>> # unnamed list, then that anonymous list was sorted in place. Sort
>>> # doesn't return anything, so there was nothing on the right hand
>>> # side of the assignment to assign to dictitems.

>>> # to solve that, save the list first, THEN sort it.

>>> dictitems = list(codebook.items())

>>> dictitems
[('e', 'r'), ('a', 'n'), ('r', 'e'), ('h', 'u'), ('f', 's'), ('j', 'w'), ('b', 'o'), ('n', 'a'), ('q', 'd'), ('c', 'p'), ('z', 'm')]

>>> dictitems.sort()

>>> # remember .sort() is in-place, that means it "mutates" the variable
>>> # it acts on, but doesn't return anything

>>> dictitems
[('a', 'n'), ('b', 'o'), ('c', 'p'), ('e', 'r'), ('f', 's'), ('h', 'u'), ('j', 'w'), ('n', 'a'), ('q', 'd'), ('r', 'e'), ('z', 'm')]

>>> # OK, I'm seeing a pattern here (I already spoitled it, but again
>>> # it's rot13 encoding, a.k.a. a substitution or Caesar cypher, and
>>> # there's actually a Unix command 'rot13' that can deocde this)

>>> # but just for kicks, let's pretend we /don't/ know and add the
>>> # reverse of all the letters in the dictionary also, since 'n' <-->
>>> # 'a' then 'a' <--> 'n', for example

>>> # here's a good place to use a Python "list comprehension"...

>>> # list comprehensions are one of my favorite features of Python;
>>> # they're like compact for loops that operate on all the elements of
>>> # a list, and return a list

>>> # maybe there are better ways of doing this, but I see a way to
>>> # reverse all the items in each tuple in 'dictitems' with a listcomp
>>> # that "emits" the items of the tuple with their indexes reversed

>>> reverses = [(i[1], i[0]) for i in dictitems]

>>> reverses
[('n', 'a'), ('o', 'b'), ('p', 'c'), ('r', 'e'), ('s', 'f'), ('u', 'h'), ('w', 'j'), ('a', 'n'), ('d', 'q'), ('e', 'r'), ('m', 'z')]

>>> # good, right? now let's add those to the dictionary; adding keys
>>> # that are already in there won't hurt anything, so we'll just
>>> # iterate over the whole list

>>> for t in reverses:
...     codebook.update(t)
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dictionary update sequence element #0 has length 1; 2 is required

>>> # oops, the documentation for .update() says it expects keyword
>>> # arguments like key='value' or an ITERABLE (e.g., list) of tuples
>>> # representing key, value pairs

>>> # for example, this works because it's a (one-item) list of tuples

>>> codebook.update([('n', 'a')])

>>> # so what we actually want to do is

>>> codebook.update(reverses)

>>> # let's see the result

>>> codebook
{'e': 'r', 'a': 'n', 'w': 'j', 'f': 's', 'b': 'o', 'd': 'q', 'c': 'p', 'q': 'd', 'r': 'e', 'p': 'c', 'h': 'u', 'j': 'w', 'n': 'a', 'u': 'h', 's': 'f', 'm': 'z', 'z': 'm', 'o': 'b'}

>>> # and do we get any farther with the decoding?

>>> decode('puvcfrd')
ch<v=?>pseq

>>> # OK, that obviously says "chipseq", so we now know the code for 'v'
>>> # and 'i'; let's update our codebook now with both of those...

>>> codebook.update({'v': 'i', 'i': 'v'})

>>> decode('puvcfrd')
chipseq

>>> # let's try the last part of the "secret code"

>>> print(macs_supersecret_password)

hfreanzr: znpf

cnffjbeq: puvcfrd


>>> decode('znpf')
macs

>>> # aha! code broken! the username is 'macs' and the password is
>>> # 'chipseq'

>>> # will our 'decode' function work on a multi-line string, I wonder?

>>> code = """hfreanzr: znpf
...
... cnffjbeq: puvcfrd"""

>>> decode(code)
username<:=?>< =?>macs<
=?><
=?>password<:=?>< =?>chipseq

>>> # yup, it did, except other symbols like space, colon, and newline
>>> # (LF) weren't in the "codebook"

>>> # pretty good for five minutes worth of work, right?

>>> # let's take a brief side trip and philosophize for a moment

>>> # here's a Python Easter egg: "the Zen of Python"

>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

>>> my_favorite = 'Readability counts.'

>>> # on that note: Python's PEP8 coding standard calls for four-space
>>> # indents, no tabs (https://www.python.org/dev/peps/pep-0008/)

>>> # it leaves it up to you whether you want to align things inside
>>> # the parens of function calls, or line up variable declarations /
>>> # definitions on the '=' like some people like to do

>>> # it also limits line length to < 80 characters (79 in the standard
>>> # library, and 72 for strings with "fewer structural restrictions"
>>> # such as docstrings)

>>> # a tool called EditorConfig (editorconfig.org) can help you achieve
>>> # harmony among different collaborators, using different editors--by
>>> # maintaining an easy-to-read config file as part of your project,
>>> # which plugins for various editors (from VS to Vim) will read and
>>> # honor the settings found within

>>> # let's talk about a few other potential pitfalls

>>> # (for a more comprehensive list--some are very advanced, and
>>> # you might never notice them in day-to-day programming), see
>>> # https://wiki.python.org/moin/PythonWarts)

>>> # we talked about .join() being a method on a string (the "joiner")
>>> # not on a list like in some other languages, notably Perl

>>> # it might help to use an "idiom" like this

>>> delim = ','

>>> l = range(0,10)

>>> delim = ', '

>>> delim.join(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 0: expected str instance, int found
sequence item 0: expected str instance, int found

>>> # oops -- here's a gotcha

>>> # Python doesn't implicitly cast everything to a string like, say,
>>> # JavaScript does but it is a "dynamic" language, so you could
>>> # change the /types/ of the contents of a nested data structure,
>>> # like a list, in-place. Python doesn't mind.

>>> l = [str(i) for i in l]

>>> l
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

>>> # see the difference now? (the range was a list--an iterable,
>>> # actually--of integers)

>>> [i for i in range(0,10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> # the call to 'join()' will work now, though, since '.join()'
>>> # operates on a string and returns a string, expecting all of its
>>> # input elements to /also/ be strings (or to have a (__str__ "magic
>>> # method" defined, if they're objects)

>>> delim.join(list)
'0, 1, 2, 3, 4, 5, 6, 7, 8, 9'

>>> # let's talk about slices

>>> # you may have noticed that range() returned values between its two
>>> # arguments, excluding the right "endpoint"

>>> [i for i in range(0,10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> # this is true of Python "slices" (selecting just a portion of a list by
>>> # numerical index)

>>> # it helps if you think of the indexes in the "slice" as
>>> # representing the space /before/ the letters you want.

>>> # you'll probably find the ASCII-art diagram from this page useful
... # https://wiki.python.org/moin/MovingToPythonFromOtherLanguages

>>> python_list_indexes_and_slices = """
... Python indexes and slices for a six-element list.
... Indexes enumerate the elements, slices enumerate the spaces between the elements.
...
... Index from rear:    -6  -5  -4  -3  -2  -1      a=[0,1,2,3,4,5]    a[1:]==[1,2,3,4,5]
... Index from front:    0   1   2   3   4   5      len(a)==6          a[:5]==[0,1,2,3,4]
...                    +---+---+---+---+---+---+    a[0]==0            a[:-2]==[0,1,2,3]
...                    | a | b | c | d | e | f |    a[5]==5            a[1:2]==[1]
...                    +---+---+---+---+---+---+    a[-1]==5           a[1:-1]==[1,2,3,4]
... Slice from front:  :   1   2   3   4   5   :    a[-2]==4
... Slice from rear:   :  -5  -4  -3  -2  -1   :
...                                                 b=a[:]
...                                                 b==[0,1,2,3,4,5] (shallow copy of a)
... """

>>> # so think of the slice indices as corresponding to the spaces
>>> # /between/ the list elements (called "Slice from front" in the
>>> # diagram above)

>>> # ======= DANGER WILL ROBINSON!!! DANGER!!! =======

>>> # oh man, by the way here's the worst one ever, and I don't even
>>> # know why this is allowed (I actually did this to myself, while
>>> # writing this tutorial--for the I don't-know-how-manyth-time)

>>> # you can actually accidentally overwrite built-in functions like
>>> # 'list()' (like I just did above and didn't realize it) with out
>>> # ANY WARNING from Python!

>>> list = [1,2,3,4]  # overwrites function 'list' with list 'list'!

>>> # now this weird error message happens if you expect the 'list'
>>> # that's part of the Python language to still be available for you
>>> # to use; a whole lotta nope!

>>> l = list('hello world')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
'list' object is not callable

>>> # in the REPL ('python', 'ipython', etc.) you can do this to rescue
>>> # the situation:

>>> del(list)  # this rescues the list() function we obliterated above

>>> # but if you do this in a program you'll just have bugs and weird
>>> # behavior that might be difficult to debug

>>> # WATCH OUT FOR THAT ONE!

>>> # now, back to regularly scheduled programming

>>> l = list('hello world')  # works as expected again

>>> l
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

>>> # OK, let's say we want 'hello' from the string above; that's
>>> # staring from the 0th "in-between-space" and going to the 5th
>>> # "in-between"

>>> l[0:5]
['h', 'e', 'l', 'l', 'o']

>>> # another way of thinking about it (if your brain likes intervals,
>>> # like from learning about the number line in math class) is the
>>> # 'start' of a slice is /inclusive/ of the list index and the end is
>>> # /exclusive/

>>> # you can also index from the rear, using negative numbers, and this
>>> # works WAY different from R, so watch out if you're used to R's way

>>> l[-1]
'd'

>>> # say we want just "world"; the end of the list has the name ':', so
>>> # here's how you slice that

>>> l[-5:]
['w', 'o', 'r', 'l', 'd']

>>> # since the 'end' of the slice is exclusive, that's why you can't
>>> # say 'l[-5:-1]' (this would yield ['w', 'o', 'r', 'l'], exclusive
>>> # of the 'd' at index -1)

>>> # as far as simple subscripts of strings (or any kind of list-like
>>> # thing) the 0th character is the first element, and the -1th is the
>>> # last

>>> l[0]  # should be 'h'
'h'

>>> l[-1]  # should be 'd' in "world"
'd'

>>> # also of note: you can't reverse a string, but you can reverse a
>>> # list (Ruby has no problem with this)

>>> 'hello'.reverse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'reverse'
'str' object has no attribute 'reverse'

>>> l = list('hello')

>>> # but it's an in-place operation, so you need to store the string as
>>> # a (list) variable, then do .reverse() on it

>>> l.reverse
<built-in method reverse of list object at 0x11134b848>

>>> # oops, forgot the parentheses

>>> l.reverse()

>>> # returns None, because it modifies the list in-place, but we can
>>> # check to see if it worked

>>> l
['o', 'l', 'l', 'e', 'h']

>>> # you can reassemble a list into a string by using the empty string
>>> # as the "joiner"

>>> ''.join(l)
'olleh'

>>> # OK, let's talk standard library

>>> # the reference for that is
>>> # https://docs.python.org/X.Y/library/index.html, where 'X.Y' is the Python
>>> # major.minor version (e.g., 3.5)

>>> # after including something from the standard library with the
>>> # 'import' statement, you can use the help() function built into
>>> # the REPL (Read-Eval-Print-Loop) to get help on individual objects
>>> # functions

>>> import os

>>> # note that you need to 'import' whatever it it, before running
>>> # help() on it, otherwise you'll get a NameError

>>> help(os.path.basename)

# the output goes through a pager like 'less', but here's what it would
# look like:
#
#     Help on function basename in module posixpath:
#   
#     basename(p)
#         Returns the final component of a pathname
#     (END)

>>> # another useful thing you can do in the REPL (or a program) for
>>> # debugging is the dir() built-in.

>>> # it shows you all the "locals" of an object instance

>>> # so let's make a pretend class to see how that works, and we'll get
>>> # back to 'dir' in a minute

>>> class FooObject:
...     foodict = {}
...     foolist = []
...     fooint  = 3

>>> foo = FooObject()

>>> # that's how you instantiate objects in Python; there is no 'new'
>>> # keyword in the language

>>> foo
<__main__.FooObject object at 0x111bb2780>

>>> # all objects have some kind of printable representation, but
>>> # they're usually not very helpful

>>> # you can provide your own by providing a "__repr__" (the "official"
>>> # string representation of an object) within the class

>>> class FooObject:
...     foodict = {}
...     foolist = []
...     fooint  = 3
...     def __repr__(self):
...         """
...         Returns the "official" string representation of FooObjects
...         Here's the convention for documenting functions and classes in Python
...         It's a triple-quoted (multi-line) string, called a "docstring"
...         """
...         # you can still use regular comments, but the docstring is
...         # special, as we'll see __repr__ should return a string
...         return "<FooObject #{}>".format(id(self))

>>> # notice that class methods need to include 'self' as the first
>>> # argument this is just a thing you have to remember; you'll get a
>>> # runtime error from the interpreter if you forget

>>> # let's instantiate a new FooObject and see what happens when we try
>>> # to print it out

>>> foo = FooObject()

>>> foo
<FooObject #4567029800>

>>> # much better! at least, it's what we /asked/ for, instead of some
>>> # generic default

>>> # now let's look at all the variables that are "in scope" for that
>>> # object

>>> dir(foo)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'foodict', 'fooint', 'foolist']

>>> # a lot of those are "magic" / internal methods and values, but you
>>> # /can/ see the foo{dict|list|int} values in there, too

>>> # this is called "introspection" and it's something Python is
>>> # exceptionally good at

>>> # it's worth mentioning, thought, that Python has no notion of
>>> # "private" variables

>>> # it's long been the policy of the language creator that modules
>>> # shouldn't try to manipulate the internal data structures of other
>>> # modules, but this is allowed between "consenting adults" (see
>>> # also: https://github.com/kennethreitz/python-guide/issues/525)

>>> # a common convention is to make internal "private" variables
>>> # prefixed by two underscores, something the Python runtime does its
>>> # best to obfuscate, but which can still be manipulated by other
>>> # modules with some effort

>>> # the upside of all this is great support for auto-completion in
>>> # the REPL (like 'ptpython') and IDEs, and better debugging error
>>> # messages

>>> # let's see about that "docstring" thing

>>> foo.__doc__

>>> # nothing. let's fix that.

>>> class FooObject:
...     """
...     The FooObject class
...     Contains some random data structures, but doesn't really do
...     anything useful
...     """
...     foodict = {}
...     foolist = []
...     fooint  = 3
...     def __repr__(self):
...         """
...         Returns the "official" string representation of FooObjects
...         Here's the convention for documenting functions and classes
...         in Python. It's a triple-quoted (multi-line) string, called
...         a "docstring"
...         """
...         # you can still use regular comments, but the docstring is
...         # special, as we'll see __repr__ should return a string
...         return "<FooObject #{}>".format(id(self))

>>> foo.__doc__

>>> # still nothing... oh, doh!, we modified the class, but this 'foo'
>>> # is an instance of the /old/ class! let's try again...

>>> foo = FooObject()

>>> foo.__doc__
"\n    The FooObject class\n    \n    Contains some random data structures, but doesn't really do anything useful\n    "

>>> # look familiar?

>>> # let's see if help() works now

>>> help(FooObject)

# the output goes through a pager like 'less', but here's what it would
# look like
#
#     Help on class FooObject in module __main__:
#     
#     class FooObject(builtins.object)
#      |  The FooObject class
#      |
#      |  Contains some random data structures, but doesn't really do anything useful
#      |
#      |  Methods defined here:
#      |
#      |  __repr__(self)
#      |      Returns the "official" string representation of FooObjects
#      |      Here's the convention for documenting functions and classes in Python
#      |      It's a triple-quoted (multi-line) string, called a "docstring"
#      |
#      |  ----------------------------------------------------------------------
#      |  Data descriptors defined here:
#      |
#      |  __dict__
#     :

>>> # did you see it? it became part of the output of the help()
>>> # function

>>> # so it's super-useful and a good habit in general to add this kind
>>> # of documentation to your classes / functions

>>> # there's almost no reason not to!

>>> # it works on functions, too:

>>> help(foo.__repr__)

# which is again paged with 'less' but it would look like
#
#     Help on method __repr__ in module __main__:
#     
#     __repr__() method of __main__.FooObject instance
#         Returns the "official" string representation of FooObjects
#         Here's the convention for documenting functions and classes
#         in Python It's a triple-quoted (multi-line) string, called
#         a "docstring"
#     (END)

>>> # docstrings undergo some reformatting (as mentioned in this PEP:
>>> # https://www.python.org/dev/peps/pep-0257) so that the leading and
>>> # trailing whitespace doesn't throw things off in the help() display

>>> help(os.path.basename)

#   Help on function basename in module posixpath:
#   
#   basename(p)
#       Returns the final component of a pathname
#   (END)


>>> os.path.basename.__doc__
'Returns the final component of a pathname'

>>> foo.__repr__.__doc__
'\n        Returns the "official" string representation of FooObjects\n        Here\'s the convention for documenting functions and classes in Python\n        It\'s a triple-quoted (multi-line) string, called a "docstring"\n        '

>>> # see all that extra whitespace? it gets trimmed off

>>> help(foo.__repr__)

>>> # OK, now some things to watch out for between Python 2.x (still the
>>> # default on many Linux systems) and 3.x (the future)

>>> # Python 2.7 will no longer be supported after 2020, so the
>>> # answer to the question of "Should I learn Python 2.x or 3.x?"
>>> # is definitely "Yes." (to both, but if you're just starting out,
>>> # Python 3.x)

>>> # Python 3.x removed a lot of duplicate methods and inconsistencies,
>>> # and fixed some of the "warts" in the language (causing some
>>> # breaking changes that make code written for Python 2.x
>>> # incompatible), and also adds more robust Unicode (international
>>> # character set) support

>>> # one big one is print() is a function, not a language keyword.

>>> # on Python 2.x you can get the "new" print function by putting

>>> from __future__ import print_function

>>> # as the first line of your script, but in Python 3.x that's not
>>> # strictly necessary unless you're writing a script that you want to
>>> # run with both versions (this becomes quite difficult for all but
>>> # the most trivial scripts)

>>> # So just remember to put parens around your print() statements

>>> # a second is the behavior of the division operator, '/'

>>> # in Python 3.x, it does normal division, returning a float; in
>>> # Python 2.x (as in C and C++) it does integer (floor) division

>>> 3/5
0.6

>>> # would have been '0' in Python 2.7.x

>>> # you can get the old behavior with the "flooring" division operator, new
>>> # in later version of Python

>>> 3//5
0

>>> # this rounds the result down; it's useful for some things, like
>>> # image manipulation (a grid of pixels can only have whole-numbered
>>> # values)

>>> # also many things that returned lists in Python 2.x return iterables,
>>> # like we saw with zip()

>>> zip([1,2,3],[4,5,6])
<zip object at 0x111d79a88>

>>> # this would have returned a list in Python 2.7.x

>>> # now you have to either spin out all the values with a 'for' loop or
>>> # a list comprehension (basically a mini for-loop) or use the 'list()'
>>> # function

>>> list(zip([1,2,3],[4,5,6]))
[(1, 4), (2, 5), (3, 6)]

>>> [i for i in zip([1,2,3],[4,5,6])]
[(1, 4), (2, 5), (3, 6)]

>>> for i in zip([1,2,3],[4,5,6]):
...     print(i)
(1, 4)
(2, 5)
(3, 6)

>>> # one other gotcha, that's kind of an odd feature of the language, but
>>> # not specific to 2.x or 3.x is putting "mutable default arguments" in a
>>> # function

>>> # in other words, don't do this:

>>> def my_func(value, list_arg=[]):
...     list_arg += value

>>> # it won't do what you expect

>>> l = []

>>> my_func(3, l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in my_func
TypeError: 'int' object is not iterable
'int' object is not iterable

>>> l
[]

>>> def my_func(value, list_arg=[]):
...     list_arg.append(value)

>>> my_func(3, l)

>>> l
[3]

>>> my_func(3, l)

>>> l
[3, 3]

>>> # you'd expect that list_arg would get a new empty list every time the
>>> # function is called, but nope

>>> # that list is created and allocated *once*, when the function is
>>> # defined, and it persists between subsequent calls to the function,
>>> # which is why it got appended to, rather than recreated the second
>>> # time we called my_func(), above

>>> # you probably want to use 'None' as a default value for a function
>>> # where you need a more complicated "default" than just a simple
>>> # primitive (string or int) remember objects are mutable (they can
>>> # be changed in-place)!

>>> # as in, you probably want to do is make the default value None and 
>>> # test for None-ness with the 'is' keyword.

>>> # there is an in-depth discussin of /why/ (a lot better than I could
>>> # explain) at https://stackoverflow.com/q/1132941

