## Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python is an object-oriented programming language which uses class inheritance while javascript is not purely object-orient based. The syntax of each differs as python utilizes indentation for code blocks while javascript uses curly braces to do so. Similar differences with python using = to define variables while javascript utilisez var or let.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") without your programming
  crashing.
  
 `dictionary = {"a": 1, "b": 2}`
 `key = "c"`
 `missing_key = dictionary.get(key, "No key present")`
 

- What is a unit test?

A unit test is the process of testing the smallest section of code within an application.

- What is an integration test?

This is the testing of the complete module of code.

- What is the role of web application framework, like Flask?

Flask is a web framework which is used to devlop web applications in python, with built in development server.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  
 The route paramter is better for the web application because it makes the URL more readable and easier to find for users or developers.
  

- How do you collect data from a URL placeholder parameter using Flask?

You collect data from a URL in Flask by defining a route with a placeholder in the URL.

- How do you collect data from the query string using Flask?

The request object or the request.args dictionary both allow you to collect data from a query string in Flask.


- How do you collect data from the body of the request using Flask?

You can do so. by accessing the request object and adjusting it based on the kind of information that is needed.

- What is a cookie and what kinds of things are they commonly used for?

Cookies are name/string value pairs stored by the browser.

- What is the session object in Flask?

This a built in object that allows for the stroage of user data in between HTTP requests, allowing data and a user's state across multiple requests within a web application.



- What does Flask's `jsonify()` do?

This function allows Flask to easily generate JSON responses using Python data structures.


