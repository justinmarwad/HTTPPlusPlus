## Project 1: Custom HTTP ## 

### Writeup: Explanation and Overview ###

#### Part #1: How it Works ####

The server is a simple HTTP server that can handle GET and PUT requests. The client is a simple HTTP client that can handle GET and PUT requests. The server and client are both written in Python. It works as follows:

1. The server is started by initializing the listen method of the HTTPPlusPlus object. The server will listen on port 8080 by default. The server will listen for HTTP 1.0 styled connections and determine whether there is a PUT or GET request. If there is a GET request, the server will send the file requested to the client. If there is a PUT request, the server will receive the file from the client and save it to the server's directory. The server will then send a response to the client. The server will then close the connection and wait for another connection.

2. The client is started by initializing the connect method of the HTTPPlusPlus object. The client will either send a GET or a PUT request based on the command line arguments of the user. If there is a GET request, the client will send a GET request to the server for the provided file. If there is a PUT request, the client will read the specified file from the command like and then send the file to the server. The client will then wait for a 200 OK response from the server. The server will then close the connection and listen for another connection. 

#### Part #2: Sketch/Diagram  ####

![](images/HTTP++_layout.png)

#### Part #3: Improvements That Could Be Made ####

None - my code is beautiful and perfect. :))))

## Tests ## 

#### Test 1A: CNN Client Connection Test ####

Connected to CNN with the command  ```python HTTPPlusPlus.py www.cnn.com 80 GET index.html``` and received the following response:

![](images/client-test-cnn.png)  

#### Test 1B: Connected to internal server ####

Connected to my own internal server with the command ```python HTTPPlusPlus.py localhost 8080 GET index.html``` and received the following response (yellow is client and blue is server output):

![](images/client-test-internal.png)  

#### TEST 2A: Connected with browser to server ####

Connected to my internal server with a browser (Microsoft Edge) and received the following response:

![](images/server-test-browser.png)  

![](images/server-test-console.png)  

#### TEST 2B: Connected to internal server with GET ####

Connected to my own internal server with the command ```python HTTPPlusPlus.py localhost 8080 GET index.html``` and received the following response (yellow is client and blue is server output):

![](images/client-test-internal.png)  


#### TEST 2C: Connected to internal server with PUT ####

Connected to my own internal server with the command ```python HTTPPlusPlus.py localhost 8080 PUT test.txt``` and received the following response (yellow is client and blue is server output):

![](images/internal_PUT.png)  


## License ##


**Copyright 2022 Justin Marwad. All rights reserved.**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

