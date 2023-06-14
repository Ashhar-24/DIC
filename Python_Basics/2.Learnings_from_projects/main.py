''' 
- quit() function: Used to exit the Python interpreter, terminating the current session and returning control to the operating system. 
                    ie, the code does not executes further.

- input() function: Used to take Inputs from the user and it stores it as a string intop the variable

- As python is object oriented, therefore Variables => Objects and Functions => Methods
          objects.lower() => reduces everything to lower-case
           objects.isdigit() => to check whether the object is a numerical value or not, provided the object is a string


- Random module:
            random.randrange(a,b) => returns a random integer N such that a <= N < b 
               random.randint(a,b) => returns a random integer N such that a <= N <= b 

- while True:
     .....         => Infinite loop until break statement is executed
     .....

- if-elif-else statements: elif can added in between if-else as many times as required.            <elif helps to reduce the need of nested if-else statements>
                         when if statement is True all the next elif/else statements shall not be executed.

-  continue: Skips the rest of the current iteration and move to the next iteration of the loop.
-  break: Exits the innermost loop (where it is encountered) and resume execution from the next statement after the loop. 
           Both continue and break when used in nested-loops, only the innermost loop is affected by their usage. 


- Pass keyword: The pass statement is often used as a placeholder when you are working on the structure or skeleton of your code and want to 
               leave a block empty for the time being. It allows you to bypass the need for any code inside a loop, function, class, or 
               conditional statement without causing a syntax error.
               eg: def view():
                       pass

-  with open() => Provides a convenient way to work with files by taking care of tasks such as opening the file, 
                 ensuring it is properly closed, and handling any potential errors that may occur during file operations. 
                Syntax: with open('filename', 'mode') as file_object/variable_name:        [mode: 'a' => append , 'w' => write, 'r' => read]
                        eg: with open('example.txt', 'r') as file:
                            content = file.read()                                          || file.readlines(): used to read lines
                            print(content)         => The content of the file is read using the read() method and stored in the content variable. Later displayed 
                            in the console by print() function.

- Crytography module: 
                    Documentation: crytography.io/en/latest/fernet  => Fernet crytography documentation
'''


