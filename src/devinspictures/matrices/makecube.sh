if cd matrices
then

for f in mat[^s]*
do mv `python ../makecube.py "$f"` ../all54
done

for f in mats*
do mv `python ../makecube.py "$f"` ../special20
done

fi
