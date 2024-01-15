# syscallTracker

Here are some (brief) directions on how to run the syscall tracker:
1. compile program you are trying to track the syscalls of (e.g. gcc -o test_program test_program.c)
2. compile print_syscall.c (gcc -o print_syscall print_syscall.c)
3. run bash script: "./getSyscalls.sh ./testProgram"
4. view contents of test_summarize.txt to see final results 🎉

Potentially, there may be a syscall that was not covered in syscalls.csv. In that case, note its syscall number and consult a list of syscalls online

Here is a quick rundown of what the files do:
      getSyscalls.sh - bash script to run the whole program (need to compile print_syscall.c first)
      print_syscall.c - prints out the syscall numbers as the syscalls are made
      syscalls.csv - list of syscalls number --> name (originally tried to automate this but yiqing found out it was much easier to hardcode it)
      test.txt - temporary txt file to store output from print_syscall.c (note that i print print_syscall's stderr output to the test.txt to avoid garbage that is printed out in stdout)
      test_summarize.txt - file to store final list of compiled names and count of the number of times syscalls were made
      summarize.py - takes in test.txt and turns the syscall numbers into names using syscalls.csv; also counts the number of times each syscall was made

      
