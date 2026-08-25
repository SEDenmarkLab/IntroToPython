# Unit 4: Functions and Other Tools

This may seem redundant given that you've been writing functions the entire time, but trust me, there are a lot of things I haven't discussed that will be very important going forward.

Here is a list of questions/comments you should be able to answer:

* What is the structure of a function?
* What are type annotations?
* What is the `typing` module in Python? How could one use it when  making more descriptive functions?
* What are `kwargs` and `args` and why do people use them in functions? What is the difference between `*` and `**`? Do you have to use the term `kwargs` and `args`?
* What is a namespace? What is the difference between global and nonlocal? When are good times to use them, and why do people generally recommend to avoid them?
* What happens if you use a mutable object as a default argument, i.e. `def add_item(item, my_list=[])`? What is one way you could handle this problem?
* What is a lambda function? When and where should you use them?
* Should lambda functions exist on their own lines?
* What do the `map`, `filter`, and `reduce` functions do, and how would you use them with a lambda function?
* What is the difference between return and print?
* What is the difference between return and yield? Why would someone use yield, and how does one use yield effectively?
* What is a `match` statement? How does it compare to `if`/`elif`/`else`statements? How would I do the equivalent of`else` in a `match` statement?
* What are the different types of errors? How do they differ from warnings, and how would you integrate them into your own code?

## Note for Exercises:

Going forward, you're going to integrate as many boundary cases into these using error/exceptions. In addition, download and figure out how to use/add numpy docStrings using the [autodoc extension](vscode:extension/njpwerner.autodocstring) in VSCode.
