#!/bin/bash
# Source this file to enable autocomplete in db command

_db()
{
  local cur prev BASE_LEVEL

  COMPREPLY=()
  cur=${COMP_WORDS[COMP_CWORD]}
  prev=${COMP_WORDS[COMP_CWORD-1]}
    
  if [ $COMP_CWORD -eq 1 ]; then
    # Options of the level 1
    COMPREPLY=( $(compgen -W "database tables info" -- $cur) )
  

      elif [ $COMP_CWORD -eq 2 ]; then
      # Options of the level 2
        case "$prev" in
          # Options of the second level
          
           database)
             COMPREPLY=( $(compgen -W "create setup" -- $cur) )
             ;;
  

           tables)
             COMPREPLY=( $(compgen -W "create drop seed" -- $cur) )
             ;;
  

           info)
             COMPREPLY=( $(compgen -W "adapter" -- $cur) )
             ;;
  
        esac
    
  fi

  return 0

} && complete -F _db db
