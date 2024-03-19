#!/bin/sh

# Add the current directory to PYTHONPATH
export PYTHONPATH=$(dirname "$(pwd)"):$PYTHONPATH

# Set LD_LIBRARY_PATH
export LD_LIBRARY_PATH="/usr/lib/openvino:$LD_LIBRARY_PATH"

show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  -f, --flask      Run flask demo"
    echo "  -g, --gradio     Run gradio ui demo"
    echo "  -h, --help       Show this help message"
}

# Parse command-line options
if [ $# -eq 0 ] || [ $# -gt 1 ]; then
    show_help
else
    # Check the provided option
    case $1 in
        --gradio|-g)
            python3 gradio/app.py
            ;;
        --flask|-f)
            python3 flask/app.py
            ;;
        --help|-h)
            show_help
            ;;
        *)
            echo "Invalid option: $1"
            show_help
            ;;
    esac
fi