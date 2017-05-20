#!/bin/bash
#=======================================================================
#
#Replace string by sed
#
#=======================================================================
#
#eg. to replace below string patterns in test.html by empty string and then change its contents.
#
#	test.html
#
#		⋯
#		<p class="codelink"><a id="p0792pro01" href="part0072.html#p0792pro01a">Click here to view code image</a></p>
#		⋯
#		<p class="codelink"><a id="p0794pro01" href="part0072.html#p0794pro01a">Click here to view code image</a></p>
#		⋯
#
#	$ sed '/<p class=\"codelink\">.*Click here to view code image<\/a><\/p>/d' test.html > tmp.html
#	$ mv tmp.html test.html

for obj in $(find . -name \*.html)
do
		file $obj | grep "XML 1.0 document text"
		if [ $? -eq 0 ];then
		hasmatch=$(grep "Click here to view code image" $obj | wc -l);
		if [ "$hasmatch" -ge 1 ]
		then
			$(sed '/<p class=\"codelink\">.*Click here to view code image<\/a><\/p>/d' $obj > tmp);
			$(mv tmp $obj);
		fi
	fi
done
