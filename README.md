This is microservice A for another person's main program. My microservice works with txt files to send and retrieve requests. The user must have a version of python that will support certain functions like 
reading from a file or writing to a file. Other than that the user will need multiple terminals open for the microservice to communicate with the main program. This microservice generates random quotes from a list.
It simply waits for a request from the main program and then picks a random quote from a list of quotes. Below is an example of this request and output.


Request
Enter 1 to generate a random quote or 2 to exit: 1
writes to the txt file run this is the request message that the microserver is looping for 

Retrieve
Reads in request by reading the txt file for a run, when the run is read in by the program it will continue on with generating a quote


- In two terminals run the main program and the microservie.
- In the main program enter the option to generate a random quote.
- The main program will write to a txt file "run"
- The microservice will loop and wait till it reads "run"
- Once the microservice reads in "run" it will generate the random quote and replace run with the quote
- The main program will sleep and then wake up to read what was replaced in the text file
- It will read the quote and print it back on the main program dedicated terminal
