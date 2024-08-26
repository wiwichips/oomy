#!/bin/bash
#
# Records the memory of a process over time
#

# Check if the command to execute is provided
if [ -z "$1" ]; then
  echo "Usage: $0 commandToExecute"
  exit 1
fi

# File to output memory usage
output_file="output.txt"
#echo "RSS memory usage in KB" > "$output_file"

# Run the command in the background
"$@" &
pid=$!

# Monitor memory usage every 100ms
while kill -0 $pid 2> /dev/null; do
  # Get the RSS value and append it to the output file
  rss=$(ps -p $pid -o rss=)
  echo "$rss" >> "$output_file"
  # Sleep for 100ms
  sleep 0.1
done

echo "Memory monitoring completed. Results saved to $output_file."

