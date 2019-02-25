#/bin/bash -u

# Turn x-vectors packed in Kaldi .ark files
# into CSV files suitable for Pandas. Mainly
# for visualising x-vectors using t-SNE.
# 
# Has to be called from within the directory
# tht contains xvector.scp and corresponding
# .ark files.

dir=$1

scp=$1/xvector.scp
echo "$scp"
echo "Removing absolute paths."
cat $scp | sed -E "s&/([^/]+/)+&&" > ${scp}.fixed
echo "Decoding corresponding ARKs."
copy-vector --verbose=0 scp:${scp}.fixed ark,t:- > ${scp}.vectors
echo "Producing CSV."
cat ${scp}.vectors | sed -E "s/([A-Z]{2})[-0-9_]+/\1/" | sed -E "s/\s+\]//g" | sed -E "s/(\s+\[\s+|\s+)/;/g" > ${scp}.csv
rm ${scp}.fixed ${scp}.vectors	
exit 0
