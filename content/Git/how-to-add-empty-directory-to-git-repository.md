Title: How To Add An Empty Directory To A Git Repository
Tags: gitignore, keep, tutorial
Category: Git
Date: 2020-04-04 13:34
Slug: how-to-add-an-empty-directory-to-a-git-repository
comment_id: g5sw8zvp2cob-how-to-add-an-empty-directory-to-a-git-repository
Subtitle: Two Different Use Cases
Summary: Git lets you only add files to the index. In this article, I describe two solutions and their real life examples to add an empty folder to the Git.
Keywords:

Git lets you only add files to the index. If you want to add a directory, then [Git does not have a builtin solution](https://git.wiki.kernel.org/index.php/Git_FAQ#Can_I_add_empty_directories.3F) for you. Of course, there are ways to work around this issue.

## Add a directory but ignore its contents

If you want to add an empty folder to Git index, but you want Git to omit the present and future contents of the directory. Then, create a `.gitignore` file inside the directory and add these lines to the `.gitignore` file:

```bash
# Disregard this entire folder
*
# Except this .gitignore file
!.gitignore
```

Then add and commit this `.gitignore` file. This solution results in a directory that is present inside Git, but its contents never get added to the Git.

A possible use case scenario of this solution is to add the debug folder of a project to the index. Almost always, you do not want the contents of your debug folder to end up in the Git index. But you may need to keep the debug folder in the index because you have relative paths in your code or you want all your teammates to have the same folder structure.

## Add an empty directory and track its future contents

Say, you want to add a folder to the index. It is currently blank, but you plan to add files to it that Git should track. The only solution is to create a file in the directory and add it to the Git.

Git community has settled on creating an empty file called `.keep` in the directory and adding it to the index.

```bash
mkdir hello
cd hello
touch .keep
git add .keep
git commit -m "add empty directory called hello"
```

`.keep` is not an officially prescribed name by the Git. You can use any other name. You can use "README" or "ABOUT", or even ["Intentionally Blank File"](https://en.wikipedia.org/wiki/Intentionally_blank_page). Your choice. `.keep` is the most preferred filename for this purpose. The `.` is the beginning of its name, ensures that it will stay hidden on Linux and macOS file systems.

A possible use case scenario is if you are creating a boilerplate folder structure, which you want to reuse in all your React projects. You create empty folders for containers, components, API and store. You add these empty folders to the Git repository. You then use the repository as a template for your future projects.
