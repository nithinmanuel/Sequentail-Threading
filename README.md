# threading

This is a simple multithreading consist of tasks that are sequential in the manner . There are several tasks that depend on each other , for instance only a one task could be installed after another one because of the dependency . there is an input which is in json file where all the tasks are listed .  the way it has to work is according to a sequential flow . There are 9 tasks in total in the json file .   


The program expects as input a json file, conforming to the schema included. This file
contains a list of tasks, each task specifies
● name
● type (eval or exec)
● arguments
● dependencies (optional)
A task can start executing after all its dependencies have been successfully executed.
If a dependency fails or is skipped, the task should be skipped.
A task of type eval has a code snippet as argument, that is to be executed within the main
process. If the code raises an exception, it is considered failed.
A task of type exec has a shell command as argument, that is to be executed in a shell. If
the return code is none zero, it is considered failed.
The output of the program should provide
 During executing tasks:
1) a line for the start of a task of the form  “Started: %(name)s”
2) a line for the end of a task of the form  “Ended : %(name)s”
3) all output produced by the tasks
