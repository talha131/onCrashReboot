Title: How I Converted C# Yellow Book Sample Code To Images
Tags: fish, fish-shell, scripting, c-sharp
Category: Command-line & Shell
Date: 2020-03-21 19:09
Slug: how-i-converted-c-sharp-yellow-book-sample-code-to-images
comment_id: 3vtbey521uwq-how-i-converted-c-yellow-book-sample-code-to-images
Subtitle: And Why
Summary:
Keywords: I converted C# Yellow Book sample code to images to force students to type the code samples.

## What is C# Yellow Book

[Rob Miles](https://www.robmiles.com/)' book, [The C# Yellow
Book](https://www.robmiles.com/c-yellow-book) is a beginner-friendly book
to introduce students to C# and programming in general. It is short and makes a
for a fun read. The book is not only free, but it also comes with code samples,
that a student can use to learn and test their concepts.

## Why convert code to images

I picked this book for a Coding Bootcamp that I am running in my local
community. I want my students to read the code samples, run them in their
Visual Studio, and explain the code line by line. It is a simple task. Unfortunately, many students
take the copy-paste path to cheat through the assignment.

I have observed that learners who make it a habit of typing the examples from
the books and coding samples perform better than those who just read the
examples. Learning programming is like learning to swim. You cannot
learn to swim by merely reading about it. Perhaps, when you are familiar with a
language and have a few years of experience under your belt, you can skip over
the trouble of typing the examples. But when you are new, typing and trying the
example code will only help you understand it better.

So to force some of my challenging students to type, I decided to provide them
with the code samples in image formats.

## How to convert code to images

[Carbon](https://carbon.now.sh/) is easy to use, and performant website
that converts your source code to beautiful photos. You can customize the
programming language parser, fonts, themes, and even window type. It is a
fantastic service.

There is a third-party command-line tool [carbon-now-cli](https://github.com/mixn/carbon-now-cli) that lets you use the Carbon service from the comforts of your terminal.

## What's the challenge

Download the code samples and archive and views its content. Notice,

1. It has 57 folders
1. Each folder contains a complete Visual Studio project
1. All projects are named `YellowBookSamples`
1. Project folders have a `bin` directory that contains the debug build of the project
1. Project folders also have an `obj` directory which holds intermediate files

I do not need to distribute the `bin` and `obj` folder. I also do not need Visual Studio projects. I expect students to create the projects themselves.

Only files that I want to loot from this sample archive is the `Program.cs` file present in every folder.

## The objective

Write a fish shell script that will pick `Program.cs` file from each folder, rename it to the folder name, convert it to an image, and then place it in a new destination folder.

So if a `Program.cs` file is in "Code Sample 37 Simple Interface" folder. I want a `Code Sample 37 Simple Interface.cs.png` file.

Let's get this task done.

### Get `carbon-now-cli`

Install [carbon-now-cli](https://github.com/mixn/carbon-now-cli).

```bash
yarn global add carbon-now-cli
```

### Fish Shell script -- Step by step

Unzip the archive and `cd` into the folder.

Run the following fish shell script.

```fish
for f in *
  echo $f
end
```

It shows the name of each folder.

We know each `Program.cs` file is present inside a folder named `YellowBookSamples` in each of these folders. Let's check this assumption.

```fish
for f in *
  test -f $f/YellowBookSamples/Program.cs; or echo "not found in '$f'"
end
```

This script tests if the file is present in the folder or not. If the file does not exist, then it prints the message "not found in &lt;folder name&gt;".

On running, I got

```fish
not found in 'Code Sample 57 WPF Adding Machine'
```

So only Project "Code Sample 57 WPF Adding Machine" is different. All other
folders have file in `YellowBookSamples/Program.cs`. "WPF Adding Machine" is
different. We will skip this WPF sample code.

We have all the information we need. Let's create a destination folder.

```fish
mkdir ../dest
```

Now we write a script to pick the `Program.cs` file and convert it to an image.

```fish
for f in *
  set code $f/YellowBookSamples/Program.cs
  test -f $code
  and begin
    mkdir ../dest/$f
    carbon-now -h -l ../dest/$f -t $f  $code
  end
end
```

1. `set code $f/YellowBookSamples/Program.cs` create the path of the file, like "Code Sample 46 Storing accounts in an array/YellowBookSamples/Program.cs", and assign it to the variable `code`
1. `test -f $code` tests if the file exists
1. `and begin` is a block of that will only run if `test` in the previous line returns true
1. `mkdir ../dest/$f` creates a sub-folder in the destination directory
1. Call `carbon-now` command to convert the file to an image

When I used `carbon-now`, it did not work unless I used it with the `-h`, i.e.
the headless option. `-l ../dest/$f` is the location to save the image and `-t $f` is the image name.

The result is that each code sample is converted to an image and placed in its folder.

![Fish script result](/images/convert-c-sharp-yellow-book-sample-code-to-images.png)

Unfortunately, `carbon-now` command did not work for eight projects. I had to convert them manually.

`carbon-now` sends the file to the Carbon via URL parameters, because as of
writing this article, [Carbon does not have an
API](https://github.com/carbon-app/carbon/issues/210). The files are probably
too long to be handled via URL.

Finally, I optimized the images using [ImageOptim](https://imageoptim.com/mac). I ran the following script from the `dest` folder.

```fish
for f in **.png
  echo $f
  open -a ImageOptim $f
  sleep 60
end
```

I had to add a one-minute because ImageOptim sometimes crashes if too many images are passed to it at once.
