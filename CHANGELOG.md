#### 1.001
- Added variables to use in templates.

New commands:
- `-X` execute after editing.
-  `--print-only` do not write a file, just print the template.
- `--vars` use variables from JSON file or from command line using `'{"varname":"varvalue"}'` .
- `--variables` lists variables.
- `--va <name> <value>`,
`--variable-add <name> <value>` add variable
- `--vr <name>`,
`--variable-remove <name>` remove variable
- `--variable-parse <template>` parses all variables from a template file and saves them to config for later use

#### 1.000
Initial release
