# python-http-json-server
All I wanted was to create a server that could return JSON data on various requests AND to be able to request data from that server in the same program. However, I had a rough time going through HTTP server and request tutorials/examples because this topic is very confusing, and I was getting weird errors from solutions online. Thus, I decided to compile features into one beginner friendly Python file after I figured out how to incorporate all the features I desired. This code is for Python 3.

This pulled a some inspiration from [Brad Montgomery's server](https://gist.github.com/bradmontgomery/2219997).

## features
- creating and running a localhost server (server side)  
- responding to client's requests to server, then returning appropiate JSON data (server side)
- sending requests for data to server getting data back (client side)

## update
Requesting data from a url is one function of REST programming. I also added a solution using Flask, as it is better for taking care of grunt work, such as processing urls.
 
