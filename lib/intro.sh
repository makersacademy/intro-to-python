#!/bin/bash

THIS_DIR="$(dirname -- "${BASH_SOURCE[0]}")"
cp $THIS_DIR/.bashrc ~/.bashrc

BLUE='\033[1;34m'
RED='\033[1;31m'
NC='\033[0m'

echo -e "${RED}If you're seeing scrolling text on the right,"
echo "  you're in the wrong place."
echo -e "Hit the 'Fork' button to get started.${NC}"
echo
echo -e "${BLUE}Otherwise: welcome home."
echo "This is your shell."
echo "You can use it to run Python programs."
echo
echo "If you ever lose it, hit the big green 'Run' button."
echo
echo "To run a test Python program, type:"
echo -e "  ${NC}python lib/trial.py${BLUE}"
echo
echo -e "And then hit enter.${NC}"

