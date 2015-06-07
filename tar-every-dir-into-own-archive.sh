#!/usr/bin/sh

# Pack and compress each directories and its subfolders into separate archives.

cd directory
for dir in */
do
  bn=$(basename "$dir")    # grep the name of the directory
  tar -czf "${bn}.tar.gz" "$dir"    # compress
done
