Title: Use sed To Split Path Into Filename, Extension, and Directory
Tags: scripting, array, sed, regex
Category: Command-line & Shell
Date: 2019-08-28 13:08
Slug: use-sed-to-split-path-into-filename-extension-and-directory
comment_id: 1zovl356murf-use-sed-to-split-path-into-filename-extension-and-directory
Subtitle:
Summary: Split a path into filename, extension, and directory using sed and fish shell. Return an array from fish function
Keywords:

[TOC]

## sed Expression

```bash
echo $var | sed 's/\(.*\)\/\(.*\)\.\(.*\)$/\2\n\3\n\1/'
```

The regex used is `\(.*\)\/\(.*\)\.\(.*\)$`. Lets analyze it step by step.

Let's say the path is `/User/talha/content/images/README.example.md`.

## Extract Directory From Path

The first part of the regex is `\(.*\)\/`.

1. `\(` escapes `(`
1. `.` means any character
1. `*` means any number of times
1. Combined, `.*` means match all the characters in a string
1. `\)` escapes `)`
1. `\/`, escapes `/`

`()` is used for capturing the match. sed matches the string and captures it.
You reference the first captured match using `\1`; second captured match using
`\2`; third using `\3` and so on. In this example, `.*` is in-between `()`,
therefore sed captures it.

`.*` means all the characters from the start.

`\(.*\)` is followed by `\/`. sed matches all the characters from the start until
it finds the `/` character.

sed regex matcher is greedy. It means it selects the longest possible match.
In our example path, sed does not stop matching at `/User`. Instead, it keeps
matching until it runs out of the `/`. Hence it matches:

<mark>/User/talha/content/images/</mark>README.example.md

Because `.*` is enclosed inside brackets `\(` and `\)`. sed captures the match, which is the first capture in the expression. It can be referenced using `\1`.

## Extract Filename From Path

The second part of the regex is `\(.*\)`.

1. `\(` escapes `(`
1. `.` means any character
1. `*` means any number of times
1. Combined, `.*` means match all the characters in a string
1. `\)` escapes `)`

So `.*` means all characters, and because of brackets, capture it, which is the second capture; hence, it is referenced using `\2`.

However, where sed starts the match from? It starts match right where the first part ended.

/User/talha/content/images/<mark>README.example.md</mark>

Till where will sed end the match? Good question. It depends on the third part of the regex.

## Extract File Extension From Path

The third part of the regex is `\.\(.*\)$`.

1. `\.` escapes `.`. It means literal `.`
1. `\(` escapes `(`
1. `.*` any string
1. `\)` escapes `)`
1. `$` end of the string

It means, **start from the end of the string**, and move towards left, till a `.`
is found. Match any character between last `.` and the end of the string and
capture it.

This part of the regex, matches:

/User/talha/content/images/README.example<mark>.md</mark>

## What Is Matched

When all these parts are combined, we get the following matches

1. <mark>/User/talha/content/images/</mark>README.example.md
1. /User/talha/content/images/<mark>README.example</mark>.md
1. /User/talha/content/images/README.example<mark>.md</mark>

## What Is Captured

Notice, in the first part, `\/` is outside the capturing `\)`. In the third part, `\.` is placed before `\(`. Because they are not inside the `()`, they are not captured.

To understand, compare the captured result with the matched result.

1. <mark>/User/talha/content/images</mark>/README.example.md
1. /User/talha/content/images/<mark>README.example</mark>.md
1. /User/talha/content/images/README.example.<mark>md</mark>

## Replace Pattern

Let's focus on the replace pattern of the sed expression. `\2\n\3\n\1`

1. `\2` prints the second captured group, which is [filename](#extract-filename-from-path)
1. `\n` prints new line
1. `\3` prints the third captured group, which is [file extension](#extract-file-extension-from-path)
1. `\n` prints new line
1. `\1` prints the first captured group, which is [directory](#extract-directory-from-path)

## Example Output

Lets run our example through the expression,

```bash
$ echo "/User/talha/content/images/README.example.md" | sed 's/\(.*\)\/\(.*\)\.\(.*\)$/\1\n\2\n\3/'
README.example
md
/User/talha/content/images
```

## sed for macOS user

sed version that comes with macOS does not support `\n`. You need to install `gnu-sed`

```bash
brew install gnu-sed
```

Then replace `sed` with `gsed` in the command.

## Further Readings

1. [sed manual](https://www.gnu.org/software/sed/manual/sed.html)
1. [Create shell script to reuse sed expression]({filename}../Command-line and Shell/fish-function-split-path-return-array.md)
