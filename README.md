# nf - New File

The nf command is a simple but powerful tool that can be used to create new files with a template based on the file extension or template switch. It has several optional arguments that allow you to customize the file creation process, add or remove custom templates, and even open the file in your preferred editor.


<details>
<summary>installation:</summary>
<br/>
<details>
<summary>Linux</summary>
user only

```
curl -s https://raw.githubusercontent.com/evantaur/nf/main/dist/nf > ~/.local/bin/nf && \
chmod +x ~/.local/bin/nf
```


global
```
sudo sh -c 'curl -L https://raw.githubusercontent.com/evantaur/nf/main/dist/nf \
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
usage: nf [-h] [--upgrade] [-d] [-v] [-x] [-t TEMPLATE] [-a] [-r] [-l]
          [--print-only] [--vars VARS] [--variables] [--va name value]
          [--vr VR] [--variable-parse VARIABLE_PARSE] [-e] [-X]
          [--change-editor]
          [filename]

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
  --print-only          Do not write to file

Variables:
  Create or remove variables to be used with templates

  --vars VARS           use variables from JSON file or from command line
                        using {"varname":"varvalue"}
  --variables           lists variables
  --va name value, --variable-add name value
                        add variable
  --vr VR, --variable-remove VR
                        remove variable
  --variable-parse VARIABLE_PARSE
                        parses all variables from a template file and saves
                        them for later use

Editor:
  Use these if you want to open the file after it has been created

  -e, --edit            open in editor
  -X, --execute         Execute after saving
  --change-editor       change editor

Examples:

  # Creates a new file called test.sh
  # with a shebang #!/bin/bash

  nf test.sh

</pre>