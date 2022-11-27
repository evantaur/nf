# nf - New File

Creates a new file with a template based on the file extension or template switch.



<details>
<summary>installation:</summary>
<br/>
<details>
<summary>Linux</summary>
user only

```
curl -s https://raw.githubusercontent.com/evantaur/nf/main/nf > ~/.local/bin/nf && \
chmod +x ~/.local/bin/nf
```


global
```
sudo sh -c 'curl -L https://raw.githubusercontent.com/evantaur/nf/main/nf \
> /usr/local/bin/nf && chmod +x /usr/local/bin/nf'
```
</details>

<details>
<summary>Windows</summary>

```
TBA
```
</details>


</details>


usage:

<pre>
usage: nf [-h] [--upgrade] [-d] [-v] [-x] [-t TEMPLATE] [-a] [-r] [-l] [-e]
          [--change-editor]
          filename

Creates a new file with a template based on the file extension or template switch

positional arguments:
  filename              filename

optional arguments:
  -h, --help            show this help message and exit
  --upgrade             Upgrade script
  -d, --dir             Create directory structure if needed
  -v, --version         Show version and exit
  -x                    Give execute permission (chmod +x)
  -t TEMPLATE, --template TEMPLATE
                        use this template
  -a, --add             add file as custom template.
  -r, --remove          remove custom template
  -l, --list            list templates

Editor:
  Use these if you want to open the file after it has been created

  -e, --edit            open in editor
  --change-editor       change editor

Examples:

  # Creates a new file called test.sh
  # with a shebang #!/bin/bash

  nf test.sh

</pre>