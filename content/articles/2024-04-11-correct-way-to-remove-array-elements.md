---
slug: correct-way-to-remove-array-elements
authors:
  - name: Talha
    image: https://github.com/talha131.png
date: 2024-04-11
title: Removing Elements from Arrays the Right Way
tags: [data structure, algorithm,functional programming, Cpp, Csharp, Python, JavaScript, Golang]
description: Learn the correct methods for removing elements from arrays in JavaScript, including best practices and common pitfalls to avoid.
keywords: [JavaScript array removal, Removing elements from arrays, Array manipulation techniques, Correct way to remove array elements, Array element removal best practices, JavaScript coding tips, Efficient array processing, Debugging arrays in JavaScript, Functional programming array methods, Software development best practices, Array splice method, Reverse iteration arrays, Programming tutorials, Data structure optimization, Code debugging techniques]
image: img/blog/2024-04-11-correct-way-to-remove-array-elements-featured.webp
---

Imagine you're working with a simple array, one that contains 16 integers.

```javascript
const eg = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610];
```

Now, let's say we need to weed out all numbers greater than 99 from our array. Sounds like a piece of cake, doesn't it?

Your code will probably look like this,

```javascript {linenos=table,hl_lines=[6],filename="JavaScript"}
const eg = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610];

for (let i = 0; i < eg.length; i++) {
  if (eg[i] > 99) {
    // Remove element
    eg.splice(i, 1);
  }
}
```

But wait, once you print the updated array, you'll notice something's off.

```javascript
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 233, 610];
```

Why are 233 and 610 still lounging in our array? They're clearly above our cut-off of 99.

## What went wrong?

{{< callout type="info" >}}

Heads up: We're using JavaScript for our examples, but the puzzle we're tackling? It's universal across all programming languages.
Near the end, I have added examples in Golang, C#, C++, Python and JavaScript.

{{< /callout >}}

Let's sprinkle our code with log statements to see what's happening under the hood. You can view and run the code [at this link](https://repl.it/@talha131/Incorrect-Iterate-Over-An-Array-And-Remove-Elements).

```javascript {linenos=table,hl_lines=[6, 11],filename="JavaScript"}
const eg = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610];

console.log(`index\tvalue\tarray length`);

for (let i = 0; i < eg.length; i++) {
  console.log(`${i}\t\t${eg[i]}\t\t\t${eg.length}`);

  if (eg[i] > 99) {
    // Remove element
    eg.splice(i, 1);
    console.log(`Element at ${i} removed. Length is  ${eg.length}`)
  }
}

console.log(eg)
```

The output is,

```bash {hl_lines=[15,16,17],filename="Output"}
index   value   array length
0       0           16
1       1           16
2       1           16
3       2           16
4       3           16
5       5           16
6       8           16
7       13          16
8       21          16
9       34          16
10      55          16
11      89          16
12      144         16
Element at 12 removed. Length is  15
13      377         15
Element at 13 removed. Length is  14
[ 0,   1,  1,  2,  3,  5, 8,  13, 21, 34, 55, 89, 233, 610 ]
```

Here's where it gets interesting. When our loop hits index 12, it encounters the number 144. 144 is removed, *which reduces array length to 15 from 16.*

Then the index `i` is 14, and it reaches element 377. 377 is removed, *which reduces array length from 15 to 14.*

Then the index `i` reaches 15, but it fails the condition `i < eg.length`, which stops the result.

**The loop ran only 14 times when it should have run 16 times.** It happens because we modified the array length during the iteration.

{{< callout type="warning" >}}


If you think forcing the loop to run 16 times will fix the issue, then you are wrong.

{{< /callout >}}

Have a look at following incorrect code.

```javascript {linenos=table,hl_lines=[3],filename="JavaScript"}
const eg = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610];

const len = eg.length;

console.log(`index\tvalue\tarray length`);

for (let i = 0; i < len; i++) {
  console.log(`${i}\t\t${eg[i]}\t\t\t${eg.length}`);

  if (eg[i] > 99) {
    // Remove element
    eg.splice(i, 1);
    console.log(`Element at ${i} removed. Length is  ${eg.length}`);
  }
}
```

If you try to [run this code](https://repl.it/@talha131/Incorrect-forward-Iterate-Over-An-Array-And-Remove-Elements), you will get "index out of bound" runtime errors.

Now, how do we solve this issue? **We have three ways to do it the right way.**

## Solution 1 – Decrement index

One way to solve this problem is to decrement `i` whenever an element from the array is removed. This way index does not skip over the remaining elements of the array.

```javascript {linenos=table,hl_lines=[12],filename="JavaScript"}
const eg = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610];

console.log(`index\tvalue\tarray length`);

for (let i = 0; i < eg.length; i++) {
  console.log(`${i}\t\t${eg[i]}\t\t\t${eg.length}`);

  if (eg[i] > 99) {
    // Remove element
    eg.splice(i, 1);
    console.log(`Element at ${i} removed. Length is  ${eg.length}`);
    i--;
  }
}

console.log(eg);
```

Its output is

```bash {hl_lines=[15,17,19,21],filename="Output"}
index   value   array length
0       0           16
1       1           16
2       1           16
3       2           16
4       3           16
5       5           16
6       8           16
7       13          16
8       21          16
9       34          16
10      55          16
11      89          16
12      144         16
Element at 12 removed. Length is  15
12      233         15
Element at 12 removed. Length is  14
12      377         14
Element at 12 removed. Length is  13
12      610         13
Element at 12 removed. Length is  12
[ 0,  1,  1,  2,  3, 5,  8, 13, 21, 34, 55, 89 ]
```

You can view and run this code [here](https://repl.it/@talha131/Decrement-i-Iterate-Over-An-Array-And-Remove-Elements-1).

## Solution 2 – Iterate in Reverse

In this solution, you start from the last element of the array and continue backwards. This way, even if array length is modified, the loop iterates over all the remaining elements.

```javascript {linenos=table,hl_lines=[3,7],filename="JavaScript"}
const eg = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610];

let i = eg.length;

console.log(`index\tvalue\tarray length`);

while (i--) {
  console.log(`${i}\t\t${eg[i]}\t\t\t${eg.length}`);

  if (eg[i] > 99) {
    // Remove element
    eg.splice(i, 1);
    console.log(`Element at ${i} removed. Length is ${eg.length}`);
  }
}

console.log(eg);
```

Its output is

```bash {hl_lines=[3,5,7,9],filename="Output"}
index   value   array length
15      610         16
Element at 15 removed. Length is 15
14      377         15
Element at 14 removed. Length is 14
13      233         14
Element at 13 removed. Length is 13
12      144         13
Element at 12 removed. Length is 12
11      89          12
10      55          12
9       34          12
8       21          12
7       13          12
6       8           12
5       5           12
4       3           12
3       2           12
2       1           12
1       1           12
0       0           12
[ 0,  1,  1,  2,  3, 5,  8, 13, 21, 34, 55, 89 ]
```

You can view and run this code [here](https://repl.it/@talha131/Iterate-Reverse-1-Iterate-Over-An-Array-And-Remove-Elements).

You can, of course, use a `for` loop in place of `while`.

```javascript
for (i = eg.length - 1; i >= 0; i--) {}
```

You can view code with a `for` loop [here](https://repl.it/@talha131/Iterate-Reverse-2-Iterate-Over-An-Array-And-Remove-Element).

## Is this problem specific to some languages?

No! Whichever programming language you pick, if you iterate and remove array elements incorrectly, you will face this issue.

[Here](https://repl.it/@talha131/Incorrect-Go-Iterate-Over-An-Array-And-Remove-Elements?language=go) is the same problem replicated in **Golang**. If you run it, the program fails during runtime.

```go {linenos=table,filename="Go"}
package main

import "fmt"

func remove(slice []int, s int) []int {
    return append(slice[:s], slice[s+1:]...)
}

func main() {
    eg := []int{0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610}
for i, el := range eg {
        if el > 99 {
            eg = remove(eg, i)
            fmt.Println(len(eg))
        }
    }

    fmt.Println(eg)
}
```

The output of the above program:

```bash {filename="Output"}
./main
15
14
panic: runtime error: slice bounds out of range

goroutine 1 [running]:
main.remove(...)
    /home/runner/main.go:6
main.main()
    /home/runner/main.go:14 +0x25b
exit status 2
```

But if we turn around the code and start iteration is reverse, then [the code works fine](https://repl.it/@talha131/Correct-Go-Iterate-Over-An-Array-And-Remove-Elements).

```go {linenos=table,hl_lines=[11,17],filename="Go"}
package main

import "fmt"

func remove(slice []int, s int) []int {
    return append(slice[:s], slice[s+1:]...)
}

func main() {
    eg := []int{0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610}
    l := len(eg) - 1
    for l >= 0 {
        if eg[l] > 99 {
                eg = remove(eg, l)
            }

        l = l - 1
    }

    fmt.Println(eg)
}
```

## Best Solution

A succinct solution is to use functional programming.

Most modern programming languages are incorporating functional programming
features. Thus, if a language supports new methods, you do not have to use the
old fashioned loops to remove elements from an array.

{{< tabs items="JavaScript,Python,C#,C++" defaultIndex="0" >}}

{{< tab >}}

In [ECMA-262 5th edition](https://en.wikipedia.org/wiki/ECMAScript?oldformat=true#5th_Edition), [`filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) method was added to the JavaScript.

We can rework the above example into [a simple oneliner](https://repl.it/@talha131/JS-Filter-Iterate-Over-An-Array-And-Remove-Elements).

```javascript {linenos=table,filename="JavaScript"}
const eg = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610];
result = eg.filter((x) => x < 99);
// Output
console.log(result);
```

{{< /tab >}}
{{< tab >}}

[Here is a working Python oneliner](https://repl.it/@talha131/Python-Iterate-Over-An-Array-And-Remove-Elements).

```python {linenos=table,filename="Python"}
eg = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
result = [x for x in eg if x < 99]
print(result)
```

{{< /tab >}}
{{< tab >}}

Either of the following way will work in C#.

[Using Linq](https://repl.it/@talha131/C-Linq-Iterate-Over-An-Array-And-Remove-Elements).

```csharp {linenos=table,filename="C#"}
using System;
using System.Collections.Generic;
using System.Linq;

class MainClass {
  public static void Main (string[] args) {
    List<int> eg = new List<int>(){0, 1, 1, 2, 3, 5, 8, 13,
                        21, 34, 55, 89, 144, 233, 377, 610};
    var result = (from x in eg where x < 99 select x).ToList();
    result.ForEach(i => Console.WriteLine(i));
  }
}
```

[Using predicate](https://repl.it/@talha131/C-Predicate-Iterate-Over-An-Array-And-Remove-Elements).

```csharp {linenos=table,filename="C#"}
using System;
using System.Collections.Generic;

class MainClass {
  public static void Main (string[] args) {
    List<int> eg = new List<int>(){0, 1, 1, 2, 3, 5, 8, 13,
                        21, 34, 55, 89, 144, 233, 377, 610};
    eg.RemoveAll(i => i > 99);
    eg.ForEach(i => Console.WriteLine(i));
  }
}
```

{{< /tab >}}
{{< tab >}}

C++ has [`std::remove_if`](https://en.cppreference.com/w/cpp/algorithm/remove) method.

```cpp {linenos=table,filename="C++"}
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  std::vector<int> eg = {0,  1,  1,  2,  3,   5,   8,   13,
                         21, 34, 55, 89, 144, 233, 377, 610};
  eg.erase(std::remove_if(
              eg.begin(),
              eg.end(),
              [](int x) {
                  return x > 99;
              }),
           eg.end());

  // Print result
  std::for_each(eg.begin(),
                eg.end(),
                [](const int &e) {
                    std::cout << e << " ";
                });
}
```

You can run this code [here](https://repl.it/@talha131/C-Iterate-Over-An-Array-And-Remove-Elements).

{{< /tab >}}
  {{< /tabs >}}


