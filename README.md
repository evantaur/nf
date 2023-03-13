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
Traceback (most recent call last):
  File "/home/runner/work/nf/nf/dist/nf", line 50, in <module>
    conf = config()
  File "/home/runner/work/nf/nf/dist/nf", line 29, in __init__
    self.userTemplates     = tuple(os.listdir(self.userTemplatesPath))
FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/.config/nf/templates'

</pre>