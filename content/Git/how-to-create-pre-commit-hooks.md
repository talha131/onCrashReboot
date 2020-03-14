Title: How To Create pre-commit Hooks For Git
Tags: git, hooks, pre-commit
Category: Git
Date: 2020-03-14 16:31
Slug: how-to-create-precommit-hooks-for-git
comment_id: d12e9ah5lnuy-how-to-create-precommit-hooks-for-git
Subtitle:
Summary: In this article, I guide you on creating Git hooks using pre-commit.
Keywords:

Git has a robust [system of hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks). Hooks are some scripts that fire off when specific actions occur. For example, you may want to make sure your code builds successfully before pushing it to the upstream. You can use Git hooks to define a script that builds your code when you issue `git push` command. Then, Git pushes the code only when the script runs successfully. If there is a build error, the push will not happen.

Most Git hooks are local to your repository, called [client-side hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks#_client_side_hooks).

> It's important to note that client-side hooks are **not** copied when you clone a repository.

It means if you add a hook to your repository, your coworker working on a fork of the repository, does not have access to your hooks. It makes it challenging to share your hooks with others. Even if you email the script to your coworker, how do you update his copy of the script when you make a change in your copy?

[Pre-commit](https://pre-commit.com/) is a beautiful tool that makes syncing and updating the hooks a breeze. You can see its documentation to see how to [set it up](https://pre-commit.com/#install).

Here, I explain the process of creating a Git hook that can be used with pre-commit.

## Create a test repository

We will use this repository to test the hook.

```bash
$ mkdir "test-my-hook"
$ cd "test-my-hook/"
$ git init
Initialized empty Git repository in /Users/talha/Repos/temp/test-my-hook/.git/
```

## Enable pre-commit in test repository

Create a file `.pre-commit-config.yaml` in the root of the repository.

```bash
$ pre-commit sample-config > .pre-commit-config.yaml
$ git add .pre-commit-config.yaml
$ git commit -m "add pre-commit configuration"
```

## Add a test file in test repository

Add a file on which we want pre-commit to run the hook.

```bash
$ echo "some random text" > example.text
$ git add example.text
```

Notice, I have staged the file `example.text` but I have not committed it.

Now that we have a repository ready to run our test hook, let's move to the next step: creating a pre-commit hook.

## Create a hook repository

Create a new repository, outside "test-my-hook" directory, where you will define your pre-commit hook.

```bash
$ cd ..
$ mkdir pre-commit-test-hook
$ cd pre-commit-test-hook/
$ git init
Initialized empty Git repository in /Users/talha/Repos/temp/pre-commit-test-hook/.git/
```

## Create pre-commit hook configuration

From the [documentation](https://pre-commit.com/#new-hooks), we know a hook repository must contain a `.pre-commit-hooks.yaml` file. Let's create it.

```bash
$ touch .pre-commit-hooks.yaml
```

Now edit the content of this file,

{% include_code pre-commit/.pre-commit-hooks.yaml lang:yaml pre-commit hook configuration %}

1. `id` is the id of the hook. Users of your hook refer to your hook using this ID.

2. `entry` is the name of the executable file that pre-commit runs. Think of it as the `main()` of a C program.

3. `types` are the types of file on which this hook runs. You can also use `files`.

4. `exclude` is a [Python regular expression](https://docs.python.org/3.8/library/re.html#regular-expression-syntax) to exclude specific files. In this case, it tells pre-commit to _not_ run the hook on files that have `.yaml` or `.yml` extension.

5. `language` tells pre-commit how to install the hook. If you use `'script'`, it means your hook is a Bash script.

6. `args` this is optional. It is used to pass arguments to your script. You can define it or leave it for your users to define it in their configuration. Of course, if your script does not accept any argument, then `args` is redundant. Here we pass two arguments, `--example`, and `example2`.

You can use other languages like Python, to create your hook. But in that case, you must provide installation instructions so that pre-commit can install the hook. For example, in the case of Python, you need `setup.py`.

A Bash script does not require any installation or extra tools. Bash is ubiquitously present wherever Git is, which is why Bash is preferred to write the hooks.

## Create the Hook Script

Now we are going to add some code to the `run-test-hook.sh` file.

{% include_code pre-commit/run-test-hook.sh lang:bash bash script %}

Commit your additions.

```bash
$ git add .pre-commit-hooks.yaml run-test-hook.sh
$ git commit -m "add an example hook"
```

## Test your hook

Luckily, you do not have to publish your hook first to test it. You can use pre-commit to run this hook locally.

Go to the [test repository](#create-a-test-repository) we created to test the hook.

```bash
$ cd "test-my-hook"
```

Run the following command in it,

```bash
pre-commit try-repo ../pre-commit-test-hook/ test-hook --all-files --verbose
```

1. `pre-commit try-repo` is the command and the switch.

2. `../pre-commit-test-hook` is the path to your `pre-commit-test-hook` repository on your file system. This path depends on where you have created these repositories.

3. `test-hook` is the ID of the hook. [Remember it](#create-pre-commit-hook-configuration)?

4. `--all-files` runs the hook on all the supported files.

5. `--verbose` is important for debugging. It displays the output of the `echo` statements in the Bash script.

## The output of the hook

When you run the hook, with the `verbose` option, you should see the following output besides a bunch of other pre-commit logs.

```bash
The hook is running
--example1 --example2 example.text
```

Remember the `--example1` and `--example2` arguments that [we mentioned earlier](#create-pre-commit-hook-configuration)?

Pre-commit passes those arguments first and then the list of files on which the hook could run to our script.

Notice, it does not pass `.pre-commit-config.yaml` file although it is a text file and present in the repository. It is because we have excluded all files ending in `.yaml` or `.yml` from the hook.

## What's next?

Now that you have the hook running, you can modify your copy of `run-test-hook.sh`. You can use a Bash script to parse the switches and arguments, using [`getopts`](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/getopts.html) for example.

Then you can use Bash and other command-line utilities to modify the files.

When your hook is ready, you can push it Github so that others can use it.

[TekWizely/pre-commit-golang](https://github.com/TekWizely/pre-commit-golang) has some brilliants scripts that you can use to learn and improve your hooks. I have created a simple hook for my [Go](https://golang.org/) projects, which you can see here, [talha131/pre-commit-golang](https://github.com/talha131/pre-commit-golang).
