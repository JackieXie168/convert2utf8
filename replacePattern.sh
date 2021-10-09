#!/bin/bash
# Author : Jackie Xie
#$ replacePattern.sh <pattern> <newPattern>
usage()
{
        echo "replaceStr <pattern> <new pattern>"
}

filerep()
{
        # $ for i in $(grep -ril 'old_pattern' *); do sed
        # "s/old_pattern/new_pattern/g" "$i" > tmp && \mv tmp "$i"; done
        # $ sed -i 's/old_pattern/new_pattern/g' `grep -ril 'old_pattern' *`
        # $ for i in $(grep -ril 'old_pattern' *); do sed -i
        # 's/old_pattern/new_pattern/g' "$i"; done
        for i in $(grep -ril $1 *); do sed "s/$1/$2/g" "$i" > tmp && \mv tmp
"$i"; done
}

if [ -z "$1" ]; then
        echo "It need the first argument."
        usage
elif [ -z "$2" ]; then
        echo "It need the second argument."
        usage
else
        if test "$1" && test "$2"
        then
                filerep $1 $2
        fi
fi
