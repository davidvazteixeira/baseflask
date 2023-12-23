#!/bin/bash

# Source this file to enable autocomplete to db command

_db()
{
  local cur prev BASE_LEVEL

  COMPREPLY=()
  cur=${COMP_WORDS[COMP_CWORD]}
  prev=${COMP_WORDS[COMP_CWORD-1]}

  if [ $COMP_CWORD -eq 1 ]; then
    # Options of the first level
    COMPREPLY=( $(compgen -W "a0 b0 c0" -- $cur) )
  
  elif [ $COMP_CWORD -eq 2 ]; then
    case "$prev" in
      # Options of the second level
      "a0")
        COMPREPLY=( $(compgen -W "a01 a02 a03" -- $cur) )
        ;;
      
      "b0")
        COMPREPLY=( $(compgen -W "b1 b2 b3" -- $cur) )
        ;;
      
    esac
  elif [ $COMP_CWORD -eq 3 ]; then
    case "$prev" in
      # Options of the third level
      "a1")
        COMPREPLY=( $(compgen -W "a1_1 a1_2 a1_3" -- $cur) )
        ;;
      
      "a2")
        COMPREPLY=( $(compgen -W "a2_1 a2_2 a2_3" -- $cur) )
        ;;
      
      "a3")
        COMPREPLY=( $(compgen -W "a3_1 a3_2 a3_3" -- $cur) )
        ;;
      
      "b1")
        COMPREPLY=( $(compgen -W "b1_1 b1_2 b1_3" -- $cur) )
        ;;
      
      "b2")
        COMPREPLY=( $(compgen -W "b2_1 b2_2 b2_3" -- $cur) )
        ;;
      
      "b3")
        COMPREPLY=( $(compgen -W "b3_1 b3_2 a3_3" -- $cur) )
        ;;
# elif [ $COMP_CWORD -eq 4 ]; then
#   case "$prev" in
#     # Options of the forth level
#     "")
#       COMPREPLY=( $(compgen -W "4l_option1 4l_option2" -- $cur) )
#       ;;
    esac
  fi

  return 0

} && complete -F _db db
