#/bin/bash -u

dir=$1

for scp in $1/*.scp; do
	echo "$scp"
	echo "Removing absolute paths."
	cat $scp | sed -E "s&/([^/]+/)+&&" > ${scp}.fixed
	echo "Decoding corresponding ARKs."
	copy-vector --verbose=0 scp:${scp}.fixed ark,t:- > ${scp}.vectors
	echo "Producing CSV."
	cat ${scp}.vectors | sed -E "s/([A-Z]{2})[-0-9_]+/\1/" | sed -E "s/\s+\]//g" | sed -E "s/(\s+\[\s+|\s+)/;/g" > ${scp}.csv
	rm ${scp}.fixed ${scp}.vectors	
done
