
# misc_utils
making my life easier with some misc tools

# Files

### [**dup.py**](./dup.py) - Duplicates the content from a file into a new one with an incremented number

<b>*Specific to Holberton's Advanced HTML project.</b>
> [!CAUTION]
> DO NOT run chmod on this. It causes an infinite loop somewhere.

To duplicate and increment by 1 pass the file you want to duplicate:
<pre>
  >>> python3 dup.py 0-index.html
</pre>
This will create `1-index.html` with all the contents of `0-index.html`
<br><br>
To duplicate and increment by any number pass the number you want after the file:
<pre>
  >>> python3 dup.py 3-index.html 2
</pre>
This will create `5-index.html` with all the contents of `3-index.html`.

To change file names pass the new name after the file or after the number you wish to increment by:
<pre>
  >>> python3 dup.py 10-index.html styleguide 
</pre>
This will create `11-styleguide.html` with all the contents of `10-index.html`
<pre>
  >>> python3 dup.py 10-index.html 4 new
</pre>
This will create `14-new.html` with all the contents of `10-index.html`

<hr>

### [**nf.py**](./nf.py) - Creates a new file and makes it executable unless it is .txt.

To create a python script :
<pre>
>>> ./nf.py <b>example_file.py</b>
</pre>
First line of the new file will be `#!/usr/bin/python3` followed by a new line.
<br><br>
To create a text file :
<pre>
>>> ./nf.py test.txt <b>here is some text with spaces</b>
</pre>
Creates the text file with the provided string as the first line.
If no string is provided it creates an empty file.
<br><br>

>[!NOTE]
> nf.py can create all types of files. Just specify the type.
