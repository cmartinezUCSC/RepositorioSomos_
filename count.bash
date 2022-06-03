#!/usr/bin/env bash
labels=(
	'__label__fear'
	'__label__anger'
	'__label__joy'
	'__label__sadness'
	'__label__trust'
	'__label__disgust'
	'__label__anticipation'
	'__label__surprise'
)

_test=0
_train=0
_total=0

for l in "${labels[@]}"; do
	echo "${l#__label__}"
	test_="$(grep "$l" test.txt | wc -l)"
	train="$(grep "$l" train.txt | wc -l)"
	total="$(grep "$l" total.txt | wc -l)"
	_train="$((_train + train))"
	_test="$((_test + test_))"
	_total="$((_total + total))"
	echo -e "\ttrain: ${train}"
    echo -e "\ttest: ${test_}"
	echo -e "\ttotal: ${total}"
done

echo all
echo -e "\ttest: ${_test}"
echo -e "\ttrain: ${_train}"
echo -e "\ttotal: ${_total}"
