
# This script expects to be executed in a folder with a subfolder called blogs,
# containing the .xml files that should be sanitized. Results are written to a
# folder called sanblogs.


# Create output folder
mkdir -p sanblogs1 
# Loop over input files (with path prefix)
for pathname in ./blogs/*.xml
do
	#Progress report
	echo "Processing $pathname..."
	# Extract filename from path ( './blogs/post.xml' -> 'post.xml' )
	filename=$(basename $pathname)
	# Sanitize and save result in new file
	cat $pathname |
	# Get rid of everything non-ascii
	iconv -c -f utf8 -t ascii |
	# Convert escape sequences "&xxx;" to ""
	sed -r "s/&[a-z]{1,6};//g" |
	
	# NEW ----------------------------------
	# Remove ' without adding a space
	sed -r "s/'//g" |
	# Change ? and ! to .
	sed -e 's/?/\./g' |
	sed -e 's/\!/\./g' |
	# Change repetitions of . to a single .
	sed -r 's/(\.)+(\.|)?/\./g' |
	sed -r 's/(\. )+(\.| )?/\./g' |
	# Add space after and before.
	sed 's/\./\. /g' |
	sed 's/\./\ ./g' |
	# --------------------------------------
	
	# Remove all lonely "<", ">" and "/" that are not part of tags
	sed -r 's/\/|>|<|(<\/?[a-zA-Z]+>)/\1/g' |
	# Remove all non alphanumeric characters except "<", ">", "." and "/"
	sed -r 's.[^a-zA-Z0-9<>/.]. .g' |
	# change Upper case to lower case
	sed -e 's/A/a/g' \
    -e 's/B/b/g' \
    -e 's/C/c/g' \
    -e 's/D/d/g' \
    -e 's/E/e/g' \
    -e 's/F/f/g' \
    -e 's/G/g/g' \
    -e 's/H/h/g' \
    -e 's/I/i/g' \
    -e 's/J/j/g' \
    -e 's/K/k/g' \
    -e 's/L/l/g' \
    -e 's/M/m/g' \
    -e 's/N/n/g' \
    -e 's/O/o/g' \
    -e 's/P/p/g' \
    -e 's/Q/q/g' \
    -e 's/R/r/g' \
    -e 's/S/s/g' \
    -e 's/T/t/g' \
    -e 's/U/u/g' \
    -e 's/V/v/g' \
    -e 's/W/w/g' \
    -e 's/X/x/g' \
    -e 's/Y/y/g' \
    -e 's/Z/z/g' |
	# Write to file
	cat > sanblogs1/$filename
done
