---
title: "理解C&#x2B;&#x2B;复杂声明"
created: 2025-04-05T17:15:17
modified: 2025-04-05T17:15:17
description: "http://www.codeproject.com/Articles/7042/How-to-interpret-complex-C-C-declarationsContentsIntroductionThe basicsThe const modifierThe subtleties of ty"
source: "https://www.cnblogs.com/answeryi/archive/2012/07/30/2615409.html"
tags:
tags-link:
type: "archive-web"
---
## [http://www.codeproject.com/Articles/7042/How-to-interpret-complex-C-C-declarations](http://www.codeproject.com/Articles/7042/How-to-interpret-complex-C-C-declarations)

## Contents

- [Introduction](https://www.cnblogs.com/answeryi/archive/2012/07/30/#intro)
- [The basics](https://www.cnblogs.com/answeryi/archive/2012/07/30/#basics)
- [The const modifier](https://www.cnblogs.com/answeryi/archive/2012/07/30/#const)
- [The subtleties of typedef](https://www.cnblogs.com/answeryi/archive/2012/07/30/#typedef)
- [Function pointers](https://www.cnblogs.com/answeryi/archive/2012/07/30/#funct_ptrs)
- [The right-left rule](https://www.cnblogs.com/answeryi/archive/2012/07/30/#right_left_rule) \[Important\]
- [Further examples](https://www.cnblogs.com/answeryi/archive/2012/07/30/#examples)
- [Suggested reading](https://www.cnblogs.com/answeryi/archive/2012/07/30/#reading)
- [Credits](https://www.cnblogs.com/answeryi/archive/2012/07/30/#credits)

## Introduction

Ever came across a declaration like `int * (* (*fp1) (int) ) [10];` or something similar that you couldn't fathom? This article will teach you to interpret C/C++ declarations, starting from mundane ones (*please* bear with me here) and moving on to very complex ones. We shall see examples of declarations that we come across in everyday life, then move on to the troublesome `const` modifier and `typedef`, conquer function pointers, and finally see the right-left rule, which will allow you to interpret any C/C++ declaration accurately. I would like to emphasize that it is not considered good practice to write messy code like this; I'm merely teaching you how to understand such declarations. **Note**: This article is best viewed with a minimum resolution of 1024x768, in order to ensure the comments don't run off into the next line.

[\[Back to contents\]](https://www.cnblogs.com/answeryi/archive/2012/07/30/#contents)

## The basics

Let me start with a very simple example. Consider the declaration:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
int n;
```

This should be interpreted as "declare `n` as an `int`".

Coming to the declaration of a pointer variable, it would be declared as something like:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
int *p;
```

This is to be interpreted as "declare `p` as an `int *` i.e., as a pointer to an `int`". I'll need to make a small note here - it is always better to write a pointer (or reference) declaration with the `*` (or `&`) preceding the variable rather than following the base type. This is to ensure there are no slip-ups when making declarations like:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
int* p,q;
```

At first sight, it looks like `p` and `q` have been declared to be of type `int *`, but actually, it is only `p` that is a pointer, `q` is a simple `int`.

We can have a pointer to a pointer, which can be declared as:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
char **argv;
```

In principle, there is no limit to this, which means you can have a pointer to a pointer to a pointer to a pointer to a `float`, and so on.

Consider the declarations:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
int RollNum[30][4];
int (*p)[4]=RollNum;
int *q[5];
```

Here, `p` is declared as a pointer to an array of 4 `int`s, while `q` is declared as an array of 5 pointers to integers.

We can have a mixed bag of `*`s and `&`s in a single declaration, as explained below:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
int **p1;  int *&p2;  int &*p3;  int &&p4;  
```  

[\[Back to contents\]](https://www.cnblogs.com/answeryi/archive/2012/07/30/#contents)

## The const modifier

The `const` keyword is used when you want to prevent a variable (oops, that's an oxymoron) from being modified. When you declare a `const` variable, you need to initialize it, because you can't give it a value at any other time.

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
const int n=5;
int const m=10;
```

The two variables `n` and `m` above are both of the same type - constant integers. This is because the C++ standard states that the `const` keyword can be placed before the type or the variable name. Personally, I prefer using the former style, since it makes the `const` modifier stand out more clearly.

`const` is a bit more confusing when it comes to dealing with pointers. For instance, consider the two variables `p` and `q` in the declaration below:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
const int *p;
int const *q;
```

Which of them is a pointer to a `const int`, and which is a `const` pointer to an `int`? Actually, they're both pointers to `const int`s. A `const` pointer to an `int` would be declared as:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
int * const r= &n; 
``` 

Here, `p` and `q` are pointers to a `const int`, which means that you can't change the value of `*p`. `r` is a `const` pointer, which means that once declared as above, an assignment like `r=&m;` would be illegal (where `m` is another `int`) but the value of `*r` can be changed.

To combine these two declarations to declare a `const` pointer to a `const int`, you would have to declare it as:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
const int * const p=&n 
``` 

The following declarations should clear up any doubts over how `const` is to be interpreted. Please note that some of the declarations will NOT compile as such unless they are assigned values during declaration itself. I have omitted them for clarity, and besides, adding that will require another two lines of code for each example.

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
char ** p1;                    const char **p2;               char * const * p3;             const char * const * p4;       char ** const p5;              const char ** const p6;        char * const * const p7;       const char * const * const p8; 
``` 

[\[Back to contents\]](https://www.cnblogs.com/answeryi/archive/2012/07/30/#contents)

## The subtleties of typedef

`typedef` allows you a way to overcome the \*-applies-to-variable-not-type rule. If you use a `typedef` like:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
typedef char * PCHAR;
PCHAR p,q;
```

both `p` and `q` become pointers. If the `typedef` had not been used, `q` would be a `char`, which is counter-intuitive.

Here are a few declarations made using `typedef`, along with the explanation:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
typedef char * a;  
typedef a b();                        
typedef b *c;                         
typedef c d();                                           
typedef d *e;                                                               
e var[10];                                               
```                                               

`typedef`s are usually used with structure declarations as shown below. The following structure declaration allows you to omit the `struct` keyword when you create structure variables even in C, as is normally done in C++.

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
typedef struct tagPOINT
{
    int x;
    int y;
}POINT;

POINT p; 
``` 

[\[Back to contents\]](https://www.cnblogs.com/answeryi/archive/2012/07/30/#contents)

## Function pointers

Function pointers are probably the greatest source of confusion when it comes to interpreting declarations. Function pointers were used in the old DOS days for writing TSRs; in the Win32 world and X-Windows, they are used in callback functions. There are lots of other places where function pointers are used: virtual function tables, some templates in STL, and Win NT/2K/XP system services. Let's see a simple example of a function pointer:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
int (*p)(char);
```

This declares `p` as a pointer to a function that takes a `char` argument and returns an `int`.

A pointer to a function that takes two `float`s and returns a pointer to a pointer to a `char` would be declared as:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
char ** (*p)(float, float);
```

How about an array of 5 pointers to functions that receive two `const` pointers to `char`s and return a `void` pointer?

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
void * (*a[5])(char * const, char * const);
```

[\[Back to contents\]](https://www.cnblogs.com/answeryi/archive/2012/07/30/#contents)

## The right-left rule \[Important\]

This is a simple rule that allows you to interpret any declaration. It runs as follows:

Start reading the declaration from the innermost parentheses, go right, and then go left. When you encounter parentheses, the direction should be reversed. Once everything in the parentheses has been parsed, jump out of it. Continue till the whole declaration has been parsed.

One small change to the right-left rule: When you start reading the declaration for the first time, you have to start from the identifier, and not the innermost parentheses.

Take the example given in the introduction:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
int * (* (*fp1) (int) ) [10];
```

This can be interpreted as follows:

1. Start from the variable name -------------------------- `fp1`
2. Nothing to right but `)` so go left to find `*` -------------- is a pointer
3. Jump out of parentheses and encounter (`int`) --------- to a function that takes an `int` as argument
4. Go left, find `*` ---------------------------------------- and returns a pointer
5. Jump put of parentheses, go right and hit `[10]` -------- to an array of 10
6. Go left find `*` ----------------------------------------- pointers to
7. Go left again, find `int` -------------------------------- `int`s.

Here's another example:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
int *( *( *arr[5])())();
```

1. Start from the variable name --------------------- `arr`
2. Go right, find array subscript --------------------- is an array of 5
3. Go left, find `*` ----------------------------------- pointers
4. Jump out of parentheses, go right to find `()` ------ to functions
5. Go left, encounter `*` ----------------------------- that return pointers
6. Jump out, go right, find `()` ----------------------- to functions
7. Go left, find `*` ----------------------------------- that return pointers
8. Continue left, find `int` ----------------------------- to `int`s.

[\[Back to contents\]](https://www.cnblogs.com/answeryi/archive/2012/07/30/#contents)

## Further examples

The following examples should make it clear:

[![](http://www.codeproject.com/images/minus.gif)](http://www.codeproject.com/images/minus.gif) Collapse | [Copy Code](https://www.cnblogs.com/answeryi/archive/2012/07/30/#)

```
float ( * ( *b()) [] )();                                                                                            
void * ( *c) ( char, int (*)());                                                                                                                                                                                                                                                 
void ** (*d) (int &, 
  char **(*)(char *, char **));                                                                                                                                                                                                                                                                                                                                
float ( * ( * e[10]) 
    (int &) ) [5];                                                                                                                                                                                
```                                                                                                                                                                                

[\[Back to contents\]](https://www.cnblogs.com/answeryi/archive/2012/07/30/#contents)

## Suggested reading

- [A Prelude to pointers](http://www.cnblogs.com/KB/cpp/pointerprelude.asp) by Nitron.
- `cdecl` is an excellent utility that explains variable declarations and does much more. You can download the Windows port of cdecl from [here](http://www.simtel.net/product.php?url_fb_product_page=41564).

[\[Back to contents\]](https://www.cnblogs.com/answeryi/archive/2012/07/30/#contents)

## Credits

I got the idea for this article after reading a thread posted by Jörgen Sigvardsson about a pointer declaration that he got in a mail, which has been reproduced in the introduction. Some of the examples were taken from the book "Test your C skills" by Yashvant Kanetkar. Some examples of function pointers were given by my cousin Madhukar M Rao. The idea of adding examples with mixed `*`s and `&`s and `typedef` with `struct`s was given by my cousin Rajesh Ramachandran. Chris Hills came up with modifications to the right-left rule and the way in which some examples were interpreted.

[\[Back to contents\]](https://www.cnblogs.com/answeryi/archive/2012/07/30/#contents)