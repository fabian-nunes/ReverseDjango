#!/bin/sh

while true
do
    echo "Please enter a command (cat, chmod, python, or exit):"
    read cmd

    case $cmd in
        cat)
            echo "Executing cat..."
            read file
            cat $file
            ;;
        chmod)
            echo "Executing chmod..."
            read permissions
            read file
            chmod $permissions $file
            ;;
        start)
            echo "Starting Django application..."
            # Replace with the command to start your Django application
            python /reverse_django/manage.py runserver 0.0.0.0:8000
            ;;
        exit)
            echo "Exiting restricted shell..."
            exit 0
            ;;
        *)
            echo "Command not allowed. Only cat, chmod, python, start, or exit are allowed."
            ;;
    esac
done
