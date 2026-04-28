#!/bin/bash

function f() {
    [ -e out ] && rm out
    for x in $(find bench -name "*.fpcore")
    do
        echo "Going for '$x'"
        racket -l herbie improve "$x" a.fpcore
    done
}

f |& tee out
