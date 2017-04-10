if cd matrices
then

for f in mat[^s]*
do mv `python ../maketikzpicts.py "$f"` ../all54
done

for f in mats*
do mv `python ../maketikzpicts.py "$f"` ../special20
done
fi
