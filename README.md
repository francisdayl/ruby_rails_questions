# ruby_rails_questions


## Ruby questions

#### 1. What is Ruby programming language?
Ruby is a dynamic, reflective, general purpose, open source programming language that focuses on simplicity and productivity. Ruby has a mixed features of Perl, small talk, Eiffel, Ada and Lisp. Ruby was designed to create a new language which makes a balance with the functionality of Imperative languages. 
#### 2.  Why Ruby is known as a language of flexibility?
Ruby is known as a language of flexibility because it facilitates its author to alter the programming elements. Some specific parts of the language can be removed or redefined. Ruby does not restrict the user. For example, to add two numbers, Ruby allows to use + sign or the word 'plus'. This alteration can be done with Ruby's built-in class Numeric.
#### 3. List some features of Ruby?
Ruby has many features. Some of them are listed below.

    Object-oriented
    Flexible
    Dynamic typing and Duck typing
    Garbage collector
    Keyword arguments

#### 4. Explain some differences between Ruby and Python.
Similarities:

    High level language
    Support multiple platforms
    Use interactive prompt called irb
    Server side scripting language

Differences:

    Ruby is fully object oriented while Python is not.
    Ruby supports EclipseIDE while Python supports multiple IDEs.
    Ruby use Mixins while Python doesn't.
    Ruby supports blocks, procs and lambdas while Python doesn't.

#### 5. What are class libraries in Ruby?
Ruby class libraries contain variety of domain such as thread programming, data types, various domains. Following is a list of domains which has relevant class libraries:

    
    Text processing: File, String, Regexp for quick and clean text processing.
    CGI Programming: There are supporting class library for CGI programming support like, data base interface, eRuby, mod_ruby for Apache, text processing classes.
    Network programming: Various well-designed sockets are available in ruby for network programming.
    GUI programming: Ruby/Tk and Ruby/Gtk are the classes for GUI programming
    XML programming: UTF-8 text processing regular expression engine make XML programming very handy in ruby.


#### 6. Name some operators used in Ruby.
Operators are a symbol which is used to perform different operations.

    Unary operator
    Airthmetic operator
    Bitwise operator
    Logical operator
    Ternary operator

#### 7. What is RubyGems in Ruby programming language?
RubyGems provides a standard format for distributing ruby programs and libraries. It works as a package manager for the Ruby programming language.
#### 8. What is the use of load and require in Ruby?
In Ruby, load and require both are used for loading the available code into the current code. In cases where loading the code required every time when changed or every times someone hits the URL, it is suggested to use 'load'.

It case of autoload, it is suggested to use 'require'.
#### 9. Explain Ruby if-else statement.
The Ruby if-else statement is used to test condition. There are various types of statement in Ruby.

    if statement
    if-else statement
    if-else-if (elsif) statement
    ternary statement

#### 10. Explain case statement in Ruby.
In Ruby, we use 'case' instead of 'switch' and 'when' instead of 'case'. The case statement matches one statement with multiple conditions just like a switch statement in other languages.

For more information: Click here
#### 11. Explain for loop in Ruby.
Ruby for loop iterates over a specific range of numbers. Hence, for loop is used if a program has fixed number of itrerations.

Ruby for loop will execute once for each element in expression. 
#### 12. Explain until loop in Ruby.
Ruby until loop runs until the given condition evaluates to true. It exits the loop when condition becomes true. It is opposite of the while loop.
#### 13. Explain next statement in Ruby.
Ruby next statement is used to skip loop's next iteration. Once the next statement is executed, no further iteration will be performed
#### 14. Explain redo statement in Ruby.
Ruby redo statement is used to repeat the current iteration of the loop. The redo statement is executed without evaluating loop's condition.
#### 15. Explain retry statement in Ruby.
Ruby retry statement is used to repeat the whole loop iteration from the start.
#### 16. How will you comment in Ruby.
Ruby comments are non-executable lines in a program. They do not take part in the execution of a program.

Single line comment syntax:

    #This is single line comment

Multi line comment syntax:

    =begin
    This
    is
    multi line
    comment
    =end
#### 17.  Explain Ruby object.
Object is the default root of all Ruby objects. Ruby objects inherit from BasicObject which allows creating alternate object hierarchies.
#### 18. How to create Ruby object?
Objects in Ruby are created by calling new method of the class. It is a unique type of method and predefined in Ruby library.
#### 19. Explain Ruby class.
Each Ruby class is an instance of Ruby class. Classes in Ruby are first class objects. It always starts with a keyword class followed by the class name.

Syntax:

    class ClassName
    codes...
    end
#### 20. In how many ways a block is written in Ruby.
A block is written in two ways:

    Multi-line between do and end
    Inline between braces {}

Both are same and have the same functionality.
#### 21. What is yield statement in Ruby.
The yield statement is used to call a block within a method with a value.
#### 22. Explain ampersand parameter (&block) in Ruby.
The &block is a way to pass a reference (instead of a local variable) to the block to a method.
Here, block word after the & is just a name for the reference, any other name can be used instead of this. 
#### 23 Explain Ruby module.
Ruby module is a collection of methods and constants. A module method may be instance method or module method. They are similar to classes as they hold a collection of methods, class definitions, constants and other modules. They are defined like classes. Objects or subclasses can not be created using modules. There is no module hierarchy of inheritance.

Modules basically serve two purposes:

    They act as namespace. They prevent the name clashes.
    They allow the mixin facility to share functionality between classes.

#### 24 Explain module mixins in Ruby.
Ruby doesn't support multiple inheritance. Modules eliminate the need of multiple inheritance using mixin in Ruby.

A module doesn't have instances because it is not a class. However, a module can be included within a class.

When you include a module within a class, the class will have access to the methods of the module.
#### 25 How to write multiline string in Ruby.
Writing multiline string is very simple in Ruby language. We will show three ways to print multiline string.

    String can be written within double quotes.
    The % character is used and string is enclosed within / character.
    In heredoc syntax, we use << and string is enclosed within word STRING.

#### 26 What is the use of global variable $ in Ruby?
The global variable is declared in Ruby that you can access it anywhere within the application because it has full scope in the application. The global variables are used in Ruby with $ prepend.
#### 27 What is concatenating string in Ruby. In how many ways you can create a concatenating string.
Ruby concatenating string implies creating one string from multiple strings. You can join more than one string to form a single string by concatenating them.

There are four ways to concatenate Ruby strings into single string:

    Using plus sign in between strings.
    Using a single space in between strings.
    Using << sign in between strings.
    Using concat method in between strings.

#### 28 What are freezing string in Ruby.
In most programming languages strings are immutable. It means that an existing string can't be modified, only a new string can be created out of them.
In Ruby, by default strings are not immutable. To make them immutable, freeze method can be used.
#### 29. In how many ways you can compare Ruby string?
Ruby strings can be compared with three operators:

    With == operator : Returns true or false
    With eql? Operator : Returns true or false
    With casecmp method : Returns 0 if matched or 1 if not matched

#### 30. What are Ruby arrays and how they can be created?
Ruby arrays are ordered collections of objects. They can hold objects like integer, number, hash, string, symbol or any other array.

Its indexing starts with 0. The negative index starts with -1 from the end of the array. For example, -1 indicates last element of the array and 0 indicates first element of the array.

A Ruby array is created in many ways.

    Using literal constructor []
    Using new class method

#### 31. How to access Ruby array elements? How many methods are used to access Ruby elements.?
Ruby array elements can be accessed using #[] method. You can pass one or more than one arguments or even a range of arguments.

Syntax:

    #[] method

Methods used to access Ruby elements:

    at method
    slice method
    fetch method
    first and last method
    take method
    drop method

#### 32.  In how many ways items can be added in an array in Ruby?
Ruby array elements can be added in different ways.

    push or <<
    unshift
    insert

#### 33 In how many ways items can be removed from array in Ruby?
Ruby array elements can be removed in different ways.

    pop
    shift
    delete
    uniq

#### 34 Explain Ruby hashes.
A Ruby hash is a collection of unique keys and their values. They are similar to arrays but array use integer as an index and hash use any object type. They are also called associative arrays, dictionaries or maps.

If a hash is accessed with a key that does not exist, the method will return nil.
#### 35 How to create a new time instance in Ruby?
A new Time instance can be created with ::new. This will use your current system's time. Parts of time like year, month, day, hour, minute, etc can also be passed.

While creating a new time instance, you need to pass at least a year. If only year is passed, then time will default to January 1 of that year at 00:00:00 with current system time zone. 
#### 36  Explain Ruby ranges. What are the ways to define ranges?
Ruby range represents a set of values with a beginning and an end. They can be constructed using s..e and s...e literals or with ::new.

The ranges which has .. in them, run from beginning to end inclusively. The ranges which has ... in them, run exclusively the end value.

Ruby has a variety of ways to define ranges.

    Ranges as sequences
    Ranges as conditions
    Ranges as intervals

#### 37 What are Ruby iterators?
erator is a concept used in object-oriented language. Iteration means doing one thing many times like a loop.

The loop method is the simplest iterator. They return all the elements from a collection, one after the other. Arrays and hashes come in the category of collection.
#### 38 How many iterators are there in Ruby?
Following iterators are there in Ruby:

    each iterator
    times iterator
    upto and downto iterator
    step iterator
    each_line iterator

#### 39Name different methods for IO console in Ruby?
The IO console provides different methods to interact with console. The class IO provides following basic methods:

    IO::console
    IO#raw#raw!
    IO#cooked
    IO#cooked!
    IO#getch


### 40. How to open a file in Ruby?
A Ruby file can be created using different methods for reading, writing or both.

There are two methods to open a file in Ruby.

    File.new method : Using this method a new file can be created for reading, writing or both.
    File.open method : Using this method a new file object is created. That file object is assigned to a file.

Difference between both the methods is that File.open method can be associated with a block while File.new method can't.
### 41.  How to read a file in Ruby?
There are three different methods to read a file.

To return a single line, following syntax is used.

Syntax:

    f.gets
    code...

To return the whole file after the current position, following syntax is used.

Syntax:

    f.read
    code...

To return file as an array of lines, following syntax is used.

Syntax:

    f.readlines
    [code...]
### 42. What is sysread method in Ruby?
The sysread method is also used to read the content of a file. With the help of this method you can open a file in any mode.
### 43. How will you rename and delete a file in Ruby?
Ruby files are renamed using rename method and deleted using delete mehtod.
To rename a file, following syntax is used.

Syntax:
    File.rename("olderName.txt","newName.txt")

To delete a file, following syntax is used.

Syntax:
    File.delete("filename.txt")
### 44. How to check whether a directory exist or not in Ruby?
To check whether a directory exists or not exists? Method is used.
Syntax:

    puts Dir.exists? "dirName"
### 45.  Explain Ruby exceptions.
Ruby exception is an object, an instance of the class Exception or descendent of that class. When something goes wrong, Ruby program throws an exceptional behavior. By default Ruby program terminates on throwing an exception.
### 46. What are some built-in Ruby class exceptions.
Built-in subclasses of exception are as follows:

    NoMemoryError
    ScriptError
    SecurityError
    SignalException

### 47. How an exception is handled in Ruby?
To handle exception, the code that raises exception is enclosed within begin-end block. Using rescue clauses we can state type of exceptions we want to handle.
### 48. Explain the use of retry statement in Ruby?
Usaually in a rescue clause, the exception is captured and code resumes after begin block. Using retry statement, the rescue block code can be resumed from begin after capturing an exception.

Syntax:

    begin
    code....
    rescue
    # capture exceptions
    retry # program will run from the begin nlock
    end
### 49. Explain raise statement in Ruby?
The raise statement is used to raise an exception.

Syntax:

    raise

Or,

    raise "Error Message"

Or,

    raise ExceptionType, "Error Message"

Or,

    raise ExceptionType, "Error Message" condition
### 50. Explain the use of ensure statement in Ruby?
There is an ensure clause which guarantees some processing at the end of code. The ensure block always run whether an exception is raised or not. It is placed after last rescue clause and will always executed as the block terminates.

The ensure block will run at any case whether an exception arises, exception is rescued or code is terminated by uncaught exception.

Syntax:

    begin
    code..
    #..raise exception
    rescue
    #.. exception is rescued
    ensure
    #.. This code will always execute.
### 51. What is the difference between calling super and calling super()?
A call to super invokes the parent method with the same arguments that were passed to the child method. An error will therefore occur if the arguments passed to the child method don’t match what the parent is expecting.

A call to super() invokes the parent method without any arguments, as presumably expected. As always, being explicit in your code is a good thing.
### 52. How is Symbol different from variables?
In the following ways, the symbol differs from the variables.

    It is more akin to a string than a variable.
    A string in Ruby is mutable, while a symbol is not.
    There is only one duplicate of the symbol that has to be produced.
    In Ruby, symbols are frequently used to correlate to enums.

### 53. Explain each of the following operators and how and when they should be used: ==, ===, eql?, equal?
== – Checks if the value of two operands are equal (often overridden to provide a class-specific definition of equality).

=== – Specifically used to test equality within the when clause of a case statement (also often overridden to provide meaningful class-specific semantics in case statements).

eql? – Checks if the value and type of two operands are the same (as opposed to the == operator which compares values but ignores types). For example, 1 == 1.0 evaluates to true, whereas 1.eql?(1.0) evaluates to false.

equal? – Compares the identity of two objects; i.e., returns true iff both operands have the same object id (i.e., if they both refer to the same object). Note that this will return false when comparing two identical copies of the same object.
### 54. Explain the difference between: {x += " world"}  and {x.concat " world"}
he += operator re-initializes the variable with a new value, so a += b is equivalent to a = a + b.

Therefore, while it may seem that += is mutating the value, it’s actually creating a new object and pointing the the old variable to that new object.

This is perhaps easier to understand if written as follows:
### 55. Mention What Is The Difference Between A Gem And A Plugin In Ruby?
Gem: A gem is a just ruby code. It is installed on a machine, and it’s available for all ruby applications running on that machine.
Plugin: Plugin is also ruby code, but it is installed in the application folder and only available for that specific application.
### 56. Explain About Garbage Collection Feature Of Ruby?
Garbage collection is a process of reclaiming the memory space. Ruby deletes unallocated and unused objects automatically. This feature can be controlled by applying proper syntax and program through ruby.

Ruby performs garbage collection automatically. Ruby is an object oriented language and every object oriented language tends to allocate many objects during execution of the program.
### 57. Explain About Float, Dig And Max?
Float class is used whenever the function changes constantly. It acts as a sub class of numeric. They represent real characters by making use of the native architecture of the double precision floating point.

Max is used whenever there is a huge need of Float.

Dig is used whenever you want to represent a float in decimal digits.
### 58. What Is The Use Of Interpolation In Ruby?
Interpolation is a process of inserting a string into a literal. It is a very important process in Ruby. A string can be interpolated into a literal by placing a hash (#) within {} open and close brackets.
### 59. Explain About Class Variable And Global Variable?
A class variable starts with an @@ sign which is immediately followed by upper or lower case letter. You can also put some name characters after the letters which stand to be a pure optional. A class variable can be shared among all the objects of a class. A single copy of a class variable exists for each and every given class.
### 60. What Is The Difference Between Procs And Blocks?
Block is just the part of the syntax of a method while proc has the characteristics of a block.
Procs are objects, blocks are not.
At most one block can appear in an argument list.
Only block is not able to be stored into a variable while Proc can
### 61. How Can We Define Ruby Regular Expressions?
Ruby regular expression is a special sequence of characters that helps you match or find other strings. A regular expression literal is a pattern between arbitrary delimiters or slashes followed by %r.
### 62. How Would You Create Getter And Setter Methods In Ruby?
Setter and getter methods in Ruby are generated with the attr_accessor method. attr_accessor is used to generate instance variables for data that’s not stored in your database column.

You can also take the long route and create them manually.
### 63. How Does A Symbol Differ From A String?
symbols are immutable and reusable, retaining the same object_id.

Be prepared to discuss the benefits of using symbols vs. strings, the effect on memory usage, and in which situations you would use one over the other.
### 64. What Are The Three Levels Of Method Access Control For Classes And What Do They Signify? What Do They Imply About The Method?
Public, protected, and private.

Public methods can be called by all objects and subclasses of the class in which they are defined in.
Protected methods are only accessible to objects within the same class.
Private methods are only accessible within the same instance.
### 65. How would you freeze an object in Ruby? Can you provide a simple example?
to prevent an object from being changed. This can be accomplished using the freeze method (Object.freeze) as in the sample code below.

water.freeze
if( water.frozen? )
puts “Water object is a frozen object”
else
puts “Water object is a normal object”
end
### 66. Can you explain the role of thread pooling in relation to the thread lifecycle in Ruby?
Ruby, the lifecycle of a single thread starts automatically as soon as CPU resources are available. The thread runs the code in the block where it was instantiated and obtains the value of the last expression in that block and returns it upon completion. Threads use up resources, but running multiple threads at a time can improve an app’s performance. Thread pooling is a technique wherein multiple pre-instantiated reusable threads are left on standby, ready to perform work when needed. Thread pooling is best used when there are a large number of short tasks that must be performed. This avoids the overhead of having to create a new thread every time a small task is about to be performed.
### 67. How do you remove nil values in array using ruby?
Array#compact removes nil values.

Example:

>> [nil,123,nil,"test"].compact
=> [123, "test"]
### 68. What is the difference between the Object methods clone and dup?
Object#dup creates a shallow copy of an object. For example, it will not copy any mixed-in module methods, whereas Object#clone will
### 69. What is the difference between extend and include in ruby?

include mixes in specified module methods as instance methods in the target class
extend mixes in specified module methods as class methods in the target class
Given the following class definitions:

Here’s how ClassThatIncludes behaves:

Here’s how ClassThatExtends behaves:

We should mention that object.extend ExampleModule makes ExampleModule methods available as singleton methods in the object.

### 70.  Describe a closure in Ruby
A closure is an object that is both an invocable function together with a variable binding. The object retains access to the local variables that were in scope at the time of the object definition.

A closure in Ruby retain variables by reference; the closure also extends the lifetimes of its variables. A closure’s reference to its variables is dynamically bound that means the values of the variables are resolved when the Proc object is executed.

It also possible to alter a closure. The binding of a closure can be altered using #binding.
### 71. What is the difference between throw/catch and raise/rescue?
Throw and catch accept matching symbols as arguments and should be considered a control-flow structure where raise and rescue is used to raise and handle exceptions. throw and catch are not commonly used while exception handling with raise and rescue is used often.
### 72. Why might you use Hash#fetch over Hash#[] when querying values in a hash? 
Hash#fetch provides options for handling the case where a key does not exist in the hash.
### 73. Describe a closure in Ruby
A closure is an object that is both an invocable function together with a variable binding. The object retains access to the local variables that were in scope at the time of the object definition.

A closure in Ruby retain variables by reference; the closure also extends the lifetimes of its variables. A closure's reference to its variables is dynamically bound that means the values of the variables are resolved when the Proc object is executed.

It also possible to alter a closure. The binding of a closure can be altered using #binding.
### 74. Explain this ruby idiom: a ||= b
a = b when a == false
otherwise a remains unchanged
a || a = b # (Kudos to Markus Prinz)

a = 1
b = 2
a ||= b #=> a = 1

a = nil
b = 2
a ||= b #=> a = 2

a = false
b = 2
a ||= b #=> a = 2
### 75. What is the difference between #== and #equal??
#== performs the generic comparison and is implemented differently across classes while #equal? is defined on BasicObject and compares object identity. Therefore, #equal? should not be overridden in subclasses.
### 76. #== performs the generic comparison and is implemented differently across classes while #equal? is defined on BasicObject and compares object identity. Therefore, #equal? should not be overridden in subclasses.
    Array#each method iterates over the elements of the array and executes the provided block each time. However, it returns the original array unaffected.
    Array#map will return a new array of elements containing the values returned by the block it is provided. It also does not affect the original array

### 78. What is the difference between a proc and a lambda? 


Both procs and lambda expressions are stored blocks, but the syntax and behavior are slightly different.
The lambda returns from itself, but the procedure returns from the method it is in.
Note that method_proc returns 1 because the call to the procedure ends execution inside the method.


### 79. 


### 80. 


## Rails questions

### 1. Explain what Ruby on Rails is.
Ruby on Rails is an open-source, server-side application framework that is written in the object-oriented programming language Ruby. It has many similarities to Python. Skilled developers use this framework to build websites and create web applications.
### 2. What is meant by Rails migration?
Candidates should be aware that developers use migrations to change databases using a structured approach. They may mention that developers can describe the changes they have made with the Ruby programming language and track the migrations they have already run with Active Record.
### 3. Explain what delete does in Ruby on Rails.
They should be able to explain that delete deletes a record, whereas destroy both deletes a record and executes any callbacks on the model.
### 4. What does “skinny controllers, skinny models” mean?
“Skinny controllers, skinny models” is a principle developers should use when their codebase grows. In situations like these, fat models can get challenging to manage, so this principle reminds developers to keep their models “skinny.”
### 5. Explain what count does in Ruby on Rails.
The count method executes SQL queries to count how many records there are. It’s handy when the number of records in the database has changed.
### 6. Explain what length does in Ruby on Rails.
The length method returns the number of items that are currently in a collection in memory. It’s different from count in that the method does not carry out a database transaction. It can also be used to count how many characters are in a string.
### 7. Explain what size does in Ruby on Rails.
size method performs the same action as the length method and that it is an alias.

### 8. Explain what the splat operator is.
Developers use the splat operator (*) when they pass arguments to a method but don’t want to specify how many arguments they are passing. Candidates may mention that there are two types of splat operators – the single splat (*) and the double splat (**).
### 9. Explain what ActiveJob is.
ActiveJob is a framework that developers use to declare jobs, such as clean-ups, billing charges, and mailings. When developers use ActiveJob, their goal is to ensure that apps have a job infrastructure.
### 10. What is a Hash in Ruby on Rails?
It’s a group of key/value pairs that makes it simpler for developers to access values by keys.
### 11. What is Active Record in Ruby on Rails?
Active Record is an object-relational mapping layer of code. Developers use Active Record as an interface that runs between the tables within a relational database and the program code in Ruby.
### 12. Outline the types of associations models can have in Ruby on Rails.
Candidates may respond to this Ruby on Rails interview question by mentioning that they use associations to create connections between models in a Rails application. They may then explain that Active Record supports three main types of associations:

    One-to-one: A relationship in which one object is linked to only one other object
    One-to-many: A relationship in which one object can be related to many other objects
    Many-to-many: A relationship in which an instance of the first type of object is linked to one or more instances of a second type of object, and an instance of a second type of object is linked to one or more instances of the first type of object
You indicate these associations by adding declarations to your models:

    has_one,
    has_many,
    belongs_to,
    has_and_belongs_to_many
### 13. When should you use Ruby on Rails
Use Ruby on Rails interview questions after you have invited candidates to complete a skills test.

Completing the hiring process in this order will:

    Enhance objectivity
    Reduce time-to-hire metrics
    Give you ideas for the interview stage

### 14. For which roles can you use Ruby on Rails
In addition to back-end developer positions, some of the roles that you might use Ruby on Rails interview questions for include:

    Server developers
    Web engineers
    Application developers
    Ruby on Rails architects
### 15. What do subdirectory app/controllers and app/helpers do?


    apps/controller: The controller classes are found in the app/controllers subfolder, which Rails searches for. A user's web request is handled by a controller.
    app/helpers: Any helper classes needed to assist the model, view, and controller classes are stored in the app/helpers subdirectory. This keeps the model, view, and controller code clean, simple, and focused.


### 16.  What is a Rails Controller?
Your application's logical heart is the Rails controller. It orchestrates the user's interaction with the views and the model. A number of key ancillary functions are also housed in the controller, including:

    It is in charge of directing external requests to internal processes.
    It controls caching, which can improve application performance by orders of magnitude.
    It handles helper modules, which add functionality to view templates without adding code to them.
    It keeps track of sessions, creating the impression that users are still interacting with our apps.


### 17. Explain Rails Migration.


A Rails migration is a tool for altering the database schema of an application. Instead of handling SQL scripts, you use a domain-specific language to define database modifications (DSL). Because the code is database-agnostic, you can quickly port your project to a different platform. Migrations can be rolled back and managed alongside your application source code.

### 18. Explain how rail implements Ajax?


The way Rails supports Ajax operations is simple and consistent. Different user actions force the browser to display a new web page (like any regular web application) or initiate an Ajax activity after the original web page has been produced and displayed.

    Some trigger is fired- This could be a user clicking on a button or link, a user changing data on a form or in a field, or just a recurring trigger (based on a timer).
    The server is contacted by the web client- The XMLHttpRequest JavaScript function transmits data associated with the trigger to a server action handler. The data could be the checkbox ID, the text in an entry field, or the entire form.
    The server performs the processing- The server-side action handler (Rails controller action) manipulates the data and sends an HTML fragment to the web client.
    The HTML fragment is received by the client-side JavaScript- The client-side JavaScript which Rails generate automatically is used to alter a specific area of the current page's HTML, usually the content of an <div> element.


### 19. What command is used to create a migration?


To create migration command includes:

C:\ruby\application>ruby script/generate migration table_name


### 20. Explain Cross-Site Request Forgery (CSRF). How is Rails protected against it?


Cross-Site Request Forgery (CSRF) is a typical online application attack that compromises a victim's authenticated session. This attack entails duping a target into executing unwanted actions on a website to which they have been authenticated. 

You must add "protect from forgery" to your ApplicationController to protect against CSRF attacks. Rails will now require a CSRF token in order to complete the request. Every form built using Rails forms builders includes a hidden field called CSRF token.

### 21. What is the difference between observers and callbacks in Ruby on rails?


    Callback methods in Rails can only be called at specific moments in an object's life cycle, such as validation, creation, updating, deletion, and so on. The rails callback, unlike the rails observers, is only active for a brief time.
    Rails observers are similar to callbacks, but they're used when a method isn't directly related to the object's life cycle. It can be attached or detached at any time and lives for a longer period of time.


### 22. What is the purpose of the rakefile available in the demo directory in Ruby?


This brief questionnaire is designed to ensure that a developer is familiar with test-driven development. This file may be unfamiliar to a newbie. The rakefile, which is analogous to the makefile in Unix, is used to package and test Rail’s code. The rake utility, which comes with the Ruby installation, makes use of it.

### 23. Explain the difference between ActiveSupport’s "HashWithIndifferentAccess" and Ruby’s "Hash"?


The "HashWithIndifferentAccess" class treats symbol and string keys as equivalent, whereas Ruby's "Hash" class uses a tighter = = comparison on keys: thus a comparable string key will not get the value for a given symbol key.

### 24. What is the difference between string and text in Rails? 

    Both string and text save information of the "string-type" that you can freely write in. The number of characters you can enter in these fields differs between the two. The character limit for a string field is 255 characters, while the character limit for a text field is 30,000 characters.
    If you wish to store data like addresses, names, or basic custom data, a string field is an excellent option. When you want to store information from a comment box on a form, or if you're importing a huge block of text, a text area field is an excellent solution.

### 25. Explain the difference between dynamic and static scaffolding.
|Dynamic Scaffolding| Static Scaffolding|
|--|--|
|At runtime, it generates all of the content and user interface. |	To produce the data with their fields, it takes explicit entry in the command.|
|It allows you to create new, delete, and modify methods for usage in your application. |	In static scaffolding, It is not necessary for such generation to occur.|
|It does not require synchronization with a database. |	It necessitates the migration of the database.|
### 26. What are strong parameters? Explain in brief.


Many Rails apps employ Strong Parameters, also known as Strong Params, to strengthen the security of data supplied through forms. Strong parameters allow developers to determine which parameters are accepted and used in the controller. Any superfluous or potentially hazardous params will be ignored and successfully filtered out by allowing only the expected params. This is especially crucial when using Active Model bulk assignments, as numerous params might be provided at the same time.

### 27. Does Ruby Support Single Inheritance/Multiple Inheritance Or Both?

Ruby only supports single inheritance. It does not support multiple inheritance directly, but it supports something similar- mixins.


### 28.  What are the limits of Ruby on Rails?

Ruby on Rails is a framework for building MVC-based CRUD web applications. Other programmers may find Rails unusable as a result of this. The following are some of the functionalities that Rails does not support.

    Databases with foreign keys.
    Linking to many databases at the same time.
    Web services for soap.
    Multiple database servers are connected at the same time.



### 29. What are the databases with which Rails can easily work without facing any compatibility problem?
These are PostgreSQL, DB2, MySQL, SQL as well as SQLite
### 30.  List out what can Rails Migration do?
Rails Migration can do following things

    Create table
    Drop table
    Rename table
    Add column
    Rename column
    Change column
    Remove column and so on

### 31. Explain when self.up and self.down method is used?
When migrating to a new version, self.up method is used while self.down method is used to roll back my changes if needed.
### 32. Mention what is the role of Rails Controller?
The Rails controller is the logical center of the application. It faciliates the interaction between the users, views, and the model. It also performs other activities like

    It is capable of routing external requests to internal actions. It handles URL extremely well
    It regulates helper modules, which extend the capabilities of the view templates without bulking of their code
    It regulates sessions; that gives users the impression of an ongoing interaction with our applications

### 33. Explain what is rake in Rails?
Rake is a Ruby Make; it is a Ruby utility that substitutes the Unix utility ‘make’, and uses a ‘Rakefile’ and ‘.rake files’ to build up a list of tasks. In Rails, Rake is used for normal administration tasks like migrating the database through scripts, loading a schema into the database, etc.
### 34.  Explain how you can list all routes for an application?
To list out all routes for an application you can write *rake routes* in the terminal.


### 35. Explain what is sweeper in Rails?
Sweepers are responsible for expiring or terminating caches when model object changes.
### 36.  Mention the log that has to be seen to report errors in Ruby Rails?
Rails will report errors from Apache in the log/Apache.log and errors from the Ruby code in log/development.log.
### 37. Mention what is the difference between redirect and render in Ruby on Rails?

    Redirect is a method that is used to issue the error message in case the page is not issued or found to the browser. It tells browser to process and issue a new request.

    Render is a method used to make the content. Render only works when the controller is being set up properly with the variables that require to be rendered.

### 38. Mention what is the purpose of RJs in Rails?
RJs is a template that produces JavaScript which is run in an eval block by the browser in response to an AJAX request. It is sometimes used to define the JavaScript, Prototype and helpers provided by Rails.
### 39. Explain what is Polymorphic Association in Ruby on Rails?
Polymorphic Association allows an ActiveRecord object to be connected with Multiple ActiveRecord objects. A perfect example of Polymorphic Association is a social site where users can comment on anywhere whether it is a videos, photos, link, status updates etc. It would be not feasible if you have to create an individual comment like photos_comments, videos_comment and so on.
### 40. Explain what is the defined operator?
Define operator states whether a passed expression is defined or not. If the expression is defined, it returns the description string and if it is not defined it returns a null value.
### 41. Mention what is the difference between a single quote and double quote?

A single-quoted strings don’t process ASCII escape codes, and they don’t do string interpolation.

### 42.  How should you use nested layouts?
The layouts removes code duplication in view layer. You are able to slice all your application pages to blocks such as header, footer, sidebar, body and etc.

A generated Rails application has a default layout and it’s defined in the app/views/layouts/application.html.erb. On the screen above there is only one dynamic block - it’s the body, the footer, the header and the sidebar are common blocks for each page. So the code for the layout may look like this:
<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <%= render 'shared/header' %>
  <%= render 'shared/sidebar' %>
  <%= yield %>
  <%= render 'shared/footer' %>
</html>

The yield in the code above is the place in which any action template will be rendered. This is a default Rails behavior.
### 43. What is the difference between #== and #equal??
#== performs the generic comparison and is implemented differently across classes while #equal? is defined on BasicObject and compares object identity. Therefore, #equal? should not be overridden in subclasses.
### 44. #== performs the generic comparison and is implemented differently across classes while #equal? is defined on BasicObject and compares object identity. Therefore, #equal? should not be overridden in subclasses.
    Array#each method iterates over the elements of the array and executes the provided block each time. However, it returns the original array unaffected.
    Array#map will return a new array of elements containing the values returned by the block it is provided. It also does not affect the original array
### 45. What are Gemsets in Rails?
Gems in Ruby are used to extend capabilities of core Ruby distribution. They add specific functionalities in programs. Some gems are also installed with Ruby installation to provide specific environments are called gemsets. You can have different versions of the same gem installed in a system.

To know all the gems available in Ruby, use the following command:

    rvm gemset list
### 46. Explain bundler in Rails.
Rails bundler provides a constant environment for applications by tracking suitable gems that are needed.

To use bundler, use the following command:

    gem install bundler
### 47. How does router work in Rails?
The Rails router recognizes URLs and dispatches them to a controller's action. It also generates paths and URLs. Rails router deals with URLs differently from other language routers. It determines controller, parameters, and action for the request.
Main purpose of Rails routers is:

    Connecting URLs to code
    Generating paths and URLs from code

### 48. Explain REST in Rails routes.

REST is very beneficial to understand routes in Rails. It stands for Representational State Transfer. Several HTTP methods are used with REST to represent the types of actions performed by the user or application. 


### 49.  Explain some features of nested scaffolding.

The Nested scaffold is the command that generates a set of correctly working nested resource for Rails 4.2 and 5.

Features

    Generates a nested child resource with a single command
    Generates a beautifully working bunch of code
    Automatically generates appropriate model associations for ActiveRecord
    Html ready


### 50. In how many ways you can create Rails layout HTTP response.

There are three ways to create an HTTP response from the controller's point of view:

    Call render to create a full response to send back to the browser
    Call redirect_to to send an HTTP redirect status code to the browser
    Call head to create a response to end back to the browser


### 51. Explain the importance of yield statement in Rails.

The yield statement in Rails decides where to render the content for the action in the layout. If there is no yield statement in the layout, the layout file itself will be rendered, but additional content into the action templates will not be correctly placed within the layout.

### 52.  How many filters are there in Rails.
Rails filters are methods that run before or after a controller's action method is executed. Rails support three types of filter methods:

    Before filters
    After filters
    Around filters

### 53. How can you protect filter methods in Rails?
All the Ruby methods have at least one of these protection level.

    Public: These methods are accessible from any external class or method that uses the same class in which they are defined.
    Protected: These methods are accessible only within the class in which they are defined and in the classes that inherit from the class in which they are defined.
    Private: These methods are only accessible within the class in which they are defined.

### 54. Explain testing in Rails.

Rails also use a separate database for testing. Rails use Ruby Test::A unit testing library. Rails application test is usually run using Rake utility.
Rails support three types of tests:

    functional
    integration
    unit tests


### 55. Explain Rails caching levels.

Rails caching is available at three levels of granularity:

    Page
    Action
    Fragment


### 56. What are Rails validation used for?

Rails validation defines valid states for each of your Active Record model classes. They are used to ensure that only valid details are entered into your database.

### 57. Explain valid and invalid in Rails?

The valid? triggers your validations and returns true if no errors are found otherwise, false.

The invalid? is simply the reverse of valid?. It triggers your validations and returns true if invalid otherwise, false.

### 58. Explain Unobtrusive JavaScript in Rails.

"Unobtrusive JavaScript" technique is considered as the best technique within the frontend community.

### 59. What is the Symbol Garbage Collector?

Passing symbols opens the possibility of several attacks in your system. The symbol garbage collector collects the symbols which prevent your system from several attacks.

### 60. What is Action Cable?

It is a framework which is used to extend Rails via WebSockets to add some functionality. It integrates WebSockets with the rest of the Rails application very smoothly. It allows you to add some real-time features to your app quickly.

### 61. What are generators in ruby on rails?

The rails include code generator scripts, which are used to generate model and controller classes for an application automatically. Code generation increases your productivity when developing web applications. By running generator command, skeleton files for all your model and controller classes will be generated. It also generates database migration files for each model it generates.

### 62. What is a webrick web server?

Rails are configured to use WEBrick server automatically. This server is written in pure Ruby and supports almost all platforms like Windows, Mac or Unix. Alternatively, if you have Mongrel or Lighttpd server installed in your system, Rails uses either of those servers.

All the three Rails servers feature automatic reloading of code. It means, when you change your source code, you do not need to restart the server.

### 63.  What is a rack? 
Rack is an API that sits between the web server and Rails. It allows you to connect and exchange frameworks like Rails with Sinatra, or web servers like Unicorn with Puma.
### 64.  What is PORO? 

PORO stands for Plain Old Ruby Object.
While almost everything in Ruby is an object, ActiveRecord tends to use many complex objects. Thus, the term PORO usually means a small, simple object used to support business logic.

### 65. 

### 66. 

### 67. 

### 68. 

### 69. 

Process finished with exit code 0








