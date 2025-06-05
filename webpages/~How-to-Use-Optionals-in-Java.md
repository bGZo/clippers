---
title: "How-to-Use-Optionals-in-Java"
created: 2025-03-16T14:20:25
modified: 2025-03-16T14:57:02
description: "I am devoted to continuously learning and improving as a software developer and sharing my experience with others in order to improve their expertise. I am also dedicated to personal and professional growth through diligent studying, discipline, and meaningful professional relationships. When not writing, I can be found playing hockey, practicing Brazilian Jiu-jitsu, watching the NJ Devils, reading, writing, or drawing. ~II Timothy 1:7~ Twitter: @justinmalbano"
source: "https://dzone.com/articles/optional-in-java"
tags:
tags-link:
type: "archive-web"
---

The introduction of the `Optional` class was a major improvement in the design of the Java language, but this improvement has been controversial. Prior the `Optional` class, many developers used either `null` or exceptions to denote when a desired value was not present; using the `Optional` class, however, allows us to explicitly state when a value may or may not be present. Despite this improvement, the `Optional` class can be applied inappropriately and cause more harm than good.

In this article, we will look at the fundamentals of the `Optional` class, including:

- The purpose and the thought process behind its introduction
- The essential methods included in the `Optional` class
- The appropriate times and places to use the `Optional` class
- A few alternative techniques that can be used instead

## Purpose

Java, like most Object-Oriented ([OO](https://dzone.com/articles/object-oriented-programming-1)) languages, has a sneaky backdoor to its type system. For example, suppose that we have the following method signature:

```java
public Foo doSomething();
```

It is obvious that this method returns an object of type `Foo`, but it can also return another value: `null`. Since any non-primitive type can be set to `null`, there is nothing stopping a developer from writing the following method implementation:

```java
public Foo doSomething() {
    return null; 
}
```

### Nullity

This creates an onerous situation for the client that calls this method. Before using the `Foo` object returned from the `doSomething` method, a client must first check that the object is not `null`:

```java
Foo foo = doSomething();
if (foo == null) {
    // handle null case...
} else {
    // do something with the foo object...
}
```

This approach ensures that the use of the `Foo` object does not result in a `NullPointerException` (NPE). This creates another problem, though: *A**ny* non-primitive object can be implicitly set to `null`. Thus, exhaustively, we must check every object returned from a method for nullity prior to using it. It goes without saying that this would not only be infeasible in a large application, but it would also muddle the clarity of our code. For example, adding extra lines for `null`\-checks would introduce boilerplate code throughout our application that makes the use of the `Foo` object less clear (hidden within an `if`\-`else` statement).

The root problem is that we do not know when a method intends to return `null `— such as when a desired value cannot be found — or can contractually guarantee that `null` will never be returned. Since we are unsure, we are forced to assume that *any* returned object can be `null`.

One solution that is commonly used is documenting that a return value can be `null` using [JavaDocs](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html). While this is an improvement over the original problem, this does not ensure that a client checks for nullity prior to the use of the object (i.e., the Java compiler will compile the code without these `null`\-checks without complaint). Similarly, annotations like [`@NotNull`](https://docs.oracle.com/javaee/7/api/javax/validation/constraints/NotNull.html) exist, but these suffer from the same drawback as the documentation approach. Namely, enforcement can be circumvented.

### `Optional` Class

Instead, we need a mechanism that allows a method developer to explicitly denote that the return value for a method may or may not be present. This mechanism was introduced in Java Development Kit ([JDK](https://dzone.com/articles/java-and-the-jdks-which-one-to-use)) 7 in the form of the [`Optional`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/Optional.html) class. This class acts as a wrapper for an object that may not be present. Therefore, if we know that our `doSomething` method may not return a desired `Foo` object, we can change the signature to:

```java
public Optional<Foo> doSomething();
```

As we will see in the following sections, `Optional` provides a suite of methods — many [functional](https://dzone.com/articles/functional-programming-patterns-with-java-8)— that allows a client to decide what to do when the desired value is not present. For example, we can use the `orElse` method to return a default value when the desired value cannot be found (called an *empty `Optional`* in the `Optional` lexicon):

```java
oo foo = doSomething()
    .orElse(new Foo());
```

Likewise, we can also throw an exception when `Optional` is empty using the `orElseThrow` method:

```java
Foo foo = doSomething()
    .orElseThrow(SomeException::new);
```

It is important to note two things:

1. The Java compiler forces us to handle the case of an empty `Optional` value
2. The client is responsible for handling a missing desired value

While documentation and annotations do move us in the correct — more-explicit — direction, they do not allow us to impose the responsibility of checking for a missing value on the client. `Optional` objects, on the other hand, require that a client make a decision about how to handle a missing value. 

For example, the following *will not* compile:

```java
Foo foo = doSomething();
```

We will instead see a compilation error alerting us that an object of type `Optional<Foo>` cannot be cast to `Foo` since the return type of `doSomething` is `Optional<Foo>` and the type of `foo` is `Foo`. Thus, we must call a method such as `orElse` or `orElseThrow`—or `get`, but we will see later why that should not be the first choice — in order to convert the `Optional<Foo>` object to a `Foo` object. Since both of those methods require a parameter, they, therefore, require us to make an explicit decision about what default value to use or what exception to throw if the `Optional` is empty.

### Client Responsibility

This brings us to note (2): The responsibility for handling the empty `Optional` rests upon the client. In essence, the `doSomething` method — by nature of returning `Optional<Foo>` rather than `Foo `— is telling the client that there is a possibility that a result will not be found. Thus, the client is now responsible for handling the case when no result is found (i.e., one of the `Optional` methods, such as `orElse`, must be called to get from `Optional<Foo>` to `Foo`).

This client-responsible approach means that the method developer does not have enough information to determine what should be done in the case of a missing value. It is possible for the developer to throw an exception when the value cannot be found, but a missing value may not be a case that warrants an exception (i.e., it may not be an *exceptional* case). 

For instance, if we want to check if an object exists already or create one, if it does not, a non-existent object would not be an error, and throwing an exception would not be warranted. What's more, throwing an exception would require that we catch the exception in the calling code in order to create the default. For example, suppose we create the following method:

```java
public Foo findIfExists() throws FooNotFoundException;
```

To use the existing value or create a default if one does not exist, we must do the following:

```java
Foo foo = null;
try {
    foo = findIfExists();
} catch (FooNotFoundException e) {
    foo = // create default value...
}
```

We can instead return an `Optional` value from `findIfExists`:

```java
public Optional<Foo> findIfExists();
```

Then we can simply use the `orElse` method to provide a default value:

```java
Foo foo = findIfExists()
    .orElse(/* create default value... */)
```

Additionally, the latter approach is much more readable. By simply reading the code, we understand that the two lines mean *find if exists or else use this value*. In the former case, we have to consciously derive the meaning of the `catch` clause to be the default value when `findIfExists` cannot find an existing value. Thus, the `Optional` lexicon matches the intended meaning much more closely than the exception approach.

Understanding this, `Optional` is a useful technique when a client is responsible for handling a missing object, *and* the absence of the object is not an error. There may be times when a missing value is an error — such as when we assume a value exists and its absence could cause fatal results for the application — and a method should throw a checked or unchecked exception. In some cases, though (such as the `findIfExists` method), an absent object is not an error, and using an `Optional` is an effective way to ensure that a missing object is explicitly handled by the client.

### `null` `Optional` Objects

There is one caveat that must be addressed: It is possible for an `Optional` object to be `null`. Since `Optional` objects are non-primitive objects just like `Foo`, they can likewise be set to `null`. For example, the following implementation of `doSomething` will compile without error:

This would lead to the bizarre case of the client having to handle both the case of a `null` return value *and* the case of handling an empty `Optional`:

Not only does this introduce duplication for the missing object case (i.e., the case of a missing object is handled in two locations), but it also reintroduces the problem of reduced clarity. Instead, when an `Optional` is returned from a method, we should not check for a `null` value. According to the [`Optional` class documentation](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/Optional.html#of\(T\)):

> A variable whose type is `Optional` should never itself be `null`; it should always point to an `Optional` instance.

If a `null` value is returned in place of an `Optional` object, this is a breach of the method [contract](https://en.wikipedia.org/wiki/Design_by_contract) on the part of the method developer. By stating that a method will return an `Optional` object, the method developer is also stating that it is invalid to return `null`. Since the `Optional` object denotes the possibility of a missing object, there is no valid use case for a `null` value (i.e., the method should return an empty `Optional` instead of `null` in all cases). 

Therefore, whenever we are dealing with an `Optional` object, we are right to assume that the `Optional` object will never be `null`. Although it is possible that the `Optional` object can be `null` in practice, this is a problem that should be resolved by the method developer rather than the client.

## Important Methods

With an understanding of the concepts behind the `Optional` class, we can now look at how to use `Optional` objects in practice. The `Optional` class contains a large suite of methods, which can be broken down into two categories: Creation methods and instances method.

### Creation Methods

The `Optional` creation methods are static methods that allow us to create various `Optional` objects to suit our needs. There are currently three such methods: One for creating a populated `Optional` (i.e., an `Optional` whose wrapped value is not `null`), one for creating a populated or empty `Optional`, and one for creating an empty `Optional`.

#### `of`

The static `of` method allows us to wrap an existing object with an `Optional`. If the existing object is not `null`, a populated `Optional` is returned:

```java
Optional<Foo> foo = Optional.of(new Foo());  // populated Optional
```

If the existing object is `null`, an NPE is thrown:

```java
Optional<Foo> foo = Optional.of(null);      // throws NullPointerException
```

#### `ofNullable`

The `ofNullable` static method is identical to the of method when a non-`null` value is passed (i.e., a populated `Optional` is produced), but will produce an empty `Optional` when `null` is passed (i.e., an NPE will not be thrown):

```java
Optional<Foo> foo1 = Optional.ofNullable(new Foo());  // populated Optional
Optional<Foo> foo2 = Optional.ofNullable(null);       // empty Optional
```

This is method is commonly used when the nullity of an object is unknown.

#### `empty`

The `empty` static method simply creates an empty `Optional`:

```java
Optional<Foo> foo = Optional.empty();    // empty Optional
```

This method is, by definition, identical to:

```java
Optional<Foo> foo = Optional.ofNullable(null);
```

As we will see in the following sections, the `empty` method is often used when it is known *a priori* that no value exists.

### Instance Methods

The instance methods allow us to interact with existing `Optional` objects and focus primarily on querying the state of an `Optional`, obtaining the wrapped object from an `Optional`, and manipulating `Optional` objects.

#### `isPresent` & `isEmpty`

Two query methods are included in the `Optional` class that allows us to check whether a given `Optional` is populated or empty:

1. `isPresent`: Returns `true` if the `Optional` is populated, or `false` otherwise
2. `isEmpty`: Returns `true` if the `Optional` is `empty`, or `false` otherwise

Therefore, given a populated `Optional`, the query methods will return the following:

```java
Optional<Foo> populated = // ...populated Optional...
populated.isPresent();    // true
populated.isEmpty();      // false
```

Given an empty `Optional`, the query methods will return the following:

```java
Optional<Foo> empty = // ...empty Optional...
populated.isPresent();    // false
populated.isEmpty();      // true
```

#### `get`

The `get` method obtains the value wrapped by an `Optional` if the `Optional` is populated or throws a [`NoSuchElementException`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/NoSuchElementException.html) if the `Optional` is empty. This method is useful for converting an existing `Optional` to its value (i.e., from `Optional<Foo>` to `Foo`) when we can guarantee that the `Optional` is populated, but we should use this method sparingly.

In practice, guaranteeing that an `Optional` is populated requires that we first query the `Optional` using the `isPresent` or `isEmpty` methods and then call `get`:

```java
Optional<Foo> possibleFoo = doSomething();
if (possibleFoo.isPresent()) {
    Foo foo = possibleFoo.get();
    // ...use the foo object...
}
else {
    // ...handle case of missing Foo...
}
```

The issue with this pattern is that is closely resembles the `null`\-check that we performed before introducing the `Optional`. Thus, this approach removes the inherent benefits of the `Optional` class. In most cases, we should avoid using the `get` method and use one of the other methods—such as `orElse` or `orElseThrow`—to obtain the value associated with a populated `Optional`.

#### `orElse` Family

The `orElse` family of methods allows us to obtain the value wrapped by an `Optional`—if the `Optional` is populated—or a default method if the `Optional` is empty. The simplest method in this family is `orElse`, which takes an object of the wrapped type and returns it if the `Optional` is empty. For example, given an `Optional<Foo>` object, the `orElse` method takes a `Foo` object. If the `Optional` is populated, it returns the populated value; if the `Optional` is empty, it returns the `Foo` object that we passed to the `orElse` method:

```java
Optional<Foo> possibleFoo = doSomething();
Foo foo = possibleFoo
    .orElse(new Foo());
```

There are times, however, where the creation of a default value may be an expensive operation and may be unlikely to be used. For example, the default value may require that a connection be established to a remote server or may require an extended or large lookup from a database. If it is likely that `Optional` will be populated, it is unlikely that we will need the default value. With the `orElse` method, we are forced to create the default value even if it goes unused, which could lead to a serious performance impact.

The `Optional` class also includes the `orElseGet` method that takes a [`Supplier`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/function/Supplier.html) that can lazily create a default object. This allows the `Optional` class to create a default object only when needed (i.e., the default object is only created when if the `Optional` is empty). For example:

```java
Optional<Foo> possibleFoo = doSomething();
Foo foo = possibleFoo
    .orElseGet(() -> { /* ...lazily create a Foo object... */ });
```

#### `orElseThrow` Family

Similar to the `orElse` method, the `Optional` class provides an `orElseThrow` method that allows us to throw an exception when obtaining the wrapped value if the `Optional` is empty. Unlike the `orElse` methods, though, the `orElseThrow` method has two forms:

1. A no-argument form that throws an `NoSuchElementException` if the `Optional` is empty or returns the wrapped value if the `Optional` is populated
2. A form that takes a `Supplier` that creates `Throwable` objects and throws the `Throwable` object if the `Optional` is empty or returns the wrapped value if the `Optional` is populated

For example, we can obtain a `Foo` object from an `Optional<Foo>` object as follows:

```java
Optional<Foo> possibleFoo = doSomething();
Foo foo = possibleFoo
    .orElseThrow();
```

If the `Optional` is empty, a `NoSuchElementException` will be thrown. If the `Optional` is populated, the wrapper value will be returned. The `orElseThrow` method, therefore, is identical to the `get` method in its functionality, but its name better describes what its purpose is. Thus, the `orElseThrow` method should be used anywhere it is value to throw a `NoSuchElementException` when an `Optional` is not populated without first checking that it is populated (i.e., not using the `isPresent` or `isEmpty` query methods).

The `get` method should be reserved for use only when it is used within one of the `Optional` query methods (i.e., the populated or empty state of the `Optional` is checked first). Note that this `orElseThrow` method was introduced in JDK 9 as a way of reducing the confusion surrounding the use of the `get` method and should be favored over the get method.

According to [Brian Goetz](https://stackoverflow.com/a/49159955/2403253):

> ...One of the few mistakes we made \[in Java 8\] was the naming of `Optional.get()`, because the name just invites people to call it without calling `isPresent()`, undermining the whole point of using `Optional` in the first place....
>
> During the Java 9 time frame, we proposed to deprecate `Optional.get()`, but the public response to that was ... let's say cold. As a smaller step, we introduced `orElseThrow()` in \[Java\] 10...as a more transparently named synonym for the current pernicious behavior of `get()`.

The `Optional` class also includes an overloaded `orElseThrow` method that throws a custom exception when the `Optional` is empty. This method accepts a `Suppler` that creates any `Throwable` object—or object that is a subclass of `Throwable`—and throws it. For example:

```java
Optional<Foo> possibleFoo = doSomething();
Foo foo = possibleFoo
    .orElseThrow(() -> { /* ...lazily create a Foo object... */ });
```

This is useful when a client considers a missing object to be an error and wishes the throw an exception when accessing an empty `Optional`. It is also a common practice to throw simple exceptions using the functional form of the constructor:

```java
Optional<Foo> possibleFoo = doSomething();
Foo foo = possibleFoo
    .orElseThrow(SomeException::new);
```

#### `ifPresent` Family

The `ifPresent` method accepts a [`Consumer`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/function/Consumer.html) that performs an action using the wrapped value if the `Optional` is populated. This is a functional alternative to obtaining the wrapped object using the `orElse` or `orElseThrow` methods, primarily when we do not wish to perform any action when the value is not present. For example:

```java
ptional<Foo> possibleFoo = doSomething();
possibleFoo.ifPresent(foo -> { /* ...do something with foo... */ });
```

The `Optional` class also includes a similar method, `ifPresentOrElse`, that allows us to handle the case when the `Optional` is empty as well. The first argument accepted by the `ifPresentOrElse` method is a `Consumer` that performs an action using the wrapped value if the `Optional` is populated, while the second argument is a [`Runnable`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/lang/Runnable.html) that performs an action if the `Optional` is empty. Thus, the `Consumer` is called only if the `Optional` is populated, while the `Runnable` is called only if the `Optional` is empty. For example:

```java
Optional<Foo> possibleFoo = doSomething();
possibleFoo.ifPresentOrElse(
    foo -> { /* ...do something with foo... */ },
    () -> { /* ...do something when no foo found... */ }
);
```

The benefit of both of these methods is that the `Consumer` is never called if the `Optional` is empty. Likewise, in the case of `ifPresentOrElse`, the `Runnable` is never called if the `Optional` is populated. This allows us to provide complex or expensive operations that will be lazily called depending on the state of the `Optional`.

Note that this method should not just be used for expensive operations. This method should be used anytime an operation should be performed on a populated value. For example, if we wanted to update an object only if it exists, we could do something similar to the following:

```java
public class Bar {
    private boolean isUpdated = false;

    public void update() {
        isUpdated = true;
    }
}

public Optional<Bar> findBar() {
    // ...return a populated Bar if it could be found...
}

findBar().ifPresent(bar -> bar.update());
```

In this case, we are not concerned with performing any action if the `Bar` object is not found. If we were, we could use the `ifPresentOrElse` method instead.

#### `map`

The `map` method allows us to convert a wrapped value from one object to another if an `Optional` is populated. This method can be thought of as a pipeline method, where the wrapped value is passed along the pipeline and transformed into a new value. This method works by accepting a [`Function`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/function/Function.html) object that is applied to the wrapped value to produce the mapped value. If the `Optional` is empty, the `Function` object is never called, and an empty `Optional` is returned from the `map` method.

This method is useful when we do not know if a value is present, but if it is, it should be transformed into another object. This is a common use case when reading from a database, which usually stores Data Transfer Objects (DTOs). In most applications, the DTO is used to store a domain object in a database efficiently, but at the higher levels of the application, the domain object itself is needed. Therefore, we must convert from the DTO to the domain object. 

If we perform a lookup of a database object, we may or may not find the object. Thus, this is a good use case for returning an `Optional` wrapping the DTO. In order to convert to the domain object, we can use the `map` method. For example, suppose we have a DTO (`PersonDto`) that stores the name of a `Person` object in a single line while the `Person` object has the name split into first and last name (i.e., the name is stored as `"John Doe"` in the `PersonDto` object, but it is stored with a first name of `"John"` and a last name of `"Joe"` in the `Person` object). We can use a mapper object to convert from the `PersonDto` to `Person` object and use the mapper to map the `PersonDto` object returned from a database to a `Person` object:

```java
public class Person {
    private String firstName;
    private String lastName;
    // ...getters & setters...
}
public class PersonDto {
    private String name;
    // ...getters & setters...
}
public class PersonMapper {
    public Person fromDto(PersonDto dto) {
        String[] names = dto.getName().split("\\s+");
        Person person = new Person();
        person.setFirstName(names[0]);
        person.setLastName(names[1]);
        return person;
    }
}
public class Database {
    public Optional<PersonDto> findPerson() {
        // ...return populated DTO if DTO is found...
    }
}
Database db = new Database();
PersonMapper mapper = new PersonMapper();
Optional<Person> person = db.findPerson()
    .map(mapper::fromDto);

```java

Note that it is possible to have a conversion that should result in an empty `Optional`. For example, if a conversion from a given object to another is not possible, then the `map` method should return an empty `Optional`. An anti-pattern for performing this technique is to have the `Function` object return `null`, which will then be wrapped by the `map` method — using `ofNullable`, which allows for our `null` object to be wrapped without throwing an exception — into an empty `Optional`:

```java
Optional<Person> person = db.findPerson()
    .map(dto -> {
        if (dtoCanBeConverted()) {
            return mapper.fromDto(dto);
        }
        else {
            return null; // 错误的做法
        }
    })
```

If the method `dtoCanBeConverted` evaluates to `false`, the `Function` object returns `null` which then results in `person` being an empty `Optional`. This approach is flawed because it reintroduces the insidious use of `null` values, whose replacement was the original purpose of the `Optional` class. Instead, we should use the `flatMap` method and explicitly return an empty `Optional`.

#### `flatMap`

The `flatMap` method is similar to the `map` method, except the `flatMap` accepts a `Function` object that converts the wrapped value to a new `Optional`. Unlike the `map` method, `flatMap` allows us to return an `Optional` of our choice. Thus, we can explicitly return an empty `Optional` if the mapping `Function` is unable to convert the wrapped value:

```java
Optional<Person> person = db.findPerson()
    .flatMap(dto -> {
        if (dtoCanBeConverted()) {
            Person person = return dao.fromDto(dto);
            return Optional.ofNullable(person);
        }
        else {
            return Optional.empty();
        }
    });
```

It is important to note that we are no longer able to simply return a `Person` object as we did with the `map` method. Instead, we are now responsible for wrapping the converted object into an `Optional`. Note that if the `Function` object returns a `null` `Optional`, an NPE is thrown. For example, the following will throw an NPE when executed:

```java
ptional<Person> person = db.findPerson()
    .flatMap(dto -> null);
```

#### `filter`

The `filter` method allows us to return a populated `Optional` if a populated `Optional` satisfies the supplied [`Predicate`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/function/Predicate.html). Thus, if the `filter` method is applied to an empty `Optional`, the `Predicate` will not be called. Likewise, if the `filter` method is applied to a populated `Optional`, but the wrapped value does not satisfy the supplied `Predicate` (i.e., the `test` method of the `Predicate` object evaluates to `false`), an empty `Optional` is returned. For example:

```java
public class Bar {
  
    private int number;
  
    public Bar(int number) {
        this.number = number;
    }
  
    // ...getters & setters...
}
Predicate<Bar> greaterThanZero = bar -> bar.getNumber() > 0;
Optional.of(new Bar(1))
    .filter(greaterThanZero)
    .isPresent();              // true
Optional.of(new Bar(-1))
    .filter(greaterThanZero)
    .isPresent();              // false
```

#### `stream`

The `stream` method allows us to transform an `Optional` into a `Stream`, which allows us to perform stream-based operations on an `Optional`. The `Stream` returned by the `stream` method has two distinct behaviors, depending on the state of the `Optional`:

1. A `Stream` containing the value wrapped by the `Optional` if the `Optional` is populated
2. An empty `Stream` if the `Optional` is empty

Once the `Stream` has been created, any `Stream` operation can be performed on the `Optional`:

```java
Set<Person> people = findPerson().stream()
    .filter(/* ... */)
    .map(/* ... */)
    .flatMap(/* ... */)
    .collect(Collectors.toSet());
```

## When and When Not To Use

One of the most controversial aspects of the `Optional` class is when it should and should not be used. In this section, we will look at some of the common use cases, such as method return values, fields, and parameters, where `Optional`s may or may not be well suited.

### Return Values

As we have seen throughout this article, `Optional`s are well suited for method return values because that was its intended purpose. According to the [`Optional` class documentation](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/Optional.html):

> `Optional` is primarily intended for use as a method return type where there is a clear need to represent "no result," and where using `null` is likely to cause errors.

In general, an `Optional` should be used as a return value if:

1. It is expected that a value may or may not be present
2. It is not an error if a value is missing
3. The client is responsible for handling the case of a missing value

`Optional` return values are often used for queries that may or may not find a desired object. For example, repositories will often be defined in the following manner:

```java
public interface BookRepository {
    public Optional<Book> findById(long id);
    public Optional<Book> findByTitle(String title);
    // ...
}
```

This allows the client to handle a missing `Book` object — such as by ignoring a missing object, creating a default object, or throwing an exception — in a manner that is appropriate to the context in which the method was called.

### Fields

While `Optional` objects are well-suited for return types, they are less apt, for instance, fields. It is possible to create a field similar to the following, but it is highly inadvisable:

```java
public class Bar {
  
    private Optional<Foo> foo;
  
    // ...getters & setters...
}
```

`Optional` fields should be avoided because the `Optional` class is not serializable (i.e., does not implement the [`Serializable`](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/io/Serializable.html) interface). According to [Brian Goetz](https://stackoverflow.com/a/26328555/2403253):

> Of course, people will do what they want. But we did have a clear intention when adding this feature, and it was *not* to be a general purpose Maybe type, as much as many people would have liked us to do so. Our intention was to provide a limited mechanism for library method return types where there needed to be a clear way to represent "no result", and using `null` for such was overwhelmingly likely to cause errors.

Therefore, `Optional` types are intended solely for method return types. Since fields constitute the internal state of a class and should not be visible to outside clients, if a field is considered optional, a getter can be created that returns an `Optional` object instead:

```java
public class Bar {
  
    private Foo foo;
  
    public Optional<Foo> getFoo() {
        return Optional.ofNullable(foo);
    }
}
```

Using this technique, clients are explicitly informed that the `foo` value may or may not be present, while the serializability of `Bar` is maintained.

### Parameters

There are valid cases when a parameter to a method or constructor may be optional, but an `Optional` should not be used for this purpose. For example, the following should be avoided:

```java
public class Bar {
    public void doSomething(Optional<Foo> foo) {
    // ...
    }
}
```

Instead of setting the parameter type to `Optional`, method overloading should be used:

```java
public class Bar {
  
    public void doSomething() {
        // ...
    }
  
    public void doSomething(Bar bar) {
        // ...
    }
}
```

Additionally, non-overloaded methods — with different method names — can also be used:

```java
public class Bar {
  
    public void doSomething() {
        // ...
    }
  
    public void doSomethingWithBar(Bar bar) {
        // ...
    }
}
```

## Alternatives

While the `Optional` class is effective in the correct context, it is not the only approach that can be used when a desired value may or may not be found. In this section, we cover three alternatives to the `Optional` class and how they can be applied in the proper context.

### `null`

The simplest alternative is to use `null`, as we saw at the beginning of this article. While this approach does accomplish our goal, after the introduction of the `Optional` class, `null`s should only be used when `Optional` objects require too much overhead. This overhead can be in terms of the extra memory requires for the `Optional` wrapper class or in terms of the extra cycles requires to execute the `Optional` methods.

It may be tempting to use performance as an excuse to use `null`s where `Optional`s would be more effective, but in a large majority of applications, the `Optional` class adds a trivial amount of overhead. Unless we are working with low-level code, just as bytes that come from a network or driver or we are working with extremely large amounts of data, `Optional`s should always be preferred over `null`s for method return types.

### Null Object

A more effective alternative than `null` values is to [introduce a Null Object](https://refactoring.guru/introduce-null-object). A null object is an object that extends the desired type but contains the logic that would have been executed for the `null` case. For example, suppose we have the following code:

```java
public class Article {
  
    private long id;
  
    public void submit() {
        // ...
    }
  
    // ...getters & setters...
}
public class ArticleRepository {
  
    public Article findById(long id) {
        // ...return the article if it can be found...
    }
}
ArticleRepository repository = new ArticleRepository();
Article article = repository.findById(1);
if (article == null) {
    throw new ArticleNotFoundException();
}
else {
    article.submit();
}
```

We can refactor this code using a null object into the following:

```java
public class Article {
    // ...same as before...
}
public class NullArticle extends Article {
  
    @Override
    public void submit() {
        throw new ArticleNotFoundException();
    }
}
public class ArticleRepository {
   
    public Article findById(long id) {
      
        if (articleIsFound()) {
            // return article...
        }
        else {
            return new NullArticle();
        }
    }
}
ArticleRepository repository = new ArticleRepository();
Article article = repository.findById(1);
article.submit();
```

It is important to note that the introduction of a null object assumes that the method itself knows how to handle the case of a missing value. 

### Exceptions

Another alternative that we saw in this article is to throw an exception when a desired object cannot be found. This approach works if the method knows that a failure to find a desired object is an error. For example:

```java
public class ArticleRepository {
   
    public Article findById(long id) {
      
        if (articleIsFound()) {
            // return article...
        }
        else {
            throw new ArticleNotFoundException();
        }
    }
}
```

## Conclusion

There are many cases in which desired values may or may not be present in an application, and handling these cases in a readable and effective manner is an important part of well-designed software. As of JDK 7, Java includes the `Optional` class, which allows developers to return values that may or may not be present and allows clients to handle these cases according to the context in which they occur. While the `Optional` class should only be used for method return values, understanding its usefulness and how to apply it using simple techniques is an important part of mastering modern Java.

Opinions expressed by DZone contributors are their own.
