(*Austin Ryf - 11512650*)

(*exists function DOESN'T NEED FIXING*)

fun exists (x, []) = false |
	exists (x, y::rest) = 
	if x = y
	then true 
	else exists (x, rest);

(*The type is (''a * ''a list) -> bool, because it needs to be supported by equality testing since the function has to check if the given value and a value in the list are equal*)



(*countInList function FIXED*)

fun countInList [] x = 0 |
	countInList (y::rest) x  = 
	if x = y
	then (countInList rest x) + 1
	else (countInList rest x);



(*listDiff function FIXED*)

fun listDiff ([], []) = [] |
	listDiff (x::rest1, []) = x::rest1 |
	listDiff ([], y::rest2) = y::rest2 |
	listDiff (x::rest1, y::rest2) =
	if exists (x, y::rest2)
	then listDiff (rest1, y::rest2)
	else x::listDiff (rest1, y::rest2);



(*firstN function DOESN'T NEED FIXING*)

fun firstN [] x = [] |
	firstN (y::rest) x =
	if x = 0
	then []
	else y::firstN rest (x - 1);



(*busFinder function*)

val buses = 
[("Lentil",["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"]),
("Wheat",["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"]),
("Silver",["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"]),
("Blue",["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"]),
("Gray",["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"])];

fun busFinder str1 (str2, []) = [] |
	busFinder str1 (str2, L::rest2) =
	if exists (str1, L)
	then str2::busFinder str1 (str2, rest2)
	else busFinder str1 (str2, rest2);

(*The type is ''a -> ('b * ''a list) list -> 'b list because when there is an 'a' and a 'b' it means that there can be different types, and we are working with a string and a list of strings, which can be
considered different types*)



(*parallelResistors function and helper function (Not sure what is wrong here, I've searched everywhere for documentation for real values and no matter what I do the function won't accept a real list)*)
fun parallelHelper (y::rest):real =
	if rest = []
	then 1.0/y
	else 1.0/y + (parallelHelper rest);

fun parallelResistors L:real =
	1.0/parallelHelper L;
	
(*It would cause an error because it would try to divide by nothing or zero which isn't possible*)



(*pairNleft and pairNright functions and helper functions*)

fun reverseList [] = [] |
	reverseList (x::rest) =
	reverseList (rest)@[x];

fun listLength [] = 0 |
	listLength (x::rest) = listLength rest + 1;

fun seperateList n buff [] = [buff] |
	seperateList n buff (y::rest) =
	if listLength buff = n
	then buff::seperateList n [y] rest
	else seperateList n (y::buff) rest;

fun map f [] = [] |
	map f (x::rest) = 
	(f x)::(map f rest);

fun pairNleft (x, []) = [[]] |
	pairNleft (x, y::rest) =
	if x < 0
	then [[]]
	else map (reverseList (seperateList x [] y::rest));
	
fun pairNright (x, []) = [[]] |
	pairNright (x, y::rest) =
	if x < 0
	then [[]]
	else reverseList (seperateList (x [] reverseList y::rest));



(*Test Cases*)

fun existsTest () =
let
	val existsT1 = (exists (4, [1, 2, 3]) = false)
	val existsT2 = (exists (0, []) = false)
	val existsT3 = (exists (2, [1, 2, 3]) = true)
in
	print ("exists:-------------------- \n" ^ 
	 		"   test1: " ^ Bool.toString(existsT1) ^ "\n" ^ 
			"   test2: " ^ Bool.toString(existsT2) ^ "\n" ^ 
			"   test3: " ^ Bool.toString(existsT3) ^ "\n")
end

val _ = existsTest ()


fun countInListTest () =
let
	val countInListT1 = (countInList "2" ["1", "2", "3", "2"] = 2)
	val countInListT2 = (countInList "1" [] = 0)
	val countInListT3 = (countInList [] [[1,2], [3,4]] = 0)
in
	print ("countInList:-------------------- \n" ^ 
	 		"   test1: " ^ Bool.toString(countInListT1) ^ "\n" ^ 
			"   test2: " ^ Bool.toString(countInListT2) ^ "\n" ^ 
			"   test3: " ^ Bool.toString(countInListT3) ^ "\n")
end

val _ = countInListTest ()


fun listDiffTest () =
let
	val listDiffT1 = (listDiff ([],[]) = [])
	val listDiffT2 = (listDiff (["x","y","z"], ["z"]) = ["x", "y"])
	val listDiffT3 = (listDiff ([5,6,7],[]) = [5,6,7])
in
	print ("listDiff:-------------------- \n" ^ 
	 		"   test1: " ^ Bool.toString(listDiffT1) ^ "\n" ^ 
			"   test2: " ^ Bool.toString(listDiffT2) ^ "\n" ^ 
			"   test3: " ^ Bool.toString(listDiffT3) ^ "\n")
end

val _ = listDiffTest ()


fun firstNTest () =
let
	val firstNT1 = (firstN [] 2 = [])
	val firstNT2 = (firstN [1,2,3] 0 = [])
	val firstNT3 = (firstN [[1,2],[3,4]] 2 = [[1,2],[3,4]])
in
	print ("firstN:-------------------- \n" ^ 
	 		"   test1: " ^ Bool.toString(firstNT1) ^ "\n" ^ 
			"   test2: " ^ Bool.toString(firstNT2) ^ "\n" ^ 
			"   test3: " ^ Bool.toString(firstNT3) ^ "\n")
end

val _ = firstNTest ()


fun busFinderTest () =
let
	val buses =
		[("Lentil",["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium",
		"Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart",
		"Bishop", "Derby", "Dilke"]),
		("Wheat",["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay",
		"Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"]),
		("Silver",["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart",
		"Shopco", "RockeyWay"]),
		("Blue",["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell",
		"Chinook", "Library"]),
		("Gray",["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview",
		"CityHall", "Stadium", "Colorado"])]

 	val busFinderT1 = ((busFinder "Walmart" buses) = ["Lentil","Wheat","Silver"])
 	val busFinderT2 = ((busFinder "Shopco" buses) = ["Silver"])
 	val busFinderT3 = ((busFinder "Main" buses) = ["Lentil","Gray"])
in
 	print ("busFinder:-------------------- \n" ^
 		" test1: " ^ Bool.toString(busFinderT1) ^ "\n" ^
 		" test2: " ^ Bool.toString(busFinderT2) ^ "\n" ^
 		" test4: " ^ Bool.toString(busFinderT3) ^ "\n")
end

val _ = busFinderTest ()


fun parallelResistorsTest () =
let
    val parallelResistorsT1 = Real.==((parallelResistors [10.0, 10.0, 10.0, 10.0]), 2.5)     
	val parallelResistorsT2 = Real.==((parallelResistors [8.0, 16.0, 4.0, 16.0]), 2.0) 
    val parallelResistorsT3 = Real.==((parallelResistors [5.0, 10.0, 2.0]) , 1.25) 
in     
 	print ("parallelResistors:-------------------- \n" ^ 
	 		"   test1: " ^ Bool.toString(parallelResistorsT1) ^ "\n" ^ 
			"   test2: " ^ Bool.toString(parallelResistorsT2) ^ "\n" ^ 
			"   test3: " ^ Bool.toString(parallelResistorsT3) ^ "\n") 
end

val _ = parallelResistorsTest ()


val pairNleftTest () =
let
	val pairNleftT1 = (pairNleft (2,[1, 2, 3, 4, 5]) = [[1], [2, 3], [4, 5]])
	val pairNleftT2 = (pairNleft (3,[1, 2, 3, 4, 5]) = [[1, 2], [3, 4, 5]])
in     
 	print ("pairNleft:-------------------- \n" ^ 
	 		"   test1: " ^ Bool.toString(pairNleftT1) ^ "\n" ^
			"   test3: " ^ Bool.toString(pairNleftT2) ^ "\n")
end

val _= pairNleftTest ()


val pairNrightTest () =
let
	val pairNrightT1 = (pairNright (2,[1, 2, 3, 4, 5]) = [[1, 2], [3, 4], [5]])
	val pairNrightT2 = (pairNright (3,[]) = [[])
in     
 	print ("pairNright:-------------------- \n" ^ 
	 		"   test1: " ^ Bool.toString(pairNrightT1) ^ "\n" ^
			"   test3: " ^ Bool.toString(pairNrightT2) ^ "\n")
end

val _= pairNrightTest ()