
# misc_utils
making my life easier with some misc tools

# Files


#### [**nf.py**](./nf.py) - Creates a new file and makes it executable unless it is .txt.

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
