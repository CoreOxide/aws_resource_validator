#!/bin/zsh

# Loop through all files in the current directory containing 'constants'
for file in *constants*; do
  # Check if the file is indeed a file and not a directory
  if [[ -f "$file" ]]; then
    # Check if the file contains the specific incorrect string
    if grep -q "BlobTypeDef = Union\[str, bytes, IO\[Any\]" "$file"; then
      # Replace the incorrect string with the corrected version
      sed -i '' 's/BlobTypeDef = Union\[str, bytes, IO\[Any\]/BlobTypeDef = Union\[str, bytes, IO\[Any\]\]/g' "$file"
      echo "Fixed BlobTypeDef in $file"
    fi

    # Temporary file to store modifications
    tmp_file="$(mktemp)"

    # Read the file line by line
    while IFS= read -r line; do
      original_line="$line"

      # Feature 1: Prefix underscore to specific strings
      for word in "or:" "and:" "lambda:" "not:" "None:" "else:" "from:"; do
        # Use word boundaries to match whole words
        line="$(echo "$line" | sed -E "s/\b${word}/_${word}/g")"
      done

      # Feature 2: Balance square brackets
      open_brackets=$(echo "$line" | grep -o '\[' | wc -l)
      close_brackets=$(echo "$line" | grep -o '\]' | wc -l)
      if (( open_brackets > close_brackets )); then
        missing_brackets=$(( open_brackets - close_brackets ))
        # Add missing brackets before '=' or at the end of the line
        if [[ "$line" == *"="* ]]; then
          # Insert missing closing brackets before the '=' sign
          line="$(echo "$line" | sed -E "s/=(.*)/$(printf ']%.0s' $(seq 1 $missing_brackets))=\1/")"
        else
          # Append missing closing brackets at the end of the line
          line="${line}$(printf ']%.0s' $(seq 1 $missing_brackets))"
        fi
      fi

      # Write the modified line to the temporary file
      echo "$line" >> "$tmp_file"
    done < "$file"

    # Replace the original file with the modified content
    mv "$tmp_file" "$file"
    echo "Applied additional features to $file"
  fi
done
