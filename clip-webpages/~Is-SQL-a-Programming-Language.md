---
title: "Is SQL a Programming Language_ _ LearnSQL.com"
created: 2025-04-05T15:50:55
modified: 2025-04-05T15:50:55
source: https://learnsql.com/blog/sql-programming-language/
tags:
tags-link:
type: archive-web
---

# Is SQL a Programming Language?


[Kateryna Koidan](https://learnsql.com/authors/kateryna-koidan/)

  * [sql](https://learnsql.com/tags/sql)
  * [learn sql](https://learnsql.com/tags/learn-sql)



_SQL is a powerful tool for communicating with database management systems. When you write SQL queries, you give instructions to the computer, and it performs these instructions—it sounds like programming. However, you cannot build an application with SQL as you can with Python or Java. So, is SQL a programming language?_

### What Is SQL?

Let’s start with the basic definition. **SQL** , or **Structured Query Language** , is a language used for communication with relational databases. Despite the importance of this role, this is quite a narrow task compared to what Python, Java, C++, etc. are used for. Naturally, there is a long-lasting [debate](https://www.quora.com/Is-SQL-a-programming-language "Is SQL a programming language? - Quora") around the question—is SQL a programming language? You cannot create an application or build a webpage with SQL, but it definitely looks like programming when you use SQL to talk to your databases. 

To address this controversial issue, I suggest starting with recognizing the differences between several key concepts. We’ll have no problem answering if SQL is a programming language after we define the term “**programming language** ” and have a clear understanding of the differences between **general-purpose programming languages** and **domain-specific programming languages**.

Learn SQL by writing SQL! Build your SQL skills (and confidence) by completing the 129 interactive exercises in our [SQL Basics](https://learnsql.com/course/sql-queries?itm_source=lsqlBlog&itm_campaign=_default&itm_medium=text&itm_content=course-sql-queries-10) course.

### Programming Language vs. General-Purpose Programming Language

[==According to Webopedia==](https://www.webopedia.com/TERM/P/programming_language.html "Programming Language Definition | Webopedia")==, “a ==**==programming language==** ==is a vocabulary and set of grammatical rules for instructing a computer or computing device to perform specific tasks.” SQL is definitely a programming language given this definition.==

It has certain **vocabulary** and strict **syntax** that should be followed. For example, all SQL statements start with specific keywords (e.g., `SELECT`, `INSERT`, `CREATE`, `UPDATE`, `DELETE`) and end with a semicolon. The order of clauses is also important. For example, `GROUP BY` should follow the `WHERE` clause and precede the `ORDER BY` clause:

`SELECT` `column_one, column_two``FROM` `table``WHERE` `column_one > 2000``GROUP` `BY` `column_one, column_two``ORDER` `BY` `column_one;` Furthermore, messages that are written using this vocabulary and syntax instruct your computer to perform specific tasks, like accessing certain data in the database; creating, updating, or deleting tables in the database; etc. Then why do we have all this controversy around recognizing SQL as a programming language? The problem is that people often mean “general-purpose programming language” when saying “programming language.” And there is a big difference between these terms. [==Wikipedia says==](https://en.wikipedia.org/wiki/General-purpose_programming_language "General-purpose programming language - Wikipedia") ==that “a ==**==general-purpose programming language is a programming language==** ==designed to be used for writing software in the widest variety of application domains.” Basically, you can create all kinds of applications using a general-purpose programming language, including desktop, mobile, or web applications. The most widely used programming languages from this category include Java, JavaScript, Python, C++, and Ruby.== In contrast to these languages, SQL has a very niche role of communicating with relational databases. Thus, you cannot build an application using only SQL. This leads us to the conclusion that SQL **is not a general-purpose programming language**.

### ==SQL as a Domain-Specific Language==

==Now we know that SQL satisfies the definition of a programming language but ==**==not==** ==a general-purpose programming language. So, where does SQL belong?== ==Apart from general-purpose programming languages, there are also ==**==domain-specific languages (DSLs)==** ==. ==[==Wikipedia defines==](https://en.wikipedia.org/wiki/Domain-specific_language "Domain-specific language - Wikipedia") ==a domain-specific language as “a computer language specialized to a particular application domain.” HTML, or Hypertext Markup Language, is one of the most popular domain-specific languages used for structuring webpages.== ==Similarly, SQL, with its specific application domain, ==**==can be defined as a domain-specific language==** ==. Structured Query Language is a highly targeted language for “talking” to databases. While being an effective and powerful tool for data management and access, SQL has limited usage compared to general-purpose programming languages. However, this drawback comes with certain benefits.== ==Because of its narrow application domain, SQL is usually ==**==easier to learn==** ==than a general-purpose programming language. You don’t need a computer science background to start with the ==[==SQL Basics==](https://learnsql.com/course/sql-queries/ "SQL Basics - SQL online course | LearnSQL.com") ==course. Moreover, even when starting with zero programming knowledge, you can become an SQL expert in a few months after taking the ==[==SQL from A to Z==](https://learnsql.com/track/sql-from-a-to-z "SQL from A to Z - SQL online learning path | LearnSQL.com") ==track.==

### SQL and Turing Completeness

If you are not yet convinced that SQL is a programming language, here is another point to consider. To evaluate how “powerful” a certain programming language is, computer scientists often use the concept of **Turing completeness**. According to the [Wikipedia definition](https://en.wikipedia.org/wiki/Turing_completeness "Turing completeness - Wikipedia"), a programming language “is said to be Turing complete or computationally universal if it can be used to simulate any Turing machine.” In simple terms, a Turing machine is a hypothetical machine, named by computer scientist Alan Turing, that can take any program of any complexity and run it. So, we could say that SQL is Turing complete if any program that can be written to run for a Turing machine can also be written in SQL. And in fact, SQL, with the addition of recursive queries, satisfies this condition. If interested, you can learn more about SQL recursive queries in this [comprehensive guide](https://learnsql.com/blog/get-to-know-the-power-of-sql-recursive-queries/ "Get to Know the Power of SQL Recursive Queries"). You can also learn how to create recursive queries or common table expressions (CTEs) in our [Recursive Queries](https://learnsql.com/course/common-table-expressions/ "Recursive Queries - SQL online course | LearnSQL.com") course. Now you know that **SQL is Turing complete** and thus, computationally universal. But this is not yet the end of the story… Want to learn SQL? Check out our [SQL From A to Z](https://learnsql.com/track/sql-from-a-to-z?itm_source=lsqlBlog&itm_campaign=_default&itm_medium=text&itm_content=track-sql-from-a-to-z-2) track!

### SQL and Procedural Languages

SQL can be extended with **procedural languages** that allow users to define their own functions and procedures. Therefore, procedural languages are programming languages in either sense of the term. All database management systems (DBMSs) accept one or more dialects of procedural languages. Let’s have a look at some examples. **PL/SQL** , or **Procedural Language for SQL** , is an extension for SQL in the Oracle database management system. Similar to general-purpose programming languages, PL/SQL includes elements like conditions and loops. With PL/SQL, you can also declare constants, variables, variable types, procedures, and functions. **PL/pgSQL** , or **Procedural Language/PostgreSQL** , is a procedural language supported by the PostgreSQL object-relational database management system. It is very similar to Oracle’s PL/SQL and allows loops and conditions as well as user-defined functions. You can learn how to create user-defined functions in PostgreSQL with our [comprehensive course](https://learnsql.com/course/user-defined-functions/ "Writing User-Defined Functions in PostgreSQL - SQL online course | LearnSQL.com").  MySQL is a database management system that doesn’t have a separate name for SQL extensions that allow the creation of functions and procedures, but it supports this functionality. MySQL has [`CREATE PROCEDURE` and CREATE FUNCTION statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html "MySQL :: MySQL 8.0 Reference Manual :: 13.1.17 CREATE PROCEDURE and <code>CREATE FUNCTION</code> Statements") that create stored routines. User-defined functions are also supported in MySQL—they are regarded as externally stored functions. As you can see, SQL is a powerful tool for data management and access. It can handle huge analytical queries with all kinds of data. But, it can also be used for fun! Read about [how to draw a Christmas tree in SQL](https://learnsql.com/blog/draw-christmas-tree-sql/ "How to Draw a Christmas Tree in SQL |   LearnSQL.com").

### Time to Learn SQL!

Now you know that SQL is a powerful programming language that is worth your attention. While Structured Query Language has been around for decades, it’s still the go-to tool for data access and management in all kinds of modern applications. Business analysts, data analysts, data scientists, and many other roles in today’s companies need SQL to perform their jobs. Except for its apparent usefulness as a domain-specific language, SQL can be also the first step towards programming and learning a general-purpose programming language.  Are you excited about where SQL can bring your career? Then check out the following courses:

  * [SQL Basics](https://learnsql.com/course/sql-queries/ "SQL Basics - SQL online course | LearnSQL.com") is an easy-to-follow introduction to SQL queries. No computer science background required!
  * [SQL from A to Z](https://learnsql.com/track/sql-from-a-to-z "SQL from A to Z - SQL online learning path | LearnSQL.com") is a track designed for ambitious and dedicated students who are ready to go from complete newbies, through intermediate and advanced topics, to an **SQL guru** level.
  * [Writing User-Defined Functions in PostgreSQL](https://learnsql.com/course/user-defined-functions/ "Writing User-Defined Functions in PostgreSQL - SQL online course | LearnSQL.com") is for those who feel confident with SQL and are ready to master the procedural extension of SQL to write user-defined functions.

Thanks for reading, and happy learning!  **Summary:** There is a long-lasting debate about recognizing SQL as a programming language. With SQL, you give your computer instructions to perform huge analytical queries, which looks like programming. However, you cannot build an application using only SQL. So, is SQL a programming language? Learn why the answer is definitely yes. 
