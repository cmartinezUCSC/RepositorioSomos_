#!/usr/bin/env bash
training_set_size=115809

head -n "${training_set_size}" total.txt >test.txt
tail -n "+$((training_set_size + 1))" total.txt >train.txt

repeated_elements="$(comm -12 <(sort train.txt) <(sort test.txt) | wc -l)"
if [[ repeated_elements -gt 0 ]]; then
	echo WARNING: Repeated elements between train and test datasets
fi
