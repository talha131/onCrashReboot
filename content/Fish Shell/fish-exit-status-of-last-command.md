Title: Use Exit Status of Command in Fish Function
Tags: fish, scripting, exit status
Category: Fish Shell
Date: 2019-09-15 21:17
Slug: use-exit-status-of-command-in-fish-function
comment_id: zd1vc5hwnijp-use-exit-status-of-command-in-fish-function
Subtitle:
Summary: In Fish shell, you can read the exit status of the last command executed and use it in number of ways
Keywords:

In the following examples, I am going to use `rg`, i.e. [ripgrep](https://github.com/BurntSushi/ripgrep). It's a modern and faster equivalent of the traditional `grep` and `ack` commands. `rg` also has a sane default configuration that does not require you to enable command switches to do mundane tasks like searching recursively or respecting `.gitignore` rules.

## `$status` variable

Fish Shell stores the exit status of the last command in the `$status` variable.

```fish
➤ true
➤ echo $status
0
➤ false
➤ echo $status
1
➤ blahblah
fish: Unknown command blahblah
➤ echo $status
127
```

Use it with `if` and `test` in your scripts.

```fish
function example -d 'Example Fish function'
    rg $argv[1] > /dev/null
    if test $status -eq 0
        echo "$argv[1] found"
    else
        echo "$argv[1] not found"
    end
end
```

Notice how I used `test` to check the value of `$status` variable.

You can read more about `$status` variable in [fish documentation](https://fishshell.com/docs/current/index.html#variables-status).

## Use `and`, `or` Combiners

Fish also supports `and` and `or`.

1. `and` runs the command if the last command execution was successful.
1. `or` runs the command if the previous command execution failed.

```fish
➤ rg "blahblah" > /dev/null; and echo "found"; or echo "not found"
```

We can use newlines instead of `;`. Use Alt (⌥Option key on macOS) and ⌤Enter key to insert newlines.

```fish
➤ rg "blahblah" > /dev/null
   and echo found
   or echo not found
```

You can read more about `and`, `or` combiners in [fish shell documentation](https://fishshell.com/docs/current/tutorial.html#tut_combiners).

### Use `and`, `or` Combiners with `begin`

We can do complex operations like running more than one command using `begin` with the combiners.

```fish
function example -d 'Example Fish function'
    rg $argv[1] > /dev/null
    and begin
        echo "$argv[1] found"
    end
    or begin
        echo "$argv[1] not found"
    end
end
```

Between `begin` and `end` you can write more commands or even more conditions.

You can read more about `begin` [here](https://fishshell.com/docs/current/commands.html#begin).

## Use `if`

You do not have to use the `$status` variable and `test` command. You can use `if` directly.

```fish
function example -d 'Example Fish function'
    if rg $argv[1] > /dev/null
        echo "$argv[1] found"
    else
        echo "$argv[1] not found"
    end
end
```

## Store output of a command in a variable and `test` it

Sometimes reading the exit status of a command is not enough. Take `git cherry`, for example. This command returns the unpushed git commits.

Whether it finds unpushed git commits push or not, it always exits successfully.

Consider the following script,

```fish
➤ git cherry
   and echo commits found
   or echo commits not found
```

I run it in a repository whose `HEAD` is one commit ahead of the upstream. The output I get is

```fish
+ 12dc1f697b714336b118f1361fa49a4ef71c44b7
commits found
```

Then I run it in a repository whose `HEAD` is in sync with the upstream. The output is,

```fish
commits found
```

Even though `git cherry` couldn't find any unpushed git commits. I cannot employ previously suggested methods that rely on the exit status of the command.

In this case, we have to `test` the output of the command.

### Test Output As String

Consider the following script,

```fish
function example -d 'Example Fish function'
    if test -n "(git cherry)"
        echo commits found
    else
        echo commits not found
    end
end
```

Do you notice the quotes around `(git cherry)`? _It is crucial._

See, `git cherry` can return more than one line in the output. With quotes, the Fish shell treats the command output as one argument, even if it has newlines.

If we remove the quotes, then if newlines are present, the output becomes a list or an array.

`test -n` returns true if the length of the string is non-zero.

You can read about `test` command [here](https://fishshell.com/docs/current/commands.html#test).

### Count Number Of Lines In Output

It is not necessary to use quotes. We can refactor the above script to handle arrays and then count the number of indices in the array.

```fish
function example -d 'Example Fish function'
    if test (count (git cherry)) -ne 0
        echo commits found
    else
        echo commits not found
    end
end
```

`count` command returns the number of elements in the list. So with `count (git cherry)`, we read the number of lines returned and compare it to 0.

`test -ne` returns true if the first number is not equal to the second number.

`count` documentation is available [here](https://fishshell.com/docs/current/commands.html#count).

## Example

You can see the above discussion in action in a script that I wrote to periodically push out git commits to the upstream, every 10 seconds.

[Source Code of `tm_git_push` script](https://github.com/talha131/dotfiles/blob/master/fish/functions/tm_git_push.fish)
