@echo off
echo "Are You sure to CREATE something?"
choice /C YN /M "Press Y for Yes or N for No."
if ERRORLEVEL 2 @echo 2 && exit
p manage.py startapp %1