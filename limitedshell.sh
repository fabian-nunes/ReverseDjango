#!/bin/bash
while true; do
    read -p "LimitedShell> " command
    case "$command" in
        "cat "*)
            eval $command
            ;;
        "chmod "*)
            eval $command
            ;;
        "echo "*)
            eval $command
            ;;
        "exit")
            break
            ;;
        "python"*)
            eval $command
            ;;
        "touch")
            eval $command
            ;;
        *)
            echo "Command not allowed."
            ;;
    esac
done
