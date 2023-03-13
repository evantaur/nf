<details>
<summary>Templating</summary>
 Templating
 
**nf** supports using variables in templates that allows you to create dynamic templates for your projects. It uses a simple syntax that can be easily extended with additional options.

### Usage

To use variables with the **nf** Template Engine, create a template file with the following syntax:
```  
<|variable|>
```
You can customize the variable by adding options between square brackets. The available options are:

-   `default=str`: Sets the default value to `str`.
-   `desc=this is description`: Sets the description for the variable.
-   `require` or just `r`: Ignores saved variables and always asks for this variable upon creation.
-   `select=(opt1,opt2,opt3)`: Asks the user to select from these predefined variables.
-   `select={"a":"hello world","b": "Goodbye world"}`: Supports dictionaries where the key is considered a value for the variable and the value is considered as a description.
-   `index`: Used with select, it will use index value instead of opt1, opt2,... It will also modify the text values to act as a description.

### Examples

Here are some examples of how to use Your Template Engine:

-   A normal variable:
`<|name|>`

-   A normal variable with a description:
`<|name[desc=Your name]|>`

-   A select with a tuple:
`<|path[desc=Where to go|select=(left,right)|default=1|r]|>` 

-   A select with a tuple but with an index:
`<|router[desc=State of router|select=(false,true)|default=1|require|index]|>` 

-   A select with a dictionary:
`<|connection[desc=Select if connection is made to localhost or url|select={"localhost":"No contact to outside world","google":"Send all your data to google!"}|default=0|require]|>`



if you have a template file formed as following:
```  
The quick brown <|creature[default=fox]|> jumps over the lazy dog.
```
It will use a variable creature if it exsists in config, if not it will ask user to input one:
```
Enter value for creature  
:fox
```
and you end up with this file:
```
The quick brown fox jumps over the lazy dog.
```

some more examples here:
```
<|age[desc=Enter your age|default=18]|>

<|fruit[desc=Select your favorite fruit|select={"apple":"Sweet and crunchy","banana":"Rich and creamy","orange":"Juicy and refreshing"}]|>

<|phone[desc=Enter your phone number|default=555-555-5555]|>

<|address[desc=Enter your address|default=123 Main Street|r]|>

<|email[desc=Enter your email|r]|>

```
</details>
