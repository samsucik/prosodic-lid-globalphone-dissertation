#!/bin/bash -u

for l in AR BG CH CR CZ FR GE JA KO PO RU SP SW TH TU WU VN; do
	echo $l
	lname=$(cat conf/lang_codes.txt | grep "$l" | sed -E "s/.*\s+//")

	for portion in enroll test; do
		echo $portion
		spks=$(cat conf/${portion}_spk.list | grep "$l" | sed -E "s/[A-Z]+\s+//")
		# echo $spks
		for spk in $spks; do
			sex=$(cat gp-sexdata/$lname | grep "$spk")
			echo "${sex}"
		done > gp-sexdata/${l}-$portion
		cat gp-sexdata/${l}-$portion | sed -E "s/.*\t//" | sort | uniq -c
	done
done
