#!/usr/bin/env bash

test_only=${test_only:-true}
cd $(dirname $0)
for f in *.in
do
    if [[ $f =~ example.in ]]
    then
        echo Testing solution with example data ...
        echo Actual:
        python solution.py < $f
        echo Expected:
        cat ${f%.in}.out
    else
        $test_only && continue
        echo Processing $f ...
        python solution.py < $f > ${f%.in}.out
    fi
done
