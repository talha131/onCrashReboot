Title: Fish Function To Split Pathname And Return Array
Tags: scripting, sed, regex, array, fish, fish-shell
Category: Command-line & Shell
Date: 2019-08-29 00:41
Slug: fish-function-to-split-pathname-and-return-an-array
comment_id: mqutgv3djwor-fish-function-to-split-pathname-and-return-an-array
Subtitle:
Summary: Create a fish function that splits pathname and return the result in an array
Keywords:

[TOC]

My preferred terminal for daily use is [fish](https://fishshell.com/). Quite
often I have to split a path and extract the filename from it. Unlike Bash, fish
does not have `basename` utility. I use sed to extract the filename from the path.

It made sense to create a function so that I wouldn't have to keep repeating the same regex.

## Fish Function

    #!fish
    function tm_split_path -d 'Return filename, ext, and directory from the path'
        echo $argv[1] | sed 's/\(.*\)\/\(.*\)\.\(.*\)$/\2\n\3\n\1/'
    end

Line 1
: Function name is `tm_split_path`. I prefer to prefix my shell functions with a
common prefix. This way, I don't have to recall the function name. I just type
`tm_` and press `tab` key. Fish shell automatically suggests the list of
possible functions.

    What follows `-d` is the description of the function. It appears in the list of suggestions.
    Notice the description in highlighted line in the following list.

    ![fish shell suggestion list demo]({static}/images/fish-shell-function-description.png)

Line 2
: `$argv` is the variable which contains the arguments passed to the function. It's an array.

!!! Important "Remember"

    Array index in Fish starts from 1, **not** 0.

## sed expression

I have written in detail about sed expression [here]({filename}../Command Line/split-path-into-filename-extension.md).

Here is an example output,

```bash
$ echo "/User/talha/content/images/README.example.md" | sed 's/\(.*\)\/\(.*\)\.\(.*\)$/\1\n\2\n\3/'
README.example
md
/User/talha/content/images
```

## Return Array

`\n` in the replace pattern of sed expression is important. Each part of the
pathname is printed on the newline.

Fish automatically converts the input that has newlines into an array.

!!! Important "Create Array In Fish"

    1. List every item on a new line
    1. Capture those lines in a command substitution

Now I can use the function, `tm_split_path`, from other fish functions or scripts this way:

```fish
set result (tm_split_path "/Library/Extensions/File.kex")
echo Filename: $res[1]
echo Extensiion: $res[2]
echo Directory: $res[3]
```

`(tm_split_path "/Library/Extensions/File.kex")` prints the filename, extension and directory, each on its own line.

`set` assigns those three lines to `result` variable.

Fish automatically assumes that the result is an array because of the new lines present.

This way, I can refer to filename, extension and, directory using array indices, like

1. `$res[1]` for filename
1. `$res[2]` for extension
1. `$res[3]` for directory

## Example

You can view complete script [here](https://github.com/talha131/dotfiles/blob/master/fish/functions/tm_split_path.fish).

This script also handles the case when the given argument does not have directory in it, like "filename.ext".
