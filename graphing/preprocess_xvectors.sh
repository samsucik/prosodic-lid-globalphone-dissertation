#/bin/bash -u

dir=$1

# Fix SCPs by removing absolute paths from them.
echo "Removing absolute paths from SCPs."
for scp in $1/*.scp; do
	head -100 $scp | sed -E "s&/([^/]+/)+&&" > ${scp}.fixed
	cat $scp | sed -E "s&/([^/]+/)+&&" > ${scp}.fixed
done

echo "Decoding ARKs."
for scp in $1/*.scp.fixed; do
	copy-vector --verbose=0 scp:${scp} ark,t:- > ${scp}.vectors
done

echo "Turning decoded ARKs into CSV."
for scp in $1/*.vectors; do
	cat $scp | sed -E "s/([A-Z]{2})[-0-9_]+/\1/" | sed -E "s/\s+\]//g" | sed -E "s/(\s+\[\s+|\s+)/;/g" > ${scp}.csv
done
