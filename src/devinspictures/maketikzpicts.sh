if [ -d all54 -a -d special20 ] && cd matrices

then

{
	for f in mat[^s]*
	do 
		newf=`python ../maketikzpicts.py "$f"`
		echo Making file $newf in directory all54
    	/bin/mv $newf ../all54
	done
	
	for f in mats*
	do 
		newf=`python ../maketikzpicts.py "$f"`
		echo Making file $newf in directory special20
		/bin/mv $newf ../special20
	done

} || cd ..
fi 

cd ..
