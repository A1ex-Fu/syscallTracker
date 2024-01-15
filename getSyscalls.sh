#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_command>"
    exit 1
fi

input_command="$1"

# Clear the test.txt and test_summarize.txt files
> test.txt
> test_summarize.txt

# Run ./print_syscall on the provided input command and redirect stderr (file descriptor 2) to test.txt
./print_syscall $input_command 2> test.txt

# Run the summarize.py script on the test.txt and redirect the output to test_summarize.txt
python3 summarize.py test_summarize.txt

