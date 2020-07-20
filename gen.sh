cd password_generator

cat readme.md

echo 'Do you want to run the generator? y/n'
read resp

if [[ $resp -eq 'y' || 'Y' ]]
then
	python generator.py
else
	exit
fi
