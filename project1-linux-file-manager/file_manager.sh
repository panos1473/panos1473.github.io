echo "Mini File Manager"

mkdir -p my_folder 
echo "Folder 'my_folder'created."


touch my_folder/file1.txt
echo "File 'file1.txt'created inside 'my_folder' ."

touch my_folder/file2.txt
echo "file 'file2.txt created inside 'my_folder'."

mkdir -p backup
mv my_folder/file1.txt backup/
mv my_folder/file2.txt backup/
echo "file moved to 'backup'folder."

echo "Contents of 'backup':"
ls backup
