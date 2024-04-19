#!/usr/bin/env bash

test_only=${test_only:-true}
cd $(dirname $0)
for f in *.in
do
    if [[ $f =~ example.in ]]
    then
        echo Testing solution with example data ...
        echo Actual:
        #python solution.py < $f &> ${f%.in}.all
        #grep -e '^.*VALID$' ${f%.in}.all
        python solution.py < $f 2>&1 | tee ${f%.in}.all
        echo Expected:
        cat ${f%.in}.out
    else
        $test_only && continue
        python solution.py < $f > ${f%.in}.out 2> ${f%.in}.err
    fi
done
