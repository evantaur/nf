# nf - New File

Creates a new file with a template based on the file extension or template switch.



<details>
<summary>installation:</summary>
<br/>
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


usage:
```
usage: nf [-h] [-d] [-v] [-x] [-t TEMPLATE] filename

options:
  -h, --help            show this help message and exit
  -d, --dir             Create directory structure if needed
  -v, --version         Show version and exit
  -x                    Give execute permission (chmod +x)
  -t TEMPLATE, --template TEMPLATE
                        use this template

Examples:

  # Creates a new file called test.sh
  # with a shebang #!/bin/bash

  nf test.sh

```
