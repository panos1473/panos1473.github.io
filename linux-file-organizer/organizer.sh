echo "the organizer starts"

TARGET_DIR="/home/vboxuser/Desktop/test_files"

mkdir -p "$TARGET_DIR/Documents"
mkdir -p "$TARGET_DIR/Images"
mkdir -p "$TARGET_DIR/Scripts"
mkdir -p "$TARGET_DIR/Other"

for file in $TARGET_DIR/*; do
  if [ -f "$file" ]; then
    filename=$(basename "$file")

    case "$filename" in
      *.pdf|*.doc|*.docx)
        mv "$file" "$TARGET_DIR/Documents/"
        ;;
      *.jpg|*.png|*.jpeg)
        mv "$file" "$TARGET_DIR/Images/"
        ;;
      *.sh)
        mv "$file" "$TARGET_DIR/Scripts/"
        ;;
      *)
        mv "$file" "$TARGET_DIR/Other/"
        ;;
    esac
  fi
done
